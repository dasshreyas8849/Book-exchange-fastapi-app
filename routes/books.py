from fastapi import Depends, HTTPException,APIRouter,Query
from auth import verify_api_key
from sqlmodel import Session,select
from models.book import Book,BookCreate,BookRead,BookUpdate
from database import get_session

router=APIRouter(prefix="/books",tags=["books"])

@router.post("/",response_model=BookRead)
def create_book(
    book_Data:BookCreate,
    session:Session=Depends(get_session),
    api_key:str=Depends(verify_api_key)
):
    book=Book.model_validate(book_Data)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@router.get("/",response_model=list[BookRead])
def list_books(
    Session:Session=Depends(get_session),
    Author:str=Query(default=None),
    Title:str=Query(default=None)
):
    query=select(Book).where(
        Book.is_sold==False
    )
    if Title:
        query=query.where(Book.Title.contains(Title))
    if Author:
        query=query.where(Book.Author.contains(Author))

    books =Session.exec(query).all
    return books

@router.patch("/{book_id}",response_model=BookRead)
def update_books(
    book_id:int,
    updates:BookUpdate,
    session:Session=Depends(get_session),
    api_key:str=Depends(verify_api_key)
):
    book=session.get(Book,book_id)
    if not book:
        raise HTTPException(status_code=404)
    book_data=updates.model_dump(exclude_unset=True)
    for key,value in book_data.items():
        setattr(book,key,value)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
@router.patch("/{book_id}/sold",response_model=BookRead)
def book_is_sold(
    book_id:int,
    session:Session=Depends(get_session),
    api_key:str=Depends(verify_api_key)
):
    book=Session.get(Book,book_id)
    if not book:
        raise HTTPException(status_code=404)
    book.is_sold=True
    session.add(book)
    session.commit()
    session.refresh(book)
    return book