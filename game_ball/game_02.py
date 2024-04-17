import pygame

pygame.init()

ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game 2")

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()


ballrect.move_ip(0, 0)

bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

baterect.move_ip(240, 450)

# INITIAL VARIABLES
running = True
game_state = False
speed = [4, 4]

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

while running:
    if game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if not baterect.left < 0:
                baterect = baterect.move(-3, 0)
        if keys[pygame.K_RIGHT]:
            if  baterect.right < ventana.get_width():
                baterect = baterect.move(3, 0)

        ballrect = ballrect.move(speed)

        if ballrect.left < 0 or ballrect.right > ventana.get_width():
            speed[0] = -speed[0]

        if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
            speed[1] = -speed[1]

        if baterect.colliderect(ballrect):
            speed[1] = -speed[1]

        ventana.fill((252, 243, 207))

        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    else:
        continue_button_rect, end_button_rect = draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button_rect.collidepoint(event.pos):
                    speed = [4, 4]
                    game_state = True
                elif end_button_rect.collidepoint(event.pos):
                    running = False

pygame.quit()