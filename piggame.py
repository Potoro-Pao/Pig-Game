import random
import time
import pygame

pygame.init()
pygame.display.set_caption("Pig Game")

WIN_WIDTH = 1000
WIN_HEIGHT = 900
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

PLAYER_ONE_P = 0
PLAYER_TW0_P = 0
Current_Point_PLAYER1 = 0
Current_Point_PLAYER2 = 0

game_over = False


class Button:
    def __init__(self, x, y, color, lt, ht):
        self.x = x
        self.y = y
        self.color = color
        self.lt = lt
        self.ht = ht

    def display_shape(self, display_text):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.lt, self.ht))
        display_text()


def display_score_1(score):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render("Player_1", 1, (255, 255, 255))
    text2 = font.render(str(score), 1, (255, 255, 255))
    win.blit(text, (150, 250))
    win.blit(text2, (240, 350))


def display_score_2(score):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render("Player_2", 1, (255, 255, 255))
    text2 = font.render(str(score), 1, (255, 255, 255))
    win.blit(text, (600, 250))
    win.blit(text2, (690, 350))


def Current_1(score):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 40)
    text = font.render("current", 1, (255, 255, 255))
    text2 = font.render(str(score), 1, (255, 255, 255))
    win.blit(text, (200, 650))
    win.blit(text2, (260, 720))


def Current_2(score):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 40)
    text = font.render("current", 1, (255, 255, 255))
    text2 = font.render(str(score), 1, (255, 255, 255))
    win.blit(text, (660, 650))
    win.blit(text2, (720, 720))


def game_area():
    pygame.draw.rect(win, (123, 123, 123), (50, 50, 900, 800), 10)
    pygame.draw.line(win, (123, 123, 123), (500, 50), (500, 840), 10)
    pygame.draw.rect(win, (123, 123, 123), (150, 650, 250, 150), 10)
    pygame.draw.rect(win, (123, 123, 123), (605, 650, 250, 150), 10)


btn_roll = Button(WIN_WIDTH // 2 - 98, WIN_HEIGHT // 2 + 200, (123, 243, 233), 200, 70)
btn_hold = Button(WIN_WIDTH // 2 - 50, WIN_HEIGHT // 2 + 280, (123, 233, 24), 100, 50)


def display_btn_text_1():
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 40)
    text = font.render("Roll", 1, (0, 0, 0))
    win.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, 650))


def display_btn_text_2():
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 40)
    text2 = font.render("Hold", 1, (0, 0, 0))
    win.blit(text2, (WIN_WIDTH // 2 - text2.get_width() // 2, 720))


#
# def display_buttons():
#     pygame.draw.rect(win, (123, 243, 233), (WIN_WIDTH//2-98,WIN_HEIGHT//2+200,200,70))
#     pygame.draw.rect(win, (123, 233, 24), (WIN_WIDTH//2-50,WIN_HEIGHT//2+280,100,50))
def display_dice():
    number = random.randint(1, 6)
    dice_img = pygame.image.load(f'dice-{number}.png')
    dice_img = pygame.transform.scale(dice_img, (100, 100))
    return dice_img, number


bg = pygame.Surface(win.get_size())
bg = bg.convert()
bg.fill((0, 0, 0))
clock = pygame.time.Clock()
FPS = 10


def display_winner(winner):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render(f"Player{winner} WON!", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, 100))


def display_author():
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 40)
    text = font.render("Thanks for Playing", 1, (255, 255, 255))
    text2 = font.render("Create by Potoro Pao", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, 170))
    win.blit(text2, (WIN_WIDTH // 2, 210))


dice, dice_number = display_dice()

player1_turn = True
player2_turn = False

while not game_over:
    win.blit(bg, (0, 0))
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEMOTION:
            mouse_hover_x = pygame.mouse.get_pos()[0]
            mouse_hover_y = pygame.mouse.get_pos()[1]
            if (mouse_hover_x >= btn_roll.x and mouse_hover_x <= btn_roll.x + btn_roll.lt) and (
                    mouse_hover_y >= btn_roll.y and mouse_hover_y <= btn_roll.y + btn_roll.ht):
                btn_roll.color = (255, 0, 0)
            else:
                btn_roll.color = (123, 243, 233)
            if (mouse_hover_x >= btn_hold.x and mouse_hover_x <= btn_hold.x + btn_hold.lt) and (
                    mouse_hover_y >= btn_hold.y and mouse_hover_y <= btn_hold.y + btn_hold.ht):
                btn_hold.color = (255, 0, 0)
            else:
                btn_hold.color = (123, 233, 24)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if (mouseX >= btn_roll.x and mouseX <= btn_roll.x + btn_roll.lt) and (
                    mouseY >= btn_roll.y and mouseY <= btn_roll.y + btn_roll.ht):
                dice, dice_number = display_dice()
                win.blit(dice, (WIN_WIDTH // 2 - dice.get_width() // 2, WIN_HEIGHT // 2 - dice.get_height()))
                if (player1_turn):
                    if dice_number != 1:
                        Current_Point_PLAYER1 += dice_number
                    else:
                        Current_Point_PLAYER1 = 0
                        player1_turn = False
                        player2_turn = True
                elif (player2_turn):
                    if dice_number != 1:
                        Current_Point_PLAYER2 += dice_number
                    else:
                        Current_Point_PLAYER2 = 0
                        player2_turn = False
                        player1_turn = True

            if (mouseX >= btn_hold.x and mouseX <= btn_hold.x + btn_hold.lt) and (
                    mouseY >= btn_hold.y and mouseY <= btn_hold.y + btn_hold.ht):
                if (player1_turn):
                    PLAYER_ONE_P += Current_Point_PLAYER1
                    Current_Point_PLAYER1 = 0
                    player1_turn = False
                    player2_turn = True
                elif (player2_turn):
                    PLAYER_TW0_P += Current_Point_PLAYER2
                    Current_Point_PLAYER2 = 0
                    player1_turn = True
                    player2_turn = False

    game_area()
    btn_roll.display_shape(display_btn_text_1)
    btn_hold.display_shape(display_btn_text_2)

    display_score_1(PLAYER_ONE_P)
    display_score_2(PLAYER_TW0_P)
    Current_1(Current_Point_PLAYER1)
    Current_2(Current_Point_PLAYER2)
    win.blit(dice, (WIN_WIDTH // 2 - dice.get_width() // 2, WIN_HEIGHT // 2 - dice.get_height()))
    if PLAYER_ONE_P >= 100:
        display_winner("Player 1")
        display_author()
        pygame.display.update()
        time.sleep(5)
        game_over = True
    elif PLAYER_TW0_P >= 100:
        display_winner("Player 2")
        display_author()
        pygame.display.update()
        time.sleep(5)
        game_over = True

    pygame.display.update()
pygame.quit()
