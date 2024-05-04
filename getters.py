class Student:
    def setName(self, Name):
        self.__Name = Name
    def getName(self, Name):
        return self.__Name
    def setAge(self, Age):
        self.__Age = Age
    def getAge(self, Age):
        return self.__Age
    def setStudentID(self, studentID):
        self.__studentID = studentID
    def getStudentID(self, studentID):
        return self.__studentID
    def display(self):
        print("name of Student is" + self.__Name)
        print("age of Student is" + self.__Age)
        print("studentID of Student is" + self.__studentID)

student1 = Student()
student1.setName(" Ben")
student1.setAge(" 19")
student1.setStudentID(" 200")
student1.display()