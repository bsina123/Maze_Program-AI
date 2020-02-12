from tkinter import * # import the tkinter library which used for GUI
from window_component import window_component # imports the window_component class
from a_star_visited import a_star # imports the a_star component class
from breadth import breadth # imports the breadth class
from depth_search import depth # imports the depth class
from greedy_search import greedy # imports the greedy class
import math

class main(window_component):

    # list for level 1
    # used 0 for unused block
    # used 1 for used block

    # 40->x

    level_d = [ [0 for x in range(40)] for y in range(34)]
    # 34x40
    level_1 = [
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
        ]

    #list of level 2
    # 0 for unused block
    # 1 for used block

    level_2 = [
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
        ]

    # list for level 3
    # 0 fo unused block
    # 1 for used block

    level_3 = [
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1],
        [1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        ]

    # list for level 4
    # 0 for unused block
    # 1 for used block

    level_4 = [
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1],
        [0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1],
        [0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
        [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
        [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1],
        [1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]]

    # list for level 5
    # 0 for unused block
    # 1 for used block

    level_5 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        ]

    levels = []
    # creating labels of specific levels, which will be shown in hte combobox
    text_level = ['Select Level','Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']
    levels.append(level_d)
    levels.append(level_1) # appending the list of level_1
    levels.append(level_2) # appending the list of level_2
    levels.append(level_3) # appending the list of level_3
    levels.append(level_4) # appending the list of level_4
    levels.append(level_5) # appending the list of level_5

    # initializing to 0 the initial point
    __x1_init = 0
    __y1_init = 0
    __x2_init = 0
    __y2_init = 0

    # initializing to 0 the final points
    __x1_goal = 0
    __y1_goal = 0
    __x2_goal = 0
    __y2_goal = 0

    # creating a three dimensional array with
    # i takes value from 0 to 33
    # j takes value fom 0 to 39
    # k takes value from 0 to 5
    __new_array = [[[0 for k in range(5)] for j in range(40)] for i in range(34)]



    #initializing constructor from the main.py class
    def __init__(self):
        super().__init__()
        self.__window = self.get_parent() # calling the constructor from the window_component class


        self.frame_canvas() # calls the frame_canvas function located within the main.py class
        self.frame_algorithm() # calls the frame_algorithm class located within the main.py class
        self.frame_status() # calls the frame_status function located within the main.py class
        self.__create_combo() # calls create_combo function located within the main.py class
        self.__display_maze() # calls the displat_maze function located within the main.py class
        self.__create_start_button() # calls the create_start_function located within the main.py class
        self.__window.mainloop() # function of tinter library which which has the functionality for displaying the gui interface


    def __create_combo(self):
        self.__text_var = StringVar() # creates a data of type of String
        self.__text_var.set(self.__window) # identifies the String vairiable as a children of main gui window
        # creates the combobox

        # self.text_level.sort()

        self.__text_var.set(self.text_level[0])

        self.__combo_box = OptionMenu(self.__window,self.__text_var,*self.text_level)

        self.__combo_box.columnconfigure(0, weight=1)

        self.__combo_box.rowconfigure(0, weight=1)


        self.__combo_box["bg"] = '#e6ee9c'
        self.__combo_box.config(highlightbackground='#e6ee9c')

        self.__combo_box.place(x=1100,y=100)



        self.__draw_maze(self.levels[0], self.__canvas)
        # responsible as an event for changing text display in combobox and changes the maze according to the option of combobox
        self.__text_var.trace('w',self.__display_maze)


    def frame_algorithm(self):
        self.v1_check = IntVar() # creates an integer variable
        self.v2_check = IntVar() # creates an integer variable
        self.v3_check = IntVar() # creates an integer varibale
        self.v4_check = IntVar() # creates an integer variable
        self.check_1 = self.cr_check_button(self.__window,"A*")
        self.check_1.place(x=1100,y=300)
        self.check_1['variable'] = self.v1_check
        self.check_1['command'] = lambda:self.__checkAction1() # creates an event for the first checkbutton
        self.check_1["bg"] = '#80cbc4'
        self.check_1.config(highlightbackground='#80cbc4')

        self.check_2 = self.cr_check_button(self.__window,"Breadth Search")
        self.check_2.place(x=1100,y=330)
        self.check_2['variable'] = self.v2_check
        self.check_2['command'] = lambda:self.__checkAction2() # creates an event for the second checkbutton
        self.check_2["bg"] = '#80cbc4'
        self.check_2.config(highlightbackground='#80cbc4')


        self.check_3 = self.cr_check_button(self.__window,"Depth Search")
        self.check_3.place(x=1100,y=360)
        self.check_3['variable'] = self.v3_check
        self.check_3['command'] = lambda:self.__checkAction3() # creates an event for the third checkbutton
        self.check_3["bg"] = '#80cbc4'
        self.check_3.config(highlightbackground='#80cbc4')



        self.check_4 = self.cr_check_button(self.__window,"Greedy Search")
        self.check_4.place(x=1100,y=390)
        self.check_4['variable'] = self.v4_check
        self.check_4['command'] = lambda:self.__checkAction4() # creates an event for the fourth checkbutton
        self.check_4["bg"] = '#80cbc4'
        self.check_4.config(highlightbackground='#80cbc4')


    def frame_status(self):
        self.v1_radio = IntVar() # creates an integer variable
        self.v2_radio = IntVar() # creates an integer variable
        self.v3_radio = IntVar() # creates an integer variable
        self.radio_1 = self.cre_radio_button(self.__window,text="Visited")
        self.radio_1.place(x=1100,y=420)
        self.radio_1['value'] = 1
        self.radio_1['variable'] = self.v1_radio
        self.radio_1['command'] = lambda :self.__actionRadio1() # creates an event for the first radio button
        self.radio_1["bg"] = '#80cbc4'
        self.radio_1.config(highlightbackground='#80cbc4')

        self.radio_2 =self.cre_radio_button(self.__window,text="Not Visited")
        self.radio_2.place(x=1100,y=450)
        self.radio_2['value'] = 2
        self.radio_2['variable'] = self.v2_radio
        self.radio_2['command'] = lambda:self.__actionRadio2() # creates an eventfor the second radio button
        self.radio_2["bg"] = '#80cbc4'
        self.radio_2.config(highlightbackground='#80cbc4')


        self.radio_3 = self.cre_radio_button(self.__window,text="Expanded")
        self.radio_3.place(x=1100,y=480)
        self.radio_3['value'] = 3
        self.radio_3['variable'] = self.v3_radio # creates an event for the third radio button
        self.radio_3['command'] = lambda:self.__actionRadio3()
        self.radio_3["bg"]='#80cbc4'
        self.radio_3.config(highlightbackground='#80cbc4')


    def __find_index(self,array,x1,y1,x2,y2):
        num1 = 0
        num2 = 0
        status = False
        for i in range(len(array)):
            if status == True: break
            for j in range(len(array[i])):
                if x1 == array[i][j][1] and y1 == array[i][j][2] and x2 == array[i][j][3] and y2 == array[i][j][4]:
                    num1 = i
                    num2 = j
                    status = True
                    break
        return num1,num2


    def __calculate_point(self,x1,y1,x2,y2):
        x1_new = x1 + 1
        y1_new = y1 + 1
        x2_new = x2 - 1
        y2_new = y2 - 1
        return x1_new,y1_new,x2_new,y2_new

    def __place_init(self,event):
        if self.__canvas.find_withtag(CURRENT):
            x1, y1, x2, y2 = self.__canvas.bbox(CURRENT)
            if self.__x1_init == 0 and self.__y1_init == 0 and self.__x2_init == 0 and self.__y2_init == 0:
                self.__x1_init,self.__y1_init,self.__x2_init,self.__y2_init = self.__calculate_point(x1,y1,x2,y2)
                self.__init_new = self.__canvas.create_rectangle(self.__x1_init,self.__y1_init,self.__x2_init,self.__y2_init,fill="yellow")
            else:
                self.__init_new = self.__canvas.create_rectangle(self.__x1_init, self.__y1_init, self.__x2_init, self.__y2_init,fill="white")
                self.__x1_init,self.__y1_init,self.__x2_init,self.__y2_init = self.__calculate_point(x1,y1,x2,y2)
                self.__init_new = self.__canvas.create_rectangle(self.__x1_init,self.__y1_init,self.__x2_init,self.__y2_init,fill="yellow")
            self.__init_row,self.__init_col = self.__find_index(self.__get_new_array(),self.__x1_init,self.__y1_init,self.__x2_init,self.__y2_init)

    def __place_goal(self,event):
        if self.__canvas.find_withtag(CURRENT):
            x1, y1, x2, y2 = self.__canvas.bbox(CURRENT)
            if self.__x1_goal ==0 and self.__y1_goal == 0 and self.__x2_goal == 0 and self.__y2_goal == 0:
                self.__x1_goal,self.__y1_goal,self.__x2_goal,self.__y2_goal = self.__calculate_point(x1,y1,x2,y2)
                self.__goal_new = self.__canvas.create_rectangle(self.__x1_goal,self.__y1_goal,self.__x2_goal,self.__y2_goal,fill="red")
            else:
                self.__goal_new = self.__canvas.create_rectangle(self.__x1_goal,self.__y1_goal,self.__x2_goal,self.__y2_goal,fill="white")
                self.__x1_goal,self.__y1_goal,self.__x2_goal,self.__y2_goal = self.__calculate_point(x1,y1,x2,y2)
                self.__goal_new = self.__canvas.create_rectangle(self.__x1_goal,self.__y1_goal,self.__x2_goal,self.__y2_goal,fill="red")
            self.__goal_row, self.__goal_col = self.__find_index(self.__new_array, self.__x1_goal, self.__y1_goal,self.__x2_goal,self.__y2_goal)


    def frame_canvas(self):
        self.__canvas = self.create_canvas(self.__window)
        self.__canvas.place(x=100,y=40)

    def __draw_maze(self,array,canvas):
       x2_position = 20 # x1 position in pixel for the first canvas box
       x1_position = 0 # y1 position in pixel for  the first canvas box
       y1_position = 0 # x2 position in pixel for the first canvas box
       y2_position = 20 # y2 position in pixel for the first canvas box
       for i in range(len(array)):
           for j in range(len(array[i])):
               # appends the data to the new list
              self.__store_array_data(array[i][j], x1_position, y1_position, x2_position, y2_position, i, j)
              # if the block is is 1 it is colored in black
              if(array[i][j] == 1):canvas.create_rectangle(x1_position,y1_position,x2_position,y2_position,fill="black")
              # if the block is 0 it is colored in whited
              elif(array[i][j] == 0):canvas.create_rectangle(x1_position,y1_position,x2_position,y2_position,fill="white")
              x1_position += 20 # increments the x1 position to indicate the x1 position of the next block
              x2_position += 20 # increments the x2 position to indicate the x2 position of the next block
           x1_position = 0
           x2_position = 20
           y1_position += 20 # increments the y1 position
           y2_position += 20 # increments the y2 position
       canvas.bind("<Button-1>",self.__place_init)
       canvas.bind("<Button-3>",self.__place_goal)

    # responsible for the drawing the maze
    def __display_maze(self,*args):
        if self.__text_var.get() == "Select Level":
            self.__draw_maze(self.levels[0], self.__canvas)  # draws level 1
        elif self.__text_var.get() == "Level 1":
            self.__draw_maze(self.levels[1], self.__canvas) # draws level 1
        elif self.__text_var.get() == "Level 2":
            self.__draw_maze(self.levels[2],self.__canvas) # draws level 2
        elif self.__text_var.get() == "Level 3":
            self.__draw_maze(self.levels[3], self.__canvas) # draws level 3
        elif self.__text_var.get() == "Level 4":
            self.__draw_maze(self.levels[4], self.__canvas) # draws level 4
        elif self.__text_var.get() == "Level 5":
            self.__draw_maze(self.levels[5],self.__canvas) # draws level 5


    def setColrs(self,widget,bcg,fg,):
        pass
    # function for creating and placing the start whose position is specified in pixels
    def __create_start_button(self):


        self.__start = Button(self.__window, text="START", command=self.__start_action)
        self.__start["bg"]='#ffbb33'
        self.__start.config(highlightbackground='#ffbb33')

        # self.__start["fg"]='#ffbb33'

        self.__start.place(x=1150, y=550)

    # the event start function called when the start button is pressed
    def __start_action(self):

        # the default option searchnig method is by using not visited list
        if(self.v1_radio.get() == 0 and self.v2_radio.get() == 0 and self.v3_radio.get() == 0):
            self.v2_radio.set(2)


        # when the a star checkbox and visited radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        if self.v1_check.get() == 1 and self.v1_radio.get() == 1:
            astar1 = a_star(self.__get_new_array(),self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1,1)
        # when the a star checkbox and not visited radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v1_check.get() == 1 and self.v2_radio.get() == 2:
             astar1 = a_star(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 2)
        # when the a star checkbox and expanded radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v1_check.get() == 1 and self.v3_radio.get() == 3:
            astar1 = a_star(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 3)
        # when the a star checkbox and no radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v1_check.get() == 1 and (self.v1_radio.get() != 1 and self.v2_radio.get() !=2 and self.v3_radio.get() != 3):
            astar1 = a_star(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 0)
        # when the breadth checkbox and visited radio button is checked then the breadth1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v2_check.get() == 1 and self.v1_radio.get() == 1:
            breadth1 = breadth(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 1)
        # when the breadth checkbox and not visited radio button is checked then the class breadth1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v2_check.get() == 1 and self.v2_radio.get() == 2:
            breadth1 = breadth(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 2)
        # when the breadth checkbox and expanded radio button is checked then the class breadth1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v2_check.get() == 1 and self.v3_radio.get() == 3:
            breadth1 = breadth(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 3)
        # when the breadth checkbox and no radio button is checked then the class breadth1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v2_check.get() == 1 and (self.v1_radio.get() != 1 and self.v2_radio.get() !=2 and self.v3_radio.get() != 3):
            breadth1 = breadth(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 0)
        # when the depth checkbox and visited radio button is checked then the class depth1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v3_check.get() == 1 and self.v1_radio.get() == 1:
            depth1 = depth(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 1)
        # when the depth checkbox and not visited radio button is checked then the class depth1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v3_check.get() == 1 and self.v2_radio.get() == 2:
            depth1 = depth(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 2)
        # when the depth checkbox and expanded button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v3_check.get() == 1 and self.v3_radio.get() == 3:
            depth1 = depth(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 3)
        # when the depth checkbox and no radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v3_check.get() == 1 and (self.v1_radio.get() != 1 and self.v2_radio.get() !=2 and self.v3_radio.get() != 3):
            depth1 = depth(self.__get_new_array(),self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 0)
        # when the greedy checkbox and visited radio button is checked then the class greedy1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v4_check.get() == 1 and self.v1_radio.get() == 1:
            greedy1 = greedy(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 1)
        # when the greedy checkbox and not visited radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v4_check.get() == 1 and self.v2_radio.get() == 2:
            greedy1 = greedy(self.__get_new_array(),self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 2)
        # when the greedy checkbox and expanded radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v4_check.get() == 1 and self.v3_radio.get() == 3:
            greedy1 = greedy(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 3)
        # when the greedy checkbox and no radio button is checked then the class astar1 is called
        # the function will contain the new array list
        # the 4 points for the initial block
        # the 4 points for the goal block
        # the value of checkbox
        # the value of radio button
        elif self.v4_check.get() == 1 and (self.v1_radio.get() != 1 and self.v2_radio.get() !=2 and self.v3_radio.get() != 3):
            greedy1 = greedy(self.__get_new_array(), self.__canvas,self.__init_row,self.__init_col,self.__goal_row,self.__goal_col,1, 0)

    # action event function that is called when the first checkbox button is checked
    def __checkAction1(self):
        if(self.v1_check.get() == 1):
            self.v2_check.set(0)
            self.v3_check.set(0)
            self.v4_check.set(0)

    # action event function that is called when the second checkbox button is checked
    def __checkAction2(self):
        if(self.v2_check.get() == 1):
            self.v1_check.set(0)
            self.v3_check.set(0)
            self.v4_check.set(0)

    # action event function that is called when the third checkbox is checked
    def __checkAction3(self):
        if(self.v3_check.get() == 1):
            self.v1_check.set(0)
            self.v2_check.set(0)
            self.v4_check.set(0)

    # action event function that is called when the fourth checkbox is clicked
    def __checkAction4(self):
        if(self.v4_check.get() == 1):
            self.v1_check.set(0)
            self.v2_check.set(0)
            self.v3_check.set(0)

    # action event function that is called when the first radio button is clicked
    def __actionRadio1(self):
        if(self.v1_radio.get() == 1):
            self.v2_radio.set(0)
            self.v3_radio.set(0)

    # action event function tha is called when the second radio button is checked
    def __actionRadio2(self):
        if(self.v2_radio.get() == 2):
            self.v1_radio.set(0)
            self.v3_radio.set(0)

    # action event function that is called when the third radio button is checked
    def __actionRadio3(self):
        if(self.v3_radio.get() == 3):
            self.v1_radio.set(0)
            self.v2_radio.set(0)

    # creates a new list
    # the list contains the value of the block
    # the position of block x1 in pixels
    # the position of block y1 in pixels
    # the position of block x2 in pixels
    # the position of block y2 in pixels
    def __store_array_data(self,data,x1,y1,x2,y2,i,j):
        self.__new_array[i][j][0] = data
        self.__new_array[i][j][1] = x1
        self.__new_array[i][j][2] = y1
        self.__new_array[i][j][3] = x2
        self.__new_array[i][j][4] = y2

    # return the new array
    def __get_new_array(self):
        return self.__new_array

main()