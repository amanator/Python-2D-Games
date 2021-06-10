import pygame
import sys
import random

pygame.init()

WIDTH = 598
HEIGHT = 657
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Background_image = pygame.image.load("aman.png")
image_pos = (0, 0)

fontt = pygame.font.SysFont("monospace", 35)

Start_pos = (250, 250)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND = YELLOW
BACKGROUND_WEIGHT = 110
BACKGROUND_HEIGHT = 40

def image(Background_image, image_pos):
    screen.blit(Background_image, (image_pos[0], image_pos[1]))

def main_func():
    # Colors used in the program
    RED = (200, 0, 0)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    YELLOW = (255, 255, 0)
    BACKGROUND_COLOR = BLUE

    SPEED = 10

    # Player Position
    player_pos = [430, 460]
    player_size = 50

    # Enemy Position
    enemy_size = 50
    ran_value = random.randint(0, WIDTH-enemy_size)
    enemy_pos = [ran_value, 0]
    enemy_list = [enemy_pos]

    level = 1
    score = 0

    clock = pygame.time.Clock()

    # Font for enemy position
    font = pygame.font.SysFont("monospace", 35)

    def drop_enemies(enemy_list):
        delay = random.random()
        if len(enemy_list) < 7 and delay < 0.06:
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


    def level_up(score, SPEED, level):
        if 10 < score < 20:
            SPEED = 10
            level = 1
        elif 20 <= score < 60:
            SPEED = 13
            level = 2
        elif 100 > score > 60:
            SPEED = 18
            level = 3
        elif 200 > score > 100:
            SPEED = 25
            level = 4
        elif score > 200:
            SPEED = 30
            level = 5
        else:
            SPEED = 5

        return SPEED, level

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


    game_overr = False
    while not game_overr:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                x = player_pos[0]
                y = player_pos[1]

                if event.key == pygame.K_LEFT and player_pos[0]>50:
                    x -= player_size
                elif event.key == pygame.K_RIGHT and player_pos[0]<WIDTH-80:
                    x += player_size

                player_pos = [x, y]

        screen.fill(BACKGROUND_COLOR)

        drop_enemies(enemy_list)
        score = enemy_position(enemy_list, score, SPEED)

        text = "Score:" + str(score)
        label = font.render(text, 1, YELLOW)
        screen.blit(label, (WIDTH-200, HEIGHT-650))

        SPEED, level = level_up(score, SPEED, level)
        text = "LEVEL:" + str(level)
        label = font.render(text, 1, YELLOW)
        screen.blit(label, (WIDTH - 550, HEIGHT - 650))

        if collition_check(player_pos, enemy_list, player_size):
            game_overr = True
            break

        draw_enemies(enemy_list)

        pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

        clock.tick(30)
        pygame.display.update()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= Start_pos[0] and pygame.mouse.get_pos()[1] >= Start_pos[1] and pygame.mouse.get_pos()[0] < 400 and pygame.mouse.get_pos()[1] < 350:
            main_func()

    image(Background_image, image_pos)

    pygame.draw.rect(screen, BACKGROUND, (Start_pos[0], Start_pos[1], BACKGROUND_WEIGHT, BACKGROUND_HEIGHT))

    textt = "START"
    labell = fontt.render(textt, 1, RED)
    screen.blit(labell, Start_pos)


    pygame.display.update()
