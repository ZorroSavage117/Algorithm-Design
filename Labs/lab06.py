# 1. Name:
#      -Arlo Jolley
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      -Read a file and find a specific word.
# 4. Algorithmic Efficiency
#      -Pretty Efficient on smaller files.
# 5. What was the hardest part? Be as specific as possible.
#      -Getting it to read the file the right way.
# 6. How long did it take for you to complete the assignment?
#      -2 Hours

import json


def search_word_in_json(file_path, word_to_search):
    with open(file_path, 'rt') as file:
        data = json.load(file)

    for value in data["array"]:
        if value == word_to_search:
            return True

    return False

tf = True
while tf:
    print()
    file = input("What is the name of the file? ")
    item = input("What name are we looking for? ")
    result = search_word_in_json("./Resources/" + file, item)
    if result:
        print(f"We found {item} in {file}.")
    else:
        print(f"{item} not found.")

    con = int(input("Continue? "))
    if con == 0:
        tf = False
    
    print()