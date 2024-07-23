from user import User

class Student(User):
    def __init__(self, firstname, lastname, email, password, regNo, department):
        super().__init__(firstname, lastname, email, password)
        self.regNo = regNo
        self.department = department
    
    def getRegNo(self):
        return self.regNo
    
    def getStudentDetails(self):
        return f"First Name: {self.firstname}\nLast Name: {self.lastname}\nemail: {self.email}\nPassword: {self.password}\nregNo: {self.regNo}\nDepartment: {self.department}"
    


