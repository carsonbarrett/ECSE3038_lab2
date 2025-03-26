from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data model for Person
class Person(BaseModel):
    name: str
    occupation: str
    address: str

# Initialize an empty list to store people
data = []

@app.post("/person")
async def add_person(person: Person):
    # Validate request to ensure all fields are filled
    if not person.name or not person.occupation or not person.address:
        return {"success": False, "result": {"error_message": "invalid request"}}
    
    # Add person to the data list
    data.append(person)
    return {"success": True, "result": person.dict()}

@app.get("/person")
async def get_people():
    return data
