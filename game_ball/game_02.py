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
def draw_menu():
    ventana.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    font1 = pygame.font.SysFont('arial', 60)

    title1 = font1.render('BALL GAME', True, (255, 255, 255))
    ventana.blit(title1, (325 - title1.get_width()/2, 150 - title1.get_height()/2))

    start_button = font.render('Play', True, (255, 255, 255))
    start_button_rect = start_button.get_rect(center=(325, 300))
    ventana.blit(start_button, (325 - start_button.get_width()/2, 250 + start_button.get_height()/2))

    end_button = font.render('Quit', True, (255, 255, 255))
    end_button_rect = end_button.get_rect(center=(325, 400))
    ventana.blit(end_button, (325 - end_button.get_width()/2, 350 + end_button.get_height()/2))

    pygame.display.update()

    return start_button_rect, end_button_rect

# MAIN LOOP
while running:
    # GAME
    if game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if not baterect.left < 0:
                baterect = baterect.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            if  baterect.right < ventana.get_width():
                baterect = baterect.move(5, 0)

        ballrect = ballrect.move(speed)

        if ballrect.left < 0 or ballrect.right > ventana.get_width():
            speed[0] = -speed[0]

        if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
            speed[1] = -speed[1]

        if baterect.colliderect(ballrect):
            speed[1] = -speed[1]
            score += 1
            first = True

        if ballrect.bottom >= ventana.get_height():
            game_state = False
        
        if score in range(5, 100, 5):
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
        print(speed)

        ventana.fill((252, 243, 207))

        font1 = pygame.font.SysFont('arial', 30)
        title1 = font1.render('SCORE: ' + str(score), True, (0, 0, 0))
        ventana.blit(title1, (70 - title1.get_width()/2, 20 - title1.get_height()/2))

        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # MENU
    else:
        continue_button_rect, end_button_rect = draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button_rect.collidepoint(event.pos):
                    score = 0
                    ballrect.x = 0
                    ballrect.y = 0
                    speed = [4, 4]
                    game_state = True
                    velocidad = 3
                elif end_button_rect.collidepoint(event.pos):
                    running = False

pygame.quit()