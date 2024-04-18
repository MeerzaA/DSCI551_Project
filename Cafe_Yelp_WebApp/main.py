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
    '''
    COPY THE ID FOR LATER CODE

    python3 main.py add_study_spot '{
    "name": "LA Study Haven",
    "address": "456 Elm St",
    "city": "Los Angeles",
    "state": "CA",
    "postal_code": "90001",
    "latitude": 34.0522,
    "longitude": -118.2437,
    "stars": 5,
    "review_count": 20,
    "attributes": {
        "WiFi": "Free",
        "NoiseLevel": "Quiet",
        "OutdoorSeating": "Yes"
    },
    "categories": [
        "Coffee & Tea",
        "Library"
    ],
    "hours": {
        "Monday": "8:00-20:00",
        "Tuesday": "8:00-20:00",
        "Wednesday": "8:00-20:00",
        "Thursday": "8:00-20:00",
        "Friday": "8:00-20:00",
        "Saturday": "9:00-17:00",
        "Sunday": "10:00-16:00"
    }
}'
    '''
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
    '''
    python3 main.py search_study_spots_by_city 'Los Angeles'
    python3 main.py search_study_spots_by_city 'Indianapolis'
    '''
    matching_spots = {}
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + f"/spots.json?orderBy=\"city\"&limitToFirst=3&print=pretty&equalTo=\"{city}\"")
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
    '''
    python3 main.py search_study_spot_by_id '-WY14B9U3ys08E9PwKOB8g'
    python3 main.py search_study_spot_by_id 

    '''
    # INPUT: ID of the study spot
    # RETURN: JSON object containing the information of the study spot with the given ID [spot_data]
    matching_spots = {}
    for db_url in DATABASE_URLS.values():
        response = requests.get(db_url + f"/spots/{spot_id}.json")
        if response.status_code == 200:
            try:
                study_spot_data = response.json()
                matching_spots.update({spot_id: study_spot_data})
            except json.decoder.JSONDecodeError:
                print(f"Failed to decode JSON response from {db_url}")
        else:
            print(f"Failed to retrieve study spot by ID {spot_id} from {db_url}. Status code: {response.status_code}")
    return matching_spots

def search_study_spots_by_postal_code(postal_code):
    '''
    python3 main.py search_study_spots_by_postal_code '46219'
    python3 main.py search_study_spots_by_postal_code '90001'
    '''
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
    '''
    python3 main.py search_study_spots_by_state 'CA'
    python3 main.py search_study_spots_by_state 'IN'
    '''
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
    '''
    python3 main.py search_study_spots_by_distance 39.780987 -86.90468924 50
    python3 main.py search_study_spots_by_distance 27.9598673716 -82.5062573701 10
    '''
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
    '''
    python3 main.py modify_study_spot '33d95f8b-c4d7-4754-8f78-c2a8efd73a74' '{
    "name": "Modified Study Spot",
    "address": "456 Elm St",
    "city": "San Jose",
    "state": "CA",
    "postal_code": "95112",
    "latitude": 37.3382,
    "longitude": -121.8863,
    "stars": 5,
    "review_count": 20,
    "attributes": {
        "WiFi": "Free",
        "NoiseLevel": "Quiet",
        "OutdoorSeating": "No"
    },
    "categories": [
        "Coffee & Tea",
        "Library"
    ],
    "hours": {
        "Monday": "9:00-18:00",
        "Tuesday": "9:00-18:00",
        "Wednesday": "9:00-18:00",
        "Thursday": "9:00-18:00",
        "Friday": "9:00-18:00",
        "Saturday": "10:00-16:00",
        "Sunday": "Closed"
    }
}'

    '''
    for db_url in DATABASE_URLS.values():
        response = requests.put(f"{db_url}/spots/{spot_id}.json", data=json.dumps(new_spot_data), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            print(f"Study spot with ID {spot_id} modified successfully.")
            return True
        else:
            print(f"Failed to modify study spot with ID {spot_id}. Status code: {response.status_code}")
    return False

def delete_study_spot(spot_id):
    '''
    python3 main.py delete_study_spot '33d95f8b-c4d7-4754-8f78-c2a8efd73a74'
    '''
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
        
        elif operation == "search_study_spots_by_city": # Search by City
            # python ./main.py search_study_spots_by_city 'Los Angeles'
            # python ./main.py search_study_spots_by_city 'Indianapolis'
            city = sys.argv[2]
            study_spots = search_study_spots_by_city(city)
            print(json.dumps(dict(list(study_spots.items())[:2]), indent=4))
        
        elif operation == "search_study_spot_by_id": # Search by ID
            # python ./main.py search_study_spot_by_id '-WY14B9U3ys08E9PwKOB8g'
            # python ./main.py search_study_spot_by_id 'ykJ9zt1fJ1cOpxz5FkpVOQ'
            spot_id = sys.argv[2]
            study_spot = search_study_spot_by_id(spot_id)
            print(json.dumps(dict(list(study_spot.items())[:2]), indent=4))
        
        elif operation == "search_study_spots_by_postal_code": # Search by Posatal Code
            # python ./main.py search_study_spots_by_postal_code '46219'
            # python ./main.py search_study_spots_by_postal_code '90001'
            postal_code = sys.argv[2]
            study_spots = search_study_spots_by_postal_code(postal_code)
            print(json.dumps(dict(list(study_spots.items())[:1]), indent=4))
        
        elif operation == "search_study_spots_by_state": # Search by State
            # python ./main.py search_study_spots_by_state 'CA'
            state = sys.argv[2]
            study_spots = search_study_spots_by_state(state)
            print(json.dumps(dict(list(study_spots.items())[:1]), indent=4))
        
        elif operation == "search_study_spots_by_distance": # Pass latitude and longitude as arguments
            # python ./main.py search_study_spots_by_distance 27.9598673716 -82.5062573701 10
            location = (float(sys.argv[2]), float(sys.argv[3]))  
            max_distance_km = float(sys.argv[4])
            study_spots = search_study_spots_by_distance(location, max_distance_km)
            print(json.dumps(dict(list(study_spots.items())[:1]), indent=4))
        
        elif operation == "modify_study_spot": # Modify a Spots
            # python ./main.py modify_study_spot '33d95f8b-c4d7-4754-8f78-c2a8efd73a74' '{\"name\": \"Modified Study Spot\",\"address\": \"456 Elm St\",\"city\": \"San Jose\",\"state\": \"CA\",\"postal_code\": \"95112\",\"latitude\": 37.3382,\"longitude\": -121.8863,\"stars\": 5,\"review_count\": 20,\"attributes\": {\"WiFi\": \"Free\",\"NoiseLevel\": \"Quiet\",\"OutdoorSeating\": \"No\"},\"categories\": [\"Coffee & Tea\",\"Library\"],\"hours\": {\"Monday\": \"9:00-18:00\",\"Tuesday\": \"9:00-18:00\",\"Wednesday\": \"9:00-18:00\",\"Thursday\": \"9:00-18:00\",\"Friday\": \"9:00-18:00\",\"Saturday\": \"10:00-16:00\",\"Sunday\": \"Closed\"}}'
            spot_id = sys.argv[2]
            new_spot_data = json.loads(sys.argv[3])
            success = modify_study_spot(spot_id, new_spot_data)
            print("Modification successful." if success else "Modification failed.")
        
        elif operation == "delete_study_spot": # Delete a spot
            # python main.py delete_study_spot '33d95f8b-c4d7-4754-8f78-c2a8efd73a74'
            spot_id = sys.argv[2]
            success = delete_study_spot(spot_id)
            print("Deletion successful." if success else "Deletion failed.")
