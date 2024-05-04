#import queue
QueueData = [" " for i in range (0, 20)] #" " or None represent empty
StartPointer = 0
EndPointer = 0
#DataToAdd = 0

def Enqueue(item):
    global QueueData, EndPointer
    if (EndPointer == 20):
        return False
    else:
        QueueData[EndPointer] = item
        EndPointer = EndPointer + 1
        return True

for i in range (0,20):
    item = input("Enter a value")
    Enqueue(item)
print(QueueData)


def ReadFile(QueueData, StartP, EndP):
    FileName = input("Enter FileName")
    if(os.path.isfile(FileName)):
        f = open('C:/Users/ENVY/Downloads/comp science revision papers/9618_y21_ss_4', "r")
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

ReturnValue, EndPointer = ReadFile(QueueData, StartPointer, EndPointer)
if(ReturnValue == -1):
    print("The file could not be found")
elif(ReturnValue == 1):
    print("The queue was full, not all items were read")
else:
    print("All items successfully added")


def Remove(QueueData, StartP, EndP):
    if(EndP - StartP < 2):
        return "No Items", StartP, EndP
    else:
        Value1 = QueueData[StartP]
        StartP = StartP + 1
        Value2 = QueueData[StartP]
        StartP = StartP + 1
        return(Value1 + " " + Value2), StartP, EndP

#QueueData.pop(StartPointer)
#print(QueueData)

