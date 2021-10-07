class CourseList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size
    def insert(self, course):
        new_course = course
        if self.head is None:
            self.head = new_course
        new_course.next_node = self.head
        self.head = new_course
        self.size += 1
    def find(self, element):
        current = self.head
        while current is not None:
            print(current)
            if current.course_name == element:
                return current
            current = current.next_node
        return -1
    def __iter__(self):
        return self
    def __next__(self):
        course = self.head
        

        