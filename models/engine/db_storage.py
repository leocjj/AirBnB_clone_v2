#!/usr/bin/python3
""" Storage class for DB for AirBnB Clone_V2 """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine


class DBStorage():
    """ Class to connect MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        dataBase = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        dbConnector = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(dbConnector.format(
            user, pwd, host, dataBase), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query all objects depending of the class name
        classes = ['State', 'City', 'User', 'Place', 'Review']
        class_dict = {}
        if cls and cls in classes:
            # busca por el tipo de objeto
            # _object = self.__session.query(cls).all()
            # for _obj in _object:
            #    key = type(_obj).__name__ + '.' + _obj.id
            #    class_dict[key] = _obj
            try:
                return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                        for obj in self.__session.query(eval(cls)).all()
                        if eval(cls).__name__ == type(obj).__name__}
            except:
                return {}
        else:
            for _class in classes:
                _object = self.__session.query(eval(_class)).all()
                for _obj in _object:
                    key = type(_obj).__name__ + '.' + _obj.id
                    class_dict[key] = _obj
        return class_dict"""
        """Show all class objects in DBStorage or specified class if given
        
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for c in classes:
                objects += self.__session.query(c)
        my_dict = {}
        for obj in objects:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict
        """
        classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        class_dict = {}
        # print("All DbStorage")
        if cls is None:
            for _class in classes:
                _object = self.__session.query(eval(_class))
                for _obj in _object:
                    key = type(_obj).__name__ + '.' + _obj.id
                    class_dict[key] = _obj
        else:
            # busca por el tipo de objeto
            _object = self.__session.query(cls).all()
            for _obj in _object:
                key = type(_obj).__name__ + '.' + _obj.id
                class_dict[key] = _obj
        return class_dict

    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects """
        Base.metadata.create_all(self.__engine)
        # sess_factory=sessionmaker(bind=self.__engine,expire_on_commit=False)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    # esto hay que revisarlo con cuidadito!!!!
    '''
    def close(self):
        self.__session.close()
    '''

    def close(self):
        """Call remove() on the private session attribute self.__session
        """
        self.__session.close()
