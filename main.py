import pygame
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

width = 500
height = 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Snake Game")
fps = 60
timer = pygame.time.Clock()
main_menu = False
font = pygame.font.Font("freesansbold.ttf", 24)
menu_command = 0

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("verdana", 15)
score_font = pygame.font.SysFont("verdana", 10)
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0,0])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = width / 2
    y1 = height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("Looser ! c -> play again, q -> quit", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change == snake_block:
                        pass
                    else:
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == -snake_block:
                        pass
                    else:
                        x1_change = snake_block
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == snake_block:
                        pass
                    else:
                        y1_change = -snake_block
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change == -snake_block:
                        pass
                    else:
                        y1_change = snake_block
                        x1_change = 0
 
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)

    pygame.quit()
    quit()

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0 ,5)
        pygame.draw.rect(screen, 'dark gray', self.button, 5, 5)
        text = font.render(self.text, True, 'black')
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def draw_game():
    button = Button('Main Menu', (230, 450))
    button.draw()
    return button.check_clicked()
   
def draw_menu():
    command = 0
    pygame.draw.rect(screen, 'black', [100, 100, 300, 300])
    menu_btn = Button('Exit Menu',(120, 350))
    btn1 = Button('Jeu',(120, 120))
    btn2 = Button('Scores',(120, 200))
    menu_btn.draw()
    btn1.draw()
    btn2.draw()
    if menu_btn.check_clicked():
        command = 1
    if btn1.check_clicked():
        command = gameLoop()
    if btn2.check_clicked():
        command = 3
    return command

run = True
while run:
    screen.fill('light blue')
    timer.tick(fps)
    if main_menu: 
        menu_command = draw_menu()
        if menu_command > 0:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command >= 1:
            text = font.render(f'Button {menu_command - 1} was clicked', True, 'black')
            screen.blit(text, (100,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

gameLoop()