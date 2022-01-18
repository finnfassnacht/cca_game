import pygame, sys
from pygame.locals import *
import random

health = 1000
level = 0
border = False

pygame.init()
pygame.mixer.music.load('misc.mp3')
pygame.mixer.music.play(-1,0.0)
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 800
surf = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combined Color Assault")

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = text_objects(text, largeText, cyan)
    TextRect.center = ((screen_width / 2), screen_height - (screen_height - 50))
    surf.blit(TextSurf, TextRect)

def message_display2(text):
    largeText = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, TextRect = text_objects(text, largeText, red_color)
    TextRect.center = ((screen_width / 2), (screen_height / 2))
    surf.blit(TextSurf, TextRect)

def message_display3(text):
    largeText = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, TextRect = text_objects(text, largeText, green_color)
    TextRect.center = ((screen_width / 2), (screen_height / 2))
    surf.blit(TextSurf, TextRect)
# Color
red_color = (255,0,0)
blue_color = (0,0,255)
green_color = (0,255,0)
back_ground2 = (0, 0, 0)
back_ground1 = (0, 45, 80)
cyan = (0, 255, 255)

back_ground = (back_ground1)
## RED DOT
dot_width = 60
dot_height = 60
dot_x = 550
dot_y = 700
red_dot_x_change = 0
def red_dot(x, y):
    rect_dot = pygame.draw.rect(surf, blue_color, pygame.Rect(x, y, dot_width, dot_height))
    return rect_dot


# KILL DOT
kill_dot_width = 100
kill_dot_height = 250
kill_dot_x = random.randint(1, screen_width)
kill_dot_y = -100
kill_dot_y_change = 0
tracker_x = 0
def kill_dot(x, y):
    rect_kill = pygame.draw.rect(surf, red_color, pygame.Rect(x, y, kill_dot_width, kill_dot_height))
    return rect_kill


# TRACKER DOT
health_dot_width = 50
health_dot_height = 50
health_dot_x = random.randint(1, screen_width)
health_dot_y = -100
health_dot_y_change = 0
def health_dot(x, y):
    health_tod = pygame.draw.rect(surf, green_color, pygame.Rect(x, y, health_dot_width, health_dot_height))
    return health_tod


# BORDER DOT
WID_dot_width = 30
WID_dot_height = screen_height * 2
WID_dot_x = (screen_width / 2)
WID_dot_y = -screen_height * 2
WID_dot_y_change = 0
def WID_dot(x, y):
    WID_tod = pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(x, y, WID_dot_width, WID_dot_height))
    return WID_tod

# KILL DOZER
DOZER_dot_width = ((screen_width / 2) + 200)
DOZER_dot_height = 70
DOZER_dot_x = ((screen_width / 4) + 60) 
DOZER_dot_y = - (screen_height - 100)
DOZER_dot_y_change = 0
lstc = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
def DOZER_dot(x, y):
    DOZER_tod = pygame.draw.rect(surf, random.choice(lstc), pygame.Rect(x, y, DOZER_dot_width, DOZER_dot_height))
    return DOZER_tod



while True:


    if level > 1000:
        WID_dot_y_change = 1
    if level > 5001:
        DOZER_dot_y_change = 10

    level += 1
    clock.tick(60)
    kill_dot_y_change = 10
    health_dot_y_change = 20


# Logic
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                red_dot_x_change = -25
            if event.key == pygame.K_RIGHT:
                red_dot_x_change = 25
        if event.type == pygame.KEYUP:
            if level > 5001 and level < 7500:
                if event.key == pygame.K_LEFT:
                    red_dot_x_change = 0
                if event.key == pygame.K_RIGHT:
                    red_dot_x_change = 0
            else:
                if event.key == pygame.K_LEFT:
                        red_dot_x_change = -10
                if event.key == pygame.K_RIGHT:
                        red_dot_x_change = 10
    if level < 4000:
        if kill_dot_y > screen_height:
            kill_dot_y = -kill_dot_height
            kill_dot_x = random.randint(1, screen_width)
    if level < 5000:
        if health_dot_y > screen_height:
            health_dot_y = -health_dot_height
            health_dot_x = random.randint(((screen_width / 2) -200), (screen_width / 2) + 200)
    if level > 5001 and level < 7500:
        if DOZER_dot_y > screen_height:
            DOZER_dot_y = -DOZER_dot_height
            DOZER_dot_x = (screen_width / 2 - (random.randint(100, 600)))
    if dot_x > screen_width - dot_width:
        dot_x = screen_width - dot_width
        red_dot_x_change = -25
        health -= 10
    if dot_x < 0:
        dot_x = 0
        health -= 10
        red_dot_x_change = 25
    
    if WID_dot_y > screen_height:
        back_ground = back_ground2




    surf.fill(back_ground)
    DOZER_dot_y += DOZER_dot_y_change
    kill_dot_y += kill_dot_y_change
    dot_x += red_dot_x_change
    health_dot_y += health_dot_y_change
    WID_dot_y += WID_dot_y_change
    DOZER_tod = DOZER_dot(DOZER_dot_x, DOZER_dot_y)
    WID_tod = WID_dot(WID_dot_x, WID_dot_y)
    health_tod = health_dot(health_dot_x, health_dot_y)
    rect_kill = kill_dot(kill_dot_x, kill_dot_y)
    rect_dot = red_dot(dot_x, dot_y)

    collide_WID = pygame.Rect.colliderect(WID_tod, rect_dot)
    collide_kill = pygame.Rect.colliderect(rect_kill, rect_dot)
    collide_plus = pygame.Rect.colliderect(health_tod, rect_dot)
    collide_DOZER = pygame.Rect.colliderect(DOZER_tod, rect_dot)
    


    if collide_kill:
        health -= 20

    if collide_plus:
        health += 10
    
    if collide_WID:
        health -= 1000
    
    if collide_DOZER:
        health -= 1000
    
    if level > 7800:
        message_display3("YOU WON!")
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(10000)
        pygame.quit()
        
    
    if health < 0:
        pygame.mixer.music.stop()
        message_display2("Game Over")
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()
    message_display(str(health))
    pygame.display.flip()
    pygame.display.update()
