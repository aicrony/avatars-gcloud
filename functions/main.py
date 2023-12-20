import os
import json
from dotenv import load_dotenv

# ----------- PRODUCTION DATABASE ----------- #
# from gcloud.create_firestore_client import create_firestore_client
# load_dotenv()
# db = create_firestore_client("os.getenv('FIRESTORE_CREDS')")


# ----------- EMULATOR DATABASE ----------- #
from emulator.create_emulator_client import create_firestore_client
load_dotenv()
db = create_firestore_client(os.getenv('FIRESTORE_EMULATOR_HOST'))


# TODO = "
#  1. Create this function (main.py) in gcloud using 'gcloud deploy'
#  2. After creation, use the URL received to create a webhook in Ghost
#  3. Add the webhook URL in Ghost for members.add, members.edit, members.delete
#  4. Use a JWT token to authenticate the user when opening the URL to the application
#  5. Call the database to verify user details, and only allow paid users to use the premium features
#   "


def get_user(user_id):
    try:
        doc = db.collection('users').document(user_id).get()

        if doc.exists:
            return f'{doc.id} => {doc.to_dict()}'
        else:
            print(f'Error: No user with id {user_id} found in the database.')
            return 'No such user!', 404

    except Exception as e:
        print(f'An error occurred: {e}')
        return 'An error occurred while processing the request', 500


def set_user(request):
    try:
        # Parse the request body
        request_json = json.loads(request.data)
        user = request_json.get('user')

        if not user:
            return 'Invalid request', 400

        # Add the user's information to the Firestore database
        doc_ref = db.collection('users').document(user['id'])
        doc_ref.set({
            'name': user['name'],
            'email': user['email'],
            # Add other user properties here
        })

        return 'User added to Firestore', 200

    except json.JSONDecodeError:
        return 'Invalid JSON format', 400

    except Exception as e:
        print(f'An error occurred: {e}')
        return 'An error occurred while processing the request', 500


def list_users():
    try:
        # Fetch all documents from 'users' collection
        docs = db.collection('users').stream()

        # Flag to check if any documents were processed
        doc_exists = False

        # Print all documents
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
            doc_exists = True

        # Check if any documents were processed
        if not doc_exists:
            return 'No records found in the users collection.'

    except Exception as e:
        print(f'An error occurred: {e}')
        return 'An error occurred while processing the request', 500


