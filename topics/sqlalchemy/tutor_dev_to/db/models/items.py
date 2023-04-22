import datetime

from sqlalchemy import (
    Table,      Column,     String,
    Integer,    MetaData,   DateTime,
    ForeignKey, Boolean,    Sequence,
)
from db.core.initializer import engine


# ---- Construct Tables
# ---------------------

table_meta = MetaData()


Item = Table(
    'item',
    table_meta,
    Column(
        'id',
        Integer,
        primary_key=True,
        autoincrement=True
    ),
    Column('category', String(200)),
    Column('name', String(250), nullable=False),
    Column(
        'date_tracked',
        DateTime,
        default=datetime.datetime.now
    ),
)


CravedItem = Table(
    'craveditem',
    table_meta,
    Column(
        'id',
        Integer,
        primary_key=True,
        autoincrement=True
    ),
    Column('item_id', ForeignKey('item.id')),
    Column('is_satisfied', Boolean(), default=False),
    Column(
        'date_tracked',
        DateTime,
        default=datetime.datetime.now
    ),
)



def create_item_table_with_core():
    """Creates item table"""
    Item.create(engine, checkfirst=True)

def create_craveditem_table_with_core():
    """Creates craved item table"""
    CravedItem.create(engine, checkfirst=True)


def drop_item():
    """Drops Item table"""
    Item.drop(engine)

def drop_craveditem():
    """Drops CravedItem table"""
    CravedItem.drop(engine)

def create_all_tables():
    """Creates all tables that share same metadata"""
    table_meta.create_all(engine)

def drop_all_tables():
    """Drop all tables"""
    table_meta.drop_all(engine)
