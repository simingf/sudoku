import pygame
import time
pygame.font.init()
Window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SUDOKU GAME")
x = 0
z = 0
diff = 500 / 9
value= 0


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
font = pygame.font.SysFont("comicsans", 30)
font1 = pygame.font.SysFont("comicsans", 20)


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

while(True):
    flag = 0
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
    Window.fill((255,255,255))
    pygame.draw.rect(Window, (255,255,0), (cursor[0] * diff, cursor[1] * diff, diff, diff))
    drawlines()
    pygame.display.update()
    if flag:
        pygame.quit()
        break
