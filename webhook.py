import os
import base64
import requests
import subprocess
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from ai_test_generator import generate_unit_test  # Importing function
from github import Github

# Load environment variables
load_dotenv()

app = FastAPI()

# Retrieve API keys securely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")

# Ensure API keys are set
if not OPENAI_API_KEY or not GITHUB_TOKEN:
    raise ValueError("Missing API keys! Set OPENAI_API_KEY and GITHUB_TOKEN as environment variables.")

@app.post("/webhook")
async def receive_github_event(request: Request):
    print("Webhook received!")
    payload = await request.json()
    commits = payload.get("commits", [])
    
    if not commits:
        return {"status": "No commits found in the payload."}

    for commit in commits:
        commit_sha = commit.get("id")
        if not commit_sha:
            continue  # If commit SHA is missing, skip this commit

        repo_name = payload["repository"]["full_name"]
        modified_files = commit.get("modified", [])

        # Check if there are any modified Python files under the src/ directory
        src_files = [file for file in modified_files if file.startswith("src/") and file.endswith(".py")]
        if not src_files:
            return {"status": "No Python files found in the src/ directory."}

        for file in src_files:
            # Fetch the code from GitHub
            content = get_file_content(repo_name, file, commit_sha)

            # Generate unit tests using OpenAI's GPT-4 model
            test_code = generate_unit_test(content, OPENAI_API_KEY)

            # Save the generated unit test in the tests/ directory
            os.makedirs("tests", exist_ok=True)
            print(f"Directory 'tests' exists: {os.path.exists('tests')}")
            test_file_path = os.path.join("tests", f"test_{os.path.basename(file)}")

            print(f"Generating tests for: {file}")
            with open(test_file_path, "w") as f:
                f.write(test_code)
                print(f"Test file saved at: {test_file_path}")

            # Commit and push the generated test file to GitHub
            commit_and_push_test_files(repo_name, test_file_path, test_code)

        # Run the generated tests
        test_results = run_tests()
        post_github_comment(repo_name, commit_sha, test_results)

    return {"status": "Tests generated and executed"}

def get_file_content(repo, file_path, commit_sha):
    """Fetch file content from GitHub."""
    url = f"https://api.github.com/repos/{repo}/contents/{file_path}?ref={commit_sha}"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch file: {file_path}, Status Code: {response.status_code}")
    
    content = response.json().get("content", "")
    return base64.b64decode(content).decode("utf-8")

def commit_and_push_test_files(repo_name, test_file_path, test_code):
    """Commit and push the generated test files to GitHub"""
    
    # Authenticate with GitHub using the token
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(repo_name)
    
    # Create or update the test file in the repository
    try:
        file_content = repo.get_contents(test_file_path, ref="main")
        # If the file already exists, update it
        repo.update_file(file_content.path, "Update generated test file", test_code, file_content.sha, branch="main")
    except:
        # If the file does not exist, create a new one
        repo.create_file(test_file_path, "Add generated test file", test_code, branch="main")

def run_tests():
    """Run tests using pytest and return results."""
    result = subprocess.run(["pytest", "tests/"], capture_output=True, text=True)
    return result.stdout

def post_github_comment(repo, commit_sha, test_results):
    """Post test results as a GitHub commit comment."""
    url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}/comments"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    data = {"body": f"### 🧪 Automated Test Results\n```\n{test_results}\n```"}
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 201:
        print(f"Failed to post comment: {response.status_code}, Response: {response.json()}")
