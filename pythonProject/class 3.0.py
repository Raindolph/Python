
class Student:

    def __init__(self, name, age, gender, sclass, coursename):
        print("Saving details...")
        self.name = name
        self.age = age
        self.gender = gender
        self.sclass = sclass
        self.coursename = coursename

    def student_details(self):
        print("\nName {}"
              "\nAge {}"
              "\nGender: {}"
              "\nClass: {}"
              "\nCourse name: {}".format(self.name, self.age, self.gender, self.sclass, self.coursename))


"""Object_name = constructor([parameters])"""

stud1 = Student("Jeff", 19, "male", "python", "OSDS")
stud1.student_details()
