import random
from datetime import datetime, timedelta

# Helper function to generate random dates
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Sample data
customers = [
    {
        "name": "John Smith",
        "address": "123 Main St, Anytown, AN 12345",
        "email": "john.smith@email.com",
        "phone": "555-123-4567",
        "customer_id": "CS001",
        "signup_date": "2023-01-15"
    },
    {
        "name": "Emma Johnson",
        "address": "456 Elm Ave, Somewhere, SW 67890",
        "email": "emma.j@email.com",
        "phone": "555-987-6543",
        "customer_id": "CS002",
        "signup_date": "2023-02-28"
    },
    {
        "name": "Michael Brown",
        "address": "789 Oak Rd, Elsewhere, EL 13579",
        "email": "m.brown@email.com",
        "phone": "555-246-8135",
        "customer_id": "CS003",
        "signup_date": "2023-03-10"
    },
    {
        "name": "Sarah Davis",
        "address": "321 Pine Ln, Nowhere, NW 24680",
        "email": "sarah.d@email.com",
        "phone": "555-369-2580",
        "customer_id": "CS004",
        "signup_date": "2023-04-05"
    },
    {
        "name": "David Wilson",
        "address": "654 Birch Blvd, Everywhere, EV 97531",
        "email": "d.wilson@email.com",
        "phone": "555-753-9514",
        "customer_id": "CS005",
        "signup_date": "2023-05-20"
    },
    {
        "name": "Lisa Taylor",
        "address": "987 Cedar St, Someplace, SP 86420",
        "email": "lisa.t@email.com",
        "phone": "555-951-7532",
        "customer_id": "CS006",
        "signup_date": "2023-06-12"
    },
    {
        "name": "Robert Anderson",
        "address": "147 Maple Dr, Anyville, AV 75319",
        "email": "r.anderson@email.com",
        "phone": "555-159-7532",
        "customer_id": "CS007",
        "signup_date": "2023-07-03"
    },
    {
        "name": "Jennifer Martinez",
        "address": "258 Willow Way, Othertown, OT 95135",
        "email": "j.martinez@email.com",
        "phone": "555-357-9514",
        "customer_id": "CS008",
        "signup_date": "2023-08-18"
    },
    {
        "name": "William Thompson",
        "address": "369 Spruce Sq, Thisplace, TP 15973",
        "email": "w.thompson@email.com",
        "phone": "555-852-9630",
        "customer_id": "CS009",
        "signup_date": "2023-09-22"
    },
    {
        "name": "Elizabeth Clark",
        "address": "741 Ash Ave, Thatville, TV 35791",
        "email": "e.clark@email.com",
        "phone": "555-741-8520",
        "customer_id": "CS010",
        "signup_date": "2023-10-07"
    },
    {
        "name": "Christopher Lee",
        "address": "852 Poplar Pl, Anotherburg, AB 24680",
        "email": "c.lee@email.com",
        "phone": "555-963-8520",
        "customer_id": "CS011",
        "signup_date": "2023-11-14"
    },
    {
        "name": "Amanda White",
        "address": "963 Sycamore St, Lasttown, LT 86420",
        "email": "a.white@email.com",
        "phone": "555-147-2580",
        "customer_id": "CS012",
        "signup_date": "2023-12-01"
    },
    {
        "name": "Daniel Harris",
        "address": "159 Redwood Rd, Firstcity, FC 13579",
        "email": "d.harris@email.com",
        "phone": "555-369-1470",
        "customer_id": "CS013",
        "signup_date": "2024-01-19"
    },
    {
        "name": "Jessica Lewis",
        "address": "357 Sequoia Ter, Middletown, MT 97531",
        "email": "j.lewis@email.com",
        "phone": "555-258-1470",
        "customer_id": "CS014",
        "signup_date": "2024-02-05"
    },
    {
        "name": "Thomas Walker",
        "address": "456 Juniper Jct, Endville, EV 75319",
        "email": "t.walker@email.com",
        "phone": "555-951-3690",
        "customer_id": "CS015",
        "signup_date": "2024-03-11"
    },
    {
        "name": "Michelle Young",
        "address": "654 Dogwood Dr, Beginburg, BB 95135",
        "email": "m.young@email.com",
        "phone": "555-753-9510",
        "customer_id": "CS016",
        "signup_date": "2024-04-23"
    },
    {
        "name": "Kevin Hall",
        "address": "789 Magnolia Mnr, Centreville, CV 15973",
        "email": "k.hall@email.com",
        "phone": "555-159-3570",
        "customer_id": "CS017",
        "signup_date": "2024-05-08"
    },
    {
        "name": "Laura Scott",
        "address": "951 Chestnut Ct, Outskirts, OS 35791",
        "email": "l.scott@email.com",
        "phone": "555-357-1590",
        "customer_id": "CS018",
        "signup_date": "2024-06-17"
    },
    {
        "name": "Richard Green",
        "address": "753 Walnut Way, Suburbia, SB 24680",
        "email": "r.green@email.com",
        "phone": "555-852-7410",
        "customer_id": "CS019",
        "signup_date": "2024-07-02"
    },
    {
        "name": "Patricia Adams",
        "address": "852 Hickory Hts, Exurbia, EB 86420",
        "email": "p.adams@email.com",
        "phone": "555-741-9630",
        "customer_id": "CS020",
        "signup_date": "2024-08-14"
    }
]

print(customers)