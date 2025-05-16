 #?   --New Program--
import os
import time
import json


# User data
users = [] 

# Save users to JSON file
def save_users():
    with open("users.json", "w") as f:
        json.dump([user.__dict__ for user in users], f)

# Load users from JSON file
def load_users():
    global users
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
            users = [User(**user_data) for user_data in data]
    except FileNotFoundError:
        users = []

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') #to work on Windows, macOS and Linux

# Users main tool
class User:
    def __init__(self, first_name, last_name, id_0, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.id_0 = id_0
        self.status = status

    def show_info(self):
        return f"First name: {self.first_name} \nLast name: {self.last_name} \nMember ID: {self.id_0} \nStatus: {self.status}"

# Choise 1
def creat_user():
    print("* Gym Membership Management *\n\n")
    
    print("Adding new member:")
    first_name = input("\nEnter first name :  ")
    last_name = input("Enter last name :  ")
    id_0 = input("Enter membership ID :  ")
    need_status = input("Enter membership status, or click ENTER :  ")
    status = need_status if need_status else 'inactive'
    print("\n -user added successfuly- \n\n")
    new_user = User(first_name, last_name, id_0, status)
    users.append(new_user)
    time.sleep(1)
    clear_screen()
    save_users()
    return new_user

# Choise 2
def display_users():
    if not users:
        print("* Gym Membership Management *\n\n")
        print("-No users registered yet!\n")
    else:
        print("Showing all members:\n")
        for user in users:
            print(user.show_info())
            print("---------------")
        time.sleep(4)
        clear_screen()

#Choise 3
def member_search():
    while True:
        if not users:
            clear_screen()
            print("* Gym Membership Management *\n\n")
            print("-No users registered yet!\n")
            break
        
        print("* Gym Membership Management *\n\n")
        print("Search by: \n")
        print("1. Membership ID")
        print("2. First Name:")
        print("3. Membership Status:")
        print("4. Exit")

        search_tool = input("Enter your choise: ")

        clear_screen()
        print("* Gym Membership Management *\n\n")
        
        if search_tool == "1":
            search_engin = input("\nEnter the ID to search: ")
            found_users = [user for user in users if user.id_0 == search_engin]
        elif search_tool == "2":
            search_engin = input("\nEnter the first name to search: ")
            found_users = [user for user in users if user.first_name == search_engin]
        elif search_tool == "3":
            search_engin = input("\nEnter the member status to search: ")
            found_users = [user for user in users if user.status == search_engin]
        elif search_tool == "4":
            print("Exiting...\n")
            time.sleep(1)
            clear_screen()
            break

        else:
            print(" - Invalide choise! -\n ")
            time.sleep(2)
            clear_screen()
            return
    
        if not users:
            clear_screen()
            print("No users registered yet!\n")
            return
        elif found_users:
            clear_screen()
            print("* Gym Membership Management *\n\n")
            for i in found_users:
                print(i.show_info())
                print("---------------")
        else:
            print("\nNot found! \n")

        time.sleep(3)
        clear_screen()



# welcom
clear_screen()
load_users()
print("Welcom to Gym Membership Management \nMade by H (as usual ⌐■_■)\n\n")

# Program 
while True:
    print("Choose an Action:\n")
    print("1. Add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit")

    choise = input("Enter your choise: ")

    if choise == "1":
        clear_screen()
        creat_user()
    elif choise == "2":
        clear_screen()
        display_users()
    elif choise == "3":
        clear_screen()
        member_search()
    elif choise == "4":
        clear_screen()
        print("\nExiting...")
        time.sleep(1)
        clear_screen()
        break
    else:
        print("\n\n - Error: unexpected choise! -\n   program down...\n\n")
        break


    if choise not in ["3", "2"]:
        print("* Gym Membership Management *\n\n")


     
#?       Follow us  ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ
#!    Youtube ->   @ZU Informatics 
