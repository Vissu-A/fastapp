from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import UUID, String, Enum, Date, Boolean, DateTime

from src.db.database import Base

class UserModel(Base):
    __tablename__ = "user"
    uid = Column(UUID, primary_key=True, index=True)
    fullname = Column(String)
    username = Column(String)
    email = Column(String)
    passcode = Column(String)
    gender = Column(Enum)
    dob = Column(Date)
    is_active = Column(Boolean)
    is_admin = Column(Boolean)
    dojoin = Column(DateTime)
    dologin = Column(DateTime)
