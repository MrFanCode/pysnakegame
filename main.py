import pygame
import time
import random

# Initializing pygame
pygame.init()


# Storing rgb colors 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0, 128, 0)


# Storing screen size value
width, height = 600, 400

# Display a window 
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()


# Defining snake size and speed
snakeSize = 10
snakeSpeed = 15

# Defining display messages font and size 
messageFont = pygame.font.SysFont('ubuntu', 25)
scoreFont = pygame.font.SysFont('ubuntu', 20)


def display_score(score):
    text = scoreFont.render("Score: " + str(score), True, white)
    screen.blit(text, [0,0])


def draw_snake(snakeSize, snakePixel):
    for pixels in snakePixel:
        pygame.draw.rect(screen, green, [pixels[0], pixels[1], snakeSize, snakeSize])


def startGame():

    gameIsOver = False
    gameClosed = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snakePixel = []
    snakeLength = 1

    target_x = round(random.randrange(0, width-snakeSize) / 10.0) * 10.0
    target_y = round(random.randrange(0, height-snakeSize) / 10.0) * 10.0

    
    while not gameIsOver:

        while gameClosed:
            screen.fill(black)
            gameOverMsg = messageFont.render("Game Over", True, red)
            screen.blit(gameOverMsg, [width / 3, height / 3])
            display_score(snakeLength - 1)
            pygame.display.update()

            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        gameIsOver = True
                        gameClosed = False

                    if event.key == pygame.K_2:
                        startGame()

                if event.type == pygame.QUIT:
                    gameIsOver = True
                    gameClosed = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsOver = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snakeSize
                    y_speed = 0

                if event.key == pygame.K_RIGHT:
                    x_speed = snakeSize
                    y_speed = 0

                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snakeSize

                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snakeSize

        if x >= width or x < 0 or y >= height or y < 0:
            gameClosed = True

        x += x_speed
        y += y_speed

        
        screen.fill(black)
        pygame.draw.rect(screen, red, [target_x, target_y, snakeSize, snakeSize])


        snakePixel.append([x, y])

        if len(snakePixel) > snakeLength:
            del snakePixel[0]

        for pixels in snakePixel[:-1]:
            if pixels == [x, y]:
                gameClosed = True

        
        # Draw the snake on screen display
        draw_snake(snakeSize, snakePixel)

        # Display score of the player
        display_score(snakeLength - 1)


        pygame.display.update()


        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width-snakeSize) / 10.0) * 10.0
            target_y = round(random.randrange(0, height-snakeSize) / 10.0) * 10.0
            snakeLength += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


startGame()
