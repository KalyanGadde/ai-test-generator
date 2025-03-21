import openai

def generate_unit_test(file_content, openai_api_key):
    openai.api_key = openai_api_key
    
    # prompt = f"Generate Python unit test cases using pytest for the following code. Do not include any markdown code block syntax (like ```python) in your response. Also include all imports needed including all files in test folder:\n{file_content}"
    
    prompt = f"""
    You are an expert Python developer. Your task is to generate comprehensive unit tests for the following function.
    Do not include any markdown code block syntax (like ```python)
    1. If the function definition is missing, first define it properly before writing the tests.
    2. Include all necessary imports such as `pytest` and any required libraries such as locally all files under tests/.
    3. Save the test files inside a `tests/` directory, ensuring the correct file structure.
    4. Use `pytest` conventions, with multiple test cases covering various edge cases.
    5. Do not include any markdown code block syntax (like ```python)
    6. Import all files from folder src (like from src import ...)
    {file_content}
    Generate the **complete** test file, ensuring it works without modifications.
    """
    
    print("file_content: ", file_content)
    
    # OpenAI API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    
    # Debugging: Print the OpenAI response
    print("OpenAI Response:", response)

    # Extracting and returning the generated test code
    return response['choices'][0]['message']['content']
