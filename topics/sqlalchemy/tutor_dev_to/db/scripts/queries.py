from typing import List, Dict, Any

from sqlalchemy import text
from db.core.initializer import create_connection


def create_item_table():
    """Creates Item table.

    col: id              Unique identifier - primary key.
    col: timestamp       datetime defaults to current
                         date and time the item is tracked.
    col: name            Name of item - field is required.
    col: category        Category of the tracked item
    """
    # Creates a connection to the database
    with create_connection() as conn:
        # Utilizes connection instance to execute SQL query
        conn.execute(
            text(
                '''
                DROP TABLE IF EXISTS Item CASCADE;
                CREATE TABLE Item (
                    id              SERIAL PRIMARY KEY,
                    date_tracked    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    name            VARCHAR(250) NOT NULL,
                    category        VARCHAR(200)
                );
                '''
            )
        )

        # Sends the query to the database
        conn.commit()


def create_craved_item_table():
    """Create CravedItem table.

    This table keeps tracks of items that are craved for

    col: id              Unique identifier - primary key.
    col: item_id         Item unique identifier - field is
                         required.
    col: date_tracked    datetime defualts to current
                         date and time the item is tracked.
    col: is_satisfied    Denotes either or not craved item
                         has been satisfied.
    """
    # Creates a connection to the database
    with create_connection() as conn:
        # Utilizes connection instance to execute SQL query
        conn.execute(
            text(
                '''
                DROP TABLE IF EXISTS CravedItem CASCADE;
                CREATE TABLE CravedItem (
                    id              SERIAL      PRIMARY KEY,
                    item_id         INT         NOT NULL,
                    date_tracked    TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
                    is_satisfied    BOOLEAN     DEFAULT False,
                    CONSTRAINT      fk_item     FOREIGN KEY(item_id) REFERENCES Item(id)
                );
                '''
            )
        )
        conn.commit()


def retrieve_all_item(tbl_name: str):
    """Retrieves all records from Item table"""
    print(f'## rows from table {tbl_name}')
    with create_connection() as conn:
        results = conn.execute(
            text(f'SELECT * FROM {tbl_name}')
        )

        for result in results:
            print(result)

def insert_item(name:str, category:str):
    """Inserts new record into Item table

    param: name [str] Represents an item name to be added
    param: category [str] Represents an item category
    """
    with create_connection() as conn:
        conn.execute(
            text("INSERT INTO Item (name, category) VALUES (:name, :category)"),   # uses dictionary to pass values
            {'name':name, 'category':category}
        )
        conn.commit()

def insert_multiple_items(data:List[Dict[str, Any]]):
    """Allows insertion of multiple records into Item table

    param: data [List] sequence of dictionary where each
           dictionary represents a record to be added to
           the db
    """
    with create_connection() as conn:
        conn.execute(
            text("INSERT INTO Item (name, category) VALUES (:name, :category)"),
            data
        )
        conn.commit()

def update_existing_item_name_by_id(item_id:int, new_value:Any):
    """Handles the update of an existing record name
    in `Item` table

    param: item_id [int] A unique identifier of the record to be
           updated.
    param: new_value [Any] Replacement value for previous `name` column value.
    """
    with create_connection() as conn:
        conn.execute(
            text("UPDATE Item SET name=:update_value WHERE id=:id"),
            {'id': item_id,  'update_value': new_value}
        )
        conn.commit()

def update_existing_item_name_by_name(item_name:str, new_value:Any):
    """Handles the update of an existing record name
    in `Item` table

    param: item_id [int] A unique identifier of the record to be
           updated.
    param: new_value [Any] Replacement value for previous `name` column value.
    """
    with create_connection() as conn:
        conn.execute(
            text("UPDATE Item SET name=:update_value WHERE name=:name_value"),
            {'name_value': item_name,  'update_value': new_value}
        )
        conn.commit()

def delete_item(id:int):
    """Removes an existing item record from `Item` table.

    param: id [int] A unique identifier for item to be deleted
    """
    with create_connection() as conn:
        conn.execute(text("DELETE FROM Item WHERE id=:id"), {'id':id})
        conn.commit()


def rename_table(old_name, new_name):
    """Rename Item table if it exists in the database"""
    with create_connection() as conn:
        conn.execute(
            text(f'ALTER TABLE {old_name} RENAME TO {new_name}')
        )
        conn.commit()


def show_all_tables():
    """Show all available tables in the database

    Returned tables excludes those having their
    schema as `pg_catalog` and `information_schema`.
    """
    with create_connection() as conn:
        results = conn.execute(
            text(
                '''
                SELECT * FROM pg_catalog.pg_tables
                WHERE schemaname != 'pg_catalog' 
                AND schemaname != 'information_schema'
                '''
            )
        )
        print(f'## printing all tables in the database: \n')
        for data in results:
            # Only print the table name contained on Index 1
            print(f' schema: {data[0]} owner: {data[2]} table: {data[1]}')
