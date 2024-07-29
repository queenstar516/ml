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
    
    def to_dict(self):
        return {
            "name": self.name,
            "courseId": self.course_id,
            "department": self.department,
            "lecturer": self.lecturer,
            "credits": self.credits,
            "schedule": self.schedule,
            "syllabus": self.syllabus,
            "enrolledStudents": [enrolled_student.to_dict() for enrolled_student in self.enrolled_students]

        }

    def __str__(self):
        return f"Course: {self.name} (ID: {self.course_id})"