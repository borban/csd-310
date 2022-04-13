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

shemp = {
    "student_id" : 1010,
    "first_name" : "Shemp",
    "last_name" : "Q",
    "enrollments" : [
        {
            "term" : "SPRING2022",
            "gpa" : 4.0,
            "start_date" : "01/01/2022",
            "end_date" : "06/01/2022",
            "courses" : [
                {
                    "course_id" : 123,
                    "description" : "Database Development",
                    "instructor" : "Professor John Woods",
                    "grade" : "A"
                }
            ]
        }
    ]
}

shemp_student_id = db.students.insert_one(shemp).inserted_id
print("\n-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id " + str(shemp_student_id))

doc = db.students.find_one({"student_id" : 1010})

print("\n-- DISPLAYING STUDENT TEST DOC --")
print("Student ID: ",  doc["student_id"])
print("First Name: ",  doc["first_name"])
print("Last Name: ", doc["last_name"] + "\n")

db.students.delete_one({"student_id" : 1010})

docs = db.students.find()

print("-- DISPLAYING DOCUMENTS FROM THE find() query --")

for document in docs:
    print("Student ID: ",  document["student_id"])
    print("First Name: ",  document["first_name"])
    print("Last Name: ", document["last_name"] + "\n")