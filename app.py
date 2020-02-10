from flask import Flask, request
from config import API_KEY, IP
import requests

app = Flask(__name__)

@app.route('/')
def index():

    #ip = request.remote_addr

    astro_data = requests.get('https://api.ipgeolocation.io/astronomy?apiKey=' + API_KEY + '&ip=' + IP).json()



    location_info = astro_data['location']

    user_ip = location_info['ip']

    user_country = location_info['country_name']

    user_state = location_info['state_prov']

    user_district = location_info['district']

    user_city = location_info['city']

    


    return "Hello World"


