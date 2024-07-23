from assignment9_faculty import Faculty
from assignment9_department import Department
from assignment9_course import Course

science_faculty = Faculty(
    name= "Sciences",
    faculty_id= "SCI098",
    dean= "Prof. Alice Brown",
    email= "sciences@example.edu",
    phone_contact= "08067239849",
    location= "Science Building, Main Campus",
    website= "http://sciences.example.edu"
)

cs_department = Department(
    name= "Computer Science",
    department_id= "CS034",
    hod= "Dr. John Smith",
    office_location= "Room 201, CS Building",
    email= "cs_dept@example.edu",
    phone_contact= "0918474757753"
)

course_ai = Course(
    name= "Artificial Intelligence",
    course_id= "CS504",
    department= "Computer Science",
    lecturer= "Dr Jane Doe",
    credits= 3,
    schedule= "Mon/Wed/Fri 10:00 - 11:30",
    syllabus= "Introduction to AI, Machine Learning, Neural Networks"
)

science_faculty.add_department(cs_department)
science_faculty.add_course(course_ai)
cs_department.add_course(course_ai)

print(science_faculty)
print(cs_department)
print(course_ai)
