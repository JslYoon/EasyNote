from flask import Flask, render)template, request, redirect, session
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processUserInfo<string:userInfo>', methods['POST'])
def processUserInfo(userInfo):
    userInfo = json.loads(userInfo)
    print(f"hi: {userInfo['string']}")
