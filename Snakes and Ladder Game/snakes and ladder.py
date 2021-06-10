import pygame
import sys
import random

pygame.init()

WIDTH = 820
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Background_Image = pygame.image.load("front.jpg")
Image_pos = (-100, -120)

Start_Image = pygame.image.load("start.png")
Start_Pos = (310, 390)

Winner_Pos = (100, 390)

RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

font = pygame.font.SysFont("monospace", 50)
fontt = pygame.font.SysFont("monospace", 20)


def game():
    TURN = 0
    key = 0
    key1 = 0

    PLAYER1_POS = [70, 630]
    PLAYER2_POS = [70, 660]
    PLAYER2_POS_FIX = 630
    PLAYER_SIZE = 20

    Winner_pos = (300, 370)

    temp = 1
    clock = pygame.time.Clock()

    chance = 1

    BACKGROUND_IMAGE = pygame.image.load("Snake.png")
    IMAGE_WIDTH = 28
    IMAGE_HEIGHT = -10
    IMAGE_POS = (IMAGE_WIDTH, IMAGE_HEIGHT)

    DICE_IMAGE = pygame.image.load("dice.png")
    DICE_POS = (740, 600)

    number = 0

    def ladder(PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX):

        if PLAYER1_POS == [280, 630]:
            PLAYER1_POS = [350, 280]
        elif PLAYER1_POS == [490.0, 560]:
            PLAYER1_POS = [420, 280]
        elif PLAYER1_POS == [630.0, 560]:
            PLAYER1_POS = [700, 350]
        elif PLAYER1_POS == [140.0, 490]:
            PLAYER1_POS = [210, 280]
        elif PLAYER1_POS == [70.0, 350]:
            PLAYER1_POS = [140, 140]
        elif PLAYER1_POS == [490.0, 280]:
            PLAYER1_POS = [560, 70]

        PLAYER2_POS[1] = PLAYER2_POS_FIX

        if PLAYER2_POS == [280, 630]:
            PLAYER2_POS = [350, 280]
        elif PLAYER2_POS == [490.0, 560]:
            PLAYER2_POS = [420, 280]
        elif PLAYER2_POS == [630.0, 560]:
            PLAYER2_POS = [700, 350]
        elif PLAYER2_POS == [140.0, 490]:
            PLAYER2_POS = [210, 280]
        elif PLAYER2_POS == [70.0, 350]:
            PLAYER2_POS = [140, 140]
        elif PLAYER2_POS == [490.0, 280]:
            PLAYER2_POS = [560, 70]

        PLAYER2_POS_FIX = PLAYER2_POS[1]
        PLAYER2_POS[1] = PLAYER2_POS_FIX + 30

        return PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX

    def snakes(PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX):

        if PLAYER1_POS == [560, 490]:
            PLAYER1_POS = [700, 630]
        elif PLAYER1_POS == [280, 420]:
            PLAYER1_POS = [210, 630]
        elif PLAYER1_POS == [490, 350]:
            PLAYER1_POS = [350, 560]
        elif PLAYER1_POS == [420, 140]:
            PLAYER1_POS = [630, 420]
        elif PLAYER1_POS == [490, 0]:
            PLAYER1_POS = [700, 140]
        elif PLAYER1_POS == [350, 0]:
            PLAYER1_POS = [140, 350]

        PLAYER2_POS[1] = PLAYER2_POS_FIX

        if PLAYER2_POS == [560, 490]:
            PLAYER2_POS = [700, 630]
        elif PLAYER2_POS == [280, 420]:
            PLAYER2_POS = [210, 630]
        elif PLAYER2_POS == [490, 350]:
            PLAYER2_POS = [350, 560]
        elif PLAYER2_POS == [420, 140]:
            PLAYER2_POS = [630, 420]
        elif PLAYER2_POS == [490, 0]:
            PLAYER2_POS = [700, 140]
        elif PLAYER2_POS == [350, 0]:
            PLAYER2_POS = [140, 350]

        PLAYER2_POS_FIX = PLAYER2_POS[1]
        PLAYER2_POS[1] = PLAYER2_POS_FIX + 30

        return PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX

    def image(BACKGROUND_IMAGE, IMAGE_POS, DICE_IMAGE, DICE_POS, label):
        screen.blit(BACKGROUND_IMAGE, IMAGE_POS)
        screen.blit(DICE_IMAGE, DICE_POS)
        screen.blit(label, (DICE_POS[0], DICE_POS[1]-50))

    def player1_position(number, PLAYER1_POS, chance):

        WIN_CHECK1 = PLAYER1_POS[0]
        WIN_CHECK2 = PLAYER1_POS[1]

        division = PLAYER1_POS[1] / 70
        if division % 2 != 0:
            extra = (number * 70) + PLAYER1_POS[0]
            if extra > 700:
                extra = (extra - 700) / 70
                PLAYER1_POS[0] = 770 - (extra * 70)
                PLAYER1_POS[1] -= 70
            else:
                PLAYER1_POS[0] = extra

        elif division % 2 == 0:
            extraa = PLAYER1_POS[0] - (number * 70)
            if extraa < 70:
                extraa = abs((extraa - 70) / 70)
                PLAYER1_POS[0] = (extraa * 70)
                PLAYER1_POS[1] -= 70
            else:
                PLAYER1_POS[0] = extraa

        if PLAYER1_POS[1] < 0:
            PLAYER1_POS[0] = WIN_CHECK1
            PLAYER1_POS[1] = WIN_CHECK2

        chance = 2
        return PLAYER1_POS, chance

    def player2_position(number, PLAYER2_POS, PLAYER2_POS_FIX, chance):

        WINCHECK1 = PLAYER2_POS[0]
        WINCHECK2 = PLAYER2_POS[1]
        FIX2 = PLAYER2_POS_FIX
        division = PLAYER2_POS_FIX / 70
        if division % 2 != 0:
            extra = (number * 70) + PLAYER2_POS[0]
            if extra > 700:
                extra = (extra - 700) / 70
                PLAYER2_POS[0] = 770 - (extra * 70)

                PLAYER2_POS_FIX -= 70
                PLAYER2_POS[1] = PLAYER2_POS_FIX + 30
            else:
                PLAYER2_POS[0] = extra

        elif division % 2 == 0:
            extraa = PLAYER2_POS[0] - (number * 70)
            if extraa < 70:
                extraa = abs((extraa - 70) / 70)
                PLAYER2_POS[0] = (extraa * 70)
                PLAYER2_POS_FIX -= 701
                PLAYER2_POS[1] = PLAYER2_POS_FIX + 30
            else:
                PLAYER2_POS[0] = extraa


        if PLAYER2_POS_FIX < 0:
            PLAYER2_POS[0] = WINCHECK1
            PLAYER2_POS[1] = WINCHECK2
            PLAYER2_POS_FIX = FIX2

        chance = 1
        return PLAYER2_POS, PLAYER2_POS_FIX, chance

    def win(PLAYER1_POS, PLAYER2_POS):

        if PLAYER1_POS[0] == 70 and PLAYER1_POS[1] == 0:
            return "Player ONE WIN", True
        if PLAYER2_POS[0] == 70 and PLAYER2_POS_FIX == 0:
            return "PLAYER TWO WIN", True
        return '', False

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= DICE_POS[0] and pygame.mouse.get_pos()[1] >= DICE_POS[1] and pygame.mouse.get_pos()[0] < 800 and pygame.mouse.get_pos()[1] < 700:
                number = random.randint(1,6)

                if PLAYER1_POS[0] == 70 and PLAYER1_POS[1] == 630 and TURN % 2 == 0 and number == 6:
                    key = 1
                    chance = 1
                    temp = 1
                    continue
                if PLAYER2_POS[0] == 70 and PLAYER2_POS[1] == 660 and TURN % 2 != 0 and number == 6:
                    key1 = 1
                    chance = 2
                    continue

                if TURN % 2 == 0 and number != 0 and key == 1:
                    PLAYER1_POS, chance = player1_position(number, PLAYER1_POS, chance)

                elif TURN % 2 != 0 and number != 0 and key1 == 1:
                    PLAYER2_POS, PLAYER2_POS_FIX, chance = player2_position(number, PLAYER2_POS, PLAYER2_POS_FIX, chance)

                PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX = ladder(PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX)
                PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX = snakes(PLAYER1_POS, PLAYER2_POS, PLAYER2_POS_FIX)

                if TURN % 2 == 0:
                    chance = 2
                else:
                    chance = 1
                TURN += 1

        screen.fill(BLACK)

        if chance == 1:
            textt = "Player1"
        elif chance == 2:
            textt = "Player2"

        labell = fontt.render(textt, 1, GREEN)
        screen.blit(labell, (DICE_POS[0] - 10, DICE_POS[1]-100))

        text = str(number)
        label = font.render(text, 1, BLUE)

        winner, check = win(PLAYER1_POS, PLAYER2_POS)
        if check:
            return winner

        clock.tick(30000)
        image(BACKGROUND_IMAGE, IMAGE_POS, DICE_IMAGE, DICE_POS, label)
        pygame.draw.rect(screen, RED, (PLAYER1_POS[0], PLAYER1_POS[1], PLAYER_SIZE, PLAYER_SIZE))
        pygame.draw.rect(screen, BLUE, (PLAYER2_POS[0], PLAYER2_POS[1], PLAYER_SIZE, PLAYER_SIZE))

        pygame.display.update()


def Winner_display(winner):
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        label = font.render(winner, 1, BLUE)
        screen.blit(label, Winner_Pos)

        pygame.display.update()


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= Start_Pos[0] and pygame.mouse.get_pos()[1] >= Start_Pos[1] and pygame.mouse.get_pos()[0] < Start_Pos[0] + 256 and pygame.mouse.get_pos()[1] < Start_Pos[1] + 256:
            winner = game()
            Winner_display(winner)

    screen.blit(Background_Image, Image_pos)
    screen.blit(Start_Image, Start_Pos)

    pygame.display.update()
