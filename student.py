# Student class mapped from the UML class diagram (see README.md)
# "-" in the diagram = private  -> in Python we use a double underscore (__name)
# "+" in the diagram = public   -> normal method name
# underlined in the diagram = static/class attribute -> class variable


class Student:
    # class variable: shared by all Student objects, counts how many were created
    student_count = 0

    # ---------- Constructor ----------
    def __init__(self, student_id, name, email, department):
        self.__student_id = student_id
        self.__name = name
        self.__email = email
        self.__department = department
        self.__gpa = 0.0       # a new student starts with GPA 0
        self.__courses = []    # empty course list
        Student.student_count += 1

    # ---------- Getters ----------
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_department(self):
        return self.__department

    def get_gpa(self):
        return self.__gpa

    def get_courses(self):
        return self.__courses

    @staticmethod
    def get_student_count():
        return Student.student_count

    # ---------- Setters ----------
    # No setter for student_id, because the ID should never change
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_department(self, department):
        self.__department = department

    # ---------- Other methods ----------

    # GPA must be between 0.0 and 4.0, otherwise we ignore it
    def update_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            print(f"Invalid GPA: {gpa} (must be 0.0 - 4.0)")

    # Adds a course only if the student isn't already enrolled in it
    def enroll_course(self, course):
        if course in self.__courses:
            print(f"{self.__name} is already enrolled in {course}")
        else:
            self.__courses.append(course)

    # Returns True if the course was removed, False if it wasn't in the list
    def drop_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
            return True
        return False

    def display_info(self):
        print("ID:", self.__student_id)
        print("Name:", self.__name)
        print("Email:", self.__email)
        print("Department:", self.__department)
        print("GPA:", self.__gpa)
        print("Courses:", self.__courses)
        print("---------------------------")


# ---------- Testing the class ----------
# This part only runs when you run this file directly (python student.py)
if __name__ == "__main__":
    # create two Student objects
    s1 = Student("20231001", "Ali Hassan", "ali.hassan@neu.edu.tr", "Computer Engineering")
    s2 = Student("20231002", "Sara Ahmed", "sara.ahmed@neu.edu.tr", "Software Engineering")

    # enroll in courses
    s1.enroll_course("AII003 Principles of Software Engineering")
    s1.enroll_course("AII406 System Programming")
    s1.enroll_course("AII003 Principles of Software Engineering")   # already enrolled, prints a message

    s2.enroll_course("AII003 Principles of Software Engineering")

    # update GPA
    s1.update_gpa(3.45)
    s2.update_gpa(5.0)      # invalid, gets rejected
    s2.update_gpa(3.80)

    # drop a course
    dropped = s1.drop_course("AII406 System Programming")
    print("Dropped AII406:", dropped)

    # change email using a setter
    s2.set_email("sara.a@neu.edu.tr")

    print()
    s1.display_info()
    s2.display_info()

    print("Total students:", Student.get_student_count())

    # private attributes can't be accessed directly from outside the class
    try:
        print(s1.__gpa)
    except AttributeError:
        print("Can't access s1.__gpa directly, use s1.get_gpa() instead:", s1.get_gpa())
