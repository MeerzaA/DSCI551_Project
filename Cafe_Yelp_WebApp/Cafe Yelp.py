# IMPORT LIBRARIES
import json
import requests
import sys
import geopy
from geopy.geocoders import Nominatim

# Firebase Database URLs (Replace these URLs with your actual Firebase URLs)
DATABASE_URLS = {
    "general_info": "https://your-project-id.firebaseio.com/general_info.json",
    "reviews_1": "https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/business_1.json",
    "reviews_2": "https://your-project-id.firebaseio.com/reviews_2.json",
    "reviews_3": "https://your-project-id.firebaseio.com/reviews_3.json",
    "reviews_4": "https://your-project-id.firebaseio.com/reviews_4.json",
    "reviews_5": "https://your-project-id.firebaseio.com/reviews_5.json"
}


# Hash Function to seperate nodes into east and west regions
# make sure to "pip install geocoder" before calling
def hsh_func_region(spot_data):

    latitude = spot_data["latitude"]
   
    #geolocator = Nominatim(user_agent="geo_locator") 
    #location = geolocator.reverse((latitude, longitude), language="en") 

    #state = location.raw.get("address", {}).get("state")        
    #print(state)

    # Any longitude value less than -100° is considered to be on the west

    if latitude > -100:
        return 1 # if east 
    else: 
        return 0 # if west 


## Define any global methods
# HERE
def add_study_spot(spot_id, spot_data):
    # INPUT : study spot id and spot data from command line
    # RETURN : status code after python REST call to add study spot [response.status_code]
    # EXPECTED RETURN : 200

    hsh_func_region(spot_data)

    response = requests.put(DATABASE_URLS["general_info"] + f"/{spot_id}.json", data=spot_data, headers={'Content-Type': 'application/json'})
    status_code = response.status_code
    return status_code
    
def search_study_spots_by_location(location):
    # INPUT: Location of the study spot
    # RETURN: JSON object having spot_ids as keys and spot information as value [spot_data] located in that location
    response = requests.get(DATABASE_URLS["general_info"] + f"?orderBy=\"location\"&equalTo=\"{location}\"")
    if response.status_code == 200:
        study_spots_by_location = response.json()
        return study_spots_by_location
    else:
        print(f"Failed to retrieve study spots by location. Status code: {response.status_code}")
        return None
    
def search_study_spot_by_id(spot_id):
    # INPUT: ID of the study spot
    # RETURN: JSON object containing the information of the study spot with the given ID [spot_data]
    response = requests.get(DATABASE_URLS["general_info"] + f"/{spot_id}.json")
    if response.status_code == 200:
        study_spot_data = response.json()
        return study_spot_data
    else:
        print(f"Failed to retrieve study spot by ID. Status code: {response.status_code}")
        return None

# Use the below main method to test your code
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py [operation] [arguments]")
    
    operation = sys.argv[1].lower()
    if operation == "add_study_spot":
        result = add_study_spot(sys.argv[2], sys.argv[3])
        print(result)
    elif operation == "search_study_spots_by_location":
        study_spots = search_study_spots_by_location(sys.argv[2])
        print(study_spots)
    elif operation == "search_study_spot_by_id":
        spot_id = sys.argv[2]
        study_spot = search_study_spot_by_id(spot_id)
        print(study_spot)
