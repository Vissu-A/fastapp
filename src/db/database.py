from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapp.db"

# MySQL URL
# pip install pymysql
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"

# PostgreSQL URL
# pip install psycopg2-binary
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://username:password@localhost/dbname"

db_engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

db_session = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=db_engine
)

Base = declarative_base()

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
