students = []
subjects_set = set()

print("Welcome to the student data orgamiser!")
while True :
    
    print("\n Select an option :")
    print("1. Add student ")
    print("2. Display all student ")
    print("3. Update student information ")
    print("4. Delete staudent ")
    print("5. Display subject offered")
    print("6. Exit")
    
    choice = input("enter your choice:")
    
    if choice == "1":
        print(" Enter students details :")
        student_id = int(input("student ID:"))
        name=input("Name :")
        age=int(input("Age:"))
        grade=input("Gread :")
        dob=input("Date of Birth (YYYY-MM-DD) :")
        
        subjects = input("Subjects (coma-separated): ").split(",")
        subjects=[subject.strip() for subject in subjects]
        student_info = (student_id,dob)
        
        student = {
            "id":student_id,
            "info":student_info,
            "name":name,
            "age":age,
            "grade":grade,
            "subjects":subjects
        }
        
        students.append(student)
        for subject in subjects:
            subjects_set.add(subject)
        print("\n student added successfully!")
        
    elif choice == "2":
        print(" \n Display all students ")
        if len(students) == 0:
            print("No student record found ")
        else:
            for student in students:
                print(
                    f"student ID:{student['id']} |"
                    f"Name :{student['name']} |"
                    f"Age :{student['age']} |"
                    f"Grade :{student['grade']} |"
                    f"Subjects:{','.join(student['subjects'])}"
                )
    elif choice == '3':
        print("\n Update student information ")
        
        update_id = int(input("Enter student ID to updatee"))
        found = False
        for student in students:
            if student["id"] == update_id:
                found = True
                student["age"]=int(input("Enter new Age:"))
                new_subject = input("enter new subject(comma-seperated:").split(",")
                new_subject=[subject.strip() for subject in new_subject]
                
                student["subject"] = new_subject
                for subject in new_subject:
                    subjects_set.add(subject)
                print("Student information update sussessfully!")
                break
                
    elif choice == '4':
        delete_id=int(input("\n Enter student ID to delete:"))
        
        found = False
        
        for i in range(len(students)):
            if students[i]["id"] == delete_id:
                del students[i]
                found = True
                print("Student deleted successfully!")
                break
            if not found:
                print("Student not found")
    elif choice == '5':
        print("\n Subjects Offered")
        if len(subjects_set) == 0:
            print("No subject avaliable.")
        else:
            for subject in subjects_set:
                print(subject)
    elif choice == '6':
        print("\n Thank you for using the student Data Organizer!")
        break
    else:
        print("Invalid choice. Pleace try agin.")
        
        
        