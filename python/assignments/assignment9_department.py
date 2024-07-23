class Department:
    def __init__(self, name, department_id, hod, office_location, email, phone_contact):
        self.name = name
        self.department = department_id
        self.hod = hod
        self.office_location = office_location
        self.email = email
        self.phone_contact = phone_contact
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
    
    def __str__(self):
        return f"Department of {self.name}"