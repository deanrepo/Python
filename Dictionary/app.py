customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1988"
print(customer.get("birthdate", "Jan 1 1980"))