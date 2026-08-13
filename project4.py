type = []


def inputArray():
    """
    ==================
    Input Array:
    ==================
    UDF to take array inputs.
    
    This function hendles both 1D and 2D integer array inputs from the user and save all elements into list named 'type'
    
    Returns :
            list : A single flat list containing all entered numbers
    """
    global type

    print("choose array type :")
    print("1. 1D-array")
    print("2. 2D-array")
    
    choice = int(input("Enter your choice :"))
    if choice == 1:
        insert = input("Enter data for a 1D array (separated by space): ")
        lst = list(map(int, insert.split()))
        type.extend(lst)
        return lst

    elif choice == 2:
    
        num_rows = int(input("Enter number of rows : "))
        num_cols = int(input("Enter number of cols : "))

        elements = [] 
        for i in range(num_rows):
            current_row = []

            for j in range(num_cols):

                value_insert = int(input(f"Enter element [{i}][{j}]: "))
                current_row.append(value_insert)
            type.extend(current_row)
            elements.extend(current_row)
        return elements

def data_summary():
    """
    ===================
    Data Summary:
    ===================
    User defined function  to display statistical summary of data.
    Returns :
         dict : a dictionary containing count , min , max , sum ,and average of the data    
    """
    

    global type
    
    print(f"""
           Data Summary :

      - Total elements : {len(type)}
      - Minimum value : {min(type)}
      - Maximum value : {max(type)}
      - Sum of all value : {sum(type)}
      - Average value : {round(sum(type) / len(type), 2)}
""")



# data_summary()

# print(type)

def factorial():
    """
    ====================
    Factorial:
    ====================
    UDF to calculate factorial using recursion
    Return :
        Tuple : a tuple containing (the_number , its_factorial_value)
    """
    
    def fact(no):
        
        if no == 0 or no == 1:
            return 1
        else:
            return no * fact(no - 1)
    result = fact(no)
    print(f"Factorial of {no} is : {result}")

# factorial()

def filter_data():
    """
    ==============
    filter_data:
    ==============
    Filter data using a lambda function based on a user threshold.
     Return :
        list : a new list containing only the filtered numbers 
    """
    global type
    
    if not type:
        print("No data available to filter.")
        return
        
    print("Choose filtering option:")
    print("1. Get numbers greater than a threshold")
    print("2. Get numbers less than a threshold")
    print("3. Get even numbers")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        threshold = int(input("Enter threshold value: "))
        # Lambda checks if x is  greater than the threshold
        filtered = list(filter(lambda x: x >= threshold, type))
        print(f"Numbers greater than {threshold}: {filtered}")
        
    elif choice == 2:
        threshold = int(input("Enter threshold value: "))
        # Lambda checks if x is  less than the threshold
        filtered = list(filter(lambda x: x <= threshold, type))
        print(f"Numbers less than {threshold}: {filtered}")
        
    elif choice == 3:
        # Lambda checks if the number is divisible by 2
        filtered = list(filter(lambda x: x % 2 == 0, type))
        print(f"Even numbers: {filtered}")
        
    else:
        print("Invalid choice.")
        
# filter_data()

def sortted():
    """
    ==================
    sortted:
    ==================
    sorted data in ascending or decending orderd 
    Return :
        list : a new sorted list , or None if the choice is invalid.
    """

    global type
    if not type:
        print("Not available ")
        return
    print(""" choose sorting option :
          1. Ascending 
          2. Descending """)
    
    choice = int(input("Enter your choice :"))
    if choice == 1:
        sorted_data = sorted(type)
        print(f"sorted Data in Ascending order: {sorted_data}")
        
    elif choice == 2:
        sorted_data = sorted(type,reverse=True)
        print(f"sorted Data in Descending orderd: {sorted_data}")
    else:
        print("Invalid choice ")
# sortted()
        
def statistics(**kwargs):
    """
    ==============
    Statistics:
    ==============
    UDF to process dataset statistics using  keyword arguments.
    args:
        **kwargs : Arbitary key word argument .
    Returns:
        tuple : (count , min , max , sum , average ) or (None , None , None , None , None)    
    """
    
    set = kwargs.get('Dataset',type)
    
    if not set:
        print("The dataset is empty.")
        return None , None, None , None, None
    tot_ele = len(set)
    min_val = min(set)
    max_val  = max(set)
    total_sum = sum(set)
    average_val = total_sum / tot_ele
    
    print(" Dataset summary using **kwargs:")
    for key,value in kwargs.items():
        print("-",key,":",value)
        
    print("--calculate dataset statistics--")
    print(f"Count:{tot_ele}")
    print(f"Min:{min_val}")
    print(f"Max:{max_val}")
    print(f"Sum :{total_sum}")
    print(f"Average:{average_val}")
    
    return tot_ele,min_val,max_val,total_sum,average_val



print("Welcome to the Data Analyzer and Transformer program")

while True:
    print("\n Main Menu:")
    print("1.Input Data")
    print("2.Display Data Summary(Built-in-Functions)")
    print("3.Calculate Factorial(Recursion)")
    print("4.Filter Data by Threshold(Lambda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics(Return Multiple Values)")
    print("7.Exit Program")
    
    user_choice = int(input("Please enter your choice:"))
    
    if user_choice == 1:
        print(inputArray())
        print("Data has been stored successfully!")
    elif user_choice == 2:
        if not type:
            print("Error: No data availabe.Please select option 1 first.")
        else:
            data_summary()
    elif user_choice == 3:
        global no
        no = int(input("Enter a number to calculate its factorial :"))
        factorial()
    elif user_choice == 4:
        filter_data()
    elif user_choice == 5:
        sortted()
    elif user_choice == 6:
        if not type:
            print("Error: No data available.Please select option 1 first.")
        else:
            statistics(set=type)
    elif user_choice == 7:
        print("Thank you for using the Data Analyzer and Transformer program . Goodbye!")    
        print(inputArray.__doc__)
        print(data_summary.__doc__)
        print(factorial.__doc__)
        print(filter_data.__doc__)
        print(sortted.__doc__)
        print(statistics.__doc__)
        break
    else:
        print("Invalid Choice.option in (1 to 7)")
    