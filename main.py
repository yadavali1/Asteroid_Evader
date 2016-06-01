import pygame
import random
import inputbox
pygame.init()
pygame.mixer.init()

# All Global Variables Are Declared Below This Line
display_width = 800
display_height = 600


# Colors Declaration
white = (255,255,255)
black = (0,0,0)
red = (223,0,0)
pink = (189,15,224)
orange = (255,137,0)
amber = (247,218,0)
blue = (77,215,250,0)
dark_blue = (182, 239, 252)
green = (0, 216, 29)

# Creating window for gaming screen & Caption
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Asteroid Evader')
#frames per second
fps = pygame.time.Clock()
background = pygame.Surface(gameDisplay.get_size())
#Convert to color maps
background = background.convert()

# Backgrounds & Game Screen
intro_screen = pygame.image.load('screens/Intro Screen.jpg')
menu_screen = pygame.image.load('screens/menu_screen.png')
how_to_screen = pygame.image.load('screens/how_to_play.png')
gaming_screen = pygame.image.load('screens/gaming_screen.png')
gender_select = pygame.image.load('screens/gender_select.png')
character_maleimg = pygame.image.load('screens/character_male.png')
character_femaleimg = pygame.image.load('screens/character_female.png')
highscore_screen = pygame.image.load('screens/highscore.png')
dashboard = pygame.image.load('screens/dashboard.png')
name_screen = pygame.image.load('screens/name_select.png')
settings_screen = pygame.image.load('screens/settings.png')
gameover_screen = pygame.image.load('screens/Game_screen.png')
paused_screen = pygame.image.load('screens/Paused_screen.png')
#SpaceShips
spaceship1 = pygame.image.load('assets/spaceships/ship1.png')
spaceship2 = pygame.image.load('assets/spaceships/ship2.png')
spaceship3 = pygame.image.load('assets/spaceships/ship3.png')
spaceship4 = pygame.image.load('assets/spaceships/ship4.png')

#rock
asteroid = pygame.image.load('assets/rocks/a.png')
#mines
mine1 = pygame.image.load('assets/mine/mine1.png')
mine2 = pygame.image.load('assets/mine/mine2.png')
mine3 = pygame.image.load('assets/mine/mine3.png')

#explosion
explosion1 = pygame.image.load('assets/explosions/1.png')

# List of Music Files
intro_music = pygame.mixer.Sound('music/intro_music.wav')
menu_music = pygame.mixer.Sound('music/menu_music.wav')
gaming_music = pygame.mixer.Sound('music/gaming.wav')

#icons
settings_icon = pygame.image.load('assets/icons/settings.png')
back_icon = pygame.image.load('assets/icons/back.png')
# fx sounds
pressed_buttons = pygame.mixer.Sound('fx/page.wav')
crashed = pygame.mixer.Sound('fx/crash.wav')

#powerups
health_powerup = pygame.image.load('assets/powerups/health.png')
username = None


#Character - Males
character_1 = pygame.image.load('assets/avatar/char_1.png')
character_2 = pygame.image.load('assets/avatar/char_2.png')
character_3 = pygame.image.load('assets/avatar/char_3.png')

#Character - Females
character_4 = pygame.image.load('assets/avatar/char_4.png')
character_5 = pygame.image.load('assets/avatar/char_5.png')
character_6 = pygame.image.load('assets/avatar/char_6.png')

# Global variables for running functions
character_img = None
run_settings = False
how_to_play = False
paused = False
running = False

#Stops the pause function from running
def unpause():
    global paused
    paused = False
#Stops the high score function from running
def not_highscore():
    global running
    running = False
#Stops the how to play function from running
def how_to_play_none():
    global how_to_play
    how_to_play = False
#Stops the settings function from running
def not_settings():
    global run_settings
    run_settings = False
# ------- Start Of Actual Programming ------

#Displays the intro screen
def introScreen(image,x,y): # allows for any the placement of any background images
    done = True
    if done:
        for i in range(255):
            background.fill(black)
            image.set_alpha(i)
            gameDisplay.blit(image,(0,0))
            pygame.display.flip()
            pygame.time.delay(10)
        for i in range(255):
            background.fill(black)
            background.set_alpha(i)
            gameDisplay.blit(background,(0,0))
            pygame.display.flip()
            pygame.time.delay(10)


def display_screen(image,x,y): # allows for any the placement of any background images
    gameDisplay.blit(image,(0,0))

#Displays the text onto the screen
def texts(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Create buttons and makes them clickable
def buttons(text,x,y,width,height,inactive,active,text_size, action=None):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(gameDisplay, active,(x,y,width,height))

        if click[0] == 1 and action is not None:
            pressed_buttons.play()
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x,y,width,height))

    buttonText = pygame.font.Font('fonts/Montserrat-Hairline.otf',text_size)
    textSurf, textRect = texts(text, buttonText)
    textRect.center = ( (x+(width/2)) , (y +(height/2)) )
    gameDisplay.blit(textSurf, textRect)

#Displays the main menu screen
def main_menu():
    pygame.time.delay(100)
    menu = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19
    while menu:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display_screen(menu_screen,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)

        star_Y += 35
        star_Y2 += 35

        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)

        buttons('START GAME', 293, 340, 212, 52, blue, white,14, gender_screen)
        buttons('HOW TO PLAY', 293, 405, 213, 52, blue, white,14, how_play)
        buttons('HIGHSCORES', 293, 469, 213, 52, blue, white,14, highscore_select)
        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        pygame.display.update()
        fps.tick(60)

#Displays the paused screen

def pausedd():
    pygame.time.delay(100)
    global paused
    paused = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19
    while paused:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display_screen(paused_screen,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)

        star_Y += 35
        star_Y2 += 35

        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)

        buttons('Resume Game', 293, 340, 212, 52, blue, white,14, unpause)
        buttons('HOW TO PLAY', 293, 405, 213, 52, blue, white,14, how_play)
        buttons('HIGHSCORES', 293, 469, 213, 52, blue, white,14, highscore_select)
        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        pygame.display.update()
        fps.tick(60)

#Displays the how to play screen

def how_play():
    pygame.time.delay(100)
    global how_to_play
    how_to_play = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19

    while how_to_play:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_screen(how_to_screen,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)

        star_Y += 35
        star_Y2 += 35

        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)

        buttons('', 0, 0, 40, 38, blue, white,14, how_to_play_none)
        gameDisplay.blit(back_icon,(10,10))

        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        pygame.display.update()
        fps.tick(60)

#Displays the gender screen

def gender_screen():
    pygame.time.delay(100)
    gender = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 3
    star_height2 = 19

    while gender:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_screen(gender_select,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,pink)

        star_Y += 35
        star_Y2 += 35

        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)

        buttons('MALE', 126, 300, 203, 64, blue, white, 15, character_male)
        buttons('FEMALE', 494, 300, 203, 64, blue, white, 15,character_female)
        buttons('', 0, 0, 40, 38, blue, white,14, main_menu)
        gameDisplay.blit(back_icon,(10,10))

        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        pygame.display.update()
        fps.tick(60)

#Displays the name selection screen

def name_selection():
    pygame.time.delay(50)
    display_screen(name_screen,0,0)
    buttons('', 0, 0, 40, 38, blue, white,14, main_menu)
    gameDisplay.blit(back_icon,(10,10))

    buttons('', 760, 0, 40, 38, blue, white,14, settings)
    gameDisplay.blit(settings_icon,(772,10))
    global username
    username = inputbox.ask(gameDisplay, '')
    pygame.display.update()

#Displays the character male screen
def character_male():
    pygame.time.delay(100)
    selection = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19
    while selection:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_screen(character_maleimg,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)

        star_Y += 35
        star_Y2 += 35

        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)

        buttons('CHOOSE ME', 127, 357, 134, 36, blue, dark_blue, 12, char_1)
        buttons('CHOOSE ME', 333, 359, 134, 36, blue, dark_blue, 12, char_2)
        buttons('CHOOSE ME', 539, 357, 134, 36, blue, dark_blue, 12, char_3)
        buttons('', 0, 0, 40, 38, blue, white,14, gender_screen)
        gameDisplay.blit(back_icon,(10,10))

        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        pygame.display.update()
        fps.tick(60)

#Displays the character_female screen
def character_female():
    pygame.time.delay(100)
    selection = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19
    while selection:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_screen(character_femaleimg,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)

        star_Y += 35
        star_Y2 += 35

        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)

        buttons('CHOOSE ME', 127, 357, 134, 36, blue, dark_blue, 12, char_4)
        buttons('CHOOSE ME', 333, 359, 134, 36, blue, dark_blue, 12, char_5)
        buttons('CHOOSE ME', 539, 357, 134, 36, blue, dark_blue, 12, char_6)
        buttons('', 0, 0, 40, 38, blue, white,14, gender_screen)
        gameDisplay.blit(back_icon,(10,10))

        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        pygame.display.update()
        fps.tick(60)

#Displays the high score screen

def highscore_select():
    pygame.time.delay(100)
    global running
    running = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19

    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_screen(highscore_screen,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)
        star_Y += 35
        star_Y2 += 35
        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)
        buttons('', 0, 0, 40, 38, blue, white,14, not_highscore)
        gameDisplay.blit(back_icon,(10,10))

        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        pygame.display.update()
        fps.tick(60)

#Displays every function below is to change the current character image.
def char_1():
    global character_img
    character_img = character_1
    game()
def char_2():
    global character_img
    character_img = character_2
    game()
def char_3():
    global character_img
    character_img = character_3
    game()
def char_4():
    global character_img
    character_img = character_4
    game()
def char_5():
    global character_img
    character_img = character_5
    game()
def char_6():
    global character_img
    character_img = character_6
    game()

#Displays the soaceship
def spaceship(spaceship,x,y):
    height = 32
    width = 32
    gameDisplay.blit(spaceship,(x,y),(random.randrange(0,4) * width, 0, width, height))

#Displays the settings screen

def settings():
    global run_settings
    run_settings = True
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20
    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19
    while run_settings:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_screen(settings_screen,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)
        star_Y += 35
        star_Y2 += 35
        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)
        buttons('Sound OFF', 400, 206, 100, 36, blue, dark_blue, 12, sound_off)
        buttons('Sound ON', 500, 206, 100, 36, blue, dark_blue, 12, sound_on)
        buttons('Visit Website', 400, 280, 150, 36, blue, dark_blue, 12, sound_on)
        buttons('', 0, 0, 40, 38, blue, white,14, not_settings)
        gameDisplay.blit(back_icon,(10,10))
        pygame.display.update()
        fps.tick(60)

#Displays the game over screen

def game_over():
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20
    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19
    game_overver = True
    while game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_screen(gameover_screen,0,0)
        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)
        star_Y += 35
        star_Y2 += 35
        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X2 = random.randrange(0,display_width)
        buttons('Back To Main Menu', 295, 383, 212, 52, blue, white,14, main_menu)
        pygame.display.update()
        fps.tick(60)

#Switches on sound

def sound_on():
    intro_music.stop()
    menu_music.play()
    gaming_music.stop()

#Switches off sound
def sound_off():
    intro_music.stop()
    menu_music.stop()
    gaming_music.stop()

#Displays obstacles
def obstacle(obstacle,obx,oby):
    gameDisplay.blit(obstacle,(obx,oby))

def highscore(score):
    font = pygame.font.Font('fonts/Montserrat-Regular.otf', 15)
    text = font.render(str(score), True, white)

    if score < 1:
        gameDisplay.blit(text,(395,40))
    if score < 10 and score > 1:
        gameDisplay.blit(text,(395,40))
    if score > 10 and score < 100:
        gameDisplay.blit(text,(390,40))
    if score > 100 and score < 1000:
        gameDisplay.blit(text,(385,40))
    if score > 1000 and score < 10000:
        gameDisplay.blit(text,(380,40))

def character(image,name,health,color):
    font = pygame.font.Font('fonts/Montserrat-Hairline.otf', 15)
    text = font.render(str(name), True, white)
    score = font.render(('SCORE'), True, white)
    if health > 60:
        color = green
    if health <= 60 and health > 30:
        color = amber
    if health <= 30:
        color = red
    if health >= 100:
        health = 100
    if health <= 0:
        health = 0
    text2 = font.render(str(health) + ' %', True, color)
    gameDisplay.blit(text,(65,9))
    gameDisplay.blit(score, (370,8))
    gameDisplay.blit(text2,(255,9))
    gameDisplay.blit(image,(10,4))


def star(star_X, star_Y, start_Width, star_Height, color):
    pygame.draw.rect(gameDisplay, color, [star_X, star_Y, start_Width, star_Height])

def game():
    name_selection()
    menu_music.stop()
    gaming_music.play(-1)
    x = 384
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    EXIT = False
    begin = False
    paused = False
    score = 0

    #Mine1
    mine1_x = random.randrange(0,display_width)
    mine1_y = -3200
    mine1_speed = 4

    #Mine2
    mine2_x = random.randrange(0,display_width)
    mine2_y = -3900
    mine2_speed = 5

    #Mine3
    mine3_x = random.randrange(0,display_width)
    mine3_y = -4100
    mine3_speed = 7

    #star 1
    star_X = random.randrange(0,display_width)
    star_Y = - 349
    star_width = 2
    star_height = 20

    #star 2
    star_X2 = random.randrange(0,display_width)
    star_Y2 = - 500
    star_width2 = 1
    star_height2 = 19

    #star 3
    star_X3 = random.randrange(0,display_width)
    star_Y3 = - 154
    star_width3 = 3
    star_height3 = 10

    #star 4
    star_X4 = random.randrange(0,display_width)
    star_Y4 = - 590
    star_width4 = 1
    star_height4 = 15


    asteroid_X = 900
    asteroid_Y = random.randrange(0,display_height - 133)

    # Character

    # Character - Health
    health = 100
    health_x = random.randrange(0,display_width)
    health_y = random.randrange(3000, 10000)
    health_y = health_y * -1

    while not EXIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y_change = 1
                if event.key == pygame.K_p:
                    pausedd()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_s or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0


        x += x_change
        y += y_change


        print(y)

        if begin == False:
            y -= 1
            if y < 400:
                y += y_change
                begin = True



        display_screen(gaming_screen, x,y)

        if x > display_width - 32 or x < 0:
            x_change = 0

        if y > display_height - 64:
            y_change = -1
        if y < 90:
            y_change = 1

        if y < mine1_y + 48 and y > mine1_y - 48:
            print ('Ship has crossed the Mines In Y')
            if x > mine1_x and x < mine1_x + 48 or x + 32 > mine1_x and x + 32 < mine1_x + 32:
                crashed.play()
                explosion(explosion1, x, y)
                mine1_y = - 900
                mine1_x = random.randrange(0,display_width)
                mine1_speed += 0.2
                mine1_y += mine1_speed
                score -= 15
                health = health - 3

        if y < mine2_y + 48 and y > mine2_y - 48:
            print ('Ship has crossed the Mines In Y')
            if x > mine2_x and x < mine2_x + 48 or x + 32 > mine2_x and x + 32 < mine2_x + 32:
                crashed.play()
                mine2_y = - 900
                mine2_x = random.randrange(0,display_width)
                mine2_speed += 0.2
                mine2_y += mine2_speed
                score -= 25
                health = health - 5

        if y < mine3_y + 48 and y > mine3_y - 48:
            print ('Ship has crossed the Mines In Y')
            if x > mine3_x and x < mine3_x + 48 or x + 32 > mine3_x and x + 32 < mine3_x + 32:
                crashed.play()
                mine3_y = - 900
                mine3_x = random.randrange(0,display_width)
                mine3_speed += 0.2
                mine3_y += mine3_speed
                score += 5
                health = health - 1

        spaceship(spaceship4,x,y)




        obstacle(mine1,mine1_x,mine1_y)
        obstacle(mine2,mine2_x,mine2_y)
        obstacle(mine3,mine3_x,mine3_y)

        mine1_y += mine1_speed
        mine2_y += mine2_speed
        mine3_y += mine3_speed
        if mine1_y > display_height:
            mine1_y = - 900
            mine1_x = random.randrange(0,display_width)
            mine1_speed += 0.1
            mine1_y += mine1_speed
            score += 15


        if mine2_y > display_height:
            mine2_y = - 500
            mine2_x = random.randrange(0,display_width)
            mine2_speed += 0.1
            mine2_y += mine2_speed
            score += 15

        if mine3_y > display_height:
            mine3_y = - 500
            mine3_x = random.randrange(0,display_width)
            mine3_speed += 0.1
            mine3_y += mine3_speed
            score += 15


        star(star_X,star_Y,star_width,star_height,blue)
        star(star_X2,star_Y2,star_width2,star_height2,blue)
        star(star_X3,star_Y3,star_width3,star_height3,blue)
        star(star_X4,star_Y4,star_width4,star_height4,blue)

        star_Y += 25
        star_Y2 += 25
        star_Y3 += 25
        star_Y4 += 25

        if star_Y > display_height:
            star_Y = -50
            star_X = random.randrange(0,display_width)
        if star_Y2 > display_height:
            star_Y2 = -150
            star_X = random.randrange(0,display_width)
        if star_Y3 > display_height:
            star_Y3 = -200
            star_X3 = random.randrange(0,display_width)
        if star_Y4 > display_height:
            star_Y4 = -300
            star_X4 = random.randrange(0,display_width)

        if score >= 500:
           obstacle(asteroid,asteroid_X,asteroid_Y)
           asteroid_X -= 6
           if y < asteroid_Y + 114 and y > asteroid_Y - 114:
               if x > asteroid_X and x < asteroid_X + 42 or x + 32 > asteroid_X and x + 32 < asteroid_X + 32:
                    crashed.play()
                    asteroid_X = random.randint(display_width,1000)
                    asteroid_Y = random.randrange(0,display_height-133)
                    health = health - 25
           elif asteroid_X <= 0 - 133:
            asteroid_X = random.randint(display_width,1000)
            asteroid_Y = random.randrange(0,display_height-133)


        obstacle(health_powerup,health_x,health_y)
        health_y += 5
        if y < health_y + 42 and y > health_y - 42:
            if x > health_x and x < health_x + 42 or x + 32 > health_x and x + 32 < health_x + 32:
                health_y = random.randrange(10000, 50000)
                health_y = health_y * -1
                health_x = random.randrange(0,display_width-32)
                health = health + 25

        display_screen(dashboard,0,0)
        character(character_img, (username[0].upper()+username[1:]),health, None)
        buttons('', 760, 0, 40, 38, blue, white,14, settings)
        gameDisplay.blit(settings_icon,(772,10))
        highscore(score)
        if score < 1:
            score = 0
        if health <= 0:
            game_over()
        pygame.display.update()

        fps.tick(60)
introScreen(intro_screen,0,0)
menu_music.play(loops = -1)
main_menu()
pygame.quit()
quit()