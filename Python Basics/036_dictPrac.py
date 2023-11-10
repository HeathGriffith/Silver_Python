'''Create and Print a Dictionary: Create a dictionary called vehicle with keys make, model, and year, and their respective values. Print the dictionary.
Modify a Dictionary: In the vehicle dictionary, change the year to the current year. Print the updated dictionary.
Add and Remove Elements: Add a new key-value pair color: 'blue' to the vehicle dictionary. Then, remove the make key from the dictionary. Print the final dictionary.
Nested Dictionary: Create a nested dictionary where each key is a user's first name, and the value is another dictionary containing their last_name and age. Example: users = {"Alice": {"last_name": "Smith", "age": 30}}. Add a new user to this dictionary and print it.
Iterate Over a Dictionary: Write a loop to iterate over the vehicle dictionary and print each key and its corresponding value in the format "Key: Value".'''

vehicle = {"make": "toyota", "model": "highlander", "year": "2021"}

vehicle["year"] = "2023"

vehicle["color"] = "blue"
del vehicle["make"]
# print(vehicle)

users = {"Heath" : {"last_name": "Griffith", "age" : "40"}, 
         "Macrina": {"last_name": "Garza", "age": "37"}}

for key in vehicle:
    print(f"{key}: {vehicle[key]}")