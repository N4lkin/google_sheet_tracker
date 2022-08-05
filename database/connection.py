from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Settings

SQLALCHEMY_DATABASE_URL = Settings.SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=Settings.DB_AUTOCOMMIT, autoflush=Settings.DB_AUTOFLUSH, bind=engine)

Base = declarative_base()
