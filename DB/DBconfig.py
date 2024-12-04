from asyncio import exceptions
import firebase_admin
from firebase_admin import credentials, db
 
try:
    # Firebase Admin SDK 초기화
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://capstone-2402-default-rtdb.firebaseio.com"
    })
except exceptions.FirebaseError as e:
    print(f"Firebase initialization error: {e}")
    exit(1)

# Firebase DB 참조
reader_test_table = db.reference("ReaderTest")
queue_table = db.reference("Queue")
patients_table = db.reference("Patients")
output_table = db.reference("Output")

# DB 참조를 export
__all__ = ["reader_test_table", "queue_table", "patients_table", "output_table"]
