from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="New York"):

    request_url=f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    try:
        weather_data = requests.get(request_url).json() 
    except:
        weather_data = {
            'cod': 300,
            'message': 'The network is shut down.'
        }
    
    return weather_data

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name: \n")

    # Check for empth strings or strings only with speces
    if not bool(city.strip()):
        city = "Kansas City"

    weather_data = get_current_weather(city)
    pprint(weather_data)

    print("\n*** Thanks For Your Request ***\n")