class employee:
    def __init__(self, name, staffno):
        self.__name = name
        self.__staffno = staffno
    def showDetails(self):
        print("Employee Name " + self.__name)
        print("Employee Number " , self.__staffno)