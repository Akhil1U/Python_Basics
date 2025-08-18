import json
import os
FILE_PATH = "Z-CLI_based/To-do-list/Contact.json"

serial = 0
# get next serial number for every operation...
def serial_number():
    global serial
    serial += 1
    return serial

### call this function for save contact to json store.
def save_contacts(phone_book):
    # phone_book = {}
    # serial = serial_number()
    with open(FILE_PATH,"w") as W:
        try:
    
            json.dump(phone_book,W, indent=4)
            
        except Exception as E:
            print()
            print("(****** Error at save_contact function. ***********",E)
            print()

###  for add contact in phoneBook for the first time..........
def initial_input():
    print("Enter name and phone number in this format (e.g. John:9876543210 or type 'exit' to quit)")
    print()
    phone_book = {}
    
    while True:
        user_input = input("name:phone  :")

        if user_input.lower() == 'exit':
            break

        if ':' not in user_input:
            print("Invalid format. Use Name:PhoneNumber")
            continue

        name, number = map(str.strip, user_input.split(':', 1))

        if not number.isdigit():
            print("Phone number should contain only digits.")
            continue
        # if not len(number) == 10:
        #     print("please enter 10 digit....")
        #     continue
        # phone_book = [name,number]
        phone_book[serial_number()] = [name, number]

    save_contacts(phone_book)


def show_phoneBook():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH,"r") as R:
            try:
                phone_book = json.load(R)
                print("-------All contacts---------")
                for s, (name, number) in phone_book.items():
                    print(f"{s}. {name} : {number}")
            except json.JSONDecodeError as JD:
                print()
                print("****json decode error***",JD)
                print()
            except KeyError as K:
                print()
                print("Key ERORRRRRRRRR ", K)
                print()
            except FileNotFoundError as ErrF:
                print()
                print("file not found......", ErrF)
                print()

    return phone_book

def add_contact():
    print("-------all contacts---------")
    phone_book = show_phoneBook()
    print()
    while True:
        
        user_input = input("enter in this format-->name:phone  : \nenter done to terminate  ")
        print()

        if user_input.lower() == 'done':
            break

        if ':' not in user_input:
            print("Invalid format. Use Name:PhoneNumber")
            continue

        name, number = map(str.strip, user_input.split(':', 1))

        if not number.isdigit():
            print("Phone number should contain only digits.")
            continue
        # if not len(number) == 10:
        #     print("please enter 10 digit....")
        #     continue

        phone_book[serial_number()] = [name, number]
        save_contacts(phone_book)
      
def update_phone_book():

    print("-------all contacts---------")
    phone_book = show_phoneBook()
    print()
    
    serial = input("enter serial number to update contact :").strip()
    while True:
        
        user_input = input("enter in this format-->name:phone  : \nenter done to terminate  ")
        print()

        if user_input.lower() == 'done':
            break

        if ':' not in user_input:
            print("Invalid format. Use Name:PhoneNumber")
            continue

        name, number = map(str.strip, user_input.split(':', 1))

        if not number.isdigit():
            print("Phone number should contain only digits.")
            continue
        # if not len(number) == 10:
        #     print("please enter 10 digit....")
        #     continue

        phone_book[serial] = [name, number]
        save_contacts(phone_book)

def main():
    print("="*50)
    print("Welcome to the Phone Book.......................")
    print("="*50)

    ### first operation of the phone Book.
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        initial_input()
    while True:
        print("\nMenu:\n1. Show PhoneBOOk\n2. Update contact\n3. Add contact\n4. Delete contact\n5. Exit")
        choice = input("Enter your choice: ").strip()
        print()
        if choice == "1":
            show_phoneBook()
        elif choice == "2":
            # continue
            update_phone_book()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            continue
            # delete_contact()
        elif choice =="5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()




# def delete_contact():
#     print("-------all contacts---------")
      # phone_book = show_phoneBook()
      # print()
#     serial = int(input("enter serial number to Delete contact :"))
#     if phone_book.pop(serial):

#         print(f"contact deleted success fully///!")
#         save_contacts(phone_book)









