import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'avatars-e0156',
})

db = firestore.client()

# Point to the Firestore emulator running on localhost
# os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"

# Remember to replace 'my-project-id' with your actual project ID. The Firestore emulator will be running on
# localhost:8080 (or whatever port you set it to).

# "firebase init" will prompt you to set up Emulators
# export FIRESTORE_EMULATOR_HOST="localhost:8080"
# Start the emulator:
# "firebase emulators:start"




