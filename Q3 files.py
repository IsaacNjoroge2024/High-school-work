def ReadFile(QueueData, StartP, EndP):
    FileName = input("Enter FileName")
    if(os.path.isfile('C:/Users/ENVY/Downloads/txt.files')):
        f = open('C:/Users/ENVY/Downloads/txt.files', "r")
        Flag = True
        itemAdd = (f.readline()).strip()
        while(Flag == True and itemAdd != null):
            Flag, EndP = Enqueue(itemAdd)
            itemAdd = (f.readline()).strip()
        if(Flag == False):
            f.close()
            return 1, EndP
        else:
            f.close()
            return 2, EndP
    else:
        return -1, EndP
ReadFile(QueueData, StartP, EndP)
print(ReadFile)
