from src.basic import run_db_select_statement
from db.scripts.queries import *
from db.scripts import items_el

from db.models.items import (
    create_item_table_with_core,
    create_craveditem_table_with_core,
    create_all_tables,
    drop_all_tables,
    drop_item,
    drop_craveditem
)

'''
tutorial: 
https://dev.to/spaceofmiah/series/20051
'''


def tutor_step_4():
    run_db_select_statement()


def tutor_step_5():
    create_item_table()
    # rename_table('Item', 'MyItem')
    create_craved_item_table()
    show_all_tables()


def tutor_step_6():
    create_item_table()
    insert_item(name='Tesla Model S', category='Auto')
    insert_multiple_items([
        {
            'name': 'Iphone 14 Pro Max',
            'category': 'mobile'
        },
        {
            'name': 'Pizza',
            'category': 'meal'
        }
    ])
    update_existing_item_name_by_id(item_id=1, new_value='Tesla Model 3')
    update_existing_item_name_by_name(item_name='Tesla Model 3', new_value='Tesla Cybertruck')

    retrieve_all_item(tbl_name='Item')
    delete_item(id=3)
    print(f'##### after item deletion')
    retrieve_all_item(tbl_name='Item')


def tutor_step_7():
    drop_all_tables()
    create_item_table_with_core()
    create_craveditem_table_with_core()
    show_all_tables()
    insert_item(name='Tesla Model S', category='Auto')
    retrieve_all_item(tbl_name='Item')


def tutor_step_8():
    drop_all_tables()
    create_all_tables()

    items_el.DML.add_item(name='Potatoes', category='Meal')
    items_el.DML.add_item(name='Tuna', category='Grocery')
    items_el.DML.add_item(name='PS 5', category='Game')

    results = items_el.DQL.retrieve_all_items()
    print_item_rows(results)

    items_el.DML.add_items(
        payload=[
            {'name': 'Addidas ZX 22 Boost', 'category': 'Shoe'},
            {'name': 'Nike Revolution', 'category': 'Shoe'},
            {'name': 'NK Force Dunk', 'category': 'Shoe'},
            {'name': 'Nike Air', 'category': 'Shoe'},
        ]
    )
    results = items_el.DQL.retrieve_all_items()
    print_item_rows(results)

    # delete a single record
    items_el.DML.delete_item(item_id=1)
    print_item_rows(items_el.DQL.retrieve_all_items())

    # delete multiple records
    items_el.DML.delete_many_items_by_id([2, 3])
    print_item_rows(items_el.DQL.retrieve_all_items())

    # Update single record
    items_el.DML.update_item(item_id=4, data={'category': 'Sneakers'})
    print_item_rows(items_el.DQL.retrieve_all_items())


def tutor_step_szi_8():
    drop_all_tables()
    create_all_tables()

    items_el.DML.add_item(name='Potatoes', category='Meal')
    items_el.DML.add_item(name='Tuna', category='Grocery')

    items_el.DML.add_craved_item(item_id=1, is_satisfied=True)
    items_el.DML.add_craved_item(item_id=2, is_satisfied=False)

    print_item_rows(items_el.DQL.retrieve_all_items())
    print_table_rows(items_el.DQL.retrieve_all_craved_items())


def print_item_rows(results):
    for row in results:
        print("{id} :{name} : {category}".format(
            id=row[0],
            name=row[2],
            category=row[1]))


def print_table_rows(results):
    for row in results:
        print(f'row: {row}')


def main():
    # tutor_step_4()
    # tutor_step_5()
    # tutor_step_6()
    # tutor_step_7()
    # tutor_step_8()
    tutor_step_szi_8()


if __name__ == "__main__":
    main()
