from assignment10_course import Course
from assignment10_lecturer import Lecturer
from assignment10_department import Department
from assignment10_faculty import Faculty

#First Faculty
faculty_eng = Faculty("Engineering")
#Create Departments
dept1 = Department("Computer Engineering")
dept2 = Department("Electrical Engineering")
dept3 = Department("Mechanical Engineering")
#Add Departments to Faculty
faculty_eng.add_department(dept1)
faculty_eng.add_department(dept2)
faculty_eng.add_department(dept3)
#Create Lecturers
lecturer1 = Lecturer("Alice Johnson", "L001")
lecturer2 = Lecturer("Bob Smith", "L002")
lecturer3 = Lecturer("Carol Taylor", "L003")
lecturer4 = Lecturer("David Brown", "L004")
lecturer5 = Lecturer("Eva White", "L005")
lecturer6 = Lecturer("Frank Green", "L006")
#Create Courses
course1 = Course("Intro to Programming", "CS201", 3)
course2 = Course("Data Structures", "CS202", 3)
course3 = Course("Electromagnetics", "EE201", 3)
course4 = Course("Circuit Analysis", "EE202", 3)
course5 = Course("Engineering Thermodynamics", "ME201", 3)
course6 = Course("Fluid Mechanics", "ME202", 3)
#Add Lecturers and Courses to Department
dept1.add_lecturer(lecturer1)
dept1.add_lecturer(lecturer2)
dept1.add_course(course1)
dept1.add_course(course2)
dept2.add_lecturer(lecturer3)
dept2.add_lecturer(lecturer4)
dept2.add_course(course3)
dept2.add_course(course4)
dept3.add_lecturer(lecturer5)
dept3.add_lecturer(lecturer6)
dept3.add_course(course5)
dept3.add_course(course6)
#Print Faculty Information
print(faculty_eng)

#Second Faculty
faculty_arts = Faculty("Arts and Humanities")
#Create Departments
dept1_arts = Department("History")
dept2_arts = Department("Philosophy")
dept3_arts = Department("Linguistics")
#Add Departments to Faculty
faculty_arts.add_department(dept1_arts)
faculty_arts.add_department(dept2_arts)
faculty_arts.add_department(dept3_arts)
#Create Lecturers
lecturer1_arts = Lecturer("John Doe", "L007")
lecturer2_arts = Lecturer("Jane Smith", "L008")
lecturer3_arts = Lecturer("Emily Davis", "L009")
lecturer4_arts = Lecturer("Micheal Johnson", "L010")
lecturer5_arts = Lecturer("Laura Brown", "L011")
lecturer6_arts = Lecturer("Robert Wilson", "L012")
#Create Courses
course1_arts = Course("World History", "HIS201", 3)
course2_arts = Course("American History", "HIS202", 3)
course3_arts = Course("Ethics", "PHI201", 3)
course4_arts = Course("Metaphysics", "PHI202", 3)
course5_arts = Course("Syntax", "LIN201", 3)
course6_arts = Course("Semantics", "LIN202", 3)
#Add Lecturers and Courses to Department
dept1_arts.add_lecturer(lecturer1_arts)
dept1_arts.add_lecturer(lecturer2_arts)
dept1_arts.add_course(course1_arts)
dept1_arts.add_course(course2_arts)
dept2_arts.add_lecturer(lecturer3_arts)
dept2_arts.add_lecturer(lecturer4_arts)
dept2_arts.add_course(course3_arts)
dept2_arts.add_course(course4_arts)
dept3_arts.add_lecturer(lecturer5_arts)
dept3_arts.add_lecturer(lecturer6_arts)
dept3_arts.add_course(course5_arts)
dept3_arts.add_course(course6_arts)
#Print Faculty Information
print(faculty_arts), 3