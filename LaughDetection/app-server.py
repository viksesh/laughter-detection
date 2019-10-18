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
        length = request.content_length
        content_type = request.content_type
        text = request.data
        return f"""Request Text is  {text}"""
    elif request.method == 'GET':
        return 'get method received'


if __name__ == 'main':
    app.run(debug=True)
