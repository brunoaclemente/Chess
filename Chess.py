from main import *

pygame.init()

SCREEN_WIDHT = 1000
SCREEN_HEIGHT = 1000

size = SCREEN_WIDHT/8
i = 8
j = 8
piece = 0
eat = False
pos = None
capture = False

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('chess')

clock = pygame.time.Clock()

startFEN = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            i = int(pos[1] / size)
            j = int(pos[0] / size)
            eat = False

    screen.fill(black)

    draw_background(screen, size, pos)
    capture = False
    draw_pieces(startFEN, screen, size)

    if 0 <= i <= 7 and 0 <= j <= 7:
        if startFEN[i][j] != '-':
            if piece != 0:
                if checkingCapture(piece, startFEN, i, j):
                    startFEN[piece[1]][piece[2]] = '-'
                    startFEN[i][j] = piece[0]
                    eat = True

            if not eat:
                piece = [startFEN[i][j], i, j]
                pos = possibilities(piece, startFEN, i, j)
            else:
                pos = possibilities(piece, startFEN, i, j)
                i = 8
                j = 8
                piece = 0

        else:
            if piece != 0:
                if checkingMovement(piece, startFEN, i, j):
                    startFEN[piece[1]][piece[2]] = '-'
                    startFEN[i][j] = piece[0]
                    piece = 0
                    i = 8
                    j = 8
                    pos = None
                else:
                    piece = 0
                    pos = None
                    i = 8
                    j = 8

    pygame.display.update()
