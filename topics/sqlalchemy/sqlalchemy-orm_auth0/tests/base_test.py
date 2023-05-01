import unittest
from examples.basic.person import Person
from examples.common.base import session_factory
from examples.repository.person_repository import PersonRepository
from datetime import date

class TestMyClass(unittest.TestCase):

    def setUp(self):
        # Setup code to be run before each test method
        self.session = session_factory()

    def tearDown(self):
        # Teardown code to be run after each test method.
        # Remove the test database file.
        PersonRepository.delete_all(self.session)
        self.session.close()

    def insert_folks(self):
        session = self.session
        bruno = Person("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
        john = Person("John Doe", date(1990, 5, 17), 173, 90)
        pierre = Person("Pierre", date(1991, 6, 17), 173, 90)
        PersonRepository.create(session, bruno)
        PersonRepository.create(session, john)
        PersonRepository.create(session, pierre)

    def test_fetch_people(self):
        session = self.session
        #clean table
        PersonRepository.delete_all(session)
        self.insert_folks()
        folks = PersonRepository.find_all(session)
        for person in folks:
                print(f'{person.name} was born in {person.date_of_birth}')
        self.assertEqual(len(folks),3)

    def test_create_person(self):
        session = self.session
        pname = "Ivan Kolkin"
        p1 = Person(pname,
                    date(1984, 10, 20),
                    182, 84.5)

        PersonRepository.create(session,p1)
        p1_f = PersonRepository.find_by_name(session, pname)
        print(f'found person(s) {p1_f}')
        self.assertEqual(p1_f.name,  pname)

    def test_update_person(self):
        session = self.session
        pname = "Ivan Kolkin"
        p1 = Person(pname,
                    date(1984, 10, 20),
                    182, 84.5)

        PersonRepository.create(session,p1)
        p1_f = PersonRepository.find_by_name(session, pname)
        print(f'found person(s) {p1_f}')
        self.assertEqual(p1_f.name,  pname)

    def test_delete_persons(self):
        session = self.session
        pname = "Alex Cowl"
        p1 = Person(pname,
                    date(1984, 10, 20),
                    182, 84.5)
        p2 = Person(pname,
                    date(1984, 10, 20),
                    202, 104.0)

        PersonRepository.create(session,p1)
        PersonRepository.create(session,p2)
        found_folks = PersonRepository.find_by_name(session, pname,isAll=True)
        print(f'found person(s) {found_folks}')
        self.assertEqual(len(found_folks), 2)


if __name__ == "__main__":
    unittest.main()
