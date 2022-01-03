import pygame
from pygame.locals import *
from Bruno_Project.Most_used.cores import *
import math


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
                        pygame.draw.circle(screen, (219, 165, 140), (j*size+(size/2), i*size+(size/2)), size/7)
                    else:
                        pygame.draw.circle(screen, (219, 165, 140), (j*size+(size/2), i*size+(size/2)), size/2, 5)


def draw_pieces(sF, screen, size):
    for r, li in enumerate(sF):
        for c, co in enumerate(li):
            y = r * size
            x = c * size
            if co in 'bknpqr':
                file = f'Images/{co}.png'
                p = pygame.image.load(file)
                p = pygame.transform.scale(p, (int(size), int(size)))
                screen.blit(p, [x, y])
            elif co in 'BKNPQR':
                file = f'Images/{co.lower()}w.png'
                p = pygame.image.load(file)
                p = pygame.transform.scale(p, (int(size), int(size)))
                screen.blit(p, [x, y])


def checkingMovement(piece, startFEN, i, j, eat=False):
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
    possibility = []
    if piece[0] in 'pP':
        if piece[0] == 'p':
            if startFEN[i+1][j] == '-':
                possibility.append([i+1, j, False])
            if i == 1 and startFEN[i+1][j] == '-' and startFEN[i+2][j] == '-':
                possibility.append([i+2, j, False])
            try:
                if startFEN[i+1][j+1] in 'BKNPQR':
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
                if startFEN[i-1][j+1] in 'bknpqr':
                    possibility.append([i - 1, j + 1, True])
            except IndexError:
                pass
            try:
                if startFEN[i-1][j-1] in 'bknpqr':
                    possibility.append([i - 1, j - 1, True])
            except IndexError:
                pass
    elif piece[0] in 'kK':
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
