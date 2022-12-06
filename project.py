import pygame
import time
import random 
import sys

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
#Color
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
green_snake = (154,205,50)
orange = (255, 165, 0)
violet = (238, 130, 238)
lime = (0, 255, 0)
indigo = (75, 0, 130)
golden = (218, 165, 32)
firered = (178, 34, 34)
ored = (255, 69, 0)

#Constant
DIS_WIDTH = 800
DIS_HEIGHT = 600



try:
    image = pygame.image.load("fon.png")
    image_table = pygame.image.load("fon-record.jpg")
    image_over = pygame.image.load("fon_gameover.jpg")
except FileNotFoundError:
    image = -999

menu = True#test

try:
    catch = pygame.mixer.Sound('point.ogg')#подключение звука 
except FileNotFoundError:
    catch = -999


alphavit = [
    'A','B','C',
    'D','E','F','G',
    'H','J','K','L'
    ]
#Window
window = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10#Speed snake
color_line = yellow
color_rect = golden


#Fonts
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 20)
pause_style = pygame.font.SysFont("verdana", 40)
menu_style = pygame.font.SysFont("arial", 45)
records_style = pygame.font.SysFont("arial", 25)

class Food:
    def __init__(self,color, x,y):
        self.__color = color
        self.__x = x
        self.__y = y
    def get_color(self):
        return self.__color
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y


def Your_score(score):
    value = score_font.render("Очки: " + str(score), True, yellow)
    window.blit(value, [DIS_WIDTH-100, 0])
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green_snake, [x[0], x[1], snake_block, snake_block])
 
 
def text(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [DIS_WIDTH / 6,
                    DIS_HEIGHT / 3])


def screen_pause(msg):
    pygame.draw.rect(window, color_rect, 
                 (250, 200, 350, 200), 8)
    pygame.draw.rect(window, color_rect, 
                 (225, 175, 400, 250), 8)
    mesg = pause_style.render(msg, True, red)
    window.blit(mesg, [DIS_WIDTH / 2-40,
                    DIS_HEIGHT / 2-25])
    


def screen_menu(color1, color2, color3):
    pygame.draw.rect(window, color_rect, 
                 (250, 120, 350, 200), 8)
    pygame.draw.rect(window, color_rect, 
                 (250, 350, 350, 200), 8)
    pygame.draw.rect(window, color_rect, 
                 (50, 50, 50, 50), 8)
    mesg = records_style.render("Р", True, color3)
    window.blit(mesg, [140 / 2 ,
                    120 / 2])
    mesg = menu_style.render("Новая игра", True, color1)
    window.blit(mesg, [DIS_WIDTH / 2-65,
                    DIS_HEIGHT / 2-105])
    mesg = menu_style.render("Выйти", True, color2)
    window.blit(mesg, [DIS_WIDTH / 2-35,
                    DIS_HEIGHT / 2+120])


def screen_records(records, snake_speed):
    while records==True:
        try:
            file = open("records-text.txt",'r')
        except FileNotFoundError:
            file = 0
        #window.fill(blue)
        image!=-999 if window.blit(image_table,(0,0)) else window.fill(blue)
        pygame.draw.rect(window, color_rect, 
                 (50, 50, 700, 450), 8)
        pygame.draw.rect(window, color_rect, 
                 (350, 520, 100, 65), 8)
        mesg = menu_style.render("<-", True, red)
        window.blit(mesg, [380,
                    525])
        for i in range(9):
            if (file != 0):
                line = file.readline()
                line = line.replace('\n','')
                mesg = menu_style.render("Результат  "+alphavit[i]+
                                        " :         "+
                                        str(line), True, orange)
                window.blit(mesg, [240,
                    60+45*i])
        pygame.display.update()
        file.close()
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        if (x>350 and x<450 and y>520 and y<585):
                            menu = True
                            gameLoop(snake_speed, menu)
    

def menu_control(snake_speed, menu):
        global game_over, game_close
        color_difficalt = yellow
        color_new= yellow
        color_exit = yellow
        color_records = yellow
        pygame.mouse.set_visible(True)#visible mouse
        while menu == True:
            image!=-999 if window.blit(image,(0,0)) else window.fill(blue)#ternary operator
            screen_menu(color_new,color_exit,color_records)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        if (x>250 and x<600 and y>120 and y<320):
                            menu = False
                            difficult = False
                            while difficult == False:
                                screen_level_difficulty()
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1: 
                                            x,y = pygame.mouse.get_pos()
                                            if (x>250 and x<600 and y>30 and y<180):
                                                difficult = True
                                                snake_speed = 5
                                                
                                            elif (x>250 and x<600 and y>230 and y<380):
                                                difficult = True
                                                snake_speed = 10
                                                
                                            elif (x>250 and x<600 and y>430 and y<580):
                                                difficult = True
                                                snake_speed = 15
                                                
                        elif (x>250 and x<600 and y>350 and y<550):
                            menu = False
                            game_over = True
                            game_close = False
                        elif (x>50 and x<100 and y>50 and y <100):
                            records = True
                            screen_records(records, snake_speed)
                elif event.type == pygame.MOUSEMOTION:
                    x,y = pygame.mouse.get_pos()
                    if (x>250 and x<600 and y>120 and y<320):
                        color_new = orange
                    elif (x>250 and x<600 and y>350 and y<550):
                        color_exit = red
                    elif (x>50 and x<100 and y>50 and y <100):
                        color_records = violet
                    else:
                        color_new = yellow
                        color_exit = yellow
                        color_records = yellow
        return snake_speed

                        

def screen_level_difficulty():
    image!=-999 if window.blit(image,(0,0)) else window.fill(blue)
    pygame.draw.rect(window, color_rect, 
                 (250, 30, 350, 150), 8)
    pygame.draw.rect(window, color_rect, 
                 (250, 230, 350, 150), 8)
    pygame.draw.rect(window, color_rect, 
                 (250, 430, 350, 150), 8)
    mesg = menu_style.render("легко", True, orange)
    window.blit(mesg, [DIS_WIDTH / 2-25,
                    DIS_HEIGHT / 2-230])
    mesg = menu_style.render("Нормально", True, orange)
    window.blit(mesg, [DIS_WIDTH / 2-55,
                    DIS_HEIGHT / 2-30])
    mesg = menu_style.render("Сложно", True, orange)
    window.blit(mesg, [DIS_WIDTH / 2-35,
                    DIS_HEIGHT / 2+170])



def save_records(record):
    try:
        file = open("records-text.txt",'r')
    except FileNotFoundError:
        file = 0
    if (file != 0):
        text = file.read()
    try:
        file = open("records-text.txt",'w')
    except FileNotFoundError:
        file = 0
    if (file != 0):
        file.write(str(record) + '\n')
        file.write(text)
        file.close()
    

def gameLoop(snake_speed, menu):
    global game_over,game_close
    paused = False
    records = False
    game_over = False
    game_close = False
    
    flag = 0
 
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2
 
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(60, DIS_WIDTH - snake_block-60) / 10.0) * 10.0
    foody = round(random.randrange(60, DIS_HEIGHT - snake_block-60) / 10.0) * 10.0

    apple = Food(red, foodx, foody)
 
    while not game_over:
        
        snake_speed = menu_control(snake_speed, menu)
        menu = False#test
        pygame.mouse.set_visible(False)#visible mouse          
        while paused == True:
            #window.fill(blue)
            image!=-999 if window.blit(image,(0,0)) else window.fill(blue)
            screen_pause("Pause")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
        while game_close == True:
            image!=-999 if window.blit(image_over,(0,0)) else window.fill(blue)
            pygame.draw.ellipse(window, orange, 
                    (100, 165, 550, 100),8)
            pygame.draw.ellipse(window, orange, 
                    (75, 140, 600, 150),4)
            pygame.draw.ellipse(window, orange, 
                    (50, 115, 650, 200),2)
            
            text("Нажмите Space - Играть снова или Escape - Выход", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_close = False
                        menu = True
                        save_records(Length_of_snake-1)
                        gameLoop(snake_speed,menu)
                    if event.key == pygame.K_SPACE:
                        menu = False#test
                        save_records(Length_of_snake-1)
                        gameLoop(snake_speed,menu)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and flag != 2 :
                    x1_change = -snake_block
                    y1_change = 0
                    flag = 1
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and flag != 1:
                    x1_change = snake_block
                    y1_change = 0
                    flag = 2
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and flag != 4:
                    y1_change = -snake_block
                    x1_change = 0
                    flag = 3
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and flag != 3:
                    y1_change = snake_block
                    x1_change = 0
                    flag = 4
                elif event.key == pygame.K_p:
                    paused = True
            if event.type == pygame.MOUSEBUTTONDOWN:#Событие mouse
                #print("Нажата кнопка: ", event.button)
                if event.button == 1:
                    x,y = pygame.mouse.get_pos()
                    
 
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, apple.get_color(),
                         [apple.get_x(), apple.get_y(), snake_block,
                          snake_block],
                         5)
        pygame.draw.line(window, color_line, 
                 [1, 1], 
                 [1, 597], 2)
        pygame.draw.line(window, color_line, 
                 [1, 1], 
                 [797, 1], 2)
        pygame.draw.line(window, color_line, 
                 [797, 1], 
                 [797, 597], 2)
        pygame.draw.line(window, color_line, 
                 [1, 597], 
                 [797, 597], 2)
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
 
        if x1 == apple.get_x() and y1 == apple.get_y():
            foodx = round(random.randrange(60, DIS_WIDTH - snake_block-60) / 10.0) * 10.0
            foody = round(random.randrange(60, DIS_HEIGHT - snake_block-60) / 10.0) * 10.0
            apple.set_x(foodx)
            apple.set_y(foody)
            Length_of_snake += 1
            if (catch != -999):
                catch.play()
            
        clock.tick(snake_speed)
    pygame.quit()
    sys.exit()
 
 
gameLoop(snake_speed,menu)


