pluralsight course:
===================

https://app.pluralsight.com/ilx/video-courses/clips/14e4063b-5bb2-45c9-84b0-2eba658922b6

# Prompts to generate TestCases
prompt to create a BankAccount class
```txt

generate a python class BankAccount. It should  allow operations of  deposit,  withdraw, get_balance  and should store internally  a balance amount
```

add tests
```txt
for the BankAccount class  create test cases to verify the functionality of this class.
```


# Prompts to create a sample data
```txt
now generate sample data  for a customer database with fields for name, address, email, phone number, customer ID, and signup date, Create 20 records.

```
for sql DDL 
```txt 

based on Sample Customer Database Records in json  create  a SQL DDL for a table customer  and  insert statements for 20 records.
```


more complex sample data
```md
Generate sample data for a shopping cart in an e-commerce application. The shopping cart should include the following properties:
- cartid (string): A unique identifier for the shopping cart.
- userld (string): The identifier of the user associated with the cart.
- items (array of objects): An array of objects representing the products in the cart.
   
Each item object should include:
- productid (string): The unique identifier of the product.
- name (string): The name of the product.
- price (number): The price of the product. 
- quantity (number): The quantity of the product in the cart.
- attributes (object): An object containing additional attributes of the product, such as color and brand.
- totalltems (number): The total number of items in the cart.
- subtotal (number): The subtotal of the cart before any discounts or taxes.
- shippingAddress (object): An object representing the shipping address.

Please provide the sample dta in JSON format.
```

propose a sql ddl schema

``` 
based on your generated Sample Shopping Cart Data  what  data model  would you propose  for a sql backend ?
```

the below generated an asciii art ERD
``` 
can you generate an image entity diagram for this schema?
```

next complex example  of smaple data from specific (sensitive) domain

```md
Generate 20 detailed patient records, each including the following:
- Name (gender-neutral)
- Date of birth, ensuring a diverse age range from children to the elderly
- Address, reflecting various regions of the United States
- Specific medical conditions relevant to the patient's age and geographical location
- A brief health history including past major illnesses or surgeries
- Current medications, ensuring no negative interactions with each other and realistic for the patient's conditions
- Allergies, particularly to medications or common allergens
- Recent lab results appropriate for their conditions (like HbA1c for diabetics, blood pressure readings for hypertensive patients)
- Vaccination status, updated according to CDC guidelines
- Next scheduled follow-up or screening tests
```

# Prompts for Debugging Techniques
## Types of errors:
- syntax errors
- runtime errors
- logical errors
- performance issues

compiler helps with syntax and runtime errors  +  debugging tools

```
this function should calculate the average of an array of numbers.  but i'm getting the wrong results. it should be 5.4. What's happening? 

###
def calculate_average(nums):
    sum = 0
    for num in nums:
        sum += num
    average = sum  / len(nums)
    return average

numbers  = [4,7,2,9,3]

result = calculate_average(numbers)
print(f"the average for {numbers} is: {result}")
 ```

# Prompts for Pair programming

``` 
I need to implement a binary search algorithm in python, but i'm not sure where to start. Can you provide a basic template and explain the key steps involved? 
```