from flask import Flask, jsonify, request
import requests
import infer_audio
from io import BytesIO
import scipy.io.wavfile as sciwav
import wave
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
        file = request.files
        # num_keys = len(file.keys())
        total_dict = file.to_dict()
        items = total_dict.keys()
        storage = total_dict['messageFile']
        data = storage.read()
        new_filename = 'test_sound_api.wav'
        # with wave.open(new_filename, 'wb') as obj:
        #     obj.setnchannels(1) #mono
        #     obj.writeframesraw(data)
        with open(new_filename, mode='wb') as f:
            f.write(data)
            f.close()

        data_type = type(data)
        storage_type = type(storage)
        #print(type(data))
        # wrapper = BytesIO(data)
        # print(type(wrapper))
        # wav_file = sciwav.read(wrapper)
        # print(type(wav_file))
        score = infer_audio.process_wav_file(new_filename)
        length = len(data)
        filename = storage.filename
        stream = storage.stream
        return f"""length is {length}  \n storage type is are {storage_type}, score is {score}"""
    elif request.method == 'GET':
        return 'get method received'


if __name__ == 'main':
    app.run(debug=True)
