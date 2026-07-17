while True:
    print("""Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
""")

    userinput = int(input("Enter your choice: "))

    if userinput == 1:
        rows = int(input("Enter number of rows for pattern: "))

        for i in range(rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif userinput == 2:
        startRange = int(input("Enter the start of the range: "))
        endRange = int(input("Enter the end of the range: "))

        sumofall = 0

        for i in range(startRange, endRange + 1):
            if i % 2 == 0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")

            sumofall += i

        print(f"Sum of all numbers from {startRange} to {endRange} is: {sumofall}")

    elif userinput == 3:
        print("Exiting the program. Goodbye!!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")