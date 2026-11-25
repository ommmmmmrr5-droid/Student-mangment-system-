students = []


# Add Student Function

def AddStudent():

    name = input("Enter name: ")
    ID = int(input("Enter ID: "))
    age = int(input("Enter age: "))

    Quizes = float(input("Enter Quizes: "))
    Mid = float(input("Enter Mid: "))
    final = float(input("Enter Final: "))
    credit_hours = int(input("Enter Credit Hours: "))

    student = Materials(
        name, ID, age,
        Quizes, Mid, final, credit_hours
    )

    students.append(student)

    print("Student added successfully!")


# Search Student Function

def SearchStudent(ID):

    for student in students:

        if student.ID == ID:

            print("Student Found!")
            student.Display()
            return

    print("Student Not Found!")


# Display All Students Function

def DisplayAll():

    if len(students) == 0:
        print("No students available")
        return

    for student in students:

        print("------------------")
        student.Display()


# Main Program

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":

        AddStudent()

    elif choice == "2":

        ID = int(input("Enter ID to search: "))
        SearchStudent(ID)

    elif choice == "3":

        DisplayAll()

    elif choice == "4":

        print("Program Closed")
        break

    else:

        print("Invalid Choice!")