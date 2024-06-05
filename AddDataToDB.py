import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("AccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://face-recognition-data-340e4-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "atanu_06": {
        "name" : "Atanu Kundu",
        "stream" : "MCA",
        "gender" : "M",
        "total_attendance": 1,
        "standing": "Good",
        "last_attendance_time": "04-06-2024 10:00:00",
        "year": "2nd",
        "starting_year": 2022
    },
    "raima_31": {
        "name" : "Raima Mandal",
        "stream" : "MCA",
        "gender" : "F",
        "total_attendance": 1,
        "standing": "Good",
        "last_attendance_time": "04-06-2024 10:00:00",
        "year": "2nd",
        "starting_year": 2022
    },
    "upashana_25": {
        "name" : "Upashana Chatterjee",
        "stream" : "MCA",
        "gender" : "F",
        "total_attendance": 1,
        "standing": "Moderate",
        "last_attendance_time": "04-06-2024 10:00:00",
        "year": "2nd",
        "starting_year": 2022
    },
    "baishakhi_05": {
        "name" : "Baishakhi Patra",
        "stream" : "MCA",
        "gender" : "F",
        "total_attendance": 1,
        "standing": "Moderate",
        "last_attendance_time": "04-06-2024 10:00:00",
        "year": "2nd",
        "starting_year": 2022
    }
}

for key, value in data.items():
    ref.child(key).set(value)