import openai

def generate_unit_test(file_content, openai_api_key):
    openai.api_key = openai_api_key
    
    prompt = f"Generate Python unit test cases using pytest for the following code. Please ensure the output is valid Python code and avoid any Markdown or special formatting. The output should only contain Python code and follow correct Python syntax. Do not include any markdown code block syntax (like ```python) in your response.:\n{file_content}"
    
    # OpenAI API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    
    # Debugging: Print the OpenAI response
    print("OpenAI Response:", response)

    # Extracting and returning the generated test code
    return response['choices'][0]['message']['content']
