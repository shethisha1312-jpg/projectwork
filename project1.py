print("Welcome to the Intaractive Personal Data Collector !")

name = input("Please Enter your Name: ")
age=int(input("Please Enter your Age: "))
height=float(input("Please Enter Height in meters: "))
favourite_number=int(input("Please Enter your favourite number: "))

birth_year=2026-age

print("\n Thank you! Here is the information we Collected:\n ")

print("Name :",name,"(Type :",type(name),",Memory Address:",id(name),")")
print("Age :",age,"(Type :",type(age),",Memory Address:",id(age),")")
print("Height :",height,"(Type :",type(height),",Memory Address:",id(height),")")
print("Favourite Number :",favourite_number,"(Type :",type(favourite_number),",Memory Address:",id(favourite_number),")")

height_as_int=int(height)

print("\n Type converstion demostaraction :")

print("Orignal height:",height,"(flot)")
print("Converted height:",height_as_int,"(int)")

print("Your birth year is approximately :",birth_year,"(based on your age of",age,")")

print("Thank you for using the Personal Data Collector. Goodbye!")