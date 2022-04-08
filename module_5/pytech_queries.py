from mongodb_test import db

docs = db.students.find({})

for document in docs:
    print(document)

doc = db.students.find_one({"student_id" : 1007})

print(doc)