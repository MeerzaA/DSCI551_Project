# IMPORT LIBRARIES
import json
import requests
import sys
import uuid
from geopy.distance import geodesic

# Firebase Database URLs (Replace these URLs with your actual Firebase URLs)
DATABASE_URLS = {
    "data_1": "https://dsci-studyyelp-1-default-rtdb.firebaseio.com/",
    "data_2": "https://dsci-studyyelp-2-288ca-default-rtdb.firebaseio.com/"
}

# Initialize an empty hash table for study spots indexed by location
study_spot_index = {}

def hash_location(location):
    return abs(hash(location))


def update_index(spot_id, spot_data):
    # Update the study_spot_index with the spot_id and spot_data
    location = spot_data.get("city")  # Assuming city is the key for indexing
    hashed_location = hash_location(location)
    if hashed_location not in study_spot_index:
        study_spot_index[hashed_location] = []
    study_spot_index[hashed_location].append(spot_id)
    print("Updated study_spot_index:", study_spot_index)  # Print the index after update


def add_study_spot(spot_data):
    # INPUT: study spot data from command line
    # RETURN: status code after python REST call to add study spot [response.status_code]
    # EXPECTED RETURN: 200
    # Generate a new UUID for the spot ID
    spot_id = str(uuid.uuid4())
    # Add the spot ID to the spot data
    spot_data["spot_id"] = spot_id
    # Check if all necessary attributes exist in the spot data
    if "address" not in spot_data or "city" not in spot_data or "state" not in spot_data or "postal_code" not in spot_data:
        print("Error: Required attributes (address, city, state, postal_code) are missing in the input data.")
        return 400
    
    # Construct the location string
    location = spot_data["address"] + ", " + spot_data["city"] + ", " + spot_data["state"] + ", " + spot_data["postal_code"]
    
    # Determine the database URL based on the hashed location
    hashed_location = hash_location(location)
    if hashed_location % 2 == 0:
        database_url = DATABASE_URLS["data_1"]
    else:
        database_url = DATABASE_URLS["data_2"]

    database_url += "spots/"
        
    # Make the REST call to add the study spot
    response = requests.put(database_url + f"/{spot_id}.json", data=json.dumps(spot_data), headers={'Content-Type': 'application/json'})
    
    # Check if the operation was successful
    status_code = response.status_code
    if status_code == 200:
        update_index(spot_id, spot_data)  # Update index after adding a new spot
    return status_code
    
def search_study_spots_by_city(city):
    matching_spots = {}
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + f"/spots.json?orderBy=\"city\"&equalTo=\"{city}\"")
        if response.status_code == 200:
            try:
                study_spots = response.json()
                matching_spots.update(study_spots)
            except json.decoder.JSONDecodeError:
                print(f"Failed to decode JSON response from {db_url}")
        else:
            print(f"Failed to retrieve study spots from {db_url}. Status code: {response.status_code}")
    return matching_spots

def search_study_spot_by_id(spot_id):
    # INPUT: ID of the study spot
    # RETURN: JSON object containing the information of the study spot with the given ID [spot_data]
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + f"/spots/{spot_id}.json")
        if response.status_code == 200:
            study_spot_data = response.json()
            return study_spot_data
        else:
            print(f"Failed to retrieve study spot by ID {spot_id} from {db_url}. Status code: {response.status_code}")
    return None

def search_study_spots_by_postal_code(postal_code):
    matching_spots = {}
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + f"/spots.json?orderBy=\"postal_code\"&equalTo=\"{postal_code}\"")
        if response.status_code == 200:
            try:
                study_spots = response.json()
                matching_spots.update(study_spots)
            except json.decoder.JSONDecodeError:
                print(f"Failed to decode JSON response from {db_url}")
        else:
            print(f"Failed to retrieve study spots from {db_url}. Status code: {response.status_code}")
    return matching_spots

def search_study_spots_by_state(state):
    matching_spots = {}
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + f"/spots.json?orderBy=\"state\"&equalTo=\"{state}\"")
        if response.status_code == 200:
            try:
                study_spots = response.json()
                matching_spots.update(study_spots)
            except json.decoder.JSONDecodeError:
                print(f"Failed to decode JSON response from {db_url}")
        else:
            print(f"Failed to retrieve study spots from {db_url}. Status code: {response.status_code}")
    return matching_spots

def calculate_distance(coord1, coord2):
    # coord1 and coord2 are tuples containing latitude and longitude, e.g., (lat1, lon1)
    return geodesic(coord1, coord2).kilometers

def search_study_spots_by_distance(origin_location, max_distance_km):
    matching_spots = {}
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + "/spots.json")
        if response.status_code == 200:
            try:
                study_spots = response.json()
                for spot_id, spot_data in study_spots.items():
                    spot_location = (spot_data.get("latitude"), spot_data.get("longitude"))
                    # Calculate distance between origin_location and spot_location
                    distance = calculate_distance(origin_location, spot_location)
                    if distance <= max_distance_km:
                        matching_spots[spot_id] = spot_data
            except json.decoder.JSONDecodeError:
                print(f"Failed to decode JSON response from {db_url}")
        else:
            print(f"Failed to retrieve study spots from {db_url}. Status code: {response.status_code}")
    return matching_spots

def modify_study_spot(spot_id, new_spot_data):
    for db_url in DATABASE_URLS.values():
        response = requests.put(f"{db_url}/spots/{spot_id}.json", data=json.dumps(new_spot_data), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            print(f"Study spot with ID {spot_id} modified successfully.")
            return True
        else:
            print(f"Failed to modify study spot with ID {spot_id}. Status code: {response.status_code}")
    return False

def delete_study_spot(spot_id):
    for db_url in DATABASE_URLS.values():
        response = requests.delete(f"{db_url}/spots/{spot_id}.json")
        if response.status_code == 200:
            print(f"Study spot with ID {spot_id} deleted successfully.")
            return True
        else:
            print(f"Failed to delete study spot with ID {spot_id}. Status code: {response.status_code}")
    return False





###def search_study_spots_by_category(category):
    matching_spots = {}
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + f"/spots.json?orderBy=\"categories\"&equalTo=\"{category}\"")
        if response.status_code == 200:
            try:
                study_spots = response.json()
                matching_spots.update(study_spots)
            except json.decoder.JSONDecodeError:
                print(f"Failed to decode JSON response from {db_url}")
        else:
            print(f"Failed to retrieve study spots from {db_url}. Status code: {response.status_code}")
    return matching_spots
###

# Use the below main method to test your code
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py [operation] [arguments]")
    else:
        operation = sys.argv[1].lower()
        if operation == "add_study_spot":
            result = add_study_spot(json.loads(sys.argv[2]))
            print(result)
        elif operation == "search_study_spots_by_city":
            city = sys.argv[2]
            study_spots = search_study_spots_by_city(city)
            print(study_spots)
        elif operation == "search_study_spot_by_id":
            spot_id = sys.argv[2]
            study_spot = search_study_spot_by_id(spot_id)
            print(study_spot)
        elif operation == "search_study_spots_by_postal_code":
            postal_code = sys.argv[2]
            study_spots = search_study_spots_by_postal_code(postal_code)
            print(study_spots)
        elif operation == "search_study_spots_by_state":
            state = sys.argv[2]
            study_spots = search_study_spots_by_state(state)
            print(study_spots)
        elif operation == "search_study_spots_by_distance":
            location = (float(sys.argv[2]), float(sys.argv[3]))  # Pass latitude and longitude as arguments
            max_distance_km = float(sys.argv[4])
            study_spots = search_study_spots_by_distance(location, max_distance_km)
            print(study_spots)
        elif operation == "modify_study_spot":
            spot_id = sys.argv[2]
            new_spot_data = json.loads(sys.argv[3])
            success = modify_study_spot(spot_id, new_spot_data)
            print("Modification successful." if success else "Modification failed.")
        elif operation == "delete_study_spot":
            spot_id = sys.argv[2]
            success = delete_study_spot(spot_id)
            print("Deletion successful." if success else "Deletion failed.")
