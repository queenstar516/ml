from user import User

class Lecturer(User):
    def __init__(self, firstname, lastname, email, password, staffId):
        super().__init__(firstname, lastname, email, password)
        self.staffId = staffId
    
    def getStaffId(self):
        return self.staffId
    
    def getLecturerDetails(self):
       return f"First Name: {self.firstname}\nLast Name: {self.lastname}\nemail: {self.email}\nPassword: {self.password}\nStaff ID: {self.staffId}"
    
