class Dog:
    def __init__(self, name, color, type):  #init is a constructor
        self.name = name #self. is setter
        self.color = color
        self.type = type
    def display(self):   #display(self) is getter
        print("name of dog is" + self.name)
        print("color of dog is" + self.color)
        print("type of dog is" + self.type)

dog1 = Dog(" bosco", " brown", " g.s") #calling the function
dog1.display()
