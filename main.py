from proto_code import User_pb2
import random
import string
import json

def randomString():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def addUserUsingProtoBuf(id, User):

    User.id = id
    User.username = randomString()
    User.email = randomString() + "@gmail.com"

    name = User.name.add()
    name.firstName = randomString()
    name.lastName = randomString()

    return

def addUserUsingJSON(id):
    
    userRecordsJson.append({
        "id": id,
        "username": randomString(),
        "name": {
            "firstName": randomString(),
            "lastName": randomString(),
        },
        "email": randomString() + "@gmail.com"
    })
    return


userRecords = User_pb2.UserRecords()
userRecordsJson = []

for i in range(1, 100):
    addUserUsingProtoBuf(i, userRecords.users.add())
    addUserUsingJSON(i)

file = open("data", "wb")
file.write(userRecords.SerializeToString())
file.close()

fileJson = open("data.json", "w")
json.dump(userRecordsJson, fileJson)
fileJson.close()

