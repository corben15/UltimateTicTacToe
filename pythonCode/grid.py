#########################################
# Author:   Nicholas Corbett
# Date:     12/23/2019
#
# Description:
#
#########################################

import numpy as np


class Grid:
    def __init__(self):
        self.grid = np.chararray((9,9))
        self.grid[:] = "-"
        self.whoseTurn = "X"

    def placeX(self, x, y):
        if(self.whoseTurn != "X"):
            print("Not X's Turn!!")
        elif(self.grid[x][y]== "-"):
            self.grid[x][y] = "X"
            self.whoseTurn = "O"
        else:
            print("Already X or O in that cell!!")

    def placeO(self, x, y):
        if(self.whoseTurn != "O"):
            print("Not O's Turn!!")
        elif(self.grid[x][y]== "-"):
            self.grid[x][y] = "O"
        else:
            print("Already X or O in that cell!!")

    def gridPrint(self):
        stringToPrint = ""
        for i in range(9):
            for j in range(9):
                if(len(stringToPrint)==6 or len(stringToPrint)==15):
                    stringToPrint += " | "
                stringToPrint += str(self.grid[i][j]) + " "
            print(stringToPrint)
            stringToPrint = ""
            if(i%3 == 2 and i !=8):
                print("-----------------------")
        print("")
    '''
    def checkCellsForWin(self):
        for i in range(len(3)):
            for j in range(len(3)):

    '''
