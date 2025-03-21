from ai_test_generator import generate_unit_test
import openai
import os
from dotenv import load_dotenv

# Test content to generate pytest for
file_content = """
def add(a, b):
    return a + b
"""
load_dotenv()
# Load the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI key:", openai_api_key)

# Generate the unit test
generated_tests = generate_unit_test(file_content, openai_api_key)

# Print the generated test code
print("Generated Test Code:\n", generated_tests)
