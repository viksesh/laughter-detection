from flask import Flask, jsonify, request, send_file
import requests

def send_audio():
    #print('attempting to send audio')
    url = 'http://127.0.0.1:5000/api/audio'
    with open('/Users/kaushikandra/laughter-detection/LaughDetection/crowd_laugh_1.wav', 'rb') as file:
        data = {'uuid':'-jx-1', 'alarmType':1, 'timeDuration':10}
        files = {'messageFile': file}

        response = requests.post(url, files=files, json=data)
        print(response.request.headers)
        print(response.text)

if __name__ == '__main__':
    send_audio()
