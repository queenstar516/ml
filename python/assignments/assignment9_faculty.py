class Faculty:
    def __init__(self, name, faculty_id, dean, email, phone_contact, location, website):
        self.name = name
        self.faculty_id = faculty_id
        self.departments = []
        self.dean = dean
        self.email = email
        self.phone_contact = phone_contact
        self.location = location
        self.website = website
        self.courses_offered = []
        self.research_areas = []
        self.affiliate_faculty_members = []
        self.libraries = []
        self.labs = []
        self.classrooms = []
    
    def add_department(self, department):
        self.departments.append(department)
    
    def add_course(self, course):
        self.courses_offered.append(course)
    
    def add_research_area(self, research_area):
        self.research_areas.append(research_area)
    
    def add_faculty_member(self, faculty_member):
        self.affiliate_faculty_members.append(faculty_member)
    
    def add_library(self, library):
        self.libraries.append(library)
    
    def add_lab(self, lab):
        self.labs.append(lab)
    
    def add_classroom(self, classroom):
        self.classrooms.append(classroom)
    
    def __str__(self):
        return f"Faculty of {self.name}"