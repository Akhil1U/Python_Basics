
import os
import requests
from dotenv import load_dotenv


# laod api key 
def load_api_key():

    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("API key not found....")
    return api_key


# get weather detial
def fetch_weather_data(city_name, api_key):
   
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        return response.json()

     # exceptin handle       
    except requests.exceptions.HTTPError as errH:
        print("HTTPS Error", errH)
    except requests.exceptions.ConnectionError as errC:
        print("internet connection not found", errC)
    except requests.exceptions.Timeout as errT: 
        print("Time our Error", errT)
    except KeyError:
        print("Unexpected response format.")
    except Exception as e:
        print("Something alse! An error occurred:", e)

                                                                            
# weather data displayed by this function
def Display_weather(data, city_name):
    
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['description']
        
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")

def main():
    api_key = load_api_key()
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(city, api_key)
    if weather_data:
        Display_weather(weather_data,city)

# to check whether file run as ascript not whean imported as a imodule.
if __name__ == "__main__":
    main()








