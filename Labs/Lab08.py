# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      Sort a list of words.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the sort to work properly.
# 5. How long did it take for you to complete the assignment?
#      2 hours.

import json

def sort(file_name):
    # Open file as list
    file_path = "./Resources/" + file_name
    with open(file_path, "rt") as file:
        file_data = json.load(file)
    file_lt = file_data["array"]

    # Debug
    print(len(file_lt))
    # Sorting the list unless the length of the list is 1
    if len(file_lt) > 1:
        pivot = len(file_lt) - 1
        check = pivot - 1
        largest = pivot 
        while pivot > 0:
            if file_lt[check] > file_lt[largest]:
                largest = check
            check -= 1
        
            if file_lt[largest] > file_lt[pivot]:
                temp = file_lt[pivot]
                file_lt[pivot] = file_lt[largest]
                file_lt[largest] = temp
            
            if check == -1:
                pivot -= 1
                check = pivot -1
                largest = pivot

    # Output.
    print(f"The values in {file_name} are:")
    for value in file_lt:
        print(f"        {value}")


print()
sort("Lab08.empty.json")
print()
sort("Lab08.trivial.json")
print()
sort("Lab08.languages.json")
print()
sort("Lab08.states.json")
print()
sort("Lab08.cities.json")
print()