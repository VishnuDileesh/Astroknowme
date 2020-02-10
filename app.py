from flask import Flask, request
from config import API_KEY, IP
import requests

app = Flask(__name__)

@app.route('/')
def index():

    #ip = request.remote_addr

    r = requests.get('https://api.ipgeolocation.io/astronomy?apiKey=' + API_KEY + '&ip=' + IP)

    print(r.content)


    return "Hello World"


