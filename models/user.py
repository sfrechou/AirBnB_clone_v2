#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class User(BaseModel):
    """This class defines a user by various attributes"""

    NEW_TYPE = getenv("HBNB_TYPE_STORAGE")
    if NEW_TYPE == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
