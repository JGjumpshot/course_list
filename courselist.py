from course import Course
new_course = Course(1200, "test", 2.0, 2.0)
print(new_course)
class CourseList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        course = Course(value)