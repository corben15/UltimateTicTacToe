#########################################
# Author:   Nicholas Corbett
# Date:     12/23/2019
#
# Description:
#
#########################################
from grid import *
import numpy as np
import pprint

pp = pprint.PrettyPrinter(indent=4)



def main():
    grid = Grid()
    pp.pprint(grid.grid)
    grid.placeX(0,1)
    pp.pprint(grid.grid)

if __name__ == '__main__':
    main()
