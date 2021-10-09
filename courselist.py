"""Linked list"""
class CourseList:
    """CourseList class"""
    def __init__(self, head=None):
        """init function"""
        self.head = head
        self.tail = None
        self.size = 0
    def is_empty(self):
        """Is empty function"""
        return self.head
    def insert(self, course):
        """insert into the list"""
        new_course = course
        if self.head is None:
            self.tail = new_course
        
            # current = self.head
            # while current is not None:
            #     if current.next_node is None:
            #         self.head = new_course
            #     elif current.next_node.number <= 
                  
            #     # if current.next_node.number
            #     current = current.next_node
        
        new_course.next_node = self.head
        self.head = new_course
        self.size += 1
    def remove(self, course):
        """Remove single item from the list"""
        current = self.head
        previous = None
        while current is not None:
            if current.data == course.data:
                break
            previous = current
            current = current.next_node
        if current is None:
            raise ValueError("{} is not in the list".format(course))
        if previous is None:
            self.head = current.next
        else:
            previous.next_node = current.next_node
    def size(self):
        """get size of linked list"""
        return self.size
    def find(self, element):
        """Find and return the element"""
        current = self.head
        while current is not None:
            if current.course_name == element:
                return True
            current = current.next_node
        return -1
    def calculate_gpa(self):
        return self.head.name

    def __str__(self):
        list_string = None
        current = self.head
        while current is not None:
            if list_string is None:
                list_string = str(current)
            else:
                list_string = list_string + " " + str(current)
            current = current.next_node
        return list_string
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
        return self.current_node.__str__()
        # course = self.head
