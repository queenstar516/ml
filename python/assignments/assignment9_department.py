class Department:
    def __init__(self, name, department_id, hod, office_location, email, phone_contact):
        self.name = name
        self.department_id = department_id
        self.hod = hod
        self.office_location = office_location
        self.email = email
        self.phone_contact = phone_contact
        self.lecturers = []
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
    
    def to_dict(self):
        return {
            "name": self.name,
            "departmentId": self.department_id,
            "HOD": self.hod,
            "Office Location": self.office_location,
            "email": self.email,
            "Phone Contact": self.phone_contact,
            "Lecturers": [lecturer.to_dict() for lecturer in self.lecturers],
            "courses": [course.to_dict() for course in self.courses]
        }
    
    def __str__(self):
        return f"Department of {self.name}"
    