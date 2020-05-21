import pygame
import random

pygame.init()

# Variables
width = 700
height = 500
fps = 60

# Color
red = (255,0,0)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)

window_screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


def snake(window,color,snake_List,snake_size):
    for snake_x,snake_y in snake_List:
        pygame.draw.rect(window,color,[snake_x,snake_y,snake_size,snake_size])

font = pygame.font.SysFont(None,45)
def textonscreen(text,color,x,y):
    screen = font.render(text,True,color)
    window_screen.blit(screen,[x,y])

def snakegame():


    # Snake
    snake_x = random.randint(1, 500)
    snake_y = random.randint(1, 200)
    snake_size = 15
    snake_list = []
    snake_length = 1
    score = 0

    # snake Movement
    snake_velocity_x = 0
    snake_velocity_y = 0
    speed = 5

    # Food
    food_x = random.randint(1, 500)
    food_y = random.randint(1, 200)

    # Game Specific Variables
    exit_game = False
    game_over = False

    # Main game
    while not exit_game:
        if game_over == True:
            window_screen.fill(white)
            textonscreen("Game Over",black,240,200)
            textonscreen("Press Enter for Play Again", black, 0, 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        snakegame()



        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        snake_velocity_x = 0
                        snake_velocity_y = speed

                    if event.key == pygame.K_UP:
                        snake_velocity_x = 0
                        snake_velocity_y = -speed

                    if event.key == pygame.K_RIGHT:
                        snake_velocity_x = speed
                        snake_velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        snake_velocity_x = -speed
                        snake_velocity_y = 0

        pygame.display.update()
        window_screen.fill(black)

        # Snake Food
        if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
            food_x = random.randint(1, 500)
            food_y = random.randint(1, 200)
            snake_length += 5
            score += 1 * 10

        textonscreen("score :"+str(score),white,500,0)


        if snake_x>width or snake_x<0 or snake_y>height or snake_y<0:
            game_over = True


        pygame.draw.rect(window_screen, red, [food_x, food_y, snake_size, snake_size])


        snake_x += snake_velocity_x
        snake_y += snake_velocity_y

        if len(snake_list)>snake_length:
            del snake_list[0]

        head = []
        head.append(snake_x)
        head.append(snake_y)

        if head in snake_list[:-1]:
            game_over = True

        snake_list.append(head)

        snake(window_screen, yellow, snake_list, snake_size)


        clock.tick(fps)
    pygame.display.update()


    pygame.quit()
    quit()


snakegame()

