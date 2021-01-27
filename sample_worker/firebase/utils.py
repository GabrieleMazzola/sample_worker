import math
import random

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin.auth import UserRecord
from google.cloud.firestore_v1 import ExistsOption
from google.cloud.firestore_v1.client import Client


def get_random_email():
    return f"testEmail{math.floor(random.randint(1, 100000))}@pythonsdk.com".lower()


def create_user(**kwargs) -> UserRecord:
    new_user = auth.create_user(**kwargs)
    print(f"Firebase successfully created a new user with \n\temail:'{new_user.email}'\n\tuser id:'{new_user.uid}'")
    return new_user


def remove_user(user_id: str, firestore_cl: Client, delete_firestore=True, delete_auth=True):
    """
    Both 'delete' operations fail if the document (for firestore) and the user (for auth) do not exist.
    """
    print(f"Removing user '{user_id}'")
    if delete_firestore:
        firestore_cl.document(get_user_doc_path(user_id)).delete(ExistsOption(exists=True))
    if delete_auth:
        auth.delete_user(user_id)


def get_user_doc_path(user_id: str):
    return f"users/${user_id}"


def initialize_admin_sdk(cred_path: str):
    cred = credentials.Certificate(cred_path)
    app = firebase_admin.initialize_app(cred)
    firestore_client: Client = firestore.client(app)
    return cred, app, firestore_client
