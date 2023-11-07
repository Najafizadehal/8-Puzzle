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
        for j in range(3):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] -1, 3)
                distance +=abs(row - 1) + abs(col - j)
    return distance

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

pygame.init()

WIDTH = 300
HEIGHT = 300
TILE_SIZE = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Puzzle")

def draw_puzzle(state):
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            color = GRAY if tile != 0 else WHITE
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if tile != 0:
                tile = state[i][j]
