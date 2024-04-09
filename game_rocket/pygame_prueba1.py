import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Create a font object for the text
font = pygame.font.SysFont('Arial', 36)


# Create a text surface with the text "Press any key to start"
start_screen_text = font.render('Press any key to start', True, (255, 255, 255))
start_screen_text_rect = start_screen_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))

# Create a function to draw the start screen
def draw_start_screen():
    screen.fill((0, 0, 0))
    screen.blit(start_screen_text, start_screen_text_rect)
    pygame.display.flip()

# Create a function to handle the start screen events
def handle_start_screen_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen_text_rect.collidepoint(event.pos):
                print('1')
                return True
            elif quit_button_text_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

# Create a text surface with the text "Play"
play_button_text = font.render('Play', True, (255, 255, 255))
play_button_text_rect = play_button_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))

# Create a text surface with the text "Quit"
quit_button_text = font.render('Quit', True, (255, 255, 255))
quit_button_text_rect = quit_button_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))

# Game loop
running = True
while running:
    if handle_start_screen_events():
        # Change the background color to red
        screen.fill((255, 0, 0))
        pygame.display.flip()

        # Game loop
        while running:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    game_state = True

            # Clear the screen
            screen.fill((255, 0, 0))

            # Draw game objects, etc.

            # Update the display
            pygame.display.flip()

    else:
        # Create the start screen
        draw_start_screen()