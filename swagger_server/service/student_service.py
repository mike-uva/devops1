```
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# Could move this to .env file
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client.student_db
students_collection = db.students

def add(student=None):
    # Always allow insert
    # student_record = students_collection.find_one({
    #     "first_name": student.first_name,
    #     "last_name": student.last_name
    # })
    #
    # if student_record:
    #     return 'Student already exists', 409

    res = students_collection.insert_one(student.to_dict())
    student.student_id = str(res.inserted_id)
    return student.student_id

def get_by_id(student_id=None, subject=None):
    student = students_collection.find_one({"_id": ObjectId(student_id)})

    if not student:
        return 'not found', 404

    student['student_id'] = str(student['_id'])
    del student['_id']
    return student

def delete(student_id=None):
    res = students_collection.delete_one({"_id": ObjectId(student_id)})

    if res.deleted_count == 0:
        return 'not found', 404

    return student_id
```