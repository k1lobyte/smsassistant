from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import weather 
import json

app = Flask(__name__)

@app.route('/')
def index():
    """ Basic route """
    return json.dumps(weather.serve_weather('orlando,us'))

@app.route('/sms', methods=['GET', 'POST'])
def sms():
    """ Handles incoming sms """
    body = request.values.get('body', None)
    print(body)


if __name__ == "__main__":
    app.run(debug=True)
