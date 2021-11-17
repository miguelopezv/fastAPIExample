from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

app = FastAPI()


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get('/')
def home():
    return {"Hello": "World"}


# request body
@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person


# Query params validation
@app.get('/person/details')
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: int = Query(...)
):
    return {name: age}


# Path params validation
@app.get('/person/details/{person_id}')
def show_person(person_id: int = Path(
    ...,
    gt=0,
    title='Person Id',
    description='Id of the user to retrieve, should be above 1'
)):
    return {person_id: "It exists"}
