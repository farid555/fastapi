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

Linux Postgresql
ls /etc/postgresql/14/main/
service postgres
sudo su postgres
psql
see current database-\du
change password psql- ALTER USER postgres WITH PASSWORD '123456';
                    - CREATE USER fastApi WITH PASSWORD '123456';
Add superuser       - ALTER USER fastapi WITH SUPERUSER;
Delete user         - DROP USER fastapi


