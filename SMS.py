class Student:
     def __init__(self,name,ID,age):
          self.name=name 
          self.ID=ID
          self.age=age
          
     def Display(self):
          print(f"The name is {self.name}")
          print(f"your age {self.age}")
          print(f"your id is {self.ID} . ")
          
     def Search(self,ID):
          if self.ID == ID :
               print(f"found the  {ID}")
          else:
               print("not found ")
               
     
class Materiles(Student):
     
     def __init__(self,name,ID,age,Quizes,Mid,final,houres,credit_houres):
          super(). __init__(name,ID,age)
          self.Quizes=Quizes
          self.Mid=Mid
          self.final=final
          self.houres=houres
          self.credit_houres=credit_houres
          
          self.grade = self.Quizes + self.Mid + self.final
     def GBA(self):
          if self.grade>=97:
               p=4.0
          elif self.grade>=93:
               p=4.0
          elif self.grade>89:
               p=3.7
          elif self.grade>=84:
               p=3.3
          elif self.grade>=80:
               p=3.0
          elif self.grade>=76:
               p=2.7
          elif self.grade>=73:
               p=2.3
          elif self.grade>=70:
               p=2.0
          elif self.grade>=67:
               p=1.7
          elif self.grade>=64:
               p=1.3
          elif self.grade>=60:
               p=1.0
          else:
               p=0.0
          g = self.houres*p/self.credit_houres
          return p
          
     def evaluation(self):
          if self.grade>=95:
               return "A+"
          elif self.grade>=93:
               return "A"
          elif self.grade>89:
               return "A-"
          elif self.grade>=84:
               return "B+"
          elif self.grade>=80:
               return "B"
          elif self.grade>=76:
               return "B-"
          elif self.grade>=73:
               return "C+"
          elif self.grade>=70:
               return "C"
          elif self.grade>=67:
               return "C-"
          elif self.grade>=64:
               return "D+"
          elif self.grade>=60:
               return "D"
          else:
               return "F"
     def Display(self):
          
          print(f"grade is : {self.evaluation()} ")
          print(f"the GBA is {self.GBA()} ")
          print(f"Total : {self.grade} ")

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
