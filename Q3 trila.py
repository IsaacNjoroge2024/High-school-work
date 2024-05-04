import os
import pickle
QueueData = [" " for i in range (0, 20)] #" " or None represent empty
StartPointer = 0
EndPointer = 0

def Enqueue(item):
    global QueueData, EndPointer
    if (EndPointer == 20):
        return False
    else:
        QueueData[EndPointer] = item
        EndPointer = EndPointer + 1
        return True

for i in range (0,2):
    item = input("Enter a value")
    Enqueue(item)
print(QueueData)


def Remove(QueueData, StartPointer, EndPointer):
    if (EndPointer - StartPointer < 2):
        return "No Items", StartPointer, EndPointer
    else:
        Value1 = QueueData[StartPointer]
        StartP = StartPointer + 1
        Value2 = QueueData[StartPointer]
        StartP = StartPointer + 1
        return (Value1 + " " + Value2), StartPointer, EndPointer


Remove(QueueData, StartPointer, EndPointer)
print(Remove)


def ReadFile(QueueData, StartPointer, EndPointer):
    FileName = input("Enter FileName")
    if(os.path.isfile(FileName)):
        f = open('SecondData.txt', "r")
        Flag = True
        itemAdd = (f.readline()).strip()
        while(Flag == True and itemAdd != null):
            Flag, EndPointer = Enqueue(itemAdd)
            itemAdd = (f.readline()).strip()
        if(Flag == False):
            f.close()
            return 1, EndPointer
            print("The queue was full, not all items were read")
        else:
            f.close()
            return 2, EndPointer
            print("All items were successfully added")
    else:
        return -1, EndPointer
        print("The file could not be found")

ReadFile(QueueData, StartPointer, EndPointer)
print(ReadFile)
ReturnValue, EndPointer = ReadFile(QueueData, StartPointer, EndPointer)

