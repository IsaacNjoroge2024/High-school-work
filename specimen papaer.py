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

def PrintArray(TheData):
    for Count in range (0, len(TheData)):
        print(TheData[Count])
print("Before")
PrintArray(TheData)
InsertionSort(TheData)
print("After")
PrintArray(TheData)

#linear search
#enter item to be found
#TheData = InsertionSort(TheData)
def GetItem(TheData):
    item = int(input("Please enter item to be found"))
    found = False
    for index in range (0, len(TheData)):
        if (TheData[index] == item):
            found = True
    if (found):
        print("Item found")
    else:
        print("Item not found")
GetItem(TheData)



