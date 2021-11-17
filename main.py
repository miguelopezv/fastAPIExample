from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query

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


@app.post('/person/new')
# request body
def create_person(person: Person = Body(...)):
    return person


# Query params validation
@app.get('/person/details')
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: int = Query(...)
):
    return {name: age}
