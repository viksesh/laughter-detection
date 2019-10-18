from flask import Flask, jsonify, request, send_file
import requests

def send_audio():
    #print('attempting to send audio')
    url = 'http://127.0.0.1:5000/api/audio'
    with open('/Users/kaushikandra/laughter-detection/LaughDetection/crowd_laugh_1.wav', 'rb') as file:
        headers = {'content-type': 'audio/wav',
                   'connection': 'keep-alive'}
        myobj = {'somekey': 'somevalue'}
        payload = {'client_id': 1}
        sample = {'audio_test': file}
        r = requests.post(url, files=sample)
        print(r.text)

if __name__ == '__main__':
    send_audio()

#send_audio()
