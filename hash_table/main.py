# Python dictionary
my_dict = {}


my_menu = {
    "lasagna": 14.75,
    "moussaka": 21.15,
    "sushi": 16.05
}

print(my_menu["sushi"])
print(my_menu.get("paella")) # test if element exists
print(my_menu.items())
print(my_menu.keys())
print(my_menu.values())

my_menu["samosas"] = 13
print(my_menu.items())

del my_menu
# remove a key-value pair
del my_menu["sushi"]
# empty the dictionary
my_menu.clear()

for key, value in my_menu.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

for dish in my_menu:
    print(dish)

for prices in my_menu.values():
    print(prices)


# Nested dictionaries
my_menu = {
    "sushi": {
        "price": 19.25,
        "best_served": "cold"
    },
    "paella": {
        "price": 15,
        "best_served": "hot"
    }
}
