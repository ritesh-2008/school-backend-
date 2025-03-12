from fastapi import FastAPI,Path,Query
from typing import Optional
from pydantic import BaseModel

app=FastAPI()
# students data
students={ 1:{"name":"ritesh",
               "age":17 ,
               "std":11},
            2:{"name":"aditya",
               "age":17,
               "std":11},
            3:{"name":"nayan",
               "age":17,
               "std":11},
            4:{"name":"yaser",
               "age":17,
               "std":11}      
        }
# trial
@app.get("/")
def index():
    return {"greeting":"thankyou for visiting here,type'/docs' beside the url"}


# getting accesse to data by id using path parameter

@app.get("/get_student/{student_id}") 
def get (student_id: int =Path(..., description="enter the id of student")):
    if student_id in students:
        return students[student_id]
    else:return{"error":"student does not exsist"}    

    
# getting access to data by name using query parameter
#combining path parametre to query parametre
@app.get("/get-bt-student/{student_id}")
def get_student(student_id :int=Path(...,description="enter the id of student"),name=Query(None,description=("enter the name of student"))):
    for students_id in students:
        if students[students_id]["name"]==name:
            return students[students_id]
    return {"data":"not found"} 


#acessing data by age using  query parametere
@app.get("/get_Age") 
def get_student(age:int= Query(...,description="enter the age")):
    for students_id in students:
        if students[students_id]["age"]==age:
            return students[students_id] 
    return {"data":"not found"}


# creating class for post parameter
class Student(BaseModel):
    name:str
    age:int
    std:int  
# creating post parametre for user input
@app.post("/create-student{student_id}")
def post_student(students_id:int,student:Student):
    if students_id in students:
        return {"data":"already exsit"}
    students[students_id]=student
    return students[students_id] 


# creating class for put method     
class update_student(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    std:Optional[int]=None
# put method is used for update the data already exsist
@app.put("/update/{students_id}") 
def update_students(students_id:int,student:update_student):
    if students_id not in students:
        return {"error":"student does not exsist"} 
# this if statement for avoiding error
    if student.name!=None:
        students[students_id].name=student.name 

    if student.age!=None:
        students[students_id].age=student.age

    if student.std!=None:
        students[students_id].std=student.std      

    return students[students_id] 


# delete method to remove the data from database
@app.delete("/delete_data")
def delete_data(students_id:int=Query(...,description="enter the id of student (to remove)")):
    if students_id not in students:
        return {"error":"the you trying to delete does not exist in database"}
    del students[students_id]
    return {"message":"data deleted sucesfully"}    