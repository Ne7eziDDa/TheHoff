import pygame
import os

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

font_name = pygame.font.match_font('Verdana')
def menu():
    menu = True
    selected = 'Start'

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = 'Start'
                elif event.key == pygame.K_DOWN:
                    selected = 'Quit'
                if event.key == pygame.K_RETURN:
                    if selected == 'Start':
                        game_process()
                    if selected == 'Quit':
                        pygame.quit()
                        quit()

        # UI
        screen.fill(black) # возможно загрузить изображение.
        title = text_format('The Hoff.', font_name, 90, white)
        if selected == 'Start':
            text_start = text_format('START', font_name, 75, yellow)
        else:
            text_start = text_format('START', font_name, 75, white)
        if selected == 'Quit':
            text_quit = text_format('QUIT', font_name, 75, yellow)
        else:
            text_quit = text_format('QUIT', font_name, 75, white)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # текст

        screen.blit(title, (WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
