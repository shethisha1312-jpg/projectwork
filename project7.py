import datetime
import time
import random
import uuid
import math
import sys
import string


# Date and Time Operations
def datetime_operations():
    while True:
        print("\n----- Date and Time Operations -----")
        print("1. Current Date and Time")
        print("2. Date Difference")
        print("3. Custom Date Format")
        print("4. Stopwatch")
        print("5. Countdown")
        print("6. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("Current Date and Time:", datetime.datetime.now())

        elif ch == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            try:
                date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
                diff = abs((date2 - date1).days)
                print("Date Difference:", diff, "days")
            except ValueError:
                print("Invalid Date Format!")

        elif ch == "3":
            now = datetime.datetime.now()
            print("Custom Date Format:", now.strftime("%d-%m-%Y %H:%M:%S"))

        elif ch == "4":
            print("Stopwatch Started...")
            input("Press Enter to stop...")
            print("Stopwatch Stopped!")

        elif ch == "5":
            try:
                sec = int(input("Enter countdown seconds: "))

                while sec > 0:
                    print("Time Remaining:", sec)
                    time.sleep(1)
                    sec -= 1

                print("Time's Up!")
            except ValueError:
                print("Please enter a valid number.")

        elif ch == "6":
            break

        else:
            print("Invalid Choice.")


# Mathematical Operations
def mathematical_operations():
    while True:
        print("\n----- Mathematical Operations -----")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Functions")
        print("4. Area of Circle")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            try:
                n = int(input("Enter a number: "))
                print("Factorial:", math.factorial(n))
            except ValueError:
                print("Please enter a valid number.")

        elif ch == "2":
            try:
                p = float(input("Enter Principal Amount: "))
                r = float(input("Enter Rate: "))
                t = float(input("Enter Time: "))
                ci = p * ((1 + r / 100) ** t) - p
                print(f"Compound Interest: {ci:.2f}")
            except ValueError:
                print("Please enter valid numbers.")

        elif ch == "3":
            try:
                a = float(input("Enter angle in degrees: "))
                rad = math.radians(a)

                print("Sin:", math.sin(rad))
                print("Cos:", math.cos(rad))
                print("Tan:", math.tan(rad))
            except ValueError:
                print("Please enter a valid number.")

        elif ch == "4":
            try:
                r = float(input("Enter radius: "))
                area = math.pi * r * r
                print("Area of Circle:", area)
            except ValueError:
                print("Please enter a valid number.")

        elif ch == "5":
            break

        else:
            print("Invalid Choice.")


# Random Data Generation
def random_data_generation():
    while True:
        print("\n----- Random Data Generation -----")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. OTP")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("Random Number:", random.randint(1, 100))

        elif ch == "2":
            try:
                n = int(input("Enter list size: "))
                lst = [random.randint(1, 100) for _ in range(n)]
                print("Random List:", lst)
            except ValueError:
                print("Please enter a valid number.")

        elif ch == "3":
            try:
                n = int(input("Enter password length: "))
                chars = string.ascii_letters + string.digits
                pwd = ''.join(random.choice(chars) for _ in range(n))
                print("Random Password:", pwd)
            except ValueError:
                print("Please enter a valid number.")

        elif ch == "4":
            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)

        elif ch == "5":
            break

        else:
            print("Invalid Choice.")


# UUID
def uuid_menu():
    print("\n----- Unique Identifier (UUID) -----")
    print("Generated UUID:", uuid.uuid4())


# File Operations
def file_operation_menu():
    while True:
        print("\n----- File Operations -----")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            filename = input("Enter filename: ")

            try:
                with open(filename, "x"):
                    pass
                print("File created Successfully!")
            except FileExistsError:
                print("File already exists!")

        elif ch == "2":
            filename = input("Enter filename: ")
            content = input("Enter content: ")

            try:
                with open(filename, "w") as f:
                    f.write(content)
                print("Data written successfully!")
            except Exception as e:
                print("Error:", e)

        elif ch == "3":
            filename = input("Enter filename: ")

            try:
                with open(filename, "r") as f:
                    content = f.read()

                print("File Content:")
                print(content)

            except FileNotFoundError:
                print("File not found!")

        elif ch == "4":
            filename = input("Enter filename: ")
            content = input("Enter content: ")

            try:
                with open(filename, "a") as f:
                    f.write(content)

                print("Data appended successfully!")

            except Exception as e:
                print("Error:", e)

        elif ch == "5":
            break

        else:
            print("Invalid Choice.")


# Explore Module Attributes
def explore_modules():
    print("\n----- Explore Module Attributes -----")

    try:
        print("Attributes of datetime module:")
        print(dir(datetime))

        print("\nAttributes of math module:")
        print(dir(math))

        print("\nAttributes of random module:")
        print(dir(random))

    except Exception as e:
        print(f"Error exploring module: {e}")


# Main Menu
while True:
    print("\n-------------------------------------------")
    print("Welcome to Multi-Utility Toolkit")
    print("-------------------------------------------")
    print("Choose an Option")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generations")
    print("4. Generate Unique Identifiers(UUID)")
    print("5. File Operations")
    print("6. Explore Module Attributes(dir())")
    print("7. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        datetime_operations()

    elif ch == "2":
        mathematical_operations()

    elif ch == "3":
        random_data_generation()

    elif ch == "4":
        uuid_menu()

    elif ch == "5":
        file_operation_menu()

    elif ch == "6":
        explore_modules()

    elif ch == "7":
        print("Thank you for using the Multi-Utility Toolkit!")
        break

    else:
        print("Invalid Choice. Please select from option 1 to 7.")