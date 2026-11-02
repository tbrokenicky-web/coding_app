import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1400, 1080))
pygame.display.set_caption("code app")


button1 = pygame.image.load("Button1_app.png")
button1 = pygame.transform.scale(button1, (400, 100))

screen.fill((211, 211, 211))

clock = pygame.time.Clock()

clicked = False

time_coding = 0

time_button_pr = True

font1 = pygame.font.SysFont("Arial", 50)

TIME_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIME_EVENT, 1000)

def timer():
     global time_coding 
    
     screen.fill((211, 211, 211))
     time_coding += 1

     text = font1.render("Your time is: " + str(time_coding), True, (0, 0, 0))
     
     screen.blit(text, (700, 300))
     
     

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
        
        if event.type == pygame.USEREVENT + 1:
            timer()
    mouse_pos = pygame.mouse.get_pos()

    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    if time_button_pr:
        screen.blit(button1, (700, 500))

    if 1100 > mouse_pos_x > 700 and 600 > mouse_pos_y > 500 and clicked:
        timer()
        clicked = False

    pygame.display.flip()
    
    clock.tick(60)