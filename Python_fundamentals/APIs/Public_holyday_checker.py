import os
import requests
from dotenv import load_dotenv


def api_loader(country,year,month,day):
    load_dotenv()
    api_key = os.getenv("ABSTRACT_API")

    if not api_key:
        raise ValueError("API key not found ")
    return f"https://holidays.abstractapi.com/v1/?api_key={api_key}&&country={country}&year={year}&month={month}&day={day}"


def fetch_data(api):
    try:
        response = requests.get(api)
        
        if response.status_code == 200:

            return response.json()
        else:
            print("HTTP Error ocurred.")
            print(response.status_code)
            print("Response:", response.text)

    except requests.exceptions.HTTPError as ErrH:
        print("Http Error..!",ErrH)
    except requests.exceptions.ConnectionError as ErrorC:
        print("Network Error",ErrorC)
    except requests.exceptions.Timeout as  ErrT:
        print("time out Error",ErrT)
    except KeyError as ErrK:
        print("Unexpected response format",ErrK)
    except Exception as E:
        print("Something else...!!!!",E)



def finds_holidays(data):
    
    print("*"*50)
    for holidays in data:
        print("holiday name: ",holidays["name"])
        print("country: ",holidays["location"])
        print("holiday date: ", holidays["date"])
        print("day pf week: ",holidays["week_day"])
        print("-"*50)

    
def main():
    country = input("please enter country to find their holiday : ").strip().upper()
    year = input("please enter year to find their holiday : ").strip()
    month = input("please enter month to find their holiday : ").strip()
    day = input("please enter day to find their holiday : ").strip()


    api = api_loader(country,year,month,day)

    data = fetch_data(api)
    if data:
        finds_holidays(data)


if __name__ == "__main__":
    main()



