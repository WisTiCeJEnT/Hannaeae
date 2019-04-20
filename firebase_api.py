import pyrebase
import json
import os

def addNewMsg(data):
    req_msg = data["req_msg"]
    db.child("/msg/").child(req_msg).set(data)

def getAllMsg():
    return db.child("/msg/").get().val()

#init
#gen serviceAccoutFile
f = open("./saf.json", 'w')
saf = {}
saf["type"] = "service_account"
saf["project_id"] = "hannaeae-db"
saf["auth_uri"] = "https://accounts.google.com/o/oauth2/auth"
saf["token_uri"] = "https://oauth2.googleapis.com/token"
saf["auth_provider_x509_cert_url"] = "https://www.googleapis.com/oauth2/v1/certs"
saf["client_id"] = "105901278562874977647"
saf["client_email"] = "firebase-adminsdk-kzut3@hannaeae-db.iam.gserviceaccount.com"
saf["private_key_id"] = os.environ["private_key_id"]
saf["private_key"] = os.environ["private_key"]
f.write(json.dumps(saf, sort_keys=True, indent=4, separators=(',', ': ')))
f.close()

config = {
    "apiKey": os.environ["FIREBASE_API_KEY"],
    "authDomain": "https://hannaeae-db.firebaseapp.com/",
    "databaseURL": "https://hannaeae-db.firebaseio.com/",
    "storageBucket": "https://hannaeae-db.appspot.com/",
    #"serviceAccount": "./saf.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
