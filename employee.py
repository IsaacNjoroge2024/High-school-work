class employee:
    def __init__ (self, name, staffno):
        self.name = name
        self.staffno = staffno
    def showDetails(self):
        print("Employee Name " + self.name)
        print("Employee Number " , self.staffno)

myStaff = employee("Eric Jones", 72)
myStaff.showDetails()