#imports Inits and variables
import pygame
import random
from random import randint
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.display.init()
width = 1600
height = 800
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()
mouse = pygame.mouse.get_pressed()
mx,my = pygame.mouse.get_pos()
back_color = (28, 0, 92)


win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

class Paddle(pygame.sprite.Sprite):
    def __init__(self,color ,width, height):
        super().__init__()
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()     
        self.points = 0
        self.sensitivity = 1
               
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.x == 0:
            self.rect.x = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.x == 400:
            self.rect.x = 400

class ball(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.velocityX = 2
        self.velocityY = 2
        self.velocity = [randint(4,8),randint(-8,8)]
        self.add_vel = 3
        self.points_limit = 7
        
    def update(self):
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

#paddles and ball
paddle2 = Paddle((255,255,255), 10, 100)
paddle2.rect.x = 40
paddle2.rect.y = 300

paddle1 = Paddle((255,255,255),10, 100)
paddle1.rect.x = 1550
paddle1.rect.y = 300

ball = ball(10, 10)
ball.rect.x = 800
ball.rect.y = 400

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

#guy1 = pygame.image.load('player1.png').convert()
#guy1_rect = pygame.Rect(400, 55 ,20, 52)
#guy1.set_colorkey((255,255,255))


#draws some important things on the screen while in game loop
def redraw():
    pygame.time.delay(0)
    clock.tick(240)
    win.fill(back_color)       
    all_sprites.update()
    all_sprites.draw(win)   
    pygame.draw.line(win, (255,255,255), (800,0), (800,800), 5)
    pygame.draw.line(win, (255,255,255), (0, 110), (1600, 110), 5)
    player1 = font.render(str(paddle1.points), False, (255,255,255))
    player2 = font.render(str(paddle2.points), False, (255,255,255))
    win.blit(player1,(0,0))
    win.blit(player2,(1560, 0))    
    #win.blit(guy1, (guy1_rect.x, guy1_rect.y))
    pygame.display.update()
    
#font vaiable
font = pygame.font.SysFont('fixedsys.ttf', 100)



#if a player wins
def Player1_wins():
    runn = True
    while runn:  
        keys = pygame.key.get_pressed()
        paddle_win = font.render("Player 1 WINS!", True, (255,255,255))
        win.blit(paddle_win, (500, 200))
        main_men = font.render("Press 'ESCAPE' to go back to the main menu", True, (255,255,255))
        win.blit(main_men, (50,400))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
        if keys[pygame.K_ESCAPE]:
            runn = False
            paddle1.points = 0
            paddle2.points = 0
            Start_menu()
        
        
def Player2_wins():
    runn = True
    while runn:
        keys = pygame.key.get_pressed()
        paddle_win = font.render("Player 2 WINS!", True, (255,255,255))
        win.blit(paddle_win, (500, 200))    
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
        if keys[pygame.K_ESCAPE]:
            runn = False
            paddle1.points = 0
            paddle2.points = 0
            Start_menu()
#paused
def pause():
    runn = True
    while runn:
        keys = pygame.key.get_pressed()
        paused = font.render("Paused", True, (255,255,255))
        win.blit(paused,(670,50))
        if keys[pygame.K_ESCAPE]:
            main()
            runn = False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()


def bot_pause():
    runn = True
    while runn:
        keys = pygame.key.get_pressed()
        paused = font.render("Paused", True, (255,255,255))
        win.blit(paused,(670,50))
        if keys[pygame.K_ESCAPE]:
            PlayBot()
            runn = False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
        

#Start menu
def Start_menu():
    
    runn = True
    click = False
    while runn:
        mouse = pygame.mouse.get_pressed()
        mx,my = pygame.mouse.get_pos()
        Pong = font.render("Pong", True, (255,255,255))
        start = font.render("Start", True ,(255,255,255))
        option = font.render("Options", True, (255,255,255))
        start_hitbox = pygame.Rect(750, 200, 170, 80)
        option_hitbox = pygame.Rect(700, 400, 270, 80)
        
        win.fill(back_color)
        
        win.blit(Pong,(750,10))        
        win.blit(start, (750, 200))  
        win.blit(option, (700, 400))
        
        
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_hitbox.collidepoint((mx, my)):  
                        runn = False
                        post_game()
                        print("bruh")
                    if option_hitbox.collidepoint((mx,my)):
                        runn = False
                        options()
                        
        pygame.display.update()

#making sure players are ready
def post_game():
    keys = pygame.key.get_pressed
    runn = True
    while runn:
        win.fill(back_color)
        keys = pygame.key.get_pressed()
        ready = font.render("Press the SpaceBar when you are ready", True, (255,255,255))
        bot = font.render("Press 'B' to play with a bot", True, (255,255,255))
        warning = font.render("You can go back to the menu by pressing", True, (255,255,255))
        warning2 = font.render("'ESCAPE'", True, (255,255,255))
        win.blit(warning, (100, 500))
        win.blit(warning2, (750, 600))
        win.blit(bot, (400, 300))
        win.blit(ready, (130, 100))       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
        
        if keys[pygame.K_SPACE]:
            runn = False
            main()

        if keys[pygame.K_b]:
            runn = False
            PlayBot()

        if keys[pygame.K_ESCAPE]:
            runn == False
            Start_menu()
        
        pygame.display.update()

particles = []

def PlayBot():
    win.fill(back_color)
    bounceX = 2
    bounceY = 2
    
    run = True
    while run:
         
        pygame.time.delay(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
        #collision
        if ball.rect.x >= 1600:
            jump = True
            ball.rect.x, ball.rect.y = 800, 400
            ball.velocityX = 1
            ball.velocityY = 1
            paddle1.points += 1 
        
                
        if ball.rect.y >= 800:  
            bounceY = bounceX + ball.add_vel / 10
            ball.velocityY = -bounceY
                
        if ball.rect.x <= 0:   
            jump = True
            ball.rect.x, ball.rect.y = 800, 400
            ball.velocityX = 1
            ball.velocityY = 1
            paddle2.points += 1
                  
        #if jump == True:
        #    print("bruh")
        #    guy1_rect.y -= 20  
       #if guy1_rect.y > win-guy1_rect.get_height():
         #
         # 
         # 
         #  pass
        if ball.rect.y <= 110:    
            bounceY = bounceX + ball.add_vel / 10
            ball.velocityY = bounceY  
            
        if paddle1.rect.colliderect(ball.rect):
            bounceX = bounceY + ball.add_vel / 10
            ball.velocityX = -bounceX
        

        if paddle2.rect.colliderect(ball.rect):   
            bounceY = bounceX + ball.add_vel / 10  
            ball.velocityX = bounceX
        
        if paddle2.rect.y > ball.rect.y:
            paddle2.moveUp(15)
                
        if paddle2.rect.y < ball.rect.y:
            paddle2.moveDown(15)

        if paddle1.points == ball.points_limit:
            run = False
            Player1_wins()
            
        if paddle2.points == ball.points_limit:
            run = False
            Player2_wins()
        
        
        #controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle1.moveUp(paddle1.sensitivity)
        if keys[pygame.K_DOWN]:
            paddle1.moveDown(paddle1.sensitivity)
            
        if keys[pygame.K_p]:
            bot_pause()
        
        
        redraw()
        

#Game in action
def main():
    win.fill(back_color)
    bounceX = 2
    bounceY = 2
    
    run = True
    while run:
        jump = False
        
        
        pygame.time.delay(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
        #collision
        if ball.rect.x >= 1600:
            jump = True
            ball.rect.x, ball.rect.y = 800, 400
            ball.velocityX = 1
            ball.velocityY = 1
            paddle1.points += 1 
        
                
        if ball.rect.y >= 800:  
            bounceY = bounceX + ball.add_vel / 10
            ball.velocityY = -bounceY
                
        if ball.rect.x <= 0:   
            jump = True
            ball.rect.x, ball.rect.y = 800, 400
            ball.velocityX = 1
            ball.velocityY = 1
            paddle2.points += 1
                  
        #if jump == True:
        #    print("bruh")
        #    guy1_rect.y -= 20  
       #if guy1_rect.y > win-guy1_rect.get_height():
         #
         # 
         # 
         #  pass
        if ball.rect.y <= 110:    
            bounceY = bounceX + ball.add_vel / 10
            ball.velocityY = bounceY  
            
        if paddle1.rect.colliderect(ball.rect):
            bounceX = bounceY + ball.add_vel / 10
            ball.velocityX = -bounceX
        

        if paddle2.rect.colliderect(ball.rect):   
            bounceY = bounceX + ball.add_vel / 10  
            ball.velocityX = bounceX
        
        if paddle1.points == ball.points_limit:
            run = False
            Player1_wins()
            
        if paddle2.points == ball.points_limit:
            run = False
            Player2_wins()
        
        
        #controls
        keys = pygame.key.get_pressed()           
        if keys[pygame.K_w]:
            paddle2.moveUp(paddle2.sensitivity)
        if keys[pygame.K_s]:
            paddle2.moveDown(paddle2.sensitivity)
        if keys[pygame.K_UP]:
            paddle1.moveUp(paddle1.sensitivity)
        if keys[pygame.K_DOWN]:
            paddle1.moveDown(paddle1.sensitivity)
            
        if keys[pygame.K_p]:
            pause()
        
        
        redraw()
        



        
#options menu   
def options():
    win.fill(back_color)
    runn = True
    click = False    
    while runn:
                    
        mouse = pygame.mouse.get_pressed()
        mx,my = pygame.mouse.get_pos()
        Option = font.render("Options", True, (255,255,255))
        controls = font.render("Controls", False, (255,255,255))
        paddle1_sens_lab = font.render("Paddle 1 Sensitivity", True, (255,255,255))
        paddle2_sens_lab = font.render("Paddle 2 Sensitivity", True, (255,255,255))       
        paddle1_sens = font.render(str(paddle2.sensitivity), False, (255,255,255))
        paddle2_sens = font.render(str(paddle1.sensitivity), False, (255,255,255))
        paddle1_plus = font.render("+", False, (255,255,255))
        paddle1_sub = font.render("-", False, (255,255,255))
        paddle2_plus = font.render("+", False, (255,255,255))
        paddle2_sub = font.render("-", False, (255,255,255))
        point_limit = font.render(str(ball.points_limit), True, (255,255,255))
        point_limit_lab = font.render("Point Limit", True, (255,255,255))
        point_limit_add = font.render("+", False, (255,255,255))
        point_limit_sub = font.render("-", False, (255,255,255))        
        ball_vel = font.render("Bounce off wall velocity", True, (255,255,255))
        ball_vel_plus = font.render("+", True, (255,255,255))
        ball_vel_sub = font.render("-", True, (255,255,255))
        ball_vel_num = font.render(str(ball.add_vel), False, (255,255,255))
        
        #for clicks
        con = pygame.Rect(100 ,70, 280, 50)
        plus2 = pygame.Rect(1150,260, 50, 50)
        sub2 = pygame.Rect(940, 260, 50 ,50)
        plus = pygame.Rect(1150, 160, 50, 50)
        sub = pygame.Rect(940, 160,50, 50)
        point_plus = pygame.Rect(1150, 360,50, 50)
        point_sub = pygame.Rect(940, 360,50, 50)
        ball_velplus = pygame.Rect(1150, 450, 50, 50)
        ball_velsub = pygame.Rect(950, 450, 50, 50)
        
        #bliting on screen               
        win.fill(back_color)  
        win.blit(ball_vel, (50, 450))
        win.blit(ball_vel_num,(1040 ,450))
        win.blit(ball_vel_plus, (1150, 450))
        win.blit(ball_vel_sub, (950, 450))
        win.blit(point_limit, (1040, 350 ))
        win.blit(point_limit_add, (1150, 350))
        win.blit(point_limit_sub, (950, 350))
        win.blit(point_limit_lab, (50, 350))
        win.blit(Option,(750,10))
        win.blit(paddle1_sens_lab,(50 , 150))        
        win.blit(controls,(50 ,60))
        win.blit(paddle2_sens_lab,(50 , 250))
        win.blit(paddle2_sens,(1040 ,150))
        win.blit(paddle1_sens,(1040, 250))
        win.blit(paddle1_plus, (1150, 150))
        win.blit(paddle2_plus, (1150, 250))
        win.blit(paddle1_sub, (950, 150))
        win.blit(paddle2_sub, (950, 250))
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_ESCAPE]:
            runn == False
            Start_menu()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()     
            #event when click mouse on rects
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if plus.collidepoint((mx, my)):
                        paddle1.sensitivity += 1
                        print("2")
                    if sub.collidepoint((mx, my)):               
                        paddle1.sensitivity -= 1
                        
                    if plus2.collidepoint((mx,my)):
                        paddle2.sensitivity += 1
                        print("1")
                    if sub2.collidepoint((mx, my)):               
                        paddle2.sensitivity -= 1   
                    if point_plus.collidepoint((mx, my)):
                        ball.points_limit += 1
                    if point_sub.collidepoint((mx, my)):
                        ball.points_limit -= 1                        
                    if ball_velplus.collidepoint((mx,my)):
                        ball.add_vel += 1
                    if ball_velsub.collidepoint((mx,my)):
                        ball.add_vel -= 1
                    if con.collidepoint((mx,my)):
                        runn = False
                        conn()

def col():
    runn = True
    while runn:
        mouse = pygame.mouse.get_pressed()
        mx,my = pygame.mouse.get_pos()
        back_color = (28, 0, 92)
        win.fill(back_color)
        background = font.render("Background", True, (255, 255,255))
        change_back = pygame.Rect(750, 20, 380, 50)
        pygame.draw.rect(win, (255,0,0), change_back)
        win.blit(background, (750,10))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if change_back.collidepoint((mx, my)):
                        back_color = (255,255,255)
                        win.fill(back_color)
                        pygame.display.update()
#show controls
def conn():

    runn = True
    while runn:
        keys = pygame.key.get_pressed()
        win.fill(back_color)           
        pygame.draw.rect(win,(255,255,255),paddle1)
        paddle1_instuct = font.render("Paddle 1", True ,(255,255,255))
        paddle1_instuct2 = font.render("Controled by ", True ,(255,255,255))
        paddle1_instuct3 = font.render("the arrow keys", True, (255,255,255))
        paddle2_instuct = font.render("Paddle 2", True ,(255,255,255))
        paddle2_instuct2 = font.render("Controled by ", True ,(255,255,255))
        paddle2_instuct3 = font.render("the W and S", True, (255,255,255))
        paddle2_instuct4 = font.render("keys", True, (255,255,255))
        Go_back = font.render("'ESCAPE' to go back", True, (255,255,255))
        pause_p = font.render("'P' to pause mid game", True, (255,255,255))
        win.blit(paddle1_instuct,(1100, 50))
        win.blit(paddle1_instuct2,(1000, 150))
        win.blit(paddle1_instuct3,(1000, 250))
        win.blit(paddle2_instuct,(100, 50))
        win.blit(paddle2_instuct2,(50, 150))
        win.blit(paddle2_instuct3,(50, 250))
        win.blit(paddle2_instuct4,(140, 350))
        win.blit(Go_back, (500, 500))
        win.blit(pause_p, (500, 700))
        pygame.draw.rect(win,(255,255,255),paddle2)
        pygame.display.update()
        if keys[pygame.K_ESCAPE]:
            runn == False
            options()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()  
                

#call start menu
Start_menu()
        
pygame.quit()
exit()
