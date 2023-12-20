import os
from google.auth import credentials
import firebase_admin
from firebase_admin import credentials, firestore


def create_firestore_client(emulator_host):
    os.environ["FIRESTORE_EMULATOR_HOST"] = emulator_host
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'avatars-e0156',
    })
    return firestore.client()
