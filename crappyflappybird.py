import pygame
import random
import time
#12/15/2018  
#just like the classic flappybird game, but shittier -Dylan Andres
'''SPACEBAR to jump, LCTRL to drop, R to reset'''
pygame.init()

winx, winy = 1380, 350 #DESKTOP: 1380 // LAPTOP: 1080
window = pygame.display.set_mode((winx, winy))
pygame.display.set_caption("Crappy Flappy Bird")

birdx, birdy = 50, 175 #starting position
birdxvel = 3 #speed
birdyvel = -3 #gravity
refresh = 100

#colors
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 191, 255)
black = (0, 0, 0)
white = (255, 255, 255)

#music/sounds
jumpsound = pygame.mixer.Sound("mario.wav")
jumpsound.set_volume(0.25)
coinsound = pygame.mixer.Sound("coin.wav")
pygame.mixer.music.load("pkmn.wav")
pygame.mixer.music.play(-1)

running = True
score = 0
while running:
    print("X:", birdx, "   ", "Y:", birdy, "   ", "Score:", score) #coord test
    pygame.time.delay(refresh)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #keystroke
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(jumpsound)
                birdy = newy - 10
            if event.key == pygame.K_LCTRL:
                birdy = newy + 2
            if event.key == ord('r'):
                birdx, birdy = 50, 175
                score = 0
        if event.type == pygame.QUIT:
            running = False

    #score counter
    for border in range(115, winx, 100): #middle of each pipe
        if birdx == border or birdx - 1 == border or birdx + 1 == border:
            pygame.mixer.Sound.play(coinsound)
            score += 1

    #bird render
    pygame.draw.circle(window, yellow, (birdx, birdy), 7, 0)
    pygame.display.update()
    window.fill(blue)
    #bird physics
    birdx += birdxvel
    birdy -= birdyvel
    newx, newy = birdx, birdy
    #bounds
    if birdy - 7 <= 0:
        birdy = 7
    if birdy + 7 >= winy:
        birdx, birdy = 50, 175
        score = 0
    if birdx + 7 >= winx: #end
        birdx, birdy = 50, 175
        running = False
    #pipe render 
    class Pipe:
        def __init__(self, x, y, width, length):
            self.x = x
            self.y = y
            self.w = width
            self.L= length
#                 x    y  wid len        x    y    wid  len
    p1, p2 = Pipe(100, 0, 30, 100), Pipe(100, 350, 30, -150)
    p3, p4 = Pipe(200, 0, 30, 200), Pipe(200, 350, 30, -100)
    p5, p6 = Pipe(300, 0, 30, 100), Pipe(300, 350, 30, -200)
    p7, p8 = Pipe(400, 0, 30, 110), Pipe(400, 350, 30, -210)
    p9, p10 = Pipe(500, 0, 30, 20), Pipe(500, 350, 30, -300)
    p11, p12 = Pipe(600, 0, 30, 100), Pipe(600, 350, 30, -150)
    p13, p14 = Pipe(700, 0, 30, 200), Pipe(700, 350, 30, -100)
    p15, p16 = Pipe(800, 0, 30, 100), Pipe(800, 350, 30, -200)
    p17, p18 = Pipe(900, 0, 30, 110), Pipe(900, 350, 30, -220)
    p19, p20 = Pipe(1000, 0, 30, 20), Pipe(1000, 350, 30, -300)
    p21, p22 = Pipe(1100, 0, 30, 100), Pipe(1100, 350, 30, -150)
    p23, p24 = Pipe(1200, 0, 30, 200), Pipe(1200, 350, 30, -100)
    p25, p26 = Pipe(1300, 0, 30, 100), Pipe(1300, 350, 30, -200)
    pygame.draw.rect(window, green, (p1.x, p1.y, p1.w, p1.L), 0)
    pygame.draw.rect(window, green, (p2.x, p2.y, p2.w, p2.L), 0)
    pygame.draw.rect(window, green, (p3.x, p3.y, p3.w, p3.L), 0)
    pygame.draw.rect(window, green, (p4.x, p4.y, p4.w, p4.L), 0)
    pygame.draw.rect(window, green, (p5.x, p5.y, p5.w, p5.L), 0)
    pygame.draw.rect(window, green, (p6.x, p6.y, p6.w, p6.L), 0)
    pygame.draw.rect(window, green, (p7.x, p7.y, p7.w, p7.L), 0)
    pygame.draw.rect(window, green, (p8.x, p8.y, p8.w, p8.L), 0)
    pygame.draw.rect(window, green, (p9.x, p9.y, p9.w, p9.L), 0)
    pygame.draw.rect(window, green, (p10.x, p10.y, p10.w, p10.L), 0)
    pygame.draw.rect(window, green, (p11.x, p11.y, p11.w, p11.L), 0)
    pygame.draw.rect(window, green, (p12.x, p12.y, p12.w, p12.L), 0)
    pygame.draw.rect(window, green, (p13.x, p13.y, p13.w, p13.L), 0)
    pygame.draw.rect(window, green, (p14.x, p14.y, p14.w, p14.L), 0)
    pygame.draw.rect(window, green, (p15.x, p15.y, p15.w, p15.L), 0)
    pygame.draw.rect(window, green, (p16.x, p16.y, p16.w, p16.L), 0)
    pygame.draw.rect(window, green, (p17.x, p17.y, p17.w, p17.L), 0)
    pygame.draw.rect(window, green, (p18.x, p18.y, p18.w, p18.L), 0)
    pygame.draw.rect(window, green, (p19.x, p19.y, p19.w, p19.L), 0)
    pygame.draw.rect(window, green, (p20.x, p20.y, p20.w, p20.L), 0)
    pygame.draw.rect(window, green, (p21.x, p21.y, p21.w, p21.L), 0)
    pygame.draw.rect(window, green, (p22.x, p22.y, p22.w, p22.L), 0)
    pygame.draw.rect(window, green, (p23.x, p23.y, p23.w, p23.L), 0)
    pygame.draw.rect(window, green, (p24.x, p24.y, p24.w, p24.L), 0)
    pygame.draw.rect(window, green, (p25.x, p25.y, p25.w, p25.L), 0)
    pygame.draw.rect(window, green, (p26.x, p26.y, p26.w, p26.L), 0)


print("Thanks for playing!")
pygame.quit()
