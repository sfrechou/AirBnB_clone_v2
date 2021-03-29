#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel):
    """ State class """
    NEW_TYPE = getenv("HBNB_TYPE_STORAGE")
    if NEW_TYPE == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        print("Crea un State")
        name = ""

    @property
    def cities(self):
        """Return City list"""
        lista = []
        obj_dict = models.storage.all(City)
        for key, value in obj_dict.items():
            if value.state_id == self.id:
                lista.append(obj_dict[key])
        return lista