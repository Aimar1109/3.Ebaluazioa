import pygame

pygame.init()

ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game 2")

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

speed = [4, 4]

ballrect.move_ip(0, 0)

bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

baterect.move_ip(240, 450)

jugando = True

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    
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

pygame.quit()