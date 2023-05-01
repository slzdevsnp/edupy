# contents

tutorial: https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

github : https://github.com/auth0-blog/sqlalchemy-orm-tutorial


# running examples
- in separate terminal run `docker-compose up`
- in separate terminal run `PGPASSWORD="dbpassword" psql --host=localhost --port=5432  --username=dbuser --dbname=sqlalchemy-orm-tutorial`
- in separate terminal run 
`source ~/.local/share/virtualenvs/sqlalchemy-orm_auth0-icutx571/bin/activate`

then:
```sh
python -m examples.basic
python -m examples.onetoone
```

or without pip activation 
```sh
pipenv run python -m examples.basic
pipenv run python -m examples.onetoone
pipenv run python -m examples.onetomany
pipenv run python -m examples.manytomany

```

# onetomany relatioship
onetomany package
 a project_manager manages many projects
 *ProjectManager*  has  `projects = relationship("Project", back_populates="project_manager")`
 *Project*  has 
```py
    project_manager_id = Column(Integer, ForeignKey('project_manager.id')) #!
    project_manager = relationship("ProjectManager", back_populates="projects")
```

# onetoone relationship
a user has 1 phone

*User* has 
```py 
    mobile = relationship("Mobile", uselist=False, backref="owner")

```
*Mobile* has 
```py 
owner_id = Column(Integer, ForeignKey('user.id'))
```
# manytomany  relationship
``` py 
association_table = Table(
    'association', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)
```
*Course* has 
```py 
students = relationship("Student", secondary=association_table)
```

*Student*  has  now specific instructions
