import pygame
import pygame.locals

WIDTH = 480
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy bird clone')
clock = pygame.time.Clock()

gravity = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT // 2

all_sprite = pygame.sprite.Group()
bird = Bird()


run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                gravity = 0
                gravity -= 5
                                           

    gravity += 0.25
    bird.rect.y += gravity

    all_sprite.update()
    screen.fill(BLACK)
    all_sprite.draw(screen)

    clock.tick(FPS)

    pygame.display.flip()

pygame.quit()