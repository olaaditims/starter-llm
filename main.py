# Basic Python LLM Starter

# Importing necessary libraries
import openai

# Set up OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Function to generate text using the LLM
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == '__main__':
    user_prompt = 'Hello, how do I start with LLM programming?'
    output = generate_text(user_prompt)
    print(output)