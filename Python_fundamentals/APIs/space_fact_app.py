import os
import requests
from dotenv import load_dotenv

# load api key from  secreate source
def load_api():
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    if not api_key:
        print("api key not found..!")
    return  f"https://api.nasa.gov/planetary/apod?api_key={api_key}&hd=true"


# looking for api response
def fetch_data(api):

    try:
        response = requests.get(api)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as errH:
        print("HTTPS Error", errH)
    except requests.exceptions.ConnectionError as errC:
        print("internet connection not found", errC)
    except requests.exceptions.Timeout as errT: 
        print("TimeOut Error", errT)
    except KeyError:
        print("Unexpected response format.")
    except Exception as e:
        print("Something alse! An error occurred:", e)
        
# if response is valid, we can get Astronomy Picture of the Day
def display_Daily_APOD(data):
    
    image_urls = data['hdurl']
    title = data["title"]
    explaination = data['explanation']
    date_of_apod = data['date']
    print()
    print(title,"--------------- date: ", date_of_apod, end = " ")
    print()
    print()
    print(explaination)
    print()
    print(image_urls)
    print()
  

def main():
    api = load_api()
    api_data = fetch_data(api)
    display_Daily_APOD(api_data)


if __name__ == "__main__":
    main()
