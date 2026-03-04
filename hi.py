capitals = {"United States" : "Washington DC",
            "India" : "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}





#values = capitals.values()
for value in capitals.values():
    print(value)


items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")