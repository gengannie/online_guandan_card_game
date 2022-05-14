import pygame
pygame.init()
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_num = 0

class Card():
    def __init__(self, num, suit, color):
        self.num = num
        self.suit = suit
        self.color = color
        self.rect = (0, 0, 5, 5) # x, y, width, height
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

class Player():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    def move(self):
        pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_LEFT]:

        #if pressed[pygame.K_RIGHT]:

        #if pressed[pygame.K_UP]:

        #if pressed[pygame.K_DOWN]

def redraw(obj):
    window.fill((255, 255, 255))
    obj.draw(window)
    pygame.display.update()

def main():
    run = True
    test_card = Card(1, "spade", (0, 255, 0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        redraw(test_card)

main()