from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.sql.sqltypes import Uuid, String, Date, Enum, DateTime, Boolean

from src.db.database import Base

class UserModel(Base):
    __tablename__ = "user"
    # # auto filled fileds
    uid = Column(Uuid, primary_key=True, index=True)
    # dojoin = Column(DateTime)
    # dologin = Column(DateTime)

    # # Role identity fields
    # is_active = Column(Boolean)
    # is_admin = Column(Boolean)

    # user input fields
    username = Column(String, unique=True, name="uq_user_username")
    email = Column(String, unique=True, name="uq_user_email")
    passcode = Column(String)
    dob = Column(Date)
    gender = Column(String)

    # __table_args__ = (
    #     UniqueConstraint('email', name="uq_user_email"),
    #     UniqueConstraint('username', name="uq_user_username")
    # )


# Relationships
