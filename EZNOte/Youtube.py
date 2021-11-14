import requests 
import youtube_dl
import sys
import time
import json





#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json
app = Flask(__name__)
a = ''
@app.route('/')
def output():
	# serve index template
	return render_template('popup.html')
@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json()
	result = ''
	for item in data:
		# loop over every row
		result += str(item)
	return result
if __name__ == '__main__':
	# run!
    app.run()

print(worker())



f = open("demofile.txt", "r")
script = f[0] 
print(script)

auth_key = "d0bc669fe76747e7a1b29c706c0feb75"


transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
headers_auth_only = {'authorization': auth_key}
headers = {
    "authorization" : auth_key,
    "content-type" : "application/json"
}
ydl_opts = {
    'format' : 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality' : '192',
    }],
    'ffmpeg-location': './',
    'outtmpl': "./%(id)s.%(ext)s",
}

def get_vid(_id):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(_id)

link_of_video = "https://www.youtube.com/watch?v=SmxEU_9ATTc&t=95s"
_id = link_of_video.strip()
print(_id)
meta = get_vid(_id)

filename = meta["id"] + ".mp3" 
def read_file(filename, chunk_size = 5242880):
    with open(filename, 'rb') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data
upload_response = requests.post(
    upload_endpoint,
    headers=headers_auth_only, data=read_file(filename)
)

transcript_request = {
    'audio_url' : upload_response.json()['upload_url']
}

print(upload_response.json())
result = upload_response.json()

transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers = headers)

polling_endpoint = "https://api.assemblyai.com/v2/transcript/" + transcript_response.json()['id']
polling_response = requests.get(polling_endpoint, headers=headers)
print(polling_response.json()['status'])
time.sleep(98)
paragraphs_endpoint = polling_endpoint + "/paragraphs"
sentences_endpoint = polling_endpoint + "/sentences"
paragraphs_response = requests.get(paragraphs_endpoint, headers = headers)
sentences_response = requests.get(sentences_endpoint, headers = headers)
print(json.dumps(paragraphs_response.json(), indent=2))
