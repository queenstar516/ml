import datetime
import uuid
class User:
    def __init__(self, firstname, lastname, email, password):
        self.uuid = uuid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.time = datetime.datetime.now
    
    def __str__(self):
        return f"{self.firstname} with the e-mail: {self.email}"
    
    def greet(self):
        return f"Hello, my name is {self.firstname} {self.lastname}"
    
    def getLoginDetails(self):
        return f"Email: {self.email} \n Password: {self.password}"
    

