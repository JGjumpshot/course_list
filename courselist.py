"""Linked list"""
class CourseList:
    """CourseList class"""
    def __init__(self, head=None):
        """init function"""
        self.head = head
        self.size = 0
    def insert(self, course):
        """insert into the list"""
        new_course = course
        if self.head is None:
            self.head = new_course
        new_course.next_node = self.head
        self.head = new_course
        self.size += 1
    def find(self, element):
        """Find and return the element"""
        current = self.head
        while current is not None:
            print(current)
            if current.course_name == element:
                return current
            current = current.next_node
        return -1
    def calculate_gpa(self):
        return self.head.name
    def __iter__(self):
        """iterate"""
        self.current_node = None
        self.next_node = self.head
        return self
    def __next__(self):
        """next"""
        # return self.next_node
        if self.next_node is None:
            raise StopIteration
        self.current_node = self.next_node
        self.next_node = self.next_node.next()
        return self.current_node
        # course = self.head
