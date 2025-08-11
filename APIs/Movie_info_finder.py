# 3. Movie Info Finder
# Use: OMDB API
# --> Search a movie title, return ratings, plot, cast, etc.


import os
import requests
api ="http://www.omdbapi.com/?i=tt34365591&apikey=27593a9d"
response = requests.get(api)

data = response.json()

if response.status_code == 200:
    for key in data:
        print(key,":   ",data[key])
else:
    print("somethingelse")

