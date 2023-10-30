from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

students={
    1:{
        "name":"john",
        "age":17,
        "year":"year 12"
    },
    2:{
        "name":"josh",
        "age":16,
        "year":"year 11"
    }

}

class Student(BaseModel):
    name:str
    age:int
    year:str
class UpdateStudent(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    year:Optional[str] = None
@app.get("/")
def index():
    return {"name":"first data"}
#path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="the id ofthe student you want to view",gt=0,lt=30)):
    return students[student_id]

#query parameter
@app.get("/get-by-name")
def get_student(*,name:Optional[str]):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"data":"not found"}

#combine path and query parameters
@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int,name:Optional[str]):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"data":"not found"}
#request body and post method
@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {"error":"student exists"}
    students[student_id]=student
    return students[student_id]

#put method
@app.put("/update-student/{student_id}")
def update_student(student_id:int,student: UpdateStudent):
    if not (student_id in students):
        return {"error":"student does not exist"}
    students[student_id]=student
    return students[student_id]

#delete method
@app.delete("/remove-student/{student_id}")
def remove_student(student_id:int):
    if not (student_id in students):
        return {"error":"student does not exist"}
    del students[student_id]
    return {"success":True}

