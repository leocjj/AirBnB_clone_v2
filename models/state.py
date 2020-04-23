#!/usr/bin/python3
"""This is the state class"""
import models
from os import getenv
from models.base_model import BaseModel
from models.city import City, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    # Added for task 6
    # if getenv("HBNB_TYPE_STORAGE") == "db":
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        @property
        def cities(self):
            """Return list of City instances with state_id equal to current
            State.id
            """
            list_cities = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    list_cities.append(city)
            return list_cities
