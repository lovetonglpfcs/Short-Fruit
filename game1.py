import pgzrun,pygame

import random

WIDTH = 640
HEIGHT = 480


apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')
pygame.mixer.music.load('azuka.mp3')
pygame.mixer.music.play(-1)
def draw():
    global xr,yr,x1,y1,x2,y2
    screen.fill((100,200,200))
    apple.draw()
    orange.draw()
    pineapple.draw()
    screen.draw.filled_rect( Rect((0,0),(140,40)) , "yellow")
    screen.draw.text("Ready?",topleft=(xr,yr),fontsize=40,color = "red")
    screen.draw.text("Good!",topleft=(x1,y1),fontsize=40,color = "red")
    screen.draw.text("Miss!",topleft=(x2,y2),fontsize=40,color = "red")
    
    

def place_apple():
    apple.x  = random.randint(40,WIDTH-40)
    apple.y  = random.randint(40,HEIGHT-40)

def place_orange():
    orange.x  = random.randint(40,WIDTH-40)
    orange.y  = random.randint(40,HEIGHT-40)

def place_pineapple():
    pineapple.x  = random.randint(40,WIDTH-40)
    pineapple.y  = random.randint(40,HEIGHT-40)

def on_mouse_down(pos):
    global xr,yr,x1,y1,x2,y2
    xr = int(WIDTH*2)
    yr = int(HEIGHT*2)
    if apple.collidepoint(pos):
        x1 = 5
        y1 = 5
        x2 = int(WIDTH*2)
        y2 = int(HEIGHT*2)
        print("good")
        place_apple()
    elif orange.collidepoint(pos):
        x1 = 5
        y1 = 5
        x2 = int(WIDTH*2)
        y2 = int(HEIGHT*2)
        print("good")
        place_orange()
    elif pineapple.collidepoint(pos) :
        x1 = 5
        y1 = 5
        x2 = int(WIDTH*2)
        y2 = int(HEIGHT*2)
        print("good")
        place_pineapple()
    else :
        x2 = 5
        y2 = 5
        x1 = int(WIDTH*2)
        y1 = int(HEIGHT*2)
        print("Missed")

xr = 5
yr = 5
x1 = int(WIDTH*2)
y1 = int(HEIGHT*2)
x2 = int(WIDTH*2)
y2 = int(HEIGHT*2)

place_apple()
place_orange()
place_pineapple()
pgzrun.go()
