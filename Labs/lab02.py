# 1. Name:
#    Arlo Jolley
# 2. Assignment Name:
#    LAB 02 : AUTHENTICATION
# 3. Assignment Description:
#    Write a program to read the contents of the file into a list.
#    The program will then prompt the user for a username and password. Finally, we will tell the user whether the user is authenticated.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was figuring out how to get the json file to read in and not throw a bunch of errors when runing the code.
# 5. How long did it take for you to complete the assignment?
#    About 2 hours
# page start
import json
print()

# varables
run_tf = True
run_tf2 = True
username_list = []
password_list = []
username = "null"
password = "null"
userpass_file = "null"
userpass_str = "null"
userpass = {}
access_tf = False

# functions


def get_access(x, y):
    try:
        u = username_list.index(x)
    except:
        return False
    try:
        p = password_list.index(y)
    except:
        return False

    if u == p:
        return True
    else:
        return False


# main code
# make sures there is no errors opening the file
try:
    userpass_file = open("./Resources/Lab02.json")
except:
    print("Unable to open file Lab02.json.")
    run_tf = False
finally:
    userpass_file.close()

if run_tf:
    while run_tf2:
        # list generate
        with open("./Resources/Lab02.json") as userpass_file:
            userpass_str = userpass_file.read()
            userpass = json.loads(userpass_str)

        username_list = userpass.get("username")
        password_list = userpass.get("password")

        # inputs from the user
        username = input("Username: ")
        password = input("Password: ")

        access_tf = get_access(username, password)

        if access_tf:
            print("You are Authenticated!")
        else:
            print("You are not authrized to use the system.")
        
        # quick video making code
        print()
        run = input()

        if run == "n":
            run_tf2 = False

# page end
print()
userpass_file.close()
