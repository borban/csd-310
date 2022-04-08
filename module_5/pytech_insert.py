from mongodb_test import db

curly = {
    "student_id" : 1007,
    "first_name" : "Curly",
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

moe = {
    "student_id" : 1008,
    "first_name" : "Moe",
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

harry = {
    "student_id" : 1009,
    "first_name" : "Harry",
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

curly_student_id = db.students.insert_one(curly).inserted_id
print(curly_student_id)
moe_student_id = db.students.insert_one(moe).inserted_id
print(moe_student_id)
harry_student_id = db.students.insert_one(harry).inserted_id
print(harry_student_id)