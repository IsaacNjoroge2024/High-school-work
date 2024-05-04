TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
for index in range(0, len(TheData)):
    key = TheData[index]
    place = index -1
    if TheData[place] > key:
        while place >= 0 and TheData[place] > key:
            temp = TheData[place + 1]
            TheData[place + 1] = TheData[place]
            TheData[place] = temp
            place = place -1
        TheData[place + 1] = key
print([TheData])

