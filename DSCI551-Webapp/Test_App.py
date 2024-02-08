import firebase_admin
from firebase_admin import credentials
import json


cred = credentials.Certificate("dsci551-test-project-firebase-adminsdk-lrct5-9425caf0b2.json")
firebase_admin.initialize_app(cred)

