class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
    
    def __str__(self):
        departments_str = "\n".join(str(dept) for dept in self.departments)
        return f"Faculty: {self.name}\n{departments_str}"