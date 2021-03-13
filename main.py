import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
# This is what you see at the top of the window
pygame.display.set_caption('Snake Game')
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()
