import pygame
import random
import time
import gc

#12/15/2018  
#just like the classic flappybird game, but shittier -Dylan Andres
'''press SPACEBAR to jump, hold LCTRL to drop faster, press R to reset'''
pygame.init()

#window
winx, winy = 1080, 350
window = pygame.display.set_mode((winx, winy))
pygame.display.set_caption("Crappy Flappy Bird")
refresh = 100

#bird attributes
birdx, birdy = 7, 175 #starting position
birdxvel = 3 #speed
birdyvel = -3 #gravity
size = 7

#colors
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 191, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#music/sounds
jumpsound = pygame.mixer.Sound("mario.wav")
jumpsound.set_volume(0.25)
coinsound = pygame.mixer.Sound("coin.wav")
pygame.mixer.music.load("pkmn.wav")
pygame.mixer.music.play(-1)

#on-screen text
def message(text, color, size, x, y):
    font = pygame.font.SysFont(None, size)
    screentext = font.render(text, True, color)
    window.blit(screentext, (x, y))

#value init
score = 0
hiscore = 0
deaths = 0

#program START
running = True
while running:
    pygame.time.delay(refresh)
    for event in pygame.event.get():
        #key strokes
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(jumpsound)
                birdy = newy - 10
            if event.key == ord('r'):
                birdx, birdy = 7, 175
                score = 0
                hiscore = 0
                deaths = 0
        #close window
        if event.type == pygame.QUIT:
            if score > hiscore:
                hiscore = score
            running = False

    #key holds
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        birdy = newy +2

    #dev tool; reposition bird
    '''if pygame.mouse.get_pressed()[0]:
        birdx = pygame.mouse.get_pos()[0]
        birdy = pygame.mouse.get_pos()[1]'''

    #score counter
    for border in range(115, winx, 100): #middle of each pipe
        if birdx == border or birdx - 1 == border or birdx + 1 == border:
            pygame.mixer.Sound.play(coinsound)
            score += 1

    #text render
    message("Jump: SPACEBAR", black, 18, 5, 20)
    message("Drop: HOLD LCTRL", black, 18, 5, 30)
    message("Reset: R", black, 18, 5, 40)
    message("Dylan Andres 12/15/2018", black, 18, 5, winy - 20)
    w = "DEATHS: " + str(deaths)
    message(w, red, 22, 240,5)
    v = "HIGH-SCORE: " + str(hiscore)
    message(v, red, 22, 100, 5)
    t = "SCORE: " + str(score)
    message(t, red, 22, 5, 5)
    print("X:", birdx, "   ", "Y:", birdy, "   ", "Score:", score) #coord test

    #bird render
    pygame.draw.circle(window, yellow, (birdx, birdy), size, 0)
    pygame.display.update()
    window.fill(blue)

    #bird physics
    birdx += birdxvel
    birdy -= birdyvel
    newx, newy = birdx, birdy

    #bounds
    if birdy - size <= 0: #too high
        birdy = size
    if birdy + size >= winy: #too low; reset
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size >= winx: #end
        birdx = 7 #reset to beginning; keep same height
        
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
    p17, p18 = Pipe(900, 0, 30, 100), Pipe(900, 350, 30, -220)
    p19, p20 = Pipe(1000, 0, 30, 20), Pipe(1000, 350, 30, -300)
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

    #pipe collision; every 2 if statements is pair of pipes (top/bottom)
    if birdx + size > p1.x and birdx - size < (p1.x + p1.w) and birdy - size < p1.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p1.x and birdx - size < (p1.x + p1.w) and birdy + size > (p2.y + p2.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p3.x and birdx - size < (p3.x + p3.w) and birdy - size < p3.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p3.x and birdx - size < (p3.x + p3.w) and birdy + size > (p4.y + p4.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p5.x and birdx - size < (p5.x + p5.w) and birdy - size < p5.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p5.x and birdx - size < (p5.x + p5.w) and birdy + size > (p6.y + p6.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p7.x and birdx - size < (p7.x + p7.w) and birdy - size < p7.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p7.x and birdx - size < (p7.x + p7.w) and birdy + size > (p8.y + p8.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p9.x and birdx - size < (p9.x + p9.w) and birdy - size < p9.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p9.x and birdx - size < (p9.x + p9.w) and birdy + size > (p10.y + p10.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p11.x and birdx - size < (p11.x + p11.w) and birdy - size < p11.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p11.x and birdx - size < (p11.x + p11.w) and birdy + size > (p12.y + p12.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p13.x and birdx - size < (p13.x + p13.w) and birdy - size < p13.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p13.x and birdx - size < (p13.x + p13.w) and birdy + size > (p14.y + p14.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p15.x and birdx - size < (p15.x + p15.w) and birdy - size < p15.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p15.x and birdx - size < (p15.x + p15.w) and birdy + size > (p16.y + p16.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p17.x and birdx - size < (p17.x + p17.w) and birdy - size < p17.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p17.x and birdx - size < (p17.x + p17.w) and birdy + size > (p18.y + p18.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p19.x and birdx - size < (p19.x + p19.w) and birdy - size < p19.L:
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
    if birdx + size > p19.x and birdx - size < (p19.x + p19.w) and birdy + size > (p20.y + p20.L):
        birdx, birdy = 7, 175
        if score > hiscore:
            hiscore = score
        score = 0
        deaths += 1
   
#program END
print("\nThanks for playing!", "\nYour score was", score, "\nYour high-score was", hiscore, "\nYou died", deaths, "time(s)", "\n")
pygame.quit()
