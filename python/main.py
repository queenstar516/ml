from student import Student
from lecturer import Lecturer

student1 = Student("Jane", "Smith", "janesmith@abc.com", "ufjfidfoi", "23/SCI01-009", "Computer Science")
student2 = Student("Henry", "Nwafor", "henrynwafor@gmail.com", "henry123", "LISTACC/CS/002", "Cyber Security")

lecturer1 = Lecturer("Miracle", "Sixtus", "miraclesixtus@gmail.com", "miratus", "LIS020")
lecturer2 = Lecturer("Counsel", "Okeke", "counselokeke@gmail.com", "counsel456", "LIST045")

print(student1.getLoginDetails())
print(student1.getStudentDetails())

print(student2.getLoginDetails())
print(student2.getStudentDetails())

print(lecturer1.getLoginDetails())
print(lecturer1.getLecturerDetails())

print(lecturer2.getLoginDetails())
print(lecturer2.getLecturerDetails())