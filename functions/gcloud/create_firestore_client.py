from google.cloud import firestore


def create_firestore_client(service_account_key_file):
    return firestore.Client.from_service_account_json(service_account_key_file)
