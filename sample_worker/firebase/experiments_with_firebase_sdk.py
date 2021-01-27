from firebase_admin.auth import UserRecord

from sample_worker.firebase.utils import initialize_admin_sdk, create_user, get_random_email, get_user_doc_path, \
    remove_user

if __name__ == "__main__":
    cred, app, firestore_client = initialize_admin_sdk(r"./dev-service-account.json")

    created_user: UserRecord = create_user(
        email=get_random_email(),
        email_verified=True,
        password='t35tpsvv55!'
    )

    result = firestore_client.document(get_user_doc_path(created_user.uid)).set({
        "email": created_user.email,
        "role": 'endUser',
        "devOpsMaturity": 'veryImmature'
    })

    print(result)

    remove_user(created_user.uid, firestore_client, delete_auth=False)
