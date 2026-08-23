class Person:
    """
    ======================
    Class: Person
    ======================
    A base class that models an individual with generic identity details.
    
    """
    def __init__(self, name, age):
        """Initializes a Person instance."""
        self.name = name
        self.age = int(age)
    
    def display(self):
        """Prints the profile name and age formatted into the terminal."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Employee(Person):
    """
    ======================================
    Class: Employee (Inherits from Person)
    ======================================
    Represents corporate employees. Implements data encapsulation 
    principles to hide critical internal parameters (ID and Salary).
    
    Attributes:
        __employee_id (str): A private alpha-numeric staff token.
        __salary (float): A private float tracking monthly earnings.
    """
    def __init__(self, *args):
        """Initializes an Employee dynamically based on argument count."""
        if len(args) >= 4:
            super().__init__(args[0], args[1])
            self.__employee_id = args[2]
            self.__salary = float(args[3])
        elif len(args) == 2:
            super().__init__(args[0], args[1])
            self.__employee_id = "not assigned"
            self.__salary = 0.0
        else:
            super().__init__("unknown", 0)
            self.__employee_id = "unknown"
            self.__salary = 0.0
            
    def get_employee_id(self):
        """Accessor method for the hidden employee identity string."""
        return self.__employee_id
    
    def set_employee_id(self, employee_id):
        """Mutator method to update the hidden corporate identification sequence."""
        self.__employee_id = employee_id
        
    def get_salary(self):
        """Accessor method for the hidden salary numeric value."""
        return self.__salary
    
    def set_salary(self, salary):
        """Mutator method with an integrated range verification mechanism."""
        if salary >= 0:
            self.__salary = float(salary)
        else:
            print("Salary cannot be negative")
                    
    def display(self):
        """Extends the parent display method to print hidden ID and currency."""
        super().display()
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary: ₹{self.get_salary():.2f}")
        
    def __del__(self):
        pass
    
class Manager(Employee):
    """
    =======================================
    Class: Manager (Inherits from Employee)
    =======================================
    Models operational leaders overseeing internal operational units.
    
    Attributes:
        department (str): Functional domain name assigned to this role.
    """
    def __init__(self, *args):
        """Initializes a Manager and attaches departmental assignments."""
        super().__init__(*args)
        if len(args) >= 5:
            self.department = args[4]
        else:
            self.department = "general"
        
    def display(self):
        """Extends standard Employee details with specific manager metadata."""
        super().display()
        print(f"Department: {self.department}")
        
def main():
    """
    ===============
    Function: main
    ===============
        This is the main starter function that runs the whole system. 
    
    What it does:
    1. Shows a menu on the screen for the user to pick choices.
    2. Takes input keys from the user.
    3. Creates new profiles and saves them into lists.
    4. Prints information out when requested.
    5. Cleans up and stops the system safely when you choose to exit.
    """
    persons = []
    employees = []
    managers = []
    
    print("--- Python OOP Project: Employee Management System ---")
    
    while True:
        print(''' 
Choose an Operation:
1.Create a Person
2.Create an Employee
3.Create a Manager
4.Show Details
5.Exit
''')
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            p = Person(name, age)
            persons.append(p)
            print(f"Person created with name: {name} and age: {age}.")
            print("--- Choose another operation ---")
            
        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            emp = Employee(name, age, emp_id, salary)
            employees.append(emp)
            print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ₹{salary:.2f}")
            print("--- Choose another operation ---")
        
        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            mgr = Manager(name, age, emp_id, salary, dept)
            managers.append(mgr)
            print(f"Manager Created with name: {name}, age: {age}, ID: {emp_id}, salary: ₹{salary:.2f}, and department: {dept}.")
            print("--- Choose another operation ---")
            
        elif choice == "4":
            print("Choose details to show:")
            print('''\
1.Person
2.Employee
3.Manager''')
            sub_choice = input("Enter your choice: ").strip()
            print()
            
            if sub_choice == "1":
                if not persons:
                    print("No records found.")
                else:
                    print("Person Details:")
                    for p in persons:
                        p.display()
                        print()
            elif sub_choice == "2":
                if not employees:
                    print("No records found.")
                else:
                    print("Employee Details:")
                    for emp in employees:
                        emp.display()
                        print()
            elif sub_choice == "3":
                if not managers:
                    print("No records found.")
                else:
                    print("Manager Details:")
                    for mgr in managers:
                        mgr.display()
                        print()
            print("--- Choose another operation ---")
            
        elif choice == "5":
            persons.clear()
            employees.clear()
            managers.clear()
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!\n")
            
            # Prints the clean documentation structure automatically upon termination
            print("================================================")
            print("      SYSTEM ARCHITECTURE DOCUMENTATION        ")
            print("================================================")
            print(Person.__doc__)
            print(Employee.__doc__)
            print(Manager.__doc__)
            print(main.__doc__)
            break
        else:
            print("Invalid choice! Please select a valid option.")
            
if __name__ == "__main__":
    main()
