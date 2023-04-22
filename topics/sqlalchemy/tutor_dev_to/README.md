# intro
SqlAlchemy is an ORM - object relational mapper.
# steps 
## 1. create ${prjroot}/docker-compose.yml    which creates a database
Tutorial step 2.

The database creation scrip is in local_db/01-init.sh
```sql
CREATE DATABASE learnsqlalchemy;
CREATE USER learner WITH PASSWORD 'StrongPassword123';
GRANT ALL PRIVILEGES ON DATABASE learnsqlalchemy TO learner;
```

## 2. install packages
install latest versions (more recneet then tutorial)
```sh
~/ven/optimiz/bin/activate
## adapter to psg  for sqlalchemy
pip3 install psycopg2-binary==2.9.6
## sqlalchemy
pip3 install SQLAlchemy==2.0.10
```
## 3. hello world example
This step does not create any ddl, it just prints hello world from sql statement.

Tutorial step 4.

- `db/core/initializer.py`
- `conf/settings/base.py`
- `config.ini`

add empty `__init__.py` in conf and settings,   in db and core , in src

- `src/basic.py`
- `main.py`  # calls src.basic.run_db_select_statement

`python main.py`

## 4. raw ddl tour
Tutorial step 5.

Perform basic DDL operations. Drops, creates 2 tables item, cravedItem linked with FK.


- `db/scripts/queries.py`   make db.scripts a package
- `main.py` #in main observe methods tutor_step_x()

## 5. raw dml & dql

Tutorial step 6

SQL DML(create, update, delete),  DQL(select)

- `db/scripts/queries.py`   make db.scripts a package
- `main.py` #in main observe methods tutor_step_x()


