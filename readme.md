
## Flask Application Structure 
```
.
|──────src/
| |────__init__.py
| |────endpoints/
| | |────__init__.py
| | |────blueprint_x.py
| | |────blueprint_y.py
| | |────forms.py
| | |────swagger.py
| |──────api_spec.py
| |──────app.py
| |──────db.sqlite
| |──────models.py
|──────migrations/
|──────tests/
| |────conftest.py
| |────test_endpoints.py


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
### Install with pip:

```
$ pip install -r requirements.txt
```



## Run Flask
### Run flask for develop


```
$ cd Backend_knowledge_application_test\src
$ flask --debug run
```
In flask, Default port is `5000`

Swagger document page:  `http://127.0.0.1:5000/api/docs`