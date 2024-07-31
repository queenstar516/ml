class Department:
    def __init__(self, name):
        self.name = name
        self.lecturers = []
        self.courses = []
    
    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def add_course(self, course):
        self.courses.append(course)
    
    def to_dict(self):
        return {
            "Department Name": self.name,
            "Lecturers": [lecturer.to_dict() for lecturer in self.lecturers],
            "Courses": [course.to_dict() for course in self.courses]
        }

    def __str__(self):
        lecturers_str = "\n".join(str(lecturer) for lecturer in self.lecturers)
        courses_str = "\n".join(str(course) for course in self.courses)
        return f"Department: {self.name}\nLecturers:\n{lecturers_str}\nCourses:\n{courses_str}"