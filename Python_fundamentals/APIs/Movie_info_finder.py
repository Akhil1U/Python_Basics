# 3. Movie Info Finder
# Use: OMDB API
# --> Search a movie title, return ratings, plot, cast, etc.

import os
import requests
from dotenv import load_dotenv

def load_api_key(movie_name, release_year):
    load_dotenv()
    api_key = os.getenv("OMDB_API_KEY")
    if not api_key:
        raise ValueError("API key not found ")
    return f"http://www.omdbapi.com/?&t={movie_name}&y={release_year}&plot=full&apikey={api_key}"


def fetch_data(api):
    try:
        response = requests.get(api)
        if response.status_code == 200:

            return response.json()
        else:
            print("HTTP Error ocurred.")

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


def Movie_finder(data):

    print("\n🎬 Movie Information:")
    print("-" * 40)
    print(f"Title: {data.get('Title')}")
    print("Released Date: ",data["Released"])
    print("Genre: ",data["Genre"])
    print("Director: ", data["Director"])
    print("Actors: ", data["Actors"])
    print("Country: ", data["Country"])
    print("Ratings Source: ",data["Ratings"][0]["Source"])
    print("Ratings: ",data["Ratings"][0]["Value"])

    print("-" * 40)
 

def main():
    
        movie_name = input("please enter movie name to search: ").strip()
        release_year = input("enter release year of movie: ").strip()

        api = load_api_key(movie_name, release_year)
        data = fetch_data(api)
        if data and data.get("Response") == "True":
            Movie_finder(data)
        
        elif data.get("Response") == "False":
            print("Resource not found..! plase enter correct title and try again: ")
            main()
        
        else:
            print("Else ")

if __name__ == "__main__":
    main()


