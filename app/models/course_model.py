from abc import ABC, abstractmethod

# Abstract Base Class representing the "Product" in Factory Pattern
class Course(ABC):
    def __init__(self, id, title, description, level, duration):
        self.id = id
        self.title = title
        self.description = description
        self.level = level
        self.duration = duration
        self.career_roles = []
        # Base curriculum structure that could be overridden
        self.levels = {
            "Beginner": ["HTML", "CSS", "Basic JS"],
            "Intermediate": ["Responsive Design", "API Integration"],
            "Advanced": ["Backend", "Database", "Deployment"]
        }

    @abstractmethod
    def get_course_category(self):
        """Must be implemented by concrete classes."""
        pass

# Concrete Product 1
class ProgrammingCourse(Course):
    def __init__(self, id, title, description, level, duration):
        super().__init__(id, title, description, level, duration)
        self.career_roles = ["Software Engineer", "Backend Developer"]
        self.levels["Beginner"] = ["Syntax", "Variables", "Loops"]

    def get_course_category(self):
        return "Core Programming"

# Concrete Product 2
class DataScienceCourse(Course):
    def __init__(self, id, title, description, level, duration):
        super().__init__(id, title, description, level, duration)
        self.career_roles = ["Data Analyst", "AI Engineer", "ML Researcher"]
        self.levels["Beginner"] = ["Math Basics", "Pandas", "Numpy"]

    def get_course_category(self):
        return "Data Science & AI"

# Concrete Product 3
class WebDevCourse(Course):
    def __init__(self, id, title, description, level, duration):
        super().__init__(id, title, description, level, duration)
        self.career_roles = ["Frontend Developer", "Full Stack Developer"]

    def get_course_category(self):
        return "Web Development"

# The Factory Class (GoF Factory Design Pattern)
class CourseFactory:
    """
    True Implementation of the Factory Design Pattern.
    Creates objects without exposing instantiation logic and refers to newly created objects via a common interface.
    """
    @staticmethod
    def create_course(course_type, id, title, description, level, duration):
        if course_type == "Programming":
            return ProgrammingCourse(id, title, description, level, duration)
        elif course_type == "Data Science":
            return DataScienceCourse(id, title, description, level, duration)
        elif course_type == "Web Development":
            return WebDevCourse(id, title, description, level, duration)
        else:
            raise ValueError(f"Unknown course type requested: {course_type}")