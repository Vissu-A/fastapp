from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

database_url = "sqlite:///./fastapp.db"

db_engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False}
)

db_session = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=db_engine
)

def get_db():
    db = db_session()
    try:
        yield db
    except Exception as e:
        print(f"get_db exception : {e}")
    finally:
        db.close()
