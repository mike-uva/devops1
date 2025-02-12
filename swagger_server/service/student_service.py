import os
import pymongo

client = pymongo.MongoClient(os.environ['MONGO_URI'])
db = client["university"]
collection = db["students1"]

def add(student=None):
    if collection.find_one({"first_name": student.first_name, "last_name": student.last_name}) is not None:
        return 'already exists', 409


    idx = collection.insert_one(student.to_dict()).inserted_id
    return str(idx), 200

def get_by_id(student_id=None, subject=None):
    student = collection.find_one({"student_id": student_id})
    if not student:
        return 'not found', 404
    print(student)
    return student

def delete(student_id=None):
    student = collection.find_one({"student_id": student_id})
    if not student:
        return 'not found', 404
    collection.delete_one(student)
    return student_id
