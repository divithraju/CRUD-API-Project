from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from . import schemas, crud, auth, database

router = APIRouter()
db = database.SessionLocal()

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/items/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate):
    return crud.create_item(db, item)

@router.get("/items/", response_model=list[schemas.ItemOut])
def read_items():
    return crud.get_items(db)
