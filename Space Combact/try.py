import pygame
import sys
import random

pygame.init()

RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

Width = 1000
Height = 700
screen = pygame.display.set_mode((Width, Height))

enemy_size = 50
ran_value = random.randint(0, Width - enemy_size)
enemy_pos = [ran_value, 0]
enemy_pic = pygame.image.load("alien-monster_1f47e.jpg")
enemy_list = [enemy_pos]

score =0

Background_pic = pygame.image.load("stat_pic.jpg")
Background_pic2 = pygame.image.load("new_star.jpg")
up = 500

Speed = 2
Fire = 0

Shuttle_pos = [500, 500]
Shuttle_size = 50
Shuttle_pic = pygame.image.load("game.jpg")

Bullet_pos = [Shuttle_pos[0] + 20, Shuttle_pos[1] - 10]
Bullets_list = [Bullet_pos]
Bullet_size = 5

clock = pygame.time.Clock()

def display(up, Bullets_list):
    screen.blit(Background_pic, (0, up))
    screen.blit(Shuttle_pic, Shuttle_pos)
    up += 1
    if up >= 500:
        up = 0
    return up

def draw():
    for Bullet_pos in Bullets_list:
        pygame.draw.circle(screen, RED, (Bullet_pos[0], Bullet_pos[1]), Bullet_size)

def bullet(Bullets_list):
    delay = random.random()
    if len(Bullets_list) <= 20:
        pos = [Shuttle_pos[0] + 20, Shuttle_pos[1] - 10]
        Bullets_list.append(pos)



def bullet_pos(Bullet_pos, Shuttle_pos):
    for idx, Bullet_pos in enumerate(Bullets_list):
        if Bullet_pos[1] >= 0:
            Bullet_pos[1] -= Speed
        else:
            Bullets_list.pop(idx)


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 7 and delay < 0.06:
        x_pos = random.randint(0, Width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        screen.blit(enemy_pic, (enemy_pos[0], enemy_pos[1]))

# function to change enemy position and to calculate score
def enemy_position(enemy_list, Speed):
    for idx, enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] <= Height:
            enemy_pos[1] += Speed
        else:
            enemy_list.pop(idx)

def collition_check(Shuttle_pos, enemy_list, Shuttle_size, Bullets_list):

    for enemy_pos in enemy_list:
        if collition(Shuttle_pos, enemy_pos, Shuttle_size, Bullets_list):
            return True
    return False


# to stop the game when collision occure
def collition(Shuttle_pos, enemy_pos, Shuttle_size, Bullets_list):
    x_p = Shuttle_pos[0]
    y_p = Shuttle_pos[1]

    x_e = enemy_pos[0]
    y_e = enemy_pos[1]

    if (x_p <= x_e < (x_p + Shuttle_size)) or (x_e <= x_p < (x_e + Shuttle_size)):
        if (y_p <= y_e < (y_p + Shuttle_size)) or (y_e <= y_p < (y_e + Shuttle_size)):
            return True
    return False

def kill(enemy_list, Bullets_list):
    temp = 0
    for idx, enemy_pos in enumerate(enemy_list):
        x_e = enemy_pos[0]
        y_e = enemy_pos[1]
        for bullet_pos in Bullets_list:
            x_b = bullet_pos[0]
            y_b = bullet_pos[1]
            if x_e < x_b < (x_e + enemy_size) and y_b == (y_e + enemy_size):
                enemy_list.pop(idx)
                Bullets_list = []
                temp = 1
                break
        if temp == 1:
           break


Game_over = False

while not Game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:

            x = Shuttle_pos[0]
            y = Shuttle_pos[1]

            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            Shuttle_pos = [x, y]

            if event.key == pygame.K_UP:
                Fire = 1
    screen.fill(BLACK)

    if Fire == 1:
        bullet_pos(Bullet_pos, Shuttle_pos)
        bullet(Bullets_list)

    up = display(up, Bullets_list)
    draw()

    if collition_check(Shuttle_pos, enemy_list, Shuttle_size, Bullets_list):
        game_over = True
        break

    drop_enemies(enemy_list)
    draw_enemies(enemy_list)
    enemy_position(enemy_list, Speed)

    if Bullets_list[0][1] == 0:
        Fire = 0

    kill(enemy_list, Bullets_list)

    clock.tick(100)
    print(Fire)
    pygame.display.update()
