# Read the value associated with a key
user = {"first_name":"Heath"}
print(user["first_name"])

# Add a key-value pair
user["last_name"] = "Griffith"
print(user)

# Modify a value
user["first_name"] = "Joseph"
print(user)

# Remove a key-value pair
del user["first_name"]
print(user)