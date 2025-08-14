from functools import reduce

def addition(*args):
    print(sum(args))

def subtraction(*args):
    sub = reduce(lambda x, y: x - y,args)
    print(sub)

def multiplication(*args):
    multi = reduce(lambda x, y: x * y,args)
    print(multi)

def division(*args):
    try:
        multi = reduce(lambda x, y: x / y,args)
        print(multi)
    except ZeroDivisionError as Z:
        print("%"*50)
        print("plase do not enter 0 ",Z)
    

def modulus(num1,num2):
    print(num1%num2)

def exponentiation(num1,num2):
    print(num1**num2)

def floor_division(num1,num2):
    print(num1//num2)


## switch cases-------
def main():
    print()
    print("Welcome to your CLI - Calculator..!")
    print("--"*40)

    while True:
        print("\nA. for sum, sub, mult, div\nB. for modulus, exponent, floor division\nQ. to quit")
        first_choice = input("Enter your choice: ").strip().upper()

        ### choice 1---->
        if first_choice == "A":
            print("\nOperations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Back")
            choice = input("Enter your choice: ").strip()
            if choice == "5":
                continue
            numbers = tuple(map(float, input("Enter numbers separated by space: ").split()))
            if not numbers:
                print("No numbers entered.")
                continue
            match choice:
                case "1":
                    addition(*numbers)
                case "2":
                    subtraction(*numbers)
                case "3":
                    multiplication(*numbers)
                case "4":
                    division(*numbers)
                case _:
                    print("Invalid choice.")

        ### choice 2------>
        elif first_choice == "B":
            print("\n6. Modulus\n7. Exponentiation\n8. Floor Division\n9. Back")
            choice = input("Enter your choice: ").strip()
            if choice == "9":
                continue
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
            match choice:
                case "6":
                    modulus(num1, num2)
                case "7":
                    exponentiation(num1, num2)
                case "8":
                    floor_division(num1, num2)
                case _:
                    print("Invalid choice.")
        

        ## back to First choice---------> 
        elif first_choice == "Q":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid main menu choice.")


if __name__ == "__main__":
    main()