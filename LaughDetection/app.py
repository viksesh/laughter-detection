from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return 'Hello from Server'


def send_audio():
    url = '/api/audio'
    file = open('/Users/kaushikandra/laughter-detection/LaughDetection/crowd_laugh_1.wav', 'rb')
    headers = {'content-type': 'audio/wav'}
    payload = {'client_id': 1}
    files = {'file': file}
    r = requests.post(url,files=files, data=data, headers=headers)
    print(r)
    print(r.text)

@app.route('/api/audio', methods=['GET', 'POST'])
def get_score():
    if request.method == 'POST':
        filepath = request.files['file']
        value = len(filepath)
        type = type(filepath)
        return ('got audio data and the number of value is {} \n \
                here are the keys {}'.format(value, type))


if __name__ == 'main':
    send_audio()
    app.run(debug=True)
