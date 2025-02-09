import os
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(os.environ['MONGO_URI'])  # Adjust the URI as needed
db = client["school"]  # Database name
students_collection = db["students"]  # Collection name


def add(student=None):
    existing_student = students_collection.find_one({
        "first_name": student.first_name,
        "last_name": student.last_name
    })

    if existing_student:
        return 'already exists', 409

    inserted_student = students_collection.insert_one(student.to_dict())
    student.student_id = str(inserted_student.inserted_id)
    return 200, student.student_id


def get_by_id(student_id=None, subject=None):
    student = students_collection.find_one({"_id": student_id})
    if not student:
        return 'not found', 404
    student['student_id'] = str(student['_id'])
    print(student)
    return student


def delete(student_id=None):
    result = students_collection.delete_one({"_id": student_id})
    if result.deleted_count == 0:
        return 'not found', 404
    return student_id
