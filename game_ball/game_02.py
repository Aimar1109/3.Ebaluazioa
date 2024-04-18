# AIMAR MARDONES AND UNAI ARCE

import pygame

pygame.init()

#SCREEN
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game 2")

# BALL
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

ballrect.move_ip(0, 0)

# PADDLE
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

baterect.move_ip(240, 450)

# INITIAL VARIABLES
running = True
game_state = False
speed = [4, 4]
score = 0
first = True

# MENU FUNCTION
def draw_menu(score):
    ventana.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    font1 = pygame.font.SysFont('arial', 60)

    # BALL GAME TITLE
    title1 = font1.render('BALL GAME', True, (255, 255, 255))
    ventana.blit(title1, (325 - title1.get_width()/2, 150 - title1.get_height()/2))

    # SCORE TITLE
    score_d = font.render('SCORE: '+ str(score), True, (255, 255, 255))
    ventana.blit(score_d, (325 - score_d.get_width()/2, 200 - score_d.get_height()/2))

    # START BUTTON
    start_button = font.render('Play', True, (255, 255, 255))
    start_button_rect = start_button.get_rect(center=(325, 300))
    ventana.blit(start_button, (325 - start_button.get_width()/2, 250 + start_button.get_height()/2))

    # QUIT BUTTON
    end_button = font.render('Quit', True, (255, 255, 255))
    end_button_rect = end_button.get_rect(center=(325, 400))
    ventana.blit(end_button, (325 - end_button.get_width()/2, 350 + end_button.get_height()/2))

    # UPDATE THE DISPLAY
    pygame.display.update()

    # RETURN BOTH BUTTTONS
    return start_button_rect, end_button_rect

# MAIN LOOP
while running:
    # GAME
    if game_state:
        # WALKING ALONG ALL THE EVENTS
        for event in pygame.event.get():
            # QUIT WHEN CLICK THE X
            if event.type == pygame.QUIT:
                running = False

        # SAVING THE PRESSED KEYS
        keys = pygame.key.get_pressed()

        # PADDLE MOVEMENT

        # TO THE LEFT
        if keys[pygame.K_LEFT]:
            # PREVENTING GOING OUT OF SCREEN
            if not baterect.left < 0:
                baterect = baterect.move(-5, 0)
        
        # TO THE RIGTH
        if keys[pygame.K_RIGHT]:
            # PREVENTING GOING OUT OF SCREEN
            if  baterect.right < ventana.get_width():
                baterect = baterect.move(5, 0)

        # MOVING THE BALL
        ballrect = ballrect.move(speed)

        # BALL COLLISIONS

        # COLLISION WITH BORDERS
        if ballrect.left < 0 or ballrect.right > ventana.get_width():
            speed[0] = -speed[0]
        # COLLISION WITH TOP
        if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
            speed[1] = -speed[1]
        # COLLISION WITH PADDLE
        if baterect.colliderect(ballrect):
            speed[1] = -speed[1]
            score += 1
            first = True
        # COLLISION WITH BOTTOM
        if ballrect.bottom >= ventana.get_height():
            game_state = False
        
        # SPEED UP EVERY 5
        if score in range(5, 1000, 5):
            if first:
                if speed[0] < 0:
                    speed[0] -= 1
                else:
                    speed[0] += 1

                if speed[1] < 0:
                    speed[1] -= 1
                else:
                    speed[1] += 1
                first = False

        # SCREEN BACKGROUND
        ventana.fill((252, 243, 207))

        # SCORE TITLE IN GAME
        font1 = pygame.font.SysFont('arial', 30)
        title1 = font1.render('SCORE: ' + str(score), True, (0, 0, 0))
        ventana.blit(title1, (70 - title1.get_width()/2, 20 - title1.get_height()/2))

        # DISPLAYING THE BALL AND THE BATE
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # MENU
    else:
        # SAVING THE MENU BUTTONS
        continue_button_rect, end_button_rect = draw_menu(score)
        # LOOP FOR EVENTS
        for event in pygame.event.get():
            # SAVING WERE IT IS CLICKED
            if event.type == pygame.MOUSEBUTTONDOWN:
                # IF PLAY
                if continue_button_rect.collidepoint(event.pos):
                    score = 0
                    ballrect.x = 0
                    ballrect.y = 0
                    speed = [4, 4]
                    game_state = True
                    velocidad = 3
                # IF QUIT
                elif end_button_rect.collidepoint(event.pos):
                    running = False

pygame.quit()