from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.database.config import settings

DATABASE_URL = settings.get_db_url()

engine = create_engine(url=DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)


class Base(DeclarativeBase):
    __abstract__ = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
