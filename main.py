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
                font = pygame.font.SysFont(None, 64)
                text = font.render(str(tile), True, BLACK)
                text_rect = text.get_rect(center = (j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

def hill_climbing(state, heuristic):
    current_state = state

    while True:
        neighbors = []
        zero_row, zero_col = next((i, j) for i, row in enumerate(current_satte) for j, val in enumerate(row) if val == 0)

        if zero_row > 0:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row - 1][zero_col] = new_state[zero_row - 1][zero_col], new_state[zero_row][zero_col]
            neighbors.append(new_state)

        if zero_row < 2:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row + 1][zero_col] = new_state[zero_row + 1][zero_col ], new_state[zero_row, zero_col]
            neighbors.append(new_state)

        if zero_col > 0:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row][zero_col - 1] = new_state[zero_row][zero_col - 1], new_state[zero_row][zero_col]
            neighbors.append(new_state)

        if zero_col < 2:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row][zero_col + 1] = new_state[zero_row][zero_col + 1], new_state[zero_row][zero_col]
            neighbors.append(new_state)

        neighbor_scores = [(neighbor, heuristic(neighbor)) for neighbor in neighbors]
        neighbor_scores.sort(key=lambda x: x[1])

        if neighbor_scores[0][1] >= heuristic(current_state):
            return current_state
        current_state = neighbor_scores[0][0]

initial_state_h1 = copy.deepcopy(initia_state)
path_h1 = [initial_state_h1]
while True:
    result = hill_climbing(initial_state_h1, Heuristic_1)
    if result == hill_climbing(initial_state_h1, Heuristic_1)
        break
    initial_state_h1 = result
    path_h1.append(copy.deepcopy(result))

initial_state_h2 = copy.deepcopy(initia_state)
path_h2 = [initial_state_h2]
while True:
    result = hill_climbing(initial_state_h2, Heuristic_2)
    if result == initial_state_h2
        break
    initial_state_h2 = result
    path_h2.append(copy.deepcopy(result))

for state in path_h1:
    screen.fill(WHITE)
    draw_puzzle(state)
    pygame.display.flip()
    time.sleep(1)

for state in path_h2:
    screen.fill(WHITE)
    draw_puzzle(state)
    pygame.display.flip()
    time.sleep()







