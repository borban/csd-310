from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.fsjpm.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find()

print("-- DISPLAYING DOCUMENTS FROM THE find() query --")

for document in docs:
    
    print("Student ID: ",  document["student_id"])
    print("First Name: ",  document["first_name"])
    print("Last Name: ", document["last_name"] + "\n")
    
filter = {"student_id" : 1007}

db.students.update_one(filter, {'$set' : {"last_name" : "Queue"}})

updated_document = db.students.find_one({"student_id" : 1007})

print("-- DISPLAYING DOCUMENTS FROM THE find_one() query --")
print("Student ID: ",  updated_document["student_id"])
print("First Name: ",  updated_document["first_name"])
print("Last Name: ", updated_document["last_name"])