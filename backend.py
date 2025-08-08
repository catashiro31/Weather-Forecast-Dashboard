from datetime import datetime

import requests

API_KEY = 'API_KEY'

def get_data(place, day = None, kind = None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    request = requests.get(url)
    if request.status_code == 404:
        return None, None
    data =request.json()
    date_time = [datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S') for item in data['list']]
    temperature = [item['main']['temp']-273.15 for item in data['list']]
    weather = [item['weather'][0]['main'] for item in data['list']]
    if kind == 'Temperature':
        return date_time[:day*8], temperature[:day*8]
    else:
        return date_time[:day*8], weather[:day*8]

if __name__ == '__main__':
    print(get_data('djfke'))