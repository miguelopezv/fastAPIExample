from typing import Optional

from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

from models import Person, PersonResponse

app = FastAPI()


@app.get('/')
def home():
    return {"Hello": "World"}


# request body
@app.post('/person/new', response_model=PersonResponse)
def create_person(person: Person = Body(...)):
    return person


# Query params validation
@app.get('/person/details')
def show_person(
    name: Optional[str] = Query(
        None, min_length=1, max_length=50, example='Miguel'),
    age: int = Query(..., example=35)
):
    return {name: age}


# Path params validation
@app.get('/person/details/{person_id}')
def show_person(person_id: int = Path(
    ...,
    gt=0,
    title='Person Id',
    description='Id of the user to retrieve, should be above 1',
    example=1423
)):
    return {person_id: "It exists"}


# Pass to body request objects
@app.put('/person/{person_id}', response_model=PersonResponse)
def update_person(
    person_id: int = Path(..., gt=0, example=1423),
    person: Person = Body(...),
    # location: Location = Body(...)
):
    # return {'person': person, 'location': location}
    return person
