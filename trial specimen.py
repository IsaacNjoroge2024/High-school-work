import array
TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
def InsertionSort(TheData):
    for i in range (0, len(TheData)):
        DataToInsert = TheData[i]
        Inserted = 0
        NextValue = i - 1
        while (NextValue >= 0 and Inserted != 1):
            if (DataToInsert < TheData[NextValue]):
                #temp = TheData[NextValue + 1]
                TheData[NextValue + 1] = TheData[NextValue]
                #TheData[NextValue] = temp
                NextValue = NextValue - 1
            else:
                Inserted = 1
        TheData[NextValue + 1] = DataToInsert
#DataToInsert.TheData[i]
#TheData = TheData[i]
InsertionSort(TheData)
print([TheData])

def GetItem(TheData):
    item = int(input("Please enter item to be found"))
    found = False
    for index in range (0, len(TheData)):
        if (TheData[index] == true):
            found = True
        if (found):
            print("Item found")
        else:
            print("Item not found")
GetItem(TheData)

def GetItem(TheData):
    lowerBound = 0
    upperBound = 9
    found = False
    item = int(input("Please enter item to be found"))
    while (not found) and (upperBound != lowerBound):
        index = ((upperBound + lowerBound) // 2)
        if (TheData[index] == item):
            found = True
        if item > TheData[index]:
            lowerBound = index + 1
        if item < TheData[index]:
            upperBound = index - 1
    if (found):
        print("Item found")
    else:
        print("Item not found")

GetItem(TheData)

