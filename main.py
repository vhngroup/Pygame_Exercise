import pygame
import random
pygame.init()

HEIGHT = 650
WIDTH = 480
BLACK = (0,0,0)
WHITE = (255,255,255)

LIVES_STARTING = 5 #Number max of lives
PLAYER_VELOCITY = 15 #Velocity of the player reaction
MASK_STARTINT_VELOCITY = 5 #Velocity of the enemy reaction
MASK_ACCELERATION = 0.5 #Acceleration of the enemy reaction increment

score = 0 #Zero score
player_lives = LIVES_STARTING #Number of lives start
mask_velocity = MASK_STARTINT_VELOCITY # Velocity of the enemy reaction start


player_image = pygame.image.load("./images/et_hand.png") #load the image of the player
player_rect = player_image.get_rect() #get the minimum rectangle that contains the image
player_rect.center = (WIDTH/2, HEIGHT*0.8) #center the player in the screen (center of the screen)

mask_image = pygame.image.load("./images/mask.png") #load the image of the player
mask_rect = mask_image.get_rect() #get the minimum rectangle that contains the image
#mask_rect.center = (WIDTH//2, HEIGHT//2) #center the player in the screen (center of the screen)
mask_rect.left = 10
mask_rect.bottom = HEIGHT - 10  

#call fonts
font_title_32 = pygame.font.Font("./fonts/Creepster-Regular.ttf", 32)
font_title_42 = pygame.font.Font("./fonts/Creepster-Regular.ttf", 42)
font_text = pygame.font.Font("./fonts/Outfit-Black.ttf", 20)

title_text = font_title_42.render("Marcianitos", True, WHITE, BLACK)
title_rect = title_text.get_rect()
title_rect.center = (WIDTH//2, HEIGHT//2)
title_rect.y = 15

lives_text = font_text.render(f"Lives: {player_lives}", True, WHITE, BLACK)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WIDTH-10, 90)


score_text = font_text.render(f"Score: {score}", True, WHITE, BLACK)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 98)

continue_game = font_title_32.render("Presiona cualquier tecla para continuar", True, WHITE, BLACK)
continue_rect = continue_game.get_rect()
continue_rect.center = (WIDTH//2, HEIGHT//2 + 60)

gameover_title = font_title_42.render("Game Over", True, WHITE, BLACK)
gameover_rect = gameover_title.get_rect()
gameover_rect.center = (WIDTH//2, HEIGHT//2)

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Marcianitos")
FPS=60
clock = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get(): #Catch events
        if event.type == pygame.QUIT: #If user close the window
            game_over = True
    
    #Event Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_VELOCITY
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_VELOCITY
    
    if mask_rect.y > HEIGHT:
        player_lives -= 1 #Effect down enemy
        mask_rect.x = random.randint(0, WIDTH - 64)
        mask_rect.y = 140
    else:
        mask_rect.y += mask_velocity #If enemy is down, increase the enemy velocity
    
    if player_rect.colliderect(mask_rect):
        score += 1 #If the player collide with the enemy, increase the score
        mask_velocity += MASK_ACCELERATION #Increase the enemy velocity
        mask_rect.x = random.randint(0, WIDTH - 64)
        mask_rect.y = 140

    #Update text
    score_text = font_text.render(f"Score: {score}", True, WHITE, BLACK)
    lives_text = font_text.render(f"Lives: {player_lives}", True, WHITE, BLACK)

    if player_lives == 0:
        display.blit(gameover_title, gameover_rect)
        display.blit(continue_game, continue_rect)
        pygame.display.update()
        is_pause = True
        while is_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    is_pause = False
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = LIVES_STARTING
                    mask_velocity = MASK_STARTINT_VELOCITY
                    is_pause = False

    display.fill(BLACK) #Fill the screen with black
    display.blit(title_text, title_rect) #Draw the score
    display.blit(lives_text, lives_rect) #Draw the score
    display.blit(score_text, score_rect) #Draw the score
    pygame.draw.line(display, WHITE, (0,140), (WIDTH, 140), 3) #Draw the player
    display.blit(player_image, player_rect) #Draw the player
    display.blit(mask_image, mask_rect) #Draw the player

    pygame.display.update() #Update the screen
    clock.tick(FPS) #Update the clock, block the overclock
    
