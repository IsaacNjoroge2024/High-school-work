class Student:
    def __init__(self, name, age, studentID):
        self.name = name
        self.age = age
        self.studentID = studentID
    def display(self):
        print("name of Student is" + self.name)
        print("age of Student is ", self.age)
        print("studentID of Student is", self.studentID)

student1 = Student(" Ben", 17, 96)
student1.display()