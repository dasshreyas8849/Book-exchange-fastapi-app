from fastapi import FastAPI
from database import create_tables
from routes import users,books
app=FastAPI(
    title="Kitab exchange API"
)


@app.on_event("startup")
def on_startup():
    create_tables()
app.include_router(users.router)
app.include_router(books.router)
