import openai

# This function will generate unit tests for the provided code using OpenAI's GPT-4 model.
def generate_unit_test(file_content, openai_api_key):
    openai.api_key = openai_api_key
    
    prompt = f"Generate Python unit tests for the following code using pytest:\n{file_content}"
    
    # OpenAI API request
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    
    # Extracting and returning the generated test code
    return response['choices'][0]['message']['content']
