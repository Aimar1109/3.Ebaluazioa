# AIMAR MARDONES ETA UNAI ARCE

# import the pygame module and the random command
import pygame
import random

# import pygame.locals for easier access to
# key coordinates.

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

clock = pygame.time.Clock()

# Setup fr sound. Defaults are good.
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("spacecraft.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 3
        self.lifes = 3
        self.score = 0

    def restart(self, x, y):
        self.surf = pygame.image.load("spacecraft.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(x, y))
        self.speed = 3

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy obect by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 4)
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            player.score += 1


# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create the screen object. The size is
# determied by the constants SCREEN_WIDTH
# and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background image
background = pygame.image.load("space.png")
# Load and play background music
pygame.mixer.music.load("Apoxode.wav")
pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.wav")
move_down_sound = pygame.mixer.Sound("Falling_putter.wav")
collision_sound = pygame.mixer.Sound("Collision.wav")

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 400)

# instantiate player - at the moment a rectangle


def create_player_enemies():
    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position up
    # - all_sprites is used for rendering
    player = Player()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    return enemies, all_sprites, player


# variable to keep the main loop running
running = True
game_state = False
first = True
game_over = False


def draw_menu(text):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title1 = font.render(text, True, (255, 255, 255))

    start_button = font.render('Play', True, (255, 255, 255))
    end_button = font.render('Quit', True, (255, 255, 255))

    start_button_rect = start_button.get_rect(center=(400, 300))
    end_button_rect = end_button.get_rect(center=(400, 400))

    screen.blit(title1, (400 - title1.get_width() /
                2, 150 - title1.get_height()/2))
    screen.blit(start_button, (400 - start_button.get_width() /
                2, 250 + start_button.get_height()/2))
    screen.blit(end_button, (400 - end_button.get_width() /
                2, 350 + end_button.get_height()/2))

    pygame.display.update()
    return start_button_rect, end_button_rect


def draw_die():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title1 = font.render('My Game', True, (255, 255, 255))

    continue_button = font.render('Continue', True, (255, 255, 255))
    end_button = font.render('Quit', True, (255, 255, 255))

    continue_button_rect = continue_button.get_rect(center=(400, 300))
    end_button_rect = end_button.get_rect(center=(400, 400))

    screen.blit(title1, (400 - title1.get_width() /
                2, 150 - title1.get_height()/2))
    screen.blit(continue_button, (400 - continue_button.get_width() /
                2, 250 + continue_button.get_height()/2))
    screen.blit(end_button, (400 - end_button.get_width() /
                2, 350 + end_button.get_height()/2))

    pygame.display.update()
    return continue_button_rect, end_button_rect


def draw_score_lifes():
    lifes = pygame.image.load("corazon.png")

    for life in range(player.lifes):
        screen.blit(lifes, (25+50*life - lifes.get_width() /
                    2, 575 - lifes.get_height()/2))

    pygame.display.update()


# main loop
while running:
    if game_state:
        # look at every event in the queue
        for event in pygame.event.get():
            # did the user hit a key?
            if event.type == KEYDOWN:
                # was it the Escape key? If so stop the loop
                if event.key == K_ESCAPE:
                    running = False
            # did the user click the window close button?
            elif event.type == QUIT:
                running = False

            # Add a new enemy?
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Draw the background using the blit() function
        screen.blit(background, (0, 0))
        # get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # update enemy position
        enemies.update()

        # update the player sprite based on user keypresses
        player.update(pressed_keys)

        # fill the screen with white
        # screen.fill((0,0,0))

        # draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, the remove the player and stop the loop
            x = player.rect.x
            y = player.rect.y
            player.kill()
            game_state = False
            player.lifes -= 1
            if player.lifes == 0:
                first = True
                game_over = True
            # Stop any moving sounds and play collision sound
            move_up_sound.stop()
            move_down_sound.stop()
            collision_sound.play()

        # draw the player on the screen
        screen.blit(player.surf, player.rect)

        # draw the score a lifes
        draw_score_lifes()

        # update the display
        pygame.display.flip()
        clock.tick(30)
    else:
        if first:
            if game_over:
                start_button_rect, end_button_rect = draw_menu('GAME OVER')
                game_over = False
            else:
                start_button_rect, end_button_rect = draw_menu('MY GAME')

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # was it the Escape key? If so stop the loop
                    if event.key == K_ESCAPE:
                        running = False
                # did the user click the window close button?
                elif event.type == QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        enemies, all_sprites, player = create_player_enemies()
                        game_state = True
                        first = False
                    elif end_button_rect.collidepoint(event.pos):
                        running = False
        else:
            continue_button_rect, end_button_rect = draw_die()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        player.restart(x, y)
                        game_state = True
                    elif end_button_rect.collidepoint(event.pos):
                        running = False

# All done! Stop and quit the moxer.
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
