# IMPORT LIBRARIES
import json
import requests
import sys

# Firebase Database URLs (Replace these URLs with your actual Firebase URLs)
DATABASE_URLS = {
    "general_info": "https://your-project-id.firebaseio.com/general_info.json",
    "reviews_1": "https://your-project-id.firebaseio.com/reviews_1.json",
    "reviews_2": "https://your-project-id.firebaseio.com/reviews_2.json",
    "reviews_3": "https://your-project-id.firebaseio.com/reviews_3.json",
    "reviews_4": "https://your-project-id.firebaseio.com/reviews_4.json",
    "reviews_5": "https://your-project-id.firebaseio.com/reviews_5.json"
}

## Define any global methods
# HERE
def add_study_spot(spot_id, spot_data):
    # INPUT : study spot id and spot data from command line
    # RETURN : status code after python REST call to add study spot [response.status_code]
    # EXPECTED RETURN : 200
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
