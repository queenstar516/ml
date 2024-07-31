class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
    
    def to_dict(self):
        return {
            "Course Title" : self.name,
            "Course Code" : self.code,
            "Credits": self.credits
        }

    def __str__(self):
        return f"{self.name} ({self.code}, {self.credits} credits)"