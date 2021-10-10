"""Linked list"""
class CourseList:
    """CourseList class"""
    def __init__(self, head=None):
        """init function"""
        self.head = head
        # self.tail = None
        self._size = 0
    def is_empty(self):
        """Is empty function"""
        return self.head
    def insert(self, course):
        """insert into the list"""
        new_course = course
        if self.head is None:
            self.head = new_course
            self._size += 1
            return
        if new_course.number() <= self.head.number():
            new_course.next_node = self.head
            self.head = new_course
            self._size += 1
            return 
        current = self.head
        while current is not None:
            if current.next_node is None:
                current.next_node = new_course
                self._size += 1
                return
            elif current.next_node.number() >= new_course.number():
                new_course.next_node = current.next_node
                current.next_node = new_course
                self._size += 1
                return
            
            # if current.next_node.number <
            current = current.next_node
        
        # new_course.next_node = self.head
        # self.head = new_course
        # self._size += 1
    def remove(self, course):
        """Remove single item from the list"""
        current = self.head
        previous = None
        while current is not None:
            if current.course_number == course:
                break
            previous = current
            current = current.next_node
        if current is None:
            raise ValueError("{} is not in the list".format(course))
        if previous.next_node is None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node
        self._size -= 1
    def remove_all(self, course):
        """Remove all items with course num from the list"""
        temp = self.head
        previous = None

        
        while temp is not None and temp.number() == course:
            self.head = temp.next_node
            temp = self.head
        while temp is not None:
            while temp is not None and temp.number() != course:
                previous = temp
                temp = temp.next_node
            if temp is None:
                return self.head
            previous.next_node = temp.next_node
            temp = previous.next_node
            self._size -= 1
        return self.head
    def size(self):
        """get _size of linked list"""
        return self._size
    def find(self, element):
        """Find and return the element"""
        current = self.head
        while current is not None:
            if current.course_number == element:
                return current
            current = current.next_node
        return -1
    def calculate_gpa(self):
        current = self.head
        _grade_pts = 0
        _credits = 0
        _raw_value = 0
        while current is not None:
            _grade_pts += current.grade()
            _credits += current.credit_hr()
            _raw_value += current.grade() * current.credit_hr()
            current = current.next_node
        if _raw_value == 0.0 and _credits == 0.0:
            return 0.0
        else:
            final_gpa = _raw_value / _credits
        if current is not None:
            return round(final_gpa, 3)
        else:
            return final_gpa
        # while current is not None:
        #     if current.next_node is None:
        #         break
    def is_sorted(self):
        current = self.head
        value = 0
        if current is None:
            return True
        try:
            while current is not None:
                if current.next_node is None:
                    value = True
                    return value
                if current.number() <= current.next_node.number():
                    current = current.next_node
                else:
                    value = False
                    return value
        except:
            value = False
            return False
    def __str__(self):
        list_string = None
        current = self.head
        while current is not None:
            if list_string is None:
                list_string = " " +str(current) + "\n"
            else:
                list_string = list_string + " " + str(current) + "\n"
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
        self.next_node = self.next_node.next_node
        return self.current_node.__str__()
        # course = self.head
