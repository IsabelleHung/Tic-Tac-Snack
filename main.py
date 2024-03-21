import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 680 #(added 80 for bottom player indication. 80 not included in the tic tac toe board)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (154, 190, 214)
bingo = False
size_of_pic = 160 #size of pixels for X and O image. width and height are same 
size_of_padding = ((SCREEN_WIDTH/3) - size_of_pic)/2 #size between each pic of X and O image and 1/3 of the board

# -1 is not set
show_1_1 = -1
show_1_2 = -1
show_1_3 = -1
show_2_1 = -1
show_2_2 = -1
show_2_3 = -1
show_3_1 = -1
show_3_2 = -1
show_3_3 = -1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

bg_img = pygame.image.load("assets/background.png").convert_alpha() #600 px by 600 px
x_img = pygame.image.load("assets/X.png").convert_alpha() #160 px by 160 px
o_img = pygame.image.load("assets/O.png").convert_alpha() #160 px by 160 px


running = True
player1turn = True
my_font = pygame.font.Font("assets/KaushanScript-Regular.ttf", 50)


while running:
    screen.fill(WHITE)
    screen.blit(bg_img, (0, 0))

    #draw rectangle for player indication
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 600, 600, 80))

    #draw player indication text
    if player1turn == True:
        player_indication_text = my_font.render("Player 1", False, BLACK)
        screen.blit(player_indication_text, (SCREEN_WIDTH/2 - 90,600))
    elif player1turn == False:
        player_indication_text = my_font.render("Player 2", False, BLACK)
        screen.blit(player_indication_text, (SCREEN_WIDTH/2 - 90,600))

    #showing the x and o
    #blitting locations row 1
    if show_1_1==1:
        screen.blit(x_img, (size_of_padding, size_of_padding))
    elif show_1_1==0:
        screen.blit(o_img, (size_of_padding, size_of_padding)) 

    if show_1_2==1:
        screen.blit(x_img, (size_of_pic + (size_of_padding*3), size_of_padding))
    elif show_1_2==0:
        screen.blit(o_img, (size_of_pic + (size_of_padding*3), size_of_padding))

    if show_1_3==1:
        screen.blit(x_img, ((size_of_pic *2) + (size_of_padding*5), size_of_padding))
    elif show_1_3==0:
        screen.blit(o_img, ((size_of_pic *2) + (size_of_padding*5), size_of_padding))
    #blitting locations row 2   
    if show_2_1==1:
        screen.blit(x_img, (size_of_padding, size_of_pic + (size_of_padding*3)))
    elif show_2_1==0:
        screen.blit(o_img, (size_of_padding, size_of_pic + (size_of_padding*3)))

    if show_2_2==1:
        screen.blit(x_img, (size_of_pic + (size_of_padding*3), size_of_pic + (size_of_padding*3)))
    elif show_2_2==0:
        screen.blit(o_img, (size_of_pic + (size_of_padding*3), size_of_pic + (size_of_padding*3)))

    if show_2_3==1:
        screen.blit(x_img, ((size_of_pic *2) + (size_of_padding*5), size_of_pic + (size_of_padding*3)))
    elif show_2_3==0:
        screen.blit(o_img, ((size_of_pic *2) + (size_of_padding*5), size_of_pic + (size_of_padding*3)))
    # #blitting locations row 3
    if show_3_1==1:
        screen.blit(x_img, (size_of_padding, (size_of_pic *2) + (size_of_padding*5))) 
    elif show_3_1==0:
        screen.blit(o_img, (size_of_padding, (size_of_pic *2) + (size_of_padding*5))) 

    if show_3_2==1:
        screen.blit(x_img, (size_of_pic + (size_of_padding*3), (size_of_pic *2) + (size_of_padding*5))) 
    elif show_3_2==0:
        screen.blit(o_img, (size_of_pic + (size_of_padding*3), (size_of_pic *2) + (size_of_padding*5))) 

    if show_3_3==1:
        screen.blit(x_img, ((size_of_pic *2) + (size_of_padding*5), (size_of_pic *2) + (size_of_padding*5))) 
    elif show_3_3==0:
        screen.blit(o_img, ((size_of_pic *2) + (size_of_padding*5), (size_of_pic *2) + (size_of_padding*5))) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos_x, pos_y = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0] and pos_x >= 0 and pos_x < SCREEN_WIDTH/3 and pos_y >= 0 and pos_y < (SCREEN_HEIGHT - 100)/3:
                show_1_1 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= SCREEN_WIDTH/3 and pos_x < (SCREEN_WIDTH/3) * 2 and pos_y >= 0 and pos_y < (SCREEN_HEIGHT - 100)/3:
                show_1_2 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= (SCREEN_WIDTH/3) * 2 and pos_x < SCREEN_WIDTH and pos_y >= 0 and pos_y < (SCREEN_HEIGHT - 100)/3:
                show_1_3 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= 0 and pos_x < SCREEN_WIDTH/3 and pos_y >= (SCREEN_HEIGHT - 100)/3 and pos_y < ((SCREEN_HEIGHT - 100)/3) * 2:
                show_2_1 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= SCREEN_WIDTH/3 and pos_x < (SCREEN_WIDTH/3) * 2 and pos_y >= (SCREEN_HEIGHT - 100)/3 and pos_y < ((SCREEN_HEIGHT - 100)/3) * 2:
                show_2_2 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= (SCREEN_WIDTH/3) * 2 and pos_x < SCREEN_WIDTH and pos_y >= (SCREEN_HEIGHT - 100)/3 and pos_y < ((SCREEN_HEIGHT - 100)/3) * 2:
                show_2_3 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= 0 and pos_x < SCREEN_WIDTH/3 and pos_y >= ((SCREEN_HEIGHT - 100)/3) * 2 and pos_y < SCREEN_HEIGHT - 100:
                show_3_1 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= SCREEN_WIDTH/3 and pos_x < (SCREEN_WIDTH/3) * 2 and pos_y >= ((SCREEN_HEIGHT - 100)/3) * 2 and pos_y < SCREEN_HEIGHT - 100:
                show_3_2 = int(player1turn)
            elif pygame.mouse.get_pressed()[0] and pos_x >= (SCREEN_WIDTH/3) * 2 and pos_x < SCREEN_WIDTH and pos_y >= ((SCREEN_HEIGHT - 100)/3) * 2 and pos_y < SCREEN_HEIGHT - 100:
                show_3_3 = int(player1turn)

            player1turn = (not player1turn)
            
        if show_1_1 == show_1_2 and show_1_1 == show_1_3 and show_1_1 != -1:
            bingo = True
        elif show_2_1 == show_2_2 and show_2_1 == show_2_3 and show_2_1 != -1:
            bingo = True
        elif show_3_1 == show_3_2 and show_3_1 == show_3_3 and show_3_1 != -1:
            bingo = True
        elif show_1_1 == show_2_2 and show_1_1 == show_3_3 and show_1_1 != -1:
            bingo = True
        elif show_1_3 == show_2_2 and show_1_3 == show_3_1 and show_1_3 != -1:
            bingo = True
        elif show_1_1 == show_2_1 and show_1_1 == show_3_1 and show_1_1 != -1:
            bingo = True
        elif show_1_3 == show_2_3 and show_1_3 == show_3_3 and show_1_3 != -1:
            bingo = True
        elif show_1_2 == show_2_2 and show_1_2 == show_3_2 and show_1_2 != -1:
            bingo = True
        elif show_1_1 != -1 and show_1_2 != -1 and show_1_3 != -1 and show_2_1 != -1 and show_2_2 != -1 and show_2_3 != -1 and show_3_1 != -1 and show_3_2 != -1 and show_3_3 != -1:
            pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 600, 700))
            player_indication_text = my_font.render("NO WINNER", False, BLACK)
            screen.blit(player_indication_text, (SCREEN_WIDTH/2 - 120,300))
            pygame.display.update()
            pygame.time.wait(2000)
            bingo = False
            show_1_1 = -1
            show_1_2 = -1
            show_1_3 = -1
            show_2_1 = -1
            show_2_2 = -1
            show_2_3 = -1
            show_3_1 = -1
            show_3_2 = -1
            show_3_3 = -1
            player1turn = True

        if bingo == True:
            pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 600, 600))
            player_indication_text = my_font.render("WINNER", False, BLACK)
            screen.blit(player_indication_text, (SCREEN_WIDTH/2 - 80,300))
            pygame.display.update()
            pygame.time.wait(2000)
            bingo = False
            show_1_1 = -1
            show_1_2 = -1
            show_1_3 = -1
            show_2_1 = -1
            show_2_2 = -1
            show_2_3 = -1
            show_3_1 = -1
            show_3_2 = -1
            show_3_3 = -1
            player1turn = True

    pygame.display.update()
pygame.quit()


