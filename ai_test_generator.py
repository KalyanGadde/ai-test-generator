import openai

def generate_unit_test(file_content, openai_api_key):
    openai.api_key = openai_api_key
    
    # prompt = f"Generate Python unit test cases using pytest for the following code. Do not include any markdown code block syntax (like ```python) in your response. Also include all imports needed including all files in test folder:\n{file_content}"
    
    prompt = f"""
    I have a Python project where all source files are inside a folder named src/, and I want to Generate Python unit test cases using pytest for the following code for those source files. Please generate test files and store them in a separate folder called tests/.
    
    Important:
        1. Do not include any markdown code block syntax (like ```python), just include actual test code.
        2. Do not use from mymodule import ... or from src.mymodule import ...
        3. Instead, use imports like from add_values import add (assuming the function is defined in src/add_values.py)
        4. In the test files, simulate that src/ is already added to sys.path, so the imports are directly from the file names (without src. prefix)
        5. Only generate test files using pytest style (functions starting with test_)
        6. Example: If the function is defined in src/add_values.py, write this in the test file:
        from add_values import add
        7. Now, generate a test file for the following module: src/add_values.py
        8. Also do not gerenate test files for __init__.py
        9. Make sure that we do not have any IndentationError
    {file_content}
    
   
    """
    
    # prompt = f"""
    # You are an expert Python developer. Your task is to generate comprehensive unit tests for the following function.
    # Do not include any markdown code block syntax (like ```python)
    # 1. If the function definition is missing, first define it properly before writing the tests.
    # 2. Include all necessary imports such as `pytest` and any required libraries such as locally all files under tests/.
    # 3. Save the test files inside a `tests/` directory, ensuring the correct file structure.
    # 4. Use `pytest` conventions, with multiple test cases covering various edge cases.
    # 5. Do not include any markdown code block syntax (like ```python)
    # 6. import all methods from files in src directory
    # 7. Import all files from folder src (such as 
    #     import sys
    #     import os
    #     # Add the parent directory of 'src' to sys.path
    #     sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
    #     from test_sample import add 
    #     Use `from test_sample import add`, NOT `from mymodule import add`
    #     )
    # {file_content}
    # Generate the **complete** test file, ensuring it works without modifications.
    # """
    
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
