import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("AccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://face-recognition-data-340e4-default-rtdb.firebaseio.com/",
    "storageBucket": "face-recognition-data-340e4.appspot.com"
})

# importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imagesList = []
studentIds = []
for path in pathList:
    imagesList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

# encoding func
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started....")
encodeListKnown = findEncodings(imagesList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Generated")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")