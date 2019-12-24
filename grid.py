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

    def placeX(self, x, y):
        if(self.grid[x][y]== "-"):
            self.grid[x][y] = "X"
        else:
            print("Already X or O in that cell!!")

    def placeO(self, x, y):
        if(self.grid[x][y]== "-"):
            self.grid[x][y] = "O"
        else:
            print("Already X or O in that cell!!")

    def checkCellsForWin():
        
