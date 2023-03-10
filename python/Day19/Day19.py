import requests
movie_name=input("Search which movie you want:")
response=requests.get(f"http://www.omdbapi.com/?t={movie_name}&apikey=1c9c01fb")
response_json=response.json()

try:
    print("Title:",response_json["Title"])
    print("Year:",response_json['Year'])
    print("Released:",response_json['Released'])
    print("Genre:",response_json['Genre'])
    print("Director",response_json["Director"])
except:
    print("This film doesnt exist!!!")