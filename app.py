from flask import Flask, request, render_template
from config import API_KEY, IP
import requests

app = Flask(__name__)

def astro_check():

    #ip = request.remote_addr

    astro_data = requests.get('https://api.ipgeolocation.io/astronomy?apiKey=' + API_KEY + '&ip=' + IP).json()



    location_info = astro_data['location']

    user_ip = location_info['ip']

    user_country = location_info['country_name']

    user_state = location_info['state_prov']

    user_district = location_info['district']

    user_city = location_info['city']

    date = astro_data['date']

    sunrise = astro_data['sunrise']

    sunset = astro_data['sunset']

    solar_noon = astro_data['solar_noon']

    day_length = astro_data['day_length']

    moonrise = astro_data['moonrise']

    moonset = astro_data['moonset']





@app.route('/')
def index():

    data = astro_check()

    return render_template('index.html', data=data)


