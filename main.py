import pygame
import random
import math

pygame.init()

#Screen making (Also called the surface of the game)
screen = pygame.display.set_mode((800, 600))

#Seting Title 
pygame.display.set_caption("Space Invaders")

#Setting Icon
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#Background Image
background = pygame.image.load('background.png')

#Setting Player
playerImg = pygame.image.load('Space_Shooter.png')
PlayerX = 370
PlayerY = 480
Player_x_Change = 0
Player_y_Change = 0

#Setting Monster
monsterImg = pygame.image.load('monster.png')
monsterX = random.randint(0, 735)
monsterY = random.randint(50, 150)
monster_x_Change = 3
monster_y_Change = 40

#Setting Bullet
bulletImg = pygame.image.load('bullet (1).png')
bulletX = 370
bulletY = 480
bullet_x_Change = 0
bullet_y_Change = 5
bullet_state = "ready" #Ready - You can't see the bullet on the screen, Fire - The bullet is currently moving

#Score
Score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

global  isGameOver
isGameOver = False

Close_program = False
def show_score(x,y):
    score = font.render("Score : " + str(Score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))

def player(x,y):
    screen.blit(playerImg, (x, y))

def monster(x,y):
    screen.blit(monsterImg, (x, y))

def Fire_bullet(x,y):
    global bullet_state
    screen.blit(bulletImg, (x + 16, y - 30))

def isCollision(monsterX, monsterY, bulletX, bulletY):
    distance = math.sqrt(math.pow((monsterX)- bulletX, 2) + (math.pow((monsterY + 16) - bulletY, 2)))   
    if distance < 40:
        return True
    else:
        return False
def Game_Over():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))
    score = font.render("Score : " + str(Score_value), True, (255, 0, 0))
    screen.blit(score, (300, 325))

#Game Loop
running = True
while running:
    # Setting Background Color
    # Color = RGB
    screen.fill((0, 0, 0))
    # Blit the background image
    screen.blit(background, (0, 0))

    # Event Handling this function will call the events from the logs and put them in event variable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            Close_program = True
            break

        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player_x_Change = -5
                
            if event.key == pygame.K_RIGHT:
                Player_x_Change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = PlayerX
                    bullet_state = "Fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player_x_Change = 0

    if Close_program:
        break
    
    #Player Movement Logic
    if isGameOver == False:
        PlayerX += Player_x_Change
    if PlayerX <= 0 and isGameOver == False:
        PlayerX = 0
    elif PlayerX >= 736 and isGameOver == False:
        PlayerX = 736

    #Monster Movement Logic
    if isGameOver == False:
        monsterX += monster_x_Change
    if monsterX <= 0 and isGameOver == False:
        monsterX = 0
        monster_x_Change = 3
        monsterY += monster_y_Change
    elif monsterX >= 736 and isGameOver == False:
        monsterX = 736
        monster_x_Change = -3
        monsterY += monster_y_Change
    Distance1 = math.sqrt(math.pow((monsterX)- PlayerX, 2) + (math.pow((monsterY + 16) - PlayerY, 2)))    
    if monsterY >= 440 and Distance1 < 50:
        Game_Over()
        isGameOver = True
    #Bullet Movement Logic
    if bullet_state == "Fire" and isGameOver == False:
        Fire_bullet(bulletX, bulletY)
        bulletY -= bullet_y_Change
    if bulletY <= 0 and isGameOver == False:
        bulletY = 480
        bullet_state = "ready"

    #Collision Logic
    collision = isCollision(monsterX, monsterY, bulletX, bulletY)
    if collision and isGameOver == False and bullet_state == "Fire":
        bulletY = 480
        bullet_state = "ready"
        monsterX = random.randint(0, 735)
        monsterY = random.randint(50, 150)
        Score_value += 1

    # Calling the player function to draw the player on the screen
    if isGameOver == False:
        player(PlayerX, PlayerY)
    # Calling the monster function to draw the monster on the screen
    if isGameOver == False:
        monster(monsterX, monsterY)
    # Calling the show_score function to display the score
    if isGameOver == False:
        show_score(textX, textY)
    pygame.display.update()
