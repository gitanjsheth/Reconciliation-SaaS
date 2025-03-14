from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")

# Create the SQLAlchemy engine (sync engine for now)
engine = create_engine(
    DATABASE_URL,
    echo=True,             # Logs all SQL queries (remove or set to False in production)
    future=True            # Makes sure we are using the SQLAlchemy 2.x style
)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# Base class for models to inherit from
Base = declarative_base()

# Dependency to get a new database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()