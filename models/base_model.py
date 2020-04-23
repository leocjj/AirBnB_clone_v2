#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

# create Base object for task 6
Base = declarative_base()


class BaseModel():
    """This class will defines all common attributes/methods
    for other classes
    """
    ''' Update class definition to use SQLAlchemy
    '''
    # attributes for task 6
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            # Aiko's change for taks 2
            # self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            # Aiko's change for task2
            # models.storage.new(self)
        else:
            # unique id
            self.id = str(uuid.uuid4())
            # datetime when is created
            self.created_at = self.updated_at = datetime.now()
            # move it to save method for task 6
            # afecta guardar de la 2
            # models.storage.new(self)

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        # self.created_at = datetime.now()
        if not self.created_at:
            self.created_at = self.updated_at
        # moved from def __init__(self, *args, **kwargs) to here task 6
        # afecta el guardar de la 2
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        # update for task6
        # pendiente revisar task2
        key_to_delete = "_sa_instance_state"
        if key_to_delete in my_dict:
            del my_dict[key_to_delete]

        return my_dict

    # Need to implement functionality for AirBnB_V2
    def delete(self):
        """delete the current instance from the storage """
        models.storage.delete(self)
