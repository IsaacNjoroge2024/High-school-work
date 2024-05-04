class employee:
    def __init__(self, name, staffno, yearlySalary, hoursWorked):
        self.__name = name
        self.__staffno = staffno
        self.__fullTimeStaff = True
        self.__yearlySalary = 0
        self.__hoursWorked = 0
    def showDetails(self):
        print("Employee Name " + self.__name)
        print("Employee Number " , self.__staffno)
        print("Employee yearlySalary", self.__yearlySalary)
        print("Employee hoursWorked", self.__hoursWorked)
class partTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = False
        self.__hoursWorked = 0
    def getHoursWorked (self):
        return(self.__hoursWorked)
class fullTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = True
        self.yearlySalary = 0
    def getYearlySalary (self):
        return(self.yearlySalary)

permanentStaff = fullTime("Eric Jones", 72)
#permanentStaff = employee.getYearlySalary()
permanentStaff.showDetails ()
permanentStaff.getYearlySalary()
temporaryStaff = partTime ("Alice Hue", 1017)
temporaryStaff.showDetails ()