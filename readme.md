
## Flask Application Structure 
```

|───backend_dev_test
| |────Backend_test/
| | |──────src/
| | | |────endpoints/
| | | | |────__init__.py
| | | | |────user_management.py
| | | | |────publication_management.py
| | | | |────swagger.py
| | | |────__init__.py
| | | |──────api_spec.py
| | | |──────app.py
| | | |──────db.sqlite
| | | |──────models.py
| | |──────tests/
| | | |────conftest.py
| | | |────test_endpoints.py
| | |──────migrations/


```

## Installation and Configuration

### clone the project:

open your git bash and write 
```
$ git clone https://github.com/jeer2234/backend_dev_test.git
$ cd backend_dev_test
```
### create a virtual environment:

```
$ python -m venv env

```

### activate your virtual environment:

on Windows cmd
```
$ env\Scripts\activate.bat
```
on bash shell
```
$ env/bin/activate
```
### Install dependencies with pip:

```
$ pip install -r requirements.txt
```
## Run Tests

```
$ python -m pytest 
```

## Run Flask

### move to flask application location
```
$ cd backend_test\src
```

### Run flask for develop

```
$ flask --debug run
```
In flask, Default port is `5000`

Go to Swagger document page:  `http://127.0.0.1:5000/api/docs`