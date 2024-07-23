class Course:
    def __init__(self, name, course_id, department, lecturer, credits, schedule, syllabus):
        self.name  = name
        self.course_id = course_id
        self.department = department
        self.lecturer = lecturer
        self.credits = credits
        self.schedule = schedule
        self.syllabus = syllabus
        self.enrolled_students = []

    def enroll_student(self, student):
        self.enrolled_students.append(student)
    
    def __str__(self):
        return f"Course: {self.name} (ID: {self.course_id})"