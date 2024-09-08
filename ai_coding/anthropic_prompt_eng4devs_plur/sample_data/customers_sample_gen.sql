-- Create the customer table
CREATE TABLE customer (
    customer_id VARCHAR(5) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    signup_date DATE NOT NULL
);

-- Insert 20 records into the customer table
INSERT INTO customer (customer_id, name, address, email, phone, signup_date) VALUES
('CS001', 'John Smith', '123 Main St, Anytown, AN 12345', 'john.smith@email.com', '555-123-4567', '2023-01-15'),
('CS002', 'Emma Johnson', '456 Elm Ave, Somewhere, SW 67890', 'emma.j@email.com', '555-987-6543', '2023-02-28'),
('CS003', 'Michael Brown', '789 Oak Rd, Elsewhere, EL 13579', 'm.brown@email.com', '555-246-8135', '2023-03-10'),
('CS004', 'Sarah Davis', '321 Pine Ln, Nowhere, NW 24680', 'sarah.d@email.com', '555-369-2580', '2023-04-05'),
('CS005', 'David Wilson', '654 Birch Blvd, Everywhere, EV 97531', 'd.wilson@email.com', '555-753-9514', '2023-05-20'),
('CS006', 'Lisa Taylor', '987 Cedar St, Someplace, SP 86420', 'lisa.t@email.com', '555-951-7532', '2023-06-12'),
('CS007', 'Robert Anderson', '147 Maple Dr, Anyville, AV 75319', 'r.anderson@email.com', '555-159-7532', '2023-07-03'),
('CS008', 'Jennifer Martinez', '258 Willow Way, Othertown, OT 95135', 'j.martinez@email.com', '555-357-9514', '2023-08-18'),
('CS009', 'William Thompson', '369 Spruce Sq, Thisplace, TP 15973', 'w.thompson@email.com', '555-852-9630', '2023-09-22'),
('CS010', 'Elizabeth Clark', '741 Ash Ave, Thatville, TV 35791', 'e.clark@email.com', '555-741-8520', '2023-10-07'),
('CS011', 'Christopher Lee', '852 Poplar Pl, Anotherburg, AB 24680', 'c.lee@email.com', '555-963-8520', '2023-11-14'),
('CS012', 'Amanda White', '963 Sycamore St, Lasttown, LT 86420', 'a.white@email.com', '555-147-2580', '2023-12-01'),
('CS013', 'Daniel Harris', '159 Redwood Rd, Firstcity, FC 13579', 'd.harris@email.com', '555-369-1470', '2024-01-19'),
('CS014', 'Jessica Lewis', '357 Sequoia Ter, Middletown, MT 97531', 'j.lewis@email.com', '555-258-1470', '2024-02-05'),
('CS015', 'Thomas Walker', '456 Juniper Jct, Endville, EV 75319', 't.walker@email.com', '555-951-3690', '2024-03-11'),
('CS016', 'Michelle Young', '654 Dogwood Dr, Beginburg, BB 95135', 'm.young@email.com', '555-753-9510', '2024-04-23'),
('CS017', 'Kevin Hall', '789 Magnolia Mnr, Centreville, CV 15973', 'k.hall@email.com', '555-159-3570', '2024-05-08'),
('CS018', 'Laura Scott', '951 Chestnut Ct, Outskirts, OS 35791', 'l.scott@email.com', '555-357-1590', '2024-06-17'),
('CS019', 'Richard Green', '753 Walnut Way, Suburbia, SB 24680', 'r.green@email.com', '555-852-7410', '2024-07-02'),
('CS020', 'Patricia Adams', '852 Hickory Hts, Exurbia, EB 86420', 'p.adams@email.com', '555-741-9630', '2024-08-14');