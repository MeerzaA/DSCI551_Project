import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json



# Fetch the service account key JSON file contents
cred = credentials.Certificate('dsci551proj-cafe-yelp-b8035-firebase-adminsdk-g0wf1-f200957c47.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://dsci551proj-cafe-yelp-b8035-default-rtdb.firebaseio.com/"
})

ref = db.reference('/business')
#print(ref.get())

print(json.dumps(ref.get(), indent=4))

