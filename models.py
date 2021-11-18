from typing import Optional
from enum import Enum

from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


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


class PersonBase(BaseModel):
    first_name: str = Field(..., min_length=5, max_length=50)
    last_name: str = Field(..., min_length=5, max_length=50)
    age: int = Field(..., gt=0, le=100)
    email: EmailStr = Field(...)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


class Person(PersonBase):
    password: str = Field(..., min_length=8)

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'Miguel',
                'last_name': 'López',
                'age': 35,
                'email': 'miguelopezv@gmail.com',
                'hair_color': 'brown',
                'password': '12345678'
            }
        }


class PersonResponse(PersonBase):
    pass
