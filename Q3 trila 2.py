QueueData = ["" for x in range(0, 20)]
StartPointer = 0
EndPointer = 0
def Enqueue(Item, EndPointer):
    if (EndPointer <  20):
        QueueData[EndPointer] = Item
        EndPointer  = EndPointer + 1
        return True,
    else:
        return False,

#Enqueue(23,19)
#print(QueueData)