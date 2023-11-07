import pygame
import copy
import time

initia_state =  [[2, 8, 3],
                 [1, 6, 4],
                 [7, 0, 5]]

goal_state =  [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

def Heuristic_1(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                count +=1
            return count

def Heuristic_2(state):
    distance = 0
    for i in range(3):
        for j in range(3)