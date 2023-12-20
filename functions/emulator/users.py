import os
from create_emulator_client import create_firestore_client

# Point to the Firestore emulator running on localhost
db = create_firestore_client(os.getenv('FIRESTORE_EMULATOR_HOST'))

# Fetch all documents from 'users' collection
docs = db.collection('users').stream()

# Print all documents
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

print("Done.")
