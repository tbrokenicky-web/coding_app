import pygame
import time

import os # allows you to acces you operating system tools for device


pygame.init()

screen = pygame.display.set_mode((1400, 1080))
pygame.display.set_caption("code app")
"""
try:
    with open("save_time.txt", "r") as file:
        total_time_coding_save = int(file.read() or 0)
except FileNotFoundError:
    total_time_coding_save = 0
"""
if not os.path.exists("save_coins.txt"):
    with open("save_coins.txt", "w") as file:
        file.write("0.0")

button1 = pygame.image.load("Button1_app.png")
button1 = pygame.transform.scale(button1, (400, 100))
button2 = pygame.image.load("Button1_app.png")
button2 = pygame.transform.scale(button2, (400, 100))
button_stats = pygame.image.load("Button1_app.png")
button_stats = pygame.transform.scale(button_stats, (250, 75))
main_screen_button = pygame.image.load("Button1_app.png")
main_screen_button = pygame.transform.scale(main_screen_button, (250, 75))
button_stats_active = True
main_screen_button_active = True

screen.fill((211, 211, 211))

clock = pygame.time.Clock()

clicked = False

time_coding = 00

total_time_coding = 0

button_1_active = True
button_2_active = False


font1 = pygame.font.SysFont("Arial", 75)
font2 =pygame.font.SysFont("Arial", 50)

TIME_EVENT = pygame.USEREVENT + 1
time_code_min = 0

time_code_hour = 0

def timer():
     global time_coding, time_code_hour,time_code_min, total_time_coding
    
     

     screen.fill((211, 211, 211))
     time_coding += 1
     # this will be used for coins system later
     total_time_coding += 1
     
     text = font1.render(str(time_code_hour)+ ":" + str(time_code_min) + ":" +str(time_coding), True, (0, 0, 0))
     if time_coding == 60:
         time_coding = 00
         time_code_min += 1
         text = font1.render(str(time_code_hour)+ ":" + str(time_code_min) + ":" +str(time_coding), True, (0, 0, 0))

         pygame.display.flip()
     if time_code_min == 60:
         time_code_hour += 1
         time_code_min = 0
         text = font1.render(str(time_code_hour)+ ":" + str(time_code_min) + ":" +str(time_coding), True, (0, 0, 0))
     
         pygame.display.flip()
     screen.blit(text, (20, 300))
     
running = True

total_time_text = False

total_coins_text = False



font3 = pygame.font.SysFont("Arial", 30)
current_coins = 0
current_coins_active = True 
coins_used = 0


while running:
    
    try:
        with open("save_time.txt", "r") as file:
            total_time_coding_save = int(file.read() or 0)
    except FileNotFoundError:
        total_time_coding_save = 0
    
    try:
        with open("save_coins.txt", "r") as file:
            current_coins_save = float(file.read() or 0)
    except FileNotFoundError:
        current_coins_save = 0
        print("nothing found")
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
        
        if event.type == pygame.USEREVENT + 1:
            timer()
    
    mouse_pos = pygame.mouse.get_pos()

    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    
    if button_1_active:
        screen.blit(button1, (20, 500))
    
    if button_2_active:
        screen.blit(button2, (20, 500))
    
    if button_stats_active:
        screen.blit(button_stats, (500, 20))
    
    if main_screen_button_active:
        screen.blit(main_screen_button, (200, 20))
    
    if total_time_text:
        screen.blit(stats_text_time_hd, (950, 100))
        screen.blit(stats_text_time, (1250, 150))

    if total_coins_text:
        screen.blit(stats_text_coins_hd, (1100, 250))
        screen.blit(stats_text_coins, (1250, 300))
    if current_coins_active:
        
        pygame.draw.rect(screen, (211, 211, 211), (1200, 0, 150, 50))
        
        coins = (total_time_coding) * 0.5

        current_coins = current_coins_save + coins - coins_used
        
        coins_main_ui = font3.render("coins: " + str(current_coins), True, (0, 0, 0))
        screen.blit(coins_main_ui, (1200, 20))
        pygame.display.flip()
    if main_screen_button_active:
        if 450 > mouse_pos_x > 200 and 95 > mouse_pos_y > 20 and clicked:
            screen.fill((211, 211, 211))

            button_1_active = True
            
            total_time_text = False
            total_coins_text = False

            clicked = False

    
    if button_stats_active:
        if 750 > mouse_pos_x > 500 and 95 > mouse_pos_y > 20 and clicked:
            screen.fill((211, 211, 211))

            
            
            button_1_active = False
            button_2_active = False
            
            stats_text_time_hd = font2.render("Total Time Coding:", True, (0, 0, 0))
            stats_text_time = font2.render(str(total_time_coding_save), True, (0, 0, 0))
            stats_text_coins_hd = font2.render("Total Coins:", True, (0, 0, 0))
            stats_text_coins = font2.render(str(current_coins), True, (0, 0, 0))

            total_coins_text = True
            total_time_text = True
            
            

            clicked = False

    if button_1_active:
        if 420 > mouse_pos_x > 20 and 600 > mouse_pos_y > 500 and clicked:
            timer()
            
            pygame.time.set_timer(TIME_EVENT, 1000)
            button_1_active = False
            button_2_active = True
            clicked = False
    
    if button_2_active:
        if 420 > mouse_pos_x > 20 and 600 > mouse_pos_y > 500 and clicked:
            pygame.time.set_timer(TIME_EVENT, 0)
            
            
            time_coding = 0
            time_code_min = 0
            time_code_hour = 0
            
            button_2_active = False
            button_1_active = True
            
            
            with open("save_time.txt", "w") as file:
                file.write(str(total_time_coding_save + total_time_coding))
            
            with open("save_coins.txt", "w") as file:
                file.write(str(current_coins))

            total_time_coding = 0
            clicked = False
            
            

            
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()