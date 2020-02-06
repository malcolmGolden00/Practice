import pygame
import os
pygame.init()

# __Display__
display_width = 1200
display_height = 775
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("")


# Button Class
class Button:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw_normal(self, surface, highlight):
        color = blue
        if highlight:
            color = grey
        surface.fill(color, self.rect)

    def is_mouse_over(self, pos):
        return self.rect.pointcollide(pos)

# ___UD Variables___
# colors
black = (0, 0, 0)
white = (255,255, 255)
blue = (0, 158, 255)
green = (0, 200, 0)
grey = (224, 224, 224)
bc = blue

# pathfinder
pathfinder = os.getcwd()

# positions
pos1a = 25
pos1b = 875
pos2 = 100
sz1 = 300
sz2 = 30

# ___Functions___
# p + odd number = x axis // p + even number = y axis
def cvr_pg(p1, p2):
    gameDisplay.blit(cvr_img, (p1, p2))
p1 = (display_width * 0.29)
p2 = (display_height * 0.07)

# cover image
cvr_img = pygame.image.load(pathfinder + '\images\cover_page (3).png')

buttons = []
buttons.append(Button(pos1a, pos2, sz1, sz2))

# ___Main Home Page Window___
# Time clock
clock = pygame.time.Clock()
# Home window
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                crashed = True


    # get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # ___DISPLAY___
    gameDisplay.fill(white)
    cvr_pg(p1, p2)

    # buttons left
    # hover
    for button in buttons:
        button.collidepoint(gameDisplay, button.is_mouse_over(mouse_pos))

    ch1 = pygame.draw.rect(gameDisplay, bc, (pos1a, 100, sz1, sz2))
    ch2 = pygame.draw.rect(gameDisplay, bc, (pos1a, 140, sz1, sz2))
    ch3 = pygame.draw.rect(gameDisplay, bc, (pos1a, 180, sz1, sz2))
    ch4 = pygame.draw.rect(gameDisplay, bc, (pos1a, 220, sz1, sz2))
    ch5 = pygame.draw.rect(gameDisplay, bc, (pos1a, 260, sz1, sz2))
    ch6 = pygame.draw.rect(gameDisplay, bc, (pos1a, 300, sz1, sz2))
    ch7 = pygame.draw.rect(gameDisplay, bc, (pos1a, 340, sz1, sz2))
    ch8 = pygame.draw.rect(gameDisplay, bc, (pos1a, 380, sz1, sz2))
    ch9 = pygame.draw.rect(gameDisplay, bc, (pos1a, 420, sz1, sz2))
    ch10 = pygame.draw.rect(gameDisplay, bc, (pos1a, 460, sz1, sz2))
    ch11 = pygame.draw.rect(gameDisplay, bc, (pos1a, 500, sz1, sz2))
    ch12 = pygame.draw.rect(gameDisplay, bc, (pos1a, 540, sz1, sz2))
    ch13 = pygame.draw.rect(gameDisplay, bc, (pos1a, 580, sz1, sz2))
    ch14 = pygame.draw.rect(gameDisplay, bc, (pos1a, 620, sz1, sz2))

    # buttons right
    ch15 = pygame.draw.rect(gameDisplay, bc, (pos1b, 100, sz1, sz2))
    ch16 = pygame.draw.rect(gameDisplay, bc, (pos1b, 140, sz1, sz2))
    ch17 = pygame.draw.rect(gameDisplay, bc, (pos1b, 180, sz1, sz2))
    ch18 = pygame.draw.rect(gameDisplay, bc, (pos1b, 220, sz1, sz2))
    ch19 = pygame.draw.rect(gameDisplay, bc, (pos1b, 260, sz1, sz2))
    ch20 = pygame.draw.rect(gameDisplay, bc, (pos1b, 300, sz1, sz2))
    ch21 = pygame.draw.rect(gameDisplay, bc, (pos1b, 340, sz1, sz2))
    ch22 = pygame.draw.rect(gameDisplay, bc, (pos1b, 380, sz1, sz2))
    ch23 = pygame.draw.rect(gameDisplay, bc, (pos1b, 420, sz1, sz2))
    ch24 = pygame.draw.rect(gameDisplay, bc, (pos1b, 460, sz1, sz2))
    ch25 = pygame.draw.rect(gameDisplay, bc, (pos1b, 500, sz1, sz2))
    ch26 = pygame.draw.rect(gameDisplay, bc, (pos1b, 540, sz1, sz2))
    ch27 = pygame.draw.rect(gameDisplay, bc, (pos1b, 580, sz1, sz2))
    ch28 = pygame.draw.rect(gameDisplay, bc, (pos1b, 620, sz1, sz2))

    # change color when hovered
#

# __screen refresher?__
    pygame.display.update()
    clock.tick(60)