import pygame, sys
import numpy as np

lul = 1

#while lul == 1

pygame.init()
# зададим размеры поля и название
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption( 'TicTacToe 2' )
color0 = (28, 170, 156) # цвет поля
color1 = (0, 135, 121) # цвет линий
rows = 3
cols = 3
figu = 1
lol = 1
#board
board = np.zeros( (rows, cols) )
screen.fill( color0 )

def draw_lines():
    pygame.draw.line(screen, color1, (210, 30), (210, 570), 10)
    pygame.draw.line(screen, color1, (390, 30), (390, 570), 10)
    pygame.draw.line(screen, color1, (30, 210), (570, 210), 10)
    pygame.draw.line(screen, color1, (30, 390), (570, 390), 10)

draw_lines()
pygame.display.update()

def mark_square(row, col, fig):
    board[row][col] = fig

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return False

def check_win(fig):
    #Ver Win Check
    for col in range(cols):
        if board[0][col] == fig and board[1][col] == fig and board[2][col] == fig:
            VerWinLine(col, fig)
            lol = 0
            return True
    # Hor Win Check
    for row in range(rows):
        if board[row][0] == fig and board[row][1] == fig and board[row][2] == fig:
            HorWinLine(row, fig)
            lol = 0
            return True
    # Ask Dia Win Check
    if board[2][0] == fig and board [1][1] == fig and board [0][2] == fig:
        AscDiaLine(fig)
        lol = 0
        return True
    # Desk Dia Win Check
    if board[0][0] == fig and board[1][1] == fig and board[2][2] == fig:
        DescDiaLine(fig)
        lol = 0
        return True
    return False

def VerWinLine(col, fig):
    Y0 = 60
    Y1 = 540
    if col == 0:
        X = 120
    elif col == 1:
        X = 300
    else:
        X = 480

    if fig == 1:
        color = (40, 40, 40)
    else:
        color = (255, 255, 255)
    pygame.draw.line(screen, color, (X, Y0), (X, Y1), 20)


def HorWinLine(row, fig):
    X0 = 60
    X1 = 540
    if row == 0:
        Y = 120
    elif row == 1:
        Y = 300
    else:
        Y = 480

    if fig == 1:
        color = (40, 40, 40)
    else:
        color = (255, 255, 255)
    pygame.draw.line(screen, color, (X0, Y), (X1, Y), 20)

def AscDiaLine(fig):
    X0 = 510
    X1 = 90
    Y0 = 90
    Y1 = 510

    if fig == 1:
        color = (40, 40, 40)
    else:
        color = (255, 255, 255)
    pygame.draw.line(screen, color, (X0, Y0), (X1, Y1), 20)

def DescDiaLine(fig):
    X0 = 90
    X1 = 510
    Y0 = 90
    Y1 = 510

    if fig == 1:
        color = (40, 40, 40)
    else:
        color = (255, 255, 255)
    pygame.draw.line(screen, color, (X0, Y0), (X1, Y1), 20)

def drawIT(row, col, fig):
    if row == 0:
        Y = 75
    elif row == 1:
        Y = 255
    else:
        Y = 435

    if col == 0:
        X = 75
    elif col == 1:
        X = 255
    else:
        X = 435
    if fig == 2:
        pygame.draw.line(screen, (55, 55, 55), (X, Y), (X + 90, Y + 90), 30)
        pygame.draw.line(screen, (55, 55, 55), (X, Y + 90), (X + 90, Y), 30)
    else:
        pygame.draw.circle(screen, (245, 245, 245), (X + 45, Y + 45) , 60, 15)

    return True
def draw_square( X, Y, fig):
    global figu
    if is_board_full() == False:
        if X > 0 and 210 >= X:
            sq_col = 0
        else:
            if X > 210 and 390 >= X:
                sq_col = 1
            else:
                sq_col = 2

        if Y > 0 and 210 >= Y:
            sq_row = 0
        else:
            if Y > 210 and 390 >= Y:
                sq_row = 1
            else:
                sq_row = 2

        if available_square(sq_row, sq_col) == True:
            figu += 1
            mark_square(sq_row, sq_col, fig)
            drawIT(sq_row, sq_col, fig)
            return figu
    else:
        return figu
        lol = 0

def restart():
    screen.fill(color0)
    draw_lines()
    global figu
    global lol
    figu = 1
    for row in range(rows):
        for col in range(cols):
            board[row][col] = 0
    lol = 1

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        if event.type == pygame.MOUSEBUTTONDOWN and lol == 0:
            restart()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if figu % 2 == 0:
                    figur = 1
                else:
                    figur = 2
                mX = event.pos[0]
                mY = event.pos[1]
                draw_square(mX, mY, figur)
                if check_win(figur):
                    lol = 0
    pygame.display.update()

