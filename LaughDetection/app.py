from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/api/audio', methods=['GET', 'POST'])
def get_score():
    if request.method == 'POST':
        # try:
        #     #content_type = request.content_type()
        #     #length = request.content_length()
        #     stream = request.content_type()
        #     if stream is None:
        #         return 'input_stream data not captured'
        #     else:
        #         return 'Here is the stream data {}'.format(stream)
        # except Exception as e:
        #     #return ('error is {}'.format(e))
        #     return ('error is {}'.format(e))
        return (request.content_type)
    elif request.method == 'GET':
        return 'get method received'


if __name__ == 'main':
    #send_audio()
    app.run(debug=True)
