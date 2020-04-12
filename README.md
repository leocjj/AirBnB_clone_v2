# AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

### Supported classes:
* [BaseModel](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/base_model.py)
* [User](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/user.py)
* [State](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/state.py)
* [City](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/city.py)
* [Amenity](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/amenity.py)
* [Place](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/place.py)
* [Review](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/review.py)

# Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

# Installation
* Clone this repository: git clone "https://github.com/alexaorrico/AirBnB_clone.git"
* Access AirBnb directory: cd AirBnB_clone
* Run SQL Scripts [`setup_mysql_dev.sql`](https://github.com/paurbano/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) or [`setup_mysql_test.sql`](https://github.com/paurbano/AirBnB_clone_v2/blob/master/setup_mysql_test.sql)
* Run hbnb(interactively): ./console and enter command
* Run hbnb(non-interactively): echo "<command>" | ./console.py

# File Descriptions
[console.py](https://github.com/paurbano/AirBnB_clone_v2/blob/master/console.py) - the console contains the entry point of the command interpreter. List of commands this console current supports:

* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name.
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

`models/` directory contains classes used for this project:

[base_model.py](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/base_model.py) - The BaseModel class from which future classes will be derived

* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute updated_at with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

`models/engine` directory contains Storage classes to File JSON or DB MySQL:
* [file_storage.py](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* [db_storage.py](https://github.com/paurbano/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) - Connect to MySQL and do CRUD operations

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

    (hbnb) create State name="California"
    (hbnb) create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10              price_by_night=300 latitude=37.773972 longitude=-122.431297

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

# Versions

V2.
