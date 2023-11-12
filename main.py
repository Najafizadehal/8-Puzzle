import pygame
import copy
import time
import random
import numpy as np
initial_state = [[0] * 3 for _ in range(3)]
print("How select initial state :")

A = int(input("1.Custom\n2.Random\n"))

if A == 1:
    numbers = []
    while len(numbers) < 9:
        num = int(input("Enter a number between 0 and 8: "))
        if num < 0 or num > 8:
            print("Number should be between 0 and 8.")
            continue
        if num in numbers:
            print("Number is already entered. Try again.")
            continue
        numbers.append(num)

    index = 0
    for i in range(3):
        for j in range(3):
            initial_state[i][j] = list(numbers)[index]
            index += 1
# if A == 2:
#     numbers_1 = list()
#     while len(numbers_1) < 2:
#         num_1 = random.sample(range(9),9)
#         numbers_1.append(num_1)
#     index = 0
#     for i in range(3):
#         for j in range(3):
#             initial_state[i][j] = list(numbers_1)[index]
#             index += 1

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]


def heuristic_1(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                count += 1
    return count


def heuristic_2(state):
    # Manhattan distance
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 3)
                distance += abs(row - i) + abs(col - j)
    return distance


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

pygame.init()

WIDTH = 300
HEIGHT = 300
TILE_SIZE = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Puzzle Visualization")


def draw_puzzle(state):
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            color = GRAY if tile != 0 else WHITE
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if tile != 0:
                font = pygame.font.SysFont(None, 64)
                text = font.render(str(tile), True, BLACK)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)


def hill_climbing(state, heuristic):
    current_state = state
    while True:
        neighbors = []
        zero_row, zero_col = next(
            (i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == 0)

        if zero_row > 0:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row - 1][zero_col] = new_state[zero_row - 1][zero_col], \
                new_state[zero_row][zero_col]
            neighbors.append(new_state)
        if zero_row < 2:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row + 1][zero_col] = new_state[zero_row + 1][zero_col], \
                new_state[zero_row][zero_col]
            neighbors.append(new_state)
        if zero_col > 0:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row][zero_col - 1] = new_state[zero_row][zero_col - 1], \
                new_state[zero_row][zero_col]
            neighbors.append(new_state)
        if zero_col < 2:
            new_state = copy.deepcopy(current_state)
            new_state[zero_row][zero_col], new_state[zero_row][zero_col + 1] = new_state[zero_row][zero_col + 1], \
                new_state[zero_row][zero_col]
            neighbors.append(new_state)

        neighbor_scores = [(neighbor, heuristic(neighbor)) for neighbor in neighbors]
        neighbor_scores.sort(key=lambda x: x[1])

        if neighbor_scores[0][1] >= heuristic(current_state):
            return current_state
        current_state = neighbor_scores[0][0]


initial_state_h1 = copy.deepcopy(initial_state)
path_h1 = [initial_state_h1]
while True:
    result = hill_climbing(initial_state_h1, heuristic_1)
    if result == initial_state_h1:
        break
    initial_state_h1 = result
    path_h1.append(copy.deepcopy(result))

initial_state_h2 = copy.deepcopy(initial_state)
path_h2 = [initial_state_h2]
while True:
    result = hill_climbing(initial_state_h2, heuristic_2)
    if result == initial_state_h2:
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
    time.sleep(1)

pygame.quit()

print("Results for h1 heuristic:")
print("Final state:", path_h1[-1])
print("Number of moves:", len(path_h1) - 1)
print("Path:", path_h1)

print("\nResults for h2 heuristic:")
print("Final state:", path_h2[-1])
print("Number of moves:", len(path_h2) - 1)
print("Path:", path_h2)
