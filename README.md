<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/Haile-08/AirBnB_clone/master/image/logo.png" alt="Markdownify" width="200">
  <br>
  AirBnB clone
  <br>
</h1>

<h4 align="center">The AirBnB clone project</h4>

## Final product

![final1](https://raw.githubusercontent.com/Haile-08/AirBnB_clone/master/image/final1.png)
![final2](https://raw.githubusercontent.com/Haile-08/AirBnB_clone/master/image/final2.png)

<h2 align="center"> Steps</h2>

--- 

# The console

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction 
between "My object" and "How they are stored and persisted". This means: from your console code (the
command interpreter itself) and from the front-end and RestAPI you will build later, you won't have to pay
attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

![console](https://raw.githubusercontent.com/Haile-08/AirBnB_clone/master/image/console.png)

### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with 
all other following projects: HTML/CSS templating, database storage, API, front-end integration...

Each task is linked and will help you to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage. 
- create all unittests to validate all our classes and storage engine

### What's a command interpreter?
Do you remember the Shell? It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc..)
- Update attributes of an object
- Destroy an object

---

# Files and Directories
- models directory will contain all classes used for the entire project. A class, called "model" in a OOP project is the representation of an object/instance.
- tests directory will contain all unit tests.
- console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements: 
	- attributes: id, created_at and updated_at
	- methods: save() and to_json()
- models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

---

# Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won't be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file. 

Why separate "storage management" from "model"? It's to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:
- Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc...)
- Provide default value of any attribute
- In the future, provide the same model behavior for file storage or database storage

---

# Data diagram

![diagram](https://raw.githubusercontent.com/Haile-08/AirBnB_clone/master/image/diagram.jpg)

---

# Execution

Should work in interactive mode:

```sh
   $ ./console.py
   (hbnb) help

   Documented commands (type help <topic>):
   ========================================
   EOF  help  quit

   (hbnb)
   (hbnb)
   (hbnb) quit
   $
```

But also in non-interactive mode: 

```sh
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
```

