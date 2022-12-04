import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def game_loop():
    game_end = False

    snake_direction = LEFT
    snake = [(200, 200), (210, 200), (220,200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))

    apple_pos = on_grid_random()
    apple = pygame.Surface((10,10))
    apple.fill((255,0,0))

    clock = pygame.time.Clock()
    while not game_end:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == QUIT:
                game_end = True

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    snake_direction = UP
                if event.key == K_DOWN:
                    snake_direction = DOWN
                if event.key == K_LEFT:
                    snake_direction = LEFT
                if event.key == K_RIGHT:
                    snake_direction = RIGHT

        if snake_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        elif snake_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        elif snake_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        elif snake_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])

        # movimento da cobra
        for i in range(len(snake)-1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        # colisão com a maçã
        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))

        # condição para determinar se a cobra morreu (Ainda não cosnegui por a funcionar)
        # for i in range(1, len(snake)):
        #     if collision(snake[0], snake[i]):
        #         game_end = True

        # condition to determine if the snake has hit the wall
        if snake[0][0] < 0 or snake[0][0] > 590 and snake[0][1] < 0 or snake[0][1] > 590:
            game_end = True


        # desenho das figuras
        screen.fill((0,0,0))
        screen.blit(apple, apple_pos)

        for pos in snake:
            screen.blit(snake_skin, pos)

        pygame.display.update()

    pygame.quit()


game_loop()
