import pygame
import time
import solve 


pygame.font.init()
Window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("SUDOKU GAME")
x = 0
z = 0
diff = 500 / 9
value= 0
new_button_width = 50
new_button_height = 25
new_button_x = 25
new_button_y = 540
new_button_text = pygame.font.SysFont("comicsans",20).render('New', True, (0,0,0))

solve_button_width = 50
solve_button_height = 25
solve_button_x = 425
solve_button_y = 540
solve_button_text = pygame.font.SysFont("comicsans",20).render('Solve', True, (0,0,0))

error_x = 225
error_y = 540
error_width = 50
error_height = 25
error_text = pygame.font.SysFont("comicsans",20).render('ERROR: invalid board', True, (0,0,0))
defaultgrid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]


cursor = [0,0]
font = pygame.font.SysFont("comicsans", 20)
font1 = pygame.font.SysFont("comicsans", 20)

def new_board():
    for i in range(9):
        for j in range(9):
            defaultgrid[i][j]=0

def drawlines():
    for i in range (9):
        for j in range (9):
            if defaultgrid[i][j]!= 0:
                # pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                Window.blit(text1, (i * diff + 15, j * diff + 15))
    for l in range(10):
        if l % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)

def grid_write(x, y, val):
    defaultgrid[x][y] = val

def display_error_message():
    pygame.draw.rect(Window,(155,100,100),[error_x,error_y,error_width,error_height])


while(True):
    flag = 0
    error_flag = 0 
    """
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                flag = 1
                """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if (cursor[1]!=0):
                    cursor[1]-=1
            elif event.key == pygame.K_a:
                if (cursor[0]!=0):
                    cursor[0]-=1
            elif event.key == pygame.K_s:
                if (cursor[1]!=8):
                    cursor[1]+=1
            elif event.key == pygame.K_d:
                if (cursor[0]!=8):
                    cursor[0]+=1
            elif event.key == pygame.K_RETURN:
                pass
            else:
                for i in range(0,10):
                    if i == event.key - 48:
                        grid_write(cursor[0], cursor[1], i)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if new_button_x <= mouse[0] <= new_button_x + new_button_width and new_button_y <= mouse[1] <= new_button_y + new_button_height:
                print("pressed new")
                new_board()
                error_flag = 0
            elif solve_button_x <= mouse[0] <= solve_button_x + solve_button_width and solve_button_y <= mouse[1] <= solve_button_y + solve_button_height:
                print("pressed solve")
                try: 
                    defaultgrid = solve(defaultgrid)
                    error_flag = 0
                except:
                    error_flag = 1
            
    Window.fill((255,255,255))
    pygame.draw.rect(Window, (255,255,0), (cursor[0] * diff, cursor[1] * diff, diff, diff))
    drawlines()

    mouse = pygame.mouse.get_pos()
    if new_button_x <= mouse[0] <= new_button_x + new_button_width and new_button_y <= mouse[1] <= new_button_y + new_button_height:
        pygame.draw.rect(Window,(155,100,100),[new_button_x,new_button_y,new_button_width,new_button_height])
    else:
        pygame.draw.rect(Window,(255,100,100),[new_button_x,new_button_y,new_button_width,new_button_height])
    Window.blit(new_button_text, (new_button_x + 5, new_button_y + 5))

    if solve_button_x <= mouse[0] <= solve_button_x + solve_button_width and solve_button_y <= mouse[1] <= solve_button_y + solve_button_height:
        pygame.draw.rect(Window,(155,100,100),[solve_button_x,solve_button_y, solve_button_width
    ,new_button_height])
    else:
        pygame.draw.rect(Window,(255,100,100),[solve_button_x,solve_button_y,solve_button_width,solve_button_height])
    Window.blit(solve_button_text, (solve_button_x + 5, solve_button_y + 5))

    if error_flag:
        display_error_message()
    pygame.display.update()
    if flag:
        pygame.quit()
        break
