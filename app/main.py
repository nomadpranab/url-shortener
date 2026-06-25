from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import URL, Base
from schemas import URLCreate
import random
import string
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

BASE_URL = os.getenv("BASE_URL")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_short_code(length=6):
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length
        )
    )


@app.post("/shorten")
def shorten_url(url: URLCreate, db: Session = Depends(get_db)):
    short_code = generate_short_code()

    db_url = URL(
        original_url=url.original_url,
        short_code=short_code
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return {
        "short_url": f"{BASE_URL}/{short_code}"
    }


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url=db_url.original_url)
