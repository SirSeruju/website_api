from pydantic import BaseModel


class Article(BaseModel):
    name: str
    text: str

    class Config:
        orm_mode = True
