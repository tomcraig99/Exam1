"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""
import CourseClass as cc


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    course = cc.Course(name, crn, seats, status)

    for student in students:
        student = cc.Register(student, crn)
        if course.get_seats() > 0:
            print()
            print("Student Name:", student.get_name())
            print("Course name:", course.get_name())
            print("CRN:", course.get_crn())
            course.update_seat_count()
            print("Seats left:", course.get_seats())
            print()
        else:
            print(
                "Sorry",
                student.get_name(),
                "registration is closed for",
                course.get_name(),
            )


main()
