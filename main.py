import json
class Student :
def init(self,student_id,name,dept,cgpa):
self.student_id=student_id
self.name=name
self.dept=dept
self.cgpa=cgpa
def display(self):
print(f"\nID :{self.student_id}")
print(f"NAME :{self.name}")
print(f"DEPARTMENT :{self.dept}")
print(f"CGPA :{self.cgpa} \n")
def to_dict(self):
return {
"student_id": self.student_id,
"name": self.name,
"dept": self.dept,
"cgpa": self.cgpa
}
students = []
def add_student():
try:
student_id=int(input("ENTER THE STUDENT ID:"))
for student in students:
if student.student_id==student_id:
print("student ID alreasy exists")
return
name=input("ENTER THE NAME OF THE STUDENT :")
dept=input("ENTER THE DEPARTMENT :")
cgpa=float(input("ENTER THE CGPA :"))
except ValueError:
print("ID and CGPA must be numbers")
return

student=Student(student_id,name,dept,cgpa)  
students.append(student)  
save_student()

def save_student():
data=[]
for student in students:
data.append(student.to_dict())
with open("stud.json","w") as file:
json.dump(data,file,indent=4)

def load_students():
try:
with open("stud.json","r")as file:
data=json.load(file)

for record in data:  
        student=Student(record["student_id"],record["name"],record["dept"],record["cgpa"])  
        students.append(student)  
except (FileNotFoundError,json.JSONDecodeError):  
    pass

def view_students(students):
if not students:
print("No student data found")
return
for student in students:
student.display()

def search_student():

if not students:  
    print("no student data found")  
    return  
try:  
    search_id=int(input("Enter ID to search :"))  
except ValueError:  
    print("ID must be number")  
    return  
found=False  
for student in students:  
    if search_id==student.student_id:  
        found=True  
        student.display()  
        return  
if not found:  
    print("Student not Found")

def update_student():
if len(students)==0:
print("NO STUDENT DATA FOUND")
return
try:
stud_id=int(input("Enter the student ID to Update :"))
except ValueError:
print("ID must be number")
return
found=False
for student in students:

if student.student_id==stud_id:  
        found=True  
        try:  
            new_id=int(input("ENTER THE NEW ID :"))  
            for s in students:  
                if s!=student and  new_id==s.student_id:  
                    print("This student id already exist")  
                    return  
            student.student_id=new_id  
            student.name=input("ENTER THE NEW NAME :")  
            student.dept=input("ENTER THE NEW DEPARTMENT :")  
            student.cgpa=float(input("ENTER THE NEW CGPA :"))  
            save_student()  

        except ValueError:  
            print("ID & CGPA must be numbers")  
            return  
        break  
if not found:  
    print("student not found")  
    return

def delete_student():
if len(students)==0:
print("NO STUDENT DATA FOUND")
return
try:
stud_id=int(input("Enter the student ID to delete :"))
except ValueError:
print("ID must be number")
return
found=False
for student in students:
if student.student_id==stud_id:
found=True
students.remove(student)
save_student()
print("student successfully deleted")
break
if not found:
print("student not found")
return

load_students()
while True:
print("--User Menu--")
print("1.add_student \n 2.view_student \n 3.search_student \n 4.Update_student \n 5.Delete_student \n 6.Exit")
try:
choice=int(input("Enter your choice 1 or 2 or 3 or 4 or 5 or 6 :"))
except ValueError:
print("Please enter the valid Number")
continue
if choice==1:
add_student()
elif choice==2:
view_students(students)
elif choice==3:
search_student()
elif choice==4:
update_student()
elif choice==5:
delete_student()
elif choice==6:
print("BYE@!@")
break
else:
print("Invalid Choice")
