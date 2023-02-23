import openai
import os

# Get OpenAI API Key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY", None)


def openai_process_message(user_message):
    # Set the prompt for OpenAI Api
    prompt = "\"Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations. " + user_message + "\""
    # Call the OpenAI Api to process our prompt
    openai_response = openai.Completion.create(model="text-davinci-003", prompt=prompt,max_tokens=4000)
    print("openai response:", openai_response)
    # Parse the response to get the response text for our prompt
    response_text = openai_response.choices[0].text
    return response_text
