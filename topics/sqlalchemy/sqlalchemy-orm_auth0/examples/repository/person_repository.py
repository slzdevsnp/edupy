from datetime import date
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from ..basic.person import Person


class PersonRepository:

    @staticmethod
    def create(session: Session, person: Person) -> Person:
        session.add(person)
        session.commit()
        return person

    @staticmethod
    def find_all(session: Session) -> List[Person]:
        persons = session.query(Person).all()
        return persons

    @staticmethod
    def find_by_id(session: Session, id: int) -> Person:
        person = session.query(Person).filter(Person.id == id).first()
        return person

    @staticmethod
    def find_by_name(session: Session, name: str, isAll=False) -> Person:
        if isAll:
            person = session.query(Person).filter(Person.name == name).all()
        else:
            person = session.query(Person).filter(Person.name == name).first()
        return person  # could return 1  or more persons

    @staticmethod
    def update(session: Session, id: int, person: Person) -> Person:
        existing_person = PersonRepository.read_by_id(session, id)

        if existing_person is None:
            raise NoResultFound(f"No person found with id {id}")

        existing_person.name = person.name
        existing_person.date_of_birth = person.date_of_birth
        existing_person.height = person.height
        existing_person.weight = person.weight

        session.commit()
        return existing_person

    @staticmethod
    def delete_by_id(session: Session, id: int) -> None:
        person = PersonRepository.find_by_id(session, id)

        if person is None:
            raise NoResultFound(f"No person found with id {id}")

        session.delete(person)
        session.commit()

    @staticmethod
    def delete_by_name(session: Session, name: str) -> None:
        persons = PersonRepository.find_by_name(session, name, isAll=True)
        if persons is None:
            raise NoResultFound(f"No person found with name {name}")
        for p in persons:
            session.delete(p)
        session.commit()

    @staticmethod
    def delete_all(session: Session) -> None:
        session.query(Person).delete()
        session.commit()
