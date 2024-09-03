import pygame
from pygame.locals import *
from Most_used.cores import *
import math
from lib import mod


def draw_background(screen, size, pos=None):
    if pos is None or type(pos) != list:
        pos = [[8, 8, False]]
    c = 0
    for i in range(0, 8):
        if c != 0:
            c += 1
        for j in range(0, 8):
            c += 1
            rectangle = pygame.Rect(j * size, i * size, size, size)
            if c % 2 != 0:
                pygame.draw.rect(screen, white_color, rectangle)
            else:
                pygame.draw.rect(screen, black_color, rectangle)
            for position in pos:
                if i == position[0] and j == position[1]:
                    if not position[2]:
                        pygame.draw.circle(screen, (219, 165, 140), (j * size + (size / 2), i * size + (size / 2)),
                                           size / 7)
                    else:
                        pygame.draw.circle(screen, (219, 165, 140), (j * size + (size / 2), i * size + (size / 2)),
                                           size / 2, 5)
    font = pygame.font.SysFont("comicsans", 40)
    whitel = font.render(
        'a                             c                             e                              g',
        True, white_color)
    blackl = font.render(
        'b                             d                             f                              h',
        True, black_color)
    text_rect1 = whitel.get_rect()
    text_rect1.center = [489, 985]
    text_rect2 = blackl.get_rect()
    text_rect2.center = [614, 985]
    screen.blit(whitel, text_rect1)
    screen.blit(blackl, text_rect2)


def draw_pieces(sF, screen, size):
    for r, li in enumerate(sF):
        for c, co in enumerate(li):
            y = r * size
            x = c * size
            if co in 'bknpqr':
                file = f'Images/{co}.png'
                p = pygame.image.load(file)
                p = pygame.transform.scale(p, (int(size-10), int(size-10)))
                screen.blit(p, [x+10, y+10])
            elif co in 'BKNPQR':
                file = f'Images/{co.lower()}w.png'
                p = pygame.image.load(file)
                p = pygame.transform.scale(p, (int(size-10), int(size-10)))
                screen.blit(p, [x+3, y+5])


king = False
KING = False


'''class Piece:
    def __init__(self, i, j, startFEN, piece, eat=False):
        self.line = i
        self.column = j
        self.pos_pieces = startFEN
        self.piece = piece[0]
        self.pos = piece[1:]
        self.eat = eat

    def p(self):
        if self.eat:
            if self.line != self.piece[1] and self.column != self.piece[2]:
                if mod(self.line - self.pos[1]) == mod(self.column - self.pos[2]) == 1:
                    if self.piece in 'bknpqr' and self.line - self.pos[1] > 0:
                        return True
                    elif self.piece in 'BKNPQR' and self.line - self.pos[1] < 0:
                        return True
        else:
            if mod(self.line - self.pos[1]) == 2:
                if self.line - self.pos[1] < 0:
                    new_pos = self.line + 1
                else:
                    new_pos = self.line - 1
                if startFEN[new_pos][j] != '-':
                    return False
            if piece[2] == j and piece[1] in [6, 1]:
                if math.sqrt((i - piece[1]) ** 2) <= 2:
                    if piece[0] in 'bknpqr' and i - piece[1] > 0:
                        return True
                    elif piece[0] in 'BKNPQR' and i - piece[1] < 0:
                        return True
            elif piece[2] == j and math.sqrt((i - piece[1]) ** 2) == 1:
                if piece[0] in 'bknpqr' and i - piece[1] > 0:
                    return True
                elif piece[0] in 'BKNPQR' and i - piece[1] < 0:
                    return True
            return False
        else:'''


def checkingMovement(piece, startFEN, i, j, eat=False):
    global king, KING
    if piece[0] in 'pP':
        if eat:
            if i != piece[1] and j != piece[2]:
                if math.sqrt((i - piece[1]) ** 2) == math.sqrt((j - piece[2]) ** 2) == 1:
                    if piece[0] in 'bknpqr' and i - piece[1] > 0:
                        return True
                    elif piece[0] in 'BKNPQR' and i - piece[1] < 0:
                        return True
        else:
            if math.sqrt((i - piece[1]) ** 2) == 2:
                if i - piece[1] < 0:
                    new_pos = i + 1
                else:
                    new_pos = i - 1
                if startFEN[new_pos][j] != '-':
                    return False
            if piece[2] == j and piece[1] in [6, 1]:
                if math.sqrt((i - piece[1]) ** 2) <= 2:
                    if piece[0] in 'bknpqr' and i - piece[1] > 0:
                        return True
                    elif piece[0] in 'BKNPQR' and i - piece[1] < 0:
                        return True
            elif piece[2] == j and math.sqrt((i - piece[1]) ** 2) == 1:
                if piece[0] in 'bknpqr' and i - piece[1] > 0:
                    return True
                elif piece[0] in 'BKNPQR' and i - piece[1] < 0:
                    return True
        return False
    if piece[0] in 'kK':
        if math.sqrt((i - piece[1]) ** 2) <= 1 and math.sqrt((j - piece[2]) ** 2) <= 1:
            if piece[0] == "K":
                king = True
            else:
                KING = True
            print(KING, king)
            return True
        if piece[0] == "K":
            if math.sqrt((j - piece[2]) ** 2) == 2 and i in [0, 7] and piece[2] == 4 and not KING:
                if startFEN[i][piece[2] + 3] in "rR" or startFEN[i][piece[2] - 4] in "rR":
                    if j - piece[2] == 2:
                        if startFEN[i][piece[2] + 3] == "R":
                            startFEN[i][piece[2] + 3] = "-"
                            startFEN[i][5] = "R"
                        elif startFEN[i][piece[2] + 3] in "r":
                            startFEN[i][piece[2] + 3] = "-"
                            startFEN[i][5] = "r"
                    if j - piece[2] == -2:
                        if startFEN[i][piece[2] - 4] == "R":
                            startFEN[i][piece[2] - 4] = "-"
                            startFEN[i][3] = "R"
                        elif startFEN[i][piece[2] - 4] in "r":
                            startFEN[i][piece[2] - 4] = "-"
                            startFEN[i][3] = "r"
                    KING = True
                    return True
        else:
            if math.sqrt((j - piece[2]) ** 2) == 2 and i in [0, 7] and piece[2] == 4 and not king:
                if startFEN[i][piece[2] + 3] in "rR" or startFEN[i][piece[2] - 4] in "rR":
                    if j - piece[2] == 2:
                        if startFEN[i][piece[2] + 3] == "R":
                            startFEN[i][piece[2] + 3] = "-"
                            startFEN[i][5] = "R"
                        elif startFEN[i][piece[2] + 3] in "r":
                            startFEN[i][piece[2] + 3] = "-"
                            startFEN[i][5] = "r"
                    if j - piece[2] == -2:
                        if startFEN[i][piece[2] - 4] == "R":
                            startFEN[i][piece[2] - 4] = "-"
                            startFEN[i][3] = "R"
                        elif startFEN[i][piece[2] - 4] in "r":
                            startFEN[i][piece[2] - 4] = "-"
                            startFEN[i][3] = "r"
                    KING = True
                    return True
        return False
    if piece[0] in 'nN':
        if math.sqrt((i - piece[1]) ** 2) == 2 and math.sqrt((j - piece[2]) ** 2) == 1:
            return True
        elif math.sqrt((i - piece[1]) ** 2) == 1 and math.sqrt((j - piece[2]) ** 2) == 2:
            return True
        return False
    if piece[0] in 'bB':
        for y in range(1, int(math.sqrt((i - piece[1]) ** 2))):
            if piece[1] - i > 0:
                pos_li = piece[1] - y
            else:
                pos_li = piece[1] + y
            if piece[2] - j > 0:
                pos_co = piece[2] - y
            else:
                pos_co = piece[2] + y
            try:
                if startFEN[pos_li][pos_co] != '-':
                    return False
            except IndexError:
                return True
        if i != piece[1] and j != piece[2]:
            if math.sqrt((i - piece[1]) ** 2) == math.sqrt((j - piece[2]) ** 2):
                return True
        return False
    if piece[0] in 'rR':
        if math.sqrt((i - piece[1]) ** 2) != 0 and math.sqrt((j - piece[2]) ** 2) == 0:
            for c in range(1, int(math.sqrt((i - piece[1]) ** 2))):
                if piece[1] - i > 0:
                    pos_li = piece[1] - c
                else:
                    pos_li = piece[1] + c
                if startFEN[pos_li][j] != '-':
                    return False
            return True
        elif math.sqrt((i - piece[1]) ** 2) == 0 and math.sqrt((j - piece[2]) ** 2) != 0:
            for c in range(1, int(math.sqrt((j - piece[2]) ** 2))):
                if piece[2] - j > 0:
                    pos_co = piece[2] - c
                else:
                    pos_co = piece[2] + c
                if startFEN[i][pos_co] != '-':
                    return False
            return True
        return False
    if piece[0] in 'qQ':
        if math.sqrt((i - piece[1]) ** 2) != 0 and math.sqrt((j - piece[2]) ** 2) == 0:
            for c in range(1, int(math.sqrt((i - piece[1]) ** 2))):
                if piece[1] - i > 0:
                    pos_li = piece[1] - c
                else:
                    pos_li = piece[1] + c
                if startFEN[pos_li][j] != '-':
                    return False
            return True
        elif math.sqrt((i - piece[1]) ** 2) == 0 and math.sqrt((j - piece[2]) ** 2) != 0:
            for c in range(1, int(math.sqrt((j - piece[2]) ** 2))):
                if piece[2] - j > 0:
                    pos_co = piece[2] - c
                else:
                    pos_co = piece[2] + c
                if startFEN[i][pos_co] != '-':
                    return False
            return True
        else:
            for y in range(1, int(math.sqrt((i - piece[1]) ** 2))):
                if piece[1] - i > 0:
                    pos_li = piece[1] - y
                else:
                    pos_li = piece[1] + y
                if piece[2] - j > 0:
                    pos_co = piece[2] - y
                else:
                    pos_co = piece[2] + y
                if startFEN[pos_li][pos_co] != '-':
                    return False
            if i != piece[1] and j != piece[2]:
                if math.sqrt((i - piece[1]) ** 2) == math.sqrt((j - piece[2]) ** 2):
                    return True
        return False


def possibilities(piece, startFEN, i, j):
    global king, KING
    possibility = []
    if piece[0] in 'pP':
        if piece[0] == 'p':
            if startFEN[i + 1][j] == '-':
                possibility.append([i + 1, j, False])
            if i == 1 and startFEN[i + 1][j] == '-' and startFEN[i + 2][j] == '-':
                possibility.append([i + 2, j, False])
            try:
                if startFEN[i + 1][j + 1] in 'BKNPQR':
                    possibility.append([i + 1, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j - 1] in 'BKNPQR':
                    possibility.append([i + 1, j - 1, True])
            except IndexError:
                pass
        else:
            if startFEN[i - 1][j] == '-':
                possibility.append([i - 1, j, False])
            if i == 6 and startFEN[i - 1][j] == '-' and startFEN[i - 2][j] == '-':
                possibility.append([i - 2, j, False])
            try:
                if startFEN[i - 1][j + 1] in 'bknpqr':
                    possibility.append([i - 1, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j - 1] in 'bknpqr':
                    possibility.append([i - 1, j - 1, True])
            except IndexError:
                pass
    elif piece[0] in 'kK':
        if piece[0] == "K":
            if i in [0, 7] and piece[2] == 4 and not KING:
                if startFEN[i][piece[2] + 3] in "rR" or startFEN[i][piece[2] - 4] in "rR":
                    if startFEN[i][piece[2] + 1] == "-" and startFEN[i][piece[2] + 2] == "-":
                        possibility.append([i, piece[2] + 2, False])
                    if startFEN[i][piece[2] - 1] == "-" and startFEN[i][piece[2] - 2] == "-" and \
                            startFEN[i][piece[2]-3] == "-":
                        possibility.append([i, piece[2] - 2, False])

        else:
            if i in [0, 7] and piece[2] == 4 and not king:
                if startFEN[i][piece[2] + 3] in "rR" or startFEN[i][piece[2] - 4] in "rR":
                    if startFEN[i][piece[2] + 1] == "-" and startFEN[i][piece[2] + 2] == "-":
                        possibility.append([i, piece[2] + 2, False])
                    if startFEN[i][piece[2] - 1] == "-" and startFEN[i][piece[2] - 2] == "-" and \
                            startFEN[i][piece[2] - 3] == "-":
                        possibility.append([i, piece[2] - 2, False])

        try:
            if startFEN[i + 1][j] == '-':
                possibility.append([i + 1, j, False])
        except IndexError:
            pass
        try:
            if startFEN[i + 1][j - 1] == '-':
                possibility.append([i + 1, j - 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i + 1][j + 1] == '-':
                possibility.append([i + 1, j + 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i][j - 1] == '-':
                possibility.append([i, j - 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i][j + 1] == '-':
                possibility.append([i, j + 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i - 1][j] == '-':
                possibility.append([i - 1, j, False])
        except IndexError:
            pass
        try:
            if startFEN[i - 1][j - 1] == '-':
                possibility.append([i - 1, j - 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i - 1][j + 1] == '-':
                possibility.append([i - 1, j + 1, False])
        except IndexError:
            pass
        if piece[0] == 'k':
            try:
                if startFEN[i + 1][j] in 'BKNPQR':
                    possibility.append([i + 1, j, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j - 1] in 'BKNPQR':
                    possibility.append([i + 1, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j + 1] in 'BKNPQR':
                    possibility.append([i + 1, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i][j - 1] in 'BKNPQR':
                    possibility.append([i, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i][j + 1] in 'BKNPQR':
                    possibility.append([i, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j] in 'BKNPQR':
                    possibility.append([i - 1, j, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j - 1] in 'BKNPQR':
                    possibility.append([i - 1, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j + 1] in 'BKNPQR':
                    possibility.append([i - 1, j + 1, True])
            except IndexError:
                pass
        else:
            try:
                if startFEN[i + 1][j] in 'bknpqr':
                    possibility.append([i + 1, j, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j - 1] in 'bknpqr':
                    possibility.append([i + 1, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j + 1] in 'bknpqr':
                    possibility.append([i + 1, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i][j - 1] in 'bknpqr':
                    possibility.append([i, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i][j + 1] in 'bknpqr':
                    possibility.append([i, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j] in 'bknpqr':
                    possibility.append([i - 1, j, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j - 1] in 'bknpqr':
                    possibility.append([i - 1, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j + 1] in 'bknpqr':
                    possibility.append([i - 1, j + 1, True])
            except IndexError:
                pass
    elif piece[0] in 'nN':
        try:
            if startFEN[i + 2][j + 1] == '-':
                possibility.append([i + 2, j + 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i + 2][j - 1] == '-':
                possibility.append([i + 2, j - 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i - 2][j + 1] == '-':
                possibility.append([i - 2, j + 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i - 2][j - 1] == '-':
                possibility.append([i - 2, j - 1, False])
        except IndexError:
            pass
        try:
            if startFEN[i + 1][j + 2] == '-':
                possibility.append([i + 1, j + 2, False])
        except IndexError:
            pass
        try:
            if startFEN[i - 1][j + 2] == '-':
                possibility.append([i - 1, j + 2, False])
        except IndexError:
            pass
        try:
            if startFEN[i + 1][j - 2] == '-':
                possibility.append([i + 1, j - 2, False])
        except IndexError:
            pass
        try:
            if startFEN[i - 1][j - 2] == '-':
                possibility.append([i - 1, j - 2, False])
        except IndexError:
            pass
        if piece[0] == 'N':
            try:
                if startFEN[i + 2][j + 1] in 'bknpqr':
                    possibility.append([i + 2, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 2][j - 1] in 'bknpqr':
                    possibility.append([i + 2, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 2][j + 1] in 'bknpqr':
                    possibility.append([i - 2, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 2][j - 1] in 'bknpqr':
                    possibility.append([i - 2, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j + 2] in 'bknpqr':
                    possibility.append([i + 1, j + 2, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j + 2] in 'bknpqr':
                    possibility.append([i - 1, j + 2, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j - 2] in 'bknpqr':
                    possibility.append([i + 1, j - 2, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j - 2] in 'bknpqr':
                    possibility.append([i - 1, j - 2, True])
            except IndexError:
                pass
        else:
            try:
                if startFEN[i + 2][j + 1] in 'BKNPQR':
                    possibility.append([i + 2, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 2][j - 1] in 'BKNPQR':
                    possibility.append([i + 2, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 2][j + 1] in 'BKNPQR':
                    possibility.append([i - 2, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 2][j - 1] in 'BKNPQR':
                    possibility.append([i - 2, j - 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j + 2] in 'BKNPQR':
                    possibility.append([i + 1, j + 2, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j + 2] in 'BKNPQR':
                    possibility.append([i - 1, j + 2, True])
            except IndexError:
                pass
            try:
                if startFEN[i + 1][j - 2] in 'BKNPQR':
                    possibility.append([i + 1, j - 2, True])
            except IndexError:
                pass
            try:
                if startFEN[i - 1][j - 2] in 'BKNPQR':
                    possibility.append([i - 1, j - 2, True])
            except IndexError:
                pass
    elif piece[0] in 'bB':
        if piece[0] == 'b':
            c = 1
            while True:
                pos_li = i + c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j - c
                if pos_li <= 7 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j - c
                if pos_li >= 0 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
        else:
            c = 1
            while True:
                pos_li = i - c
                pos_co = j + c
                if pos_li >= 0 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j - c
                if pos_li >= 0 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j - c
                if pos_li <= 7 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
    elif piece[0] in 'rR':
        if piece[0] == 'r':
            c = 1
            while True:
                pos_li = i + c
                pos_co = j
                if pos_li <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j
                if pos_li >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j + c
                if pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j - c
                if pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
        else:
            c = 1
            while True:
                pos_li = i + c
                pos_co = j
                if pos_li <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j
                if pos_li >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j + c
                if pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j - c
                if pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
    elif piece[0] in 'qQ':
        if piece[0] == 'q':
            c = 1
            while True:
                pos_li = i + c
                pos_co = j
                if pos_li <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j
                if pos_li >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j + c
                if pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j - c
                if pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j - c
                if pos_li <= 7 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j - c
                if pos_li >= 0 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j - c
                if pos_li <= 7 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j - c
                if pos_li >= 0 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'BKNPQR':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
        else:
            c = 1
            while True:
                pos_li = i + c
                pos_co = j
                if pos_li <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j
                if pos_li >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j + c
                if pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i
                pos_co = j - c
                if pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j + c
                if pos_li >= 0 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i - c
                pos_co = j - c
                if pos_li >= 0 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j + c
                if pos_li <= 7 and pos_co <= 7:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break
            c = 1
            while True:
                pos_li = i + c
                pos_co = j - c
                if pos_li <= 7 and pos_co >= 0:
                    if startFEN[pos_li][pos_co] == '-':
                        possibility.append([pos_li, pos_co, False])
                        c += 1
                    else:
                        if startFEN[pos_li][pos_co] in 'bknpqr':
                            possibility.append([pos_li, pos_co, True])
                            break
                        else:
                            break
                else:
                    break

    return possibility


def checkingCapture(piece, startFEN, i, j):
    capture = False
    if piece[0] in 'BKNPQR' and startFEN[i][j] in 'bknpqr':
        if checkingMovement(piece, startFEN, i, j, True):
            capture = True
    elif piece[0] in 'bknpqr' and startFEN[i][j] in 'BKNPQR':
        if checkingMovement(piece, startFEN, i, j, True):
            capture = True

    return capture
