import json
import os
FILE_PATH = "Z-CLI_based/To-do-list/Contact.json"

def show_phoneBook():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH,"r") as R:
            try:
                phone_book = json.load(R)
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

def update_phone_book():
    phone_book = show_phoneBook()
    print("enter serial number of contact list to update  contact")


def save_contacts(phone_book):
    with open(FILE_PATH,"w") as W:
        try:
            json.dump(phone_book,W, indent=4)
        except Exception as E:
            print()
            print("(****** Error at save_contact function. ***********",E)
            print()



def initial_input():
    print("Enter name and phone number in this format (e.g. John:9876543210 or type 'exit' to quit)")
    print()
    phone_book = {}
    serial = 1
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

        phone_book[serial] = (name, number)
        serial += 1

    save_contacts(phone_book)

def main():
    print("="*50)
    print("Welcome to the Phone Book.......................")
    print("="*50)
    
    initial_input()





if __name__ == "__main__":
    main()







# loaded_contact = load()
# for serial, key

# def add_contact():
#     loaded_contact = load()

#     loaded_contact["priyank"] = "0123456789"

    # dumper(loaded_contact)

    # print(load())



# def delete_contact():
#     loaded_contact = load()
#     print("enter contact name to delete")

    
#     return print(loaded_contact)

# delete_contact()
 






