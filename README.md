# fastapi

## Virtual machine install in Linux 

```sh 
python3 -m pip install --user virtualenv
```

## python3 -m venv venv
## source venv/bin/activate 
## virtual machine Deactivate > Deactivate

```sh 
 uvicorn main:app --reload

```

### Fastapi installation
### Install > 
```sh 
pip install "fastapi[all]"

```
### http://127.0.0.1:8000/docs fastapi documentation
### http://127.0.0.1:8000/rdoc fastapi documentation

## Linux Postgresql
- [x] ls /etc/postgresql/14/main/
- [x] service postgres
- [x] sudo su postgres
- [x] run- psql
- [x] see current database-\du
- [x] Change password psql - ALTER USER postgres WITH PASSWORD '123456';
- [x] Create new user      - CREATE USER fastApi WITH PASSWORD '123456';
- [x] Add superuser        - ALTER USER fastapi WITH SUPERUSER;
- [x] Delete user          - DROP USER fastapi


