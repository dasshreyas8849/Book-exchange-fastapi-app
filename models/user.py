from sqlmodel import SQLModel,Field,Relationship
from typing import List,Optional
#Database table for the user
class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str=Field(index=True)
    email:str=Field(unique=True)
    college:str
    #one user can have many books
    books:List["Book"]=Relationship(back_populates="user")
#request body for creating a user
class UserCreate(SQLModel):
    name:str
    email:str
    college:str

#response body
class UserRead(SQLModel):
    id:int
    name:str
    email:str
    college:str




#avoid circular import
from models.book import Book
User.model_rebuild()