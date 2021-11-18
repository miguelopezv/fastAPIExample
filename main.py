from typing import Optional
from enum import Enum

from pydantic import BaseModel
from pydantic import Field

from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

app = FastAPI()


class HairColor(Enum):
    white = 'white'
    brown = 'brown'
    black = 'black'
    blonde = 'blonde'
    red = 'red'


class Location(BaseModel):
    city: str
    state: str
    country: str


class Person(BaseModel):
    first_name: str = Field(..., min_length=5, max_length=50)
    last_name: str = Field(..., min_length=5, max_length=50)
    age: int = Field(..., gt=0, le=100)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


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


# Pass to body request objects
@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(..., gt=0),
    person: Person = Body(...),
    location: Location = Body(...)
):
    return {'person': person, 'location': location}
