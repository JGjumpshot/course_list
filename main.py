from course import Course
from courselist import CourseList

def main():
    linked_list = CourseList()
    test = open("data.txt", "r")
    for i in test.readlines():
        # print(type(i))
        course = i.strip().split(',')
        # print(course)
        course = Course(int(course[0]), course[1], float(course[2]), float(course[3]))
        linked_list.insert(course)
    # iter_linked_list = linked_list.__iter__()
    # print(iter_linked_list.__next__())
    # print(linked_list.get_size())
    myList = linked_list
    print(myList.get_size())
if __name__ == "__main__":
    main()