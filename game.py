# Pygame game template

import pygame, sys, config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
# Write function above your main( ) function
def draw_line(screen, color, start_pos, end_pos, thickness):
    """Draws a line on the screen with the specified color and thickness."""

    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    while running:
        running = handle_events()
        screen.fill(config.COLOR_WHITE)
        positions_for_grid = 
        draw_line(screen, config.COLOR_BLACK, 
        
        pygame.display.flip()

        clock.tick(config.FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
