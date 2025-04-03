from typing import  Dict
if __name__ == "__main__":
    # Creating a key-value pair map
    my_map = {
        "name": "Aamir",
        "age": 30,
        "city": "London"
    }

    # Displaying the map
    print(my_map)
    new_map: Dict[str, str] = {} # Empty dictionary

    # Adding key-value pairs dynamically
    new_map["name"] = "Shehzal"
    new_map["age"] = 4
    new_map["city"] = "riyadh"

    print(new_map)
    print(new_map["age"])

