import base64
import json
from flask import Flask, render_template, request
from worker import openai_process_message
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/process-message', methods=['POST'])
def process_prompt_route():
    user_message = request.json['userMessage'] # Get user's message from their request
    print('user_message', user_message)
    # Call openai_process_message function to process the user's message and get a response back
    openai_response_text = openai_process_message(user_message)
    # Clean the response to remove any emptylines
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])
    # Send a JSON response back to the user containing their message's response both in text and speech formats
    response = app.response_class(
        response=json.dumps({"openaiResponseText": openai_response_text}),
        status=200,
        mimetype='application/json'
    )
    print(response)
    return response


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
