import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAFaiqVZ1wTmPkKJZvWf8gPjfVEiWWy7mw",
    "authDomain": "movie-ab85f.firebaseapp.com",
    "databaseURL": "https://movie-ab85f-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "movie-ab85f",
    "storageBucket": "movie-ab85f.firebasestorage.app",
    "messagingSenderId": "429674536464",
    "appId": "1:429674536464:web:1f9682d9f95210d5a5f495",
    "measurementId": "G-S1X7BW39CS"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
