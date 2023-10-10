import pygame, random

#Initialize Pygame
pygame.init()

#Intialize screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Title and Icon
pygame.display.set_caption("JETPACK")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Set for background
background = pygame.image.load('forest.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
back_rect = background.get_rect()

#Draw background
bg_x_1 = 0
bg_x_2 = background.get_width()
bg_y = 0

#Manage fps
clock = pygame.time.Clock()
fps = 60

#Speed of background
speed = 2.5
game_loop = True

#Setting up the girlgun
girlgun = pygame.image.load('girlgun.png')
girlgun = pygame.transform.scale(girlgun, (girlgun.get_width() * 0.5, girlgun.get_height() * 0.5))
girlgun_x = 100
girlgun_y = SCREEN_HEIGHT / 2.5
girlgun_x_change = 0
print(girlgun.get_width())
print(girlgun.get_height())

#Setting up bullets
bullets = []
bullet_delay_ms = 300
last_bullet_time = 0
bullet_image = pygame.image.load('greenbullet.png')
bullet_image = pygame.transform.scale(bullet_image, (bullet_image.get_width() * 0.05, bullet_image.get_height() * 0.05))

#Setting up Enemy
enemy_image = pygame.image.load('enemy.png')
enemy_image = pygame.transform.scale(enemy_image, (enemy_image.get_width() * 0.25, enemy_image.get_height() * 0.25))
enemy_x = random.randint(800, 1000)
enemy_y = random.randint(0, 500)

#Setting up scores
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 20
textY = 20

def show_score(x, y):
    global score_value
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def enemy_respawn():
    global enemy_x
    global enemy_y
    enemy_x = random.randint(800, 1000)
    enemy_y = random.randint(0, 500)
    
def enemy (x, y):
    global score_value
    screen.blit(enemy_image,(x, y))

    #BULLETS
    for bullet in bullets:
        screen.blit(bullet_image, pygame.Rect(bullet[0], bullet[1], bullet_image.get_width(), bullet_image.get_height()))

    for bullet in bullets:
        bullet[0] += 15

        temp_bullet_x = bullet[0]
        temp_bullet_y = bullet[1]

        # HIT
        if temp_bullet_x >= enemy_x and \
                temp_bullet_y >= enemy_y and \
                    temp_bullet_y <= enemy_y + enemy_image.get_height():
            bullets.remove(bullet)
            enemy_respawn()
            score_value += 1
              
    for bullet in bullets:
        if bullet[0] < 0:
            bullets.remove(bullet)

#GAME LOOP
while game_loop:
    clock.tick(fps)

#ANIMATE
    bg_x_1 = bg_x_1 - speed
    bg_x_2 = bg_x_2 - speed

#Reset position kapag yung x ay lagpas
    if bg_x_1 < background.get_width() * -1:
        bg_x_1 = background.get_width()
    if bg_x_2 < background.get_width() * -1:
        bg_x_2 = background.get_width()
    screen.blit(background, (bg_x_1, bg_y))
    screen.blit(background, (bg_x_2, bg_y))
    screen.blit(girlgun, (girlgun_x, girlgun_y))

#GIRLGUN SCREEN BOUNDERY
    print("girlgun: {}, {}".format(girlgun_x, girlgun_y))

    if girlgun_x <= 0:
        girlgun_x = 0
    elif girlgun_x >= 670:
        girlgun_x = 670 

    if girlgun_y <= 0:
        girlgun_y = 0
    elif girlgun_y >= 600:
        girlgun_y = 600

#ENEMIES
    enemy(enemy_x, enemy_y)
     
#PRINT SCORE
    show_score(textX, textY)

#PLAYER CONTROLS
    movement_speed = 7
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        girlgun_y = girlgun_y - movement_speed
    if keys[pygame.K_DOWN]:
        girlgun_y = girlgun_y + movement_speed
    if keys[pygame.K_LEFT]:
        girlgun_x = girlgun_x - movement_speed
    if keys[pygame.K_RIGHT]:
        girlgun_x = girlgun_x + movement_speed
    if keys[pygame.K_SPACE]:
        now = pygame.time.get_ticks()
        if now - last_bullet_time >= bullet_delay_ms:
            last_bullet_time = now
            bullets.append([girlgun_x + girlgun.get_width(), girlgun_y + girlgun.get_height() / 2 - bullet_image.get_height() / 2 + 7])

    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            game_loop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                game_loop = False
    
    pygame.display.update()