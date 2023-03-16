import openai
import os

# Get OpenAI API Key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY", None)


def openai_process_message(user_message):
    # Set the prompt for OpenAI Api
    messages = [
        {
            "role": "system",
            "content": "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
        },
        {"role": "user", "content": user_message}
    ]
    # Call the OpenAI Api to process our prompt
    openai_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=2000)
    
    print("openai response:", openai_response)
    # Parse the response to get the response text for our prompt
    response_text = openai_response.choices[0].message.content
    return response_text
