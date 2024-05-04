class HiddenBox:
    #__BoxName = BoxName
    #__Creator = Creator
    #__DataHidden = DataHidden
    #__GameLocation = GameLocation
    #__LastFinds = LastFinds
    #__Active = Active

    def __init__(self, BoxNameP, CreatorP, DataHiddenP, GameLocationP):
        self.__BoxName = BoxNameP
        self.__Creator = CreatorP
        self.__DataHidden = DataHiddenP
        self.__GameLocation = GameLocationP
        self.__LastFinds = [[" " for j in range (0,2) ]for i in range (0,10)]
        self.__Active = False
    def GetBoxName():
        return BoxName
    def GetGameLocation():
        return GameLocation
TheBoxes = [HiddenBox(" ", " ", " ", " ") for i in range (0, 10000)]

def NewBox(TheBoxes, NumBoxes):
    BoxName = input("Please enter the name of the box")
    Creator = input("Please enter the creator of the box")
    DataHidden = input("Please enter the hidden data")
    GameLocation = input("Please enter the location of the box")
    TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DataHidden, GameLocation)
    return (NumBoxes + 1)

NumBoxes = 0
Boxes = NewBox(TheBoxes, NumBoxes)

class PuzzleBox(HiddenBox):
    def __init__(self, TheBoxesP, CreatorP, DataHiddenP, GameLocationP, PuzzleTextP, SolutionP):
        HiddenBox.__init__(self, TheBoxesP, CreatorP, DataHiddenP, GameLocationP, PuzzleTextP, SolutionP)
        self.__PuzzleText = PuzzleTextP
        self.__Solution = SolutionP





