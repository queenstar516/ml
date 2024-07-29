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
    
    def to_dict(self):
        return {
            "name": self.name,
            "facultyId": self.faculty_id,
            "departments": [department.to_dict() for department in self.departments],
            "dean": self.dean,
            "email": self.email,
            "phoneContact": self.phone_contact,
            "location": self.location,
            "website": self.website,
            "courses Offered": [course_offered.to_dict() for course_offered in self.courses_offered],
            "Research Areas": [research_area.to_dict() for research_area in self.research_areas],
            "Faculty Members": [faculty_member.to_dict() for faculty_member in self.affiliate_faculty_members],
            "Libraries": [library.to_dict() for library in self.libraries],
            "Labs": [lab.to_dict() for lab in self.labs],
            "Classrooms": [classroom.to_dict() for classroom in self.classrooms]
        }

    def __str__(self):
        return f"Faculty of {self.name}"