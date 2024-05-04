import datetime
import pickle
class student:
    def __init__(self):
        self.name = ""
        self.registerNumber = 0
        self.dateOfBirth = datetime.date
        self.fullTime = True
studentRecord = student()
studentFile = open('student.dat','a+b')
print("Please enter student details")
studentRecord.name = input("Please enter student name ")
studentRecord.registerNumber = int(input("Please enter student's register number "))
year = int(input("Please enter student's year of birth YYYY "))
month = int(input("Please enter student's month of birth MM "))
day = int(input("Please enter student's day of birth DD "))
studentRecord.dateOfBirth = datetime.date(year, month, day)
studentRecord.fullTime = bool(input("Please enter True for full-time or False forpart-time "))
pickle.dump (studentRecord, studentFile)
print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)
studentFile.close()
studentFile = open('student.dat','rb')
studentRecord = pickle.load(studentFile)
print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)
studentFile.close()
