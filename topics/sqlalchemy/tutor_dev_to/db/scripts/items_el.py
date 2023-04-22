from typing import List, Dict

from sqlalchemy import select, bindparam, Integer, String, Boolean

from db.core.initializer import create_connection
from db.models.items import Item, CravedItem


class DQL:
    """Encapsulates database query language (DML)"""

    @staticmethod
    def retrieve_all_items():
        """Retrieves all data entries and
        corresponding columns from Item table.
        """
        with create_connection() as conn:
            return conn.execute(select(Item))

    @staticmethod
    def retrieve_item_by_id(id: int):
        """Retrieves a single item by it's id.

        - id <int> A unique identifier of an item.
        """
        statement = (
            select(Item)
            .where(Item.c.id == bindparam('id', type_=Integer))
        )
        with create_connection() as conn:
            result = conn.execute(statement, {'id': id})
            return result

    @staticmethod
    def retrieve_all_craved_items():
        """Retrieves all data entries and
        corresponding columns from CravedItem table.
        """
        with create_connection() as conn:
            return conn.execute(select(CravedItem))


class DML:
    """Encapsulates database manipulation language (DML)"""

    @staticmethod
    def add_item(name: str, category: str):
        """Adds a single item to Item table"""
        statement = Item.insert().values(name=name, category=category)
        with create_connection() as conn:
            conn.execute(statement)
            conn.commit()

    @staticmethod
    def add_item_alt(name: str, category: str):
        """Adds a single item to Item table"""
        statement = Item.insert().values(
            name=bindparam('name', type_=String),
            category=bindparam('category', type_=String)
        )
        with create_connection() as conn:
            conn.execute(statement, {'name': name, 'category': category})
            conn.commit()

    @staticmethod
    def add_craved_item(item_id: int, is_satisfied: bool):
        """Adds a single item to CravedItem table"""
        statement = CravedItem.insert().values(
            item_id=bindparam('item_id', type_=Integer),
            is_satisfied=bindparam('is_satisfied', type_=Boolean)
        )
        with create_connection() as conn:
            conn.execute(statement, {'item_id': item_id,
                                     'is_satisfied': is_satisfied})
            conn.commit()

    @staticmethod
    def add_items(payload: List[Dict[str, str]]):
        """Inserts multiple items to Item table

        - payload <list> new data to be added to
                         Item table. Each dict has
                         key mapped to the Item table
                         and it's corresponding value.
        """
        with create_connection() as conn:
            conn.execute(Item.insert(), payload)
            conn.commit()

    @staticmethod
    def delete_item(item_id: int):
        """Deletes an item whose id is passed as a
        parameter

        - item_id <int> Uniquely identifies an item
                        instance
        """
        with create_connection() as conn:
            statement = Item.delete().where(
                Item.c.id == bindparam('id', type_=Integer)
            )
            conn.execute(statement, {'id': item_id})
            conn.commit()

    @staticmethod
    def delete_many_items_by_id(ids: list):
        """Deletes multiple items with the corresponding
        id
        """
        with create_connection() as conn:
            statement = Item.delete().where(Item.c.id.in_(ids))
            conn.execute(statement)
            conn.commit()

    @staticmethod
    def update_item(item_id: int, data: Dict[str, str]):
        """Updates an existing item

        - item_id <int> Uniquely identifies an item
                        instance

        - data <dict>   Key-value pair with column name
                        as key and the new entry for
                        column as value.
        """
        with create_connection() as conn:
            statement = Item.update().where(
                Item.c.id == bindparam('item_id', type_=Integer)
            ).values(**data)
            conn.execute(statement, {'item_id': item_id})
            conn.commit()
