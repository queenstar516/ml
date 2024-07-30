class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
    
    def __str__(self):
        return f"{self.name} ({self.code}, {self.credits} credits)"