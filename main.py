import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import*
import random
from pygame import mixer



pygame.init()
textfont = pygame.font.SysFont("monospace",50)
class display:

    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.window = window
        

    
    def update(self):
        pygame.display.flip()
        pygame.time.wait(10)

    def clear(self):
        glClearColor(0,0,0.1,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

screen = display(800, 400, pygame.display.set_mode((800, 400), DOUBLEBUF|OPENGL))
pygame.display.set_caption('Space Shooter 1v1')

#BGMUSIC########


index = 0
rages = True
bgmusiclist = ['bgmusic.mp3','low.mp3']
pygame.mixer.music.load(bgmusiclist[index])
mixer.music.play(-100)


bullet2_sound = mixer.Sound('blaster2.mp3')###
collide_sound = mixer.Sound('coolide.mp3')###
player_hitsound = mixer.Sound('playerhit.mp3')####
player_hitsound.set_volume(0.5)
bullet1_sound = mixer.Sound('blaster1.mp3')###
alarm = mixer.Sound('alarm.mp3')#####
end = mixer.Sound('end.mp3')#####


#BGMUSIC########

def rage_true():
        global index
        index = 1
        pygame.mixer.music.load(bgmusiclist[index])
        pygame.mixer.music.play(-100)
def rage_false():
        global index
        index = 0
        pygame.mixer.music.load(bgmusiclist[index])
        pygame.mixer.music.play(-100) 



class player_one:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.pos = [-13,0,0]
        self.int = 0.02
        
        
    def move(self):
        self.k_press = pygame.key.get_pressed()
        if self.k_press[pygame.K_w]:
            if self.pos[1] < 6:
                self.pos[1] += self.int
            
            
        if self.k_press[pygame.K_s]:
            if self.pos[1] > -6:
                self.pos[1] -= self.int

        #if self.k_press[pygame.K_d]:
            #if self.pos[0] < -1.2:
          #      self.pos[0] += self.int 
                
     #   if self.k_press[pygame.K_a]:
      #      if self.pos[0] > -13.8:
         #       self.pos[0] -= self.int
     
    def draw(self):
        glPushMatrix()
        glTranslatef(*self.pos)
        r = random.uniform(0,1)
        g = random.uniform(0,1)
        b = random.uniform(0,1)
        if one_health.int <= 5:
                glColor3f(r,g,b)
        #RAGEEEEEEE
        if one_health.int <= 5:
                if finish == False:
                        glColor3f(r,g,b)
                        self.int = 0.3
                        bullet_one.int = 0.8
                        rage = True
                        
                     
                        
                        
        else:
                glColor3f(1,1,1)
                
        glBegin(GL_LINES)
        glVertex2f(0,0)
        glVertex2f(0,1)

        glVertex2f(0,1)
        glVertex2f(1,0.0)

        glVertex2f(1,0)
        glVertex2f(0,-1.0)

        glVertex2f(0,-1.0)
        glVertex2f(0,0.0)
        glEnd()
        glPopMatrix()


    def draw_line(self):
        if finish == True:
                glColor3f(0,0,0)
        elif title == True:
                glColor3f(0,0,0)
        else:
                glColor3f(1,1,1)
        glPushMatrix()
        
        glBegin(GL_LINES)
        glVertex2f(0,8)
        glVertex2f(0,-8)            
        glEnd()

        #player 1 bar
        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(-13.62,5.3)
        glVertex2f(-3.05,5.3)

        glVertex2f(-3.05,5.3)
        glVertex2f(-3.05,6.67)

        glVertex2f(-3.05,6.67)
        glVertex2f(-13.62,6.67)

        glVertex2f(-13.62,6.67)
        glVertex2f(-13.62,5.3)
        glEnd()
        #player 2 bar
        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(13.62,5.3)
        glVertex2f(3.05,5.3)

        glVertex2f(3.05,5.3)
        glVertex2f(3.05,6.67)

        glVertex2f(3.05,6.67)
        glVertex2f(13.62,6.67)

        glVertex2f(13.62,6.67)
        glVertex2f(13.62,5.3)
        glEnd()
        glPopMatrix()
        
                

    def random_stars(self):  
        for i in range(10):
                glEnable(GL_POINT_SMOOTH)
                sizerandom = random.uniform(0.5,2.5)
                glPointSize(sizerandom)
                clockobject = pygame.time.Clock()
                starsX = random.uniform(-15.6,15.2)
                starsY = random.uniform(-15.2,12.4)
                rr = random.randint(0,1)
                gg = random.randint(0,1)
                bb = random.randint(0,1)
                glBegin(GL_POINTS)
                glColor3f(rr,gg,bb)
                glVertex3d(starsX,starsY,0)
                glEnd()
    
class one_health:
    def __init__(selfh, vertices, edges):
        selfh.vertices = vertices
        selfh.edges = edges
        selfh.pos = [-13,6.5,0]
        selfh.int = 15
       
            

    def draw(selfh,size,health_num):
        
            glPushMatrix()
            glTranslatef(*selfh.pos)
            rg = random.uniform(0.5,1)
            rb = random.uniform(0.5,0.5)
            rr = random.uniform(0.5,1)
        
            if selfh.int >= 10:
                glColor3f(0,rg,rb)
            if selfh.int <= 9:
                glColor3f(rr,rg,0)
            if selfh.int <= 5:
                glColor3f(rr,0,rb)
                
            glBegin(GL_QUADS)
            for i in range(selfh.int):
        
                
                glVertex2f(0+size,0)
                glVertex2f(-0.5+size,0)

                glVertex2f(-0.5+size,0)
                glVertex2f(-0.5+size,-1)

                glVertex2f(-0.5+size,-1)
                glVertex2f(0+size,-1.0)
    
                glVertex2f(0+size,-1)
                glVertex2f(0+size,0)
                
                size += 0.7
                
                
                     
            glEnd()
            glPopMatrix()

class two_health:
    def __init__(selfh, vertices, edges):
        selfh.vertices = vertices
        selfh.edges = edges
        selfh.pos = [13,5.5,0]
        selfh.int = 15
       
            

    def draw(selfh,size,health_num):
        
            glPushMatrix()
            glTranslatef(*selfh.pos)
            glRotatef(180,0,0,0)
            rg = random.uniform(0.5,1)
            rb = random.uniform(0.5,0.5)
            rr = random.uniform(0.5,1)

            if selfh.int >= 10:
                glColor3f(0,rg,rb)
            if selfh.int <= 9:
                glColor3f(rr,rg,0)
            if selfh.int <= 5:
                glColor3f(rr,0,rb)
            
            glBegin(GL_QUADS)
            for i in range(selfh.int):
        
                
                glVertex2f(0+size,0)
                glVertex2f(-0.5+size,0)

                glVertex2f(-0.5+size,0)
                glVertex2f(-0.5+size,-1)

                glVertex2f(-0.5+size,-1)
                glVertex2f(0+size,-1.0)
    
                glVertex2f(0+size,-1)
                glVertex2f(0+size,0)
                
                size += 0.7
                
                
                     
            glEnd()
            glPopMatrix()


class player_two:
    def __init__(selfs, vertices, edges):
        selfs.vertices = vertices
        selfs.edges = edges
        selfs.pos = [13,0,0]
        selfs.int = 0.02


    def move(selfs):
        selfs.k_press = pygame.key.get_pressed()
        if selfs.k_press[pygame.K_UP]:
            if selfs.pos[1] < 6:
                selfs.pos[1] += selfs.int
           
        if selfs.k_press[pygame.K_DOWN]:
            if selfs.pos[1] > -6:
                selfs.pos[1] -= selfs.int
        #if selfs.k_press[pygame.K_RIGHT]:
        #    if selfs.pos[0] < 13.8:
         #       selfs.pos[0] += selfs.int
               
        #if selfs.k_press[pygame.K_LEFT]:
          #  if selfs.pos[0] > 1.2:
             #   selfs.pos[0] -= selfs.int
        
                

    def draw(selfs):
        glPushMatrix()
        glTranslatef(*selfs.pos)
        r = random.uniform(0,1)
        g = random.uniform(0,1)
        b = random.uniform(0,1)
        #RAGEEEEEEE
        if two_health.int <= 5:
                if finish == False:
                        glColor3f(r,g,b)
                        selfs.int = 0.3
                        bullet_two.int = 0.8
                        
                        
        else:
                glColor3f(1,1,1)
                
        glBegin(GL_LINES)
        glVertex2f(0,0)
        glVertex2f(0,-1)

        glVertex2f(0,-1)
        glVertex2f(-1,0.0)

        glVertex2f(-1,0)
        glVertex2f(0,1.0)

        glVertex2f(0,1.0)
        glVertex2f(0,0.0)
        glEnd()
        glPopMatrix()

class bullet_one:
    def __init__(selfr, vertices, edges):
        selfr.vertices = vertices
        selfr.edges = edges
        selfr.pos = [-12,0,0]
        selfr.int = 0.009
        
    def draw(selfr):
        glPushMatrix()
        glTranslatef(*selfr.pos)
        glPointSize(20)
        rg = random.uniform(0.5,1)
        rb = random.uniform(1,0.5)
        rr = random.uniform(0.5,0.5)
        glColor3f(0,rg,rb)
        glBegin(GL_POINTS)
        glVertex2d(0,0)
        glEnd()
        glPopMatrix()

    

    def shoot(selfr):
        global rages
        selfr.pos[0] += selfr.int
        
        #bulletsound condition
        if selfr.pos[0] <= player_one.pos[0] + 0.8:
            if finish == False:
                bullet1_sound.set_volume(0.3)
                bullet1_sound.play()####
                

        
        if selfr.pos[0] > 16:
            selfr.pos[0] = player_one.pos[0]
            selfr.pos[1] = player_one.pos[1]
            

        if selfr.pos[0] >= (player_two.pos[0] -0.5):
            if selfr.pos[0] <= (player_two.pos[0] + 0.5):
                if selfr.pos[1] < (player_two.pos[1]+1):
                    if selfr.pos[1] > (player_two.pos[1]-1):
                        if finish == False:
                            selfr.pos[0] = player_one.pos[0]
                            selfr.pos[1] = player_one.pos[1]
                            player_hitsound.play()
                            two_health.int -= 1
                            print("player 1 hit")
                            if two_health.int == 5:
                                alarm.play()#####
                                rages = True
                                
                                if rages == True:
                                    rage_true()
                                    rages = False
                                
                                
                                
                                
                            if two_health.int == 0:
                                rage_false()
                                end.play()#####
                            
                
        if selfr.pos[0] >= bullet_two.pos[0]:
            if selfr.pos[1] < (bullet_two.pos[1]+ 0.5):
                if selfr.pos[1] > (bullet_two.pos[1]- 0.5):
                    if finish == False:
                        selfr.pos[0] = player_one.pos[0]
                        selfr.pos[1] = player_one.pos[1]
                        bullet_two.pos[0] = player_two.pos[0]
                        bullet_two.pos[1] = player_two.pos[1]
                        collide_sound.set_volume(0.5)
                        collide_sound.play()
                    
                    
            
        
           

class bullet_two:
    def __init__(selft, vertices, edges):
        selft.vertices = vertices
        selft.edges = edges
        selft.pos = [12,0,0]
        selft.int = 0.009
        
    def draw(selft):
        glPushMatrix()
        glTranslatef(*selft.pos)
        glPointSize(20)
        rg = random.uniform(0.5,1)
        rb = random.uniform(0,1)
        rr = random.uniform(0.5,1)
        glColor3f(rr,0,rb)
        glBegin(GL_POINTS)
        glVertex2d(0,0)
        glEnd()
        glPopMatrix()

    def shoot(selft):
        global rages
        selft.pos[0] -= selft.int

        

        #bulletsound condition
        if selft.pos[0] >= player_two.pos[0] - 0.8:
            if finish == False:
               
                bullet2_sound.set_volume(0.2)###
                bullet2_sound.play()####
            
                
        
        if selft.pos[0] < -16:
            selft.pos[0] = player_two.pos[0]
            selft.pos[1] = player_two.pos[1]
            
        if selft.pos[0] <= (player_one.pos[0]+0.5):
            if selft.pos[0] >= (player_one.pos[0] - 0.5):
                if selft.pos[1] < (player_one.pos[1] + 1):
                    if selft.pos[1] > (player_one.pos[1] - 1):
                        if finish == False:
                            selft.pos[0] = player_two.pos[0]
                            selft.pos[1] = player_two.pos[1]
                            print("player 2 hit")
                            player_hitsound.play()
                            one_health.int -= 1
                            if one_health.int == 5:
                                alarm.play()#####
                                rages = True
                                if rages == True:
                                    rage_true()
                                    rages = False
                            
                            if one_health.int == 0:
                                rage_false()

                                end.play()#####
                            
                    
                    
        if one_health.int <= 0:
            selft.int = 0.01
            bullet_one.int = 0.01
            player_one.int = 0.01
            player_two.int = 0.01

        if two_health.int <= 0:
            selft.int = 0.01
            bullet_one.int = 0.01
            player_one.int = 0.01
            player_two.int = 0.01
                         
        
class GameOver:
        def __init__(selfg, vertices, edges):
                selft.vertices = vertices
                selft.edges = edges
                selft.pos = [0,0,0]

        def drawText(x, y, text):
                r = random.uniform(150,255)
                g = random.uniform(150,255)
                b = random.uniform(150,255)
                textSurface = font.render(text, True, (255, r, g, 255)).convert_alpha()
                textData = pygame.image.tostring(textSurface, "RGBA", True)
                glWindowPos2d(x, y)
                glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


        
        

player_one = player_one(((1, -1)),((0, 0)))
player_two = player_two(((1, -1)),((0, 0)))
bullet_one = bullet_one(((1, -1)),((0, 0)))
bullet_two = bullet_two(((1, -1)),((0, 0)))
one_health = one_health(((1, -1)),((0, 0)))
two_health = two_health(((1, -1)),((0, 0)))




class main:
    
        
        
    def display_all():
        player_one.move()
        player_one.draw()
        one_health.draw(0,0)
    
        player_one.draw_line()
        player_one.random_stars()
    
        player_two.move()
        player_two.draw()
        two_health.draw(0,0)
    
        bullet_one.shoot()
        bullet_one.draw()
    
    
        bullet_two.shoot()
        bullet_two.draw()


glMatrixMode(GL_PROJECTION)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
gluPerspective(45, (screen.width/screen.height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0,0,-17)

game_over = False
finish = False
hideone = 1000
hidetwo = 1000
spacetext = 1000
hidetitle = 180
hidetitle2 = 120
title = True
coder = 0
hide1v1 = 260
rage = False 


while not game_over:
   
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            print('gameover')
            pygame.quit()

        if bullet_two.pos[0] <= bullet_one.pos[0]:
            if bullet_two.pos[1] < (bullet_one.pos[1] + 0.5):
                if bullet_two.pos[1] > (bullet_one.pos[1] - 0.5):
                   if finish == False:
                        bullet_two.pos[0] = player_two.pos[0]
                        bullet_two.pos[1] = player_two.pos[1]
                        bullet_one.pos[0] = player_one.pos[0]
                        bullet_one.pos[1] = player_one.pos[1]
                        collide_sound.play()
                        print('bullet collide')
                        


        
        
        
        if one_health.int <=0:
            if two_health.int > one_health.int:
                print('PLAYER TWO WINS')
                hidetwo = 220
                spacetext = 150
                coder =0
                finish = True
            
        if two_health.int <=0:
            if one_health.int > two_health.int:
                print('PLAYER ONE WINS')
                hideone = 220
                spacetext = 150
                coder = 0
                finish = True

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        if finish == True:
                                print(index)
                                if title == False:
                                    if index == 0:
                                        rage_false()
                                        print('restart')
                                        #player health
                                        one_health.int =15
                                        two_health.int = 15
                                        #reset movement speed and position p1
                                        player_one.int = 0.2
                                        player_one.pos[1] = 0
                                        player_one.pos[0] = -13
                                         #reset movement speed and position p2
                                        player_two.int = 0.2
                                        player_two.pos[1] = 0
                                        player_two.pos[0] = 13
                                        #bullet speed
                                        bullet_one.int = 0.5
                                        bullet_two.int = 0.5
                                        #bullet position reset Y
                                        bullet_one.pos[1] = 0
                                        bullet_two.pos[1] = 0
                                        #bullet position reset X
                                        bullet_one.pos[0] = -13
                                        bullet_two.pos[0] = 13
                                        
                                        hideone = 1000
                                        hidetwo = 1000
                                        spacetext = 1000
                                        coder =1000
                                        finish = False
                                
                        if title == True:
                                print('Startgame')
                                #player health
                                one_health.int =15
                                two_health.int = 15
                                #reset movement speed and position p1
                                player_one.int = 0.2
                                player_one.pos[1] = 0
                                player_one.pos[0] = -13
                                #reset movement speed and position p2
                                player_two.int = 0.2
                                player_two.pos[1] = 0
                                player_two.pos[0] = 13
                                #bullet speed
                                bullet_one.int = 0.5
                                bullet_two.int = 0.5
                                #bullet position reset Y
                                bullet_one.pos[1] = 0
                                bullet_two.pos[1] = 0
                                #bullet position reset X
                                bullet_one.pos[0] = -13
                                bullet_two.pos[0] = 13
                                
                                hideone = 1000
                                hidetwo = 1000
                                spacetext = 1000
                                hidetitle = 1000
                                hidetitle2 = 1000
                                hide1v1 = 1000
                                coder =1000

                                title = False
                                
                   
    
    screen.clear()
    main.display_all()
    font = pygame.font.SysFont('impact', 80)
    
    GameOver.drawText(120, hideone, "Player One Wins")
    GameOver.drawText(120, hidetwo, "Player Two Wins")
    font = pygame.font.SysFont('impact', 80)
    GameOver.drawText(351, hide1v1, "1v1")
    GameOver.drawText(140, hidetitle, "SPACE SHOOTER")
    font = pygame.font.SysFont('impact', 60)
    
    GameOver.drawText(225, hidetitle2, "SPACE to Start")
    GameOver.drawText(190, spacetext, "SPACE to Restart")
    font = pygame.font.SysFont('impact', 20)
    GameOver.drawText(0, coder, "Code by John Patrick Quintos - BT701")
    
    screen.update()
