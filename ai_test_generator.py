import openai

def generate_unit_test(file_content, openai_api_key):
    openai.api_key = openai_api_key
    
    prompt = f"Generate Python unit tests for the following code using pytest:\n{file_content}"
    
    # OpenAI API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    
    # Debugging: Print the OpenAI response
    print("OpenAI Response:", response)

    # Extracting and returning the generated test code
    return response['choices'][0]['message']['content']
