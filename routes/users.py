from fastapi import Depends, HTTPException,APIRouter
from auth import verify_api_key
from sqlmodel import Session,select
from models.user import User,UserCreate,UserRead
from database import get_session

router=APIRouter(prefix="/user",tags=["user"])

@router.post("/",response_model=UserRead)
def register_user(
    user_data:UserCreate,
    session: Session=Depends(get_session),
    api_key:str=Depends(verify_api_key)
):
    existing=session.exec(
        select(User).where(User.email==user_data.email)
    ).first()

    if existing:
        raise HTTPException(status_code=400)
    user=User.model_validate(user_data)
    session.add(user)
    session.commit( )
    session.refresh(user)
    return user

@router.get("/",response_model=list[UserRead])
def list_users(
    session:Session=Depends(get_session),
):
    users=session.exec(select(User)).all()
    return users

