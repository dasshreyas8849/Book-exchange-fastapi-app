from sqlmodel import SQLModel,Field,Relationship
from typing import Optional 

class Book(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    Title:str=Field(index=True)
    Author:str=Field(index=True)
    price:float
    is_sold:bool=Field(default=False)
    #foreign key to user table
    user_id:int=Field(foreign_key="user.id")
    owner:Optional["User"]=Relationship(back_populates="books")
#request body for creating a book
class BookCreate(SQLModel):
    Title:str
    Author:str
    price:float
    user_id:int
#response body
class BookRead(SQLModel):
    id:int
    Title:str
    author:str
    price:int
    is_Sold:bool
    user_id:int

class BookUpdate(SQLModel):
    price:Optional[int]=None
    is_Sold:Optional[bool]=None

    
from models.user import User
Book.model_rebuild()