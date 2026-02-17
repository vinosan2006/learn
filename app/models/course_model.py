class Course:
    def __init__(self, name):
        self.name = name
        self.levels = {
            "Beginner": ["HTML", "CSS", "Basic JS"],
            "Intermediate": ["Responsive Design", "API Integration"],
            "Advanced": ["Backend", "Database", "Deployment"]
        }
        self.career_roles = [
            "Junior Web Developer",
            "Frontend Developer",
            "Full Stack Developer"
        ]
