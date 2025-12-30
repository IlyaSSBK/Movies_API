from pydantic import BaseModel
from datetime import date

class MovieCreate(BaseModel):
    title: str
    release_date: date
    rating: float

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True
