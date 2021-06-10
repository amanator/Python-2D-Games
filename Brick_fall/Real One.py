import pygame
import sys
import random

pygame.init()

WIDTH = 700
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors used in the program
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = BLACK

SPEED = 10

# Player Position
player_pos = [430, 460]
player_size = 50

# Enemy Position
enemy_size = 50
ran_value = random.randint(0, WIDTH-enemy_size)
enemy_pos = [ran_value, 0]
enemy_list = [enemy_pos]

score = 0

clock = pygame.time.Clock()

# Font for enemy position
font = pygame.font.SysFont("monospace", 35)

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-player_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, GREEN, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

# function to change enemy position and to calculate score
def enemy_position(enemy_list, score, SPEED):
    for idx, enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] <= HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score


def level_up(score, SPEED):
    if score > 10:
        SPEED = 10
    elif score > 30:
        SPEED = 20
    elif score > 60:
        SPEED = 30
    elif score > 100:
        SPEED = 40
    elif score > 200:
        SPEED = 70
    else:
        SPEED = 5
    return SPEED

def collition_check(player_pos, enemy_list, player_size):

    for enemy_pos in enemy_list:
        if collition(player_pos, enemy_pos, player_size):
            return True
    return False


# to stop the game when collision occure
def collition(player_pos, enemy_pos, player_size):
    x_p = player_pos[0]
    y_p = player_pos[1]

    x_e = enemy_pos[0]
    y_e = enemy_pos[1]

    if (x_p <= x_e < (x_p + player_size)) or (x_e <= x_p < (x_e + player_size)):
        if (y_p <= y_e < (y_p + player_size)) or (y_e <= y_p < (y_e + player_size)):
            return True
    return False


game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]

    screen.fill(BACKGROUND_COLOR)

    drop_enemies(enemy_list)
    score = enemy_position(enemy_list, score, SPEED)

    text = "Score:" + str(score)
    label = font.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGHT-600))

    SPEED = level_up(score, SPEED)

    if collition_check(player_pos, enemy_list, player_size):
        game_over = True
        break

    draw_enemies(enemy_list)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()


