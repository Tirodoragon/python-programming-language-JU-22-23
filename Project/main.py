import pygame
import random
import re
import copy


# Klasa reprezentujaca statek na planszy
class Ship:
    def __init__(self, x, y, typ, identifier):
        self.id = identifier
        self.x = self.defx = x
        self.y = self.defy = y
        self.type = typ
        if typ == 1:
            self.image = pygame.transform.scale(pygame.image.load("ship1.png"),
                                                [56, 56])
        if typ == 2:
            self.image = pygame.transform.scale(pygame.image.load("ship2.png"),
                                                [56, 116])
        if typ == 3:
            self.image = pygame.transform.scale(pygame.image.load("ship3.png"),
                                                [56, 176])
        if typ == 4:
            self.image = pygame.transform.scale(pygame.image.load("ship4.png"),
                                                [56, 236])
        self.clicked = False
        self.vertical = True
        self.onboard = False

    def default_position(self):
        self.x = self.defx
        self.y = self.defy
        self.onboard = False

    def flip(self):
        if self.type != 1:
            if self.vertical:
                self.image = pygame.transform.rotate(self.image, 90)
                self.vertical = False
            else:
                self.image = pygame.transform.rotate(self.image, -90)
                self.vertical = True


# Funkcja tworzaca macierz ze statkami bazujac na polozeniu przodu statku
def create_player_board(ships):
    board = [['p' for _ in range(10)] for _ in range(10)]
    for s in ships:
        x = int(s.x / 60)
        y = int(s.y / 60)
        board[x][y] = str(s.id)
        if s.type == 2:
            if s.vertical:
                board[x][y + 1] = str(s.id)
            else:
                board[x + 1][y] = str(s.id)
        elif s.type == 3:
            if s.vertical:
                board[x][y + 1] = str(s.id)
                board[x][y + 2] = str(s.id)
            else:
                board[x + 1][y] = str(s.id)
                board[x + 2][y] = str(s.id)
        elif s.type == 4:
            if s.vertical:
                board[x][y + 1] = str(s.id)
                board[x][y + 2] = str(s.id)
                board[x][y + 3] = str(s.id)
            else:
                board[x + 1][y] = str(s.id)
                board[x + 2][y] = str(s.id)
                board[x + 3][y] = str(s.id)
    return board


# Funkcja tworzaca plansze komputera zgodnie z zasadami
def create_computer_board():
    board = [['p' for _ in range(10)] for _ in range(10)]
    t = 4
    num = 1
    id_s = 1
    for i in range(10):
        notonboard = True
        while notonboard:
            v = random.randint(0, 1)
            if v:
                x = random.randint(0, 9)
                y = random.randint(0, 9 - t)
                able = True
                for j in range(t):
                    if isinstance(board[x][y + j], int) \
                            or board[x][y + j] == 'n':
                        able = False
                if able:
                    if (y - 1) >= 0:
                        if (x - 1) >= 0:
                            board[x - 1][y - 1] = 'n'
                        if (x + 1) <= 9:
                            board[x + 1][y - 1] = 'n'
                        board[x][y - 1] = 'n'
                    for j in range(t):
                        board[x][y + j] = id_s
                        if (x - 1) >= 0:
                            board[x - 1][y + j] = 'n'
                        if (x + 1) <= 9:
                            board[x + 1][y + j] = 'n'
                    if (y + t) <= 9:
                        if (x - 1) >= 0:
                            board[x - 1][y + t] = 'n'
                        if (x + 1) <= 9:
                            board[x + 1][y + t] = 'n'
                        board[x][y + t] = 'n'
                    id_s += 1
                    notonboard = False
            else:
                x = random.randint(0, 9 - t)
                y = random.randint(0, 9)
                able = True
                for j in range(t):
                    if isinstance(board[x + j][y], int) \
                            or board[x + j][y] == 'n':
                        able = False
                if able:
                    if (x - 1) >= 0:
                        if (y - 1) >= 0:
                            board[x - 1][y - 1] = 'n'
                        if (y + 1) <= 9:
                            board[x - 1][y + 1] = 'n'
                        board[x - 1][y] = 'n'
                    for j in range(t):
                        board[x + j][y] = id_s
                        if (y - 1) >= 0:
                            board[x + j][y - 1] = 'n'
                        if (y + 1) <= 9:
                            board[x + j][y + 1] = 'n'
                    if (x + t) <= 9:
                        if (y - 1) >= 0:
                            board[x + t][y - 1] = 'n'
                        if (y + 1) <= 9:
                            board[x + t][y + 1] = 'n'
                        board[x + t][y] = 'n'
                    id_s += 1
                    notonboard = False
        num -= 1
        if num == 0:
            t -= 1
            num = 5 - t
    for i in range(10):
        for j in range(10):
            board[i][j] = str(board[i][j])
            if board[i][j] == 'n':
                board[i][j] = 'p'

    return board


# Funkcja rysujaca linie podzialu planszy
def board_lines(screen):
    for i in range(0, 601, 60):
        if i != 600:
            pygame.draw.rect(screen, "white", [0, i, 600, 1])
        else:
            pygame.draw.rect(screen, "white", [0, 599, 600, 1])
    for i in range(0, 601, 60):
        if i != 600:
            pygame.draw.rect(screen, "white", [i, 0, 1, 600])
        else:
            pygame.draw.rect(screen, "white", [599, 0, 1, 600])


# Funkcja sprawdzajaca czy statek na mapie jest zniszczony
def ship_is_destroyed(board, number):
    destroyed = True
    for i in range(10):
        for j in range(10):
            if board[i][j] == str(number):
                destroyed = False
    return destroyed


# Funkcja zmieniajaca status statku na zniszczony
def ship_destroy(board, cell):
    t = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == cell:
                board[i][j] = board[i][j].replace('t', 'z')
                for m in range(max(i - 1, 0), min(i + 1, 9) + 1):
                    for k in range(max(j - 1, 0), min(j + 1, 9) + 1):
                        if board[m][k] == 'p':
                            board[m][k] = 'n'
                t += 1
    return board, t


# Funkcja sprawdzajaca i zmieniajaca stan statku na zniszczony
def ship_destroy_computer(board):
    t = 0
    num = 0
    for i in range(10):
        for j in range(10):
            if re.search('t', board[i][j]):
                num = board[i][j].replace('t', '')
    destroyed = True
    for i in range(10):
        for j in range(10):
            if board[i][j] == num:
                destroyed = False
    if destroyed:
        for i in range(10):
            for j in range(10):
                if re.search('t', board[i][j]):
                    board[i][j] = board[i][j].replace('t', 'z')
                    for m in range(max(i - 1, 0), min(i + 1, 9) + 1):
                        for k in range(max(j - 1, 0), min(j + 1, 9) + 1):
                            if board[m][k] == 'p':
                                board[m][k] = 'n'
                    t += 1
    return board, t


# Funkcja rysujaca ruchy graczy na mapie
def board_moves(screen, board):
    down_img = pygame.transform.scale(pygame.image.load("down.png"), [60, 60])
    destroyed_img = pygame.transform.scale(pygame.image.load("destroyed.png"),
                                           [60, 60])
    for i in range(10):
        for j in range(10):
            if board[i][j] == 'n':
                pygame.draw.line(screen, "white", [i * 60, j * 60],
                                 [i * 60 + 60, j * 60 + 60])
                pygame.draw.line(screen, "white", [i * 60 + 60, j * 60],
                                 [i * 60, j * 60 + 60])
            elif re.search('t', board[i][j]):
                screen.blit(down_img, [60 * i, 60 * j])
            elif re.search('z', board[i][j]):
                screen.blit(destroyed_img, [60 * i, 60 * j])


# Funkcja sprawdzajaca czy isnieje niezatopiony statek z 3 trafieniami
def move3(board):
    for i in range(8):
        for j in range(10):
            if re.search('t', board[i][j]) and re.search('t', board[i + 1][j])\
                    and re.search('t', board[i + 2][j]):
                if i - 1 < 0:
                    board[i + 3][j] = 't' + board[i + 3][j]
                    return board
                elif i + 3 > 9:
                    board[i - 1][j] = 't' + board[i - 1][j]
                    return board
                else:
                    if board[i + 3][j] == 'n':
                        board[i - 1][j] = 't' + board[i - 1][j]
                        return board
                    elif board[i - 1][j] == 'n':
                        board[i + 3][j] = 't' + board[i + 3][j]
                        return board
                    else:
                        directory = random.randint(0, 1)
                        if directory:
                            if board[i - 1][j] != 'p':
                                board[i - 1][j] = 't' + board[i - 1][j]
                                return board
                            else:
                                board[i - 1][j] = 'n'
                                return board
                        else:
                            if board[i + 3][j] != 'p':
                                board[i + 3][j] = 't' + board[i + 3][j]
                                return board
                            else:
                                board[i + 3][j] = 'n'
                                return board
    for i in range(10):
        for j in range(8):
            if re.search('t', board[i][j]) and re.search('t', board[i][j + 1])\
                    and re.search('t', board[i][j + 2]):
                if j - 1 < 0:
                    board[i][j + 3] = 't' + board[i][j + 3]
                    return board
                elif j + 3 > 9:
                    board[i][j - 1] = 't' + board[i][j - 1]
                    return board
                else:
                    if board[i][j + 3] == 'n':
                        board[i][j - 1] = 't' + board[i][j - 1]
                        return board
                    elif board[i][j - 1] == 'n':
                        board[i][j + 3] = 't' + board[i][j + 3]
                        return board
                    else:
                        directory = random.randint(0, 1)
                        if directory:
                            if board[i][j - 1] != 'p':
                                board[i][j - 1] = 't' + board[i][j - 1]
                                return board
                            else:
                                board[i][j - 1] = 'n'
                                return board
                        else:
                            if board[i][j + 3] != 'p':
                                board[i][j + 3] = 't' + board[i][j + 3]
                                return board
                            else:
                                board[i][j + 3] = 'n'
                                return board
    return False


# Funkcja sprawdzajaca czy isnieje niezatopiony statek z 2 trafieniami
def move2(board):
    for i in range(9):
        for j in range(10):
            if re.search('t', board[i][j]) and re.search('t', board[i + 1][j]):
                if i - 1 < 0:
                    board[i + 3][j] = 't' + board[i + 2][j]
                    return board
                elif i + 2 > 9:
                    board[i - 1][j] = 't' + board[i - 1][j]
                    return board
                else:
                    if board[i + 2][j] == 'n':
                        board[i - 1][j] = 't' + board[i - 1][j]
                        return board
                    elif board[i - 1][j] == 'n':
                        board[i + 2][j] = 't' + board[i + 2][j]
                        return board
                    else:
                        directory = random.randint(0, 1)
                        if directory:
                            if board[i - 1][j] != 'p':
                                board[i - 1][j] = 't' + board[i - 1][j]
                                return board
                            else:
                                board[i - 1][j] = 'n'
                                return board
                        else:
                            if board[i + 2][j] != 'p':
                                board[i + 2][j] = 't' + board[i + 2][j]
                                return board
                            else:
                                board[i + 2][j] = 'n'
                                return board
    for i in range(10):
        for j in range(9):
            if re.search('t', board[i][j]) and re.search('t', board[i][j + 1]):
                if j - 1 < 0:
                    board[i][j + 2] = 't' + board[i][j + 2]
                    return board
                elif j + 2 > 9:
                    board[i][j - 1] = 't' + board[i][j - 1]
                    return board
                else:
                    if board[i][j + 2] == 'n':
                        board[i][j - 1] = 't' + board[i][j - 1]
                        return board
                    elif board[i][j - 1] == 'n':
                        board[i][j + 2] = 't' + board[i][j + 2]
                        return board
                    else:
                        directory = random.randint(0, 1)
                        if directory:
                            if board[i][j - 1] != 'p':
                                board[i][j - 1] = 't' + board[i][j - 1]
                                return board
                            else:
                                board[i][j - 1] = 'n'
                                return board
                        else:
                            if board[i][j + 2] != 'p':
                                board[i][j + 2] = 't' + board[i][j + 2]
                                return board
                            else:
                                board[i][j + 2] = 'n'
                                return board
    return False


# Funkcja sprawdzajaca czy isnieje niezatopiony statek z 1 trafieniem
def move1(board):
    for i in range(10):
        for j in range(10):
            if re.search('t', board[i][j]):
                move = True
                while move:
                    direction = random.randint(0, 3)
                    idir = 0
                    jdir = 0
                    if direction == 0 and i + 1 <= 9:
                        idir = 1
                    elif direction == 1 and i - 1 > - 0:
                        idir = -1
                    elif direction == 2 and j + 1 <= 9:
                        jdir = 1
                    elif direction == 3 and j - 1 >= 0:
                        jdir = -1

                    if board[i + idir][j + jdir] == 'p':
                        board[i + idir][j + jdir] = 'n'
                        return board
                    elif board[i + idir][j + jdir].isdigit():
                        board[i + idir][j + jdir] = 't' + \
                                                    board[i + idir][j + jdir]
                        return board
    return False


# Funkcja wybierajaca losowy punkt w celu wykonania ruchu
def moverandom(board):
    move = True
    while move:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if board[x][y] == 'p':
            board[x][y] = 'n'
            return board
        elif board[x][y].isdigit():
            board[x][y] = 't' + board[x][y]
            return board


# Funkcja decyzji o ruchu komputera
def computer_make_move(board):
    m3 = move3(board)
    if not m3:
        m2 = move2(board)
        if not m2:
            m1 = move1(board)
            if not m1:
                return moverandom(board)
            else:
                return m1
        else:
            return m2
    else:
        return m3


# Funkcja odnajdujaca ostatni ruch komputera
def find_move(pl_board, new_pl_board):
    for i in range(10):
        for j in range(10):
            if pl_board[i][j] != new_pl_board[i][j]:
                return i, j
    return 0, 0


# Funkcja wyswietlajaca plansze jednego z graczy
def board_show(screen, player_board, computer_board, new_pl_board):
    screen.fill("black")
    screen.blit(pygame.transform.scale(pygame.image.load("stars_texture.png"),
                                       [600, 600]), [0, 0])
    board_lines(screen)
    if computer_board is None:
        board_moves(screen, new_pl_board)
        p_x, p_y = find_move(player_board, new_pl_board)
        pygame.draw.rect(screen, "red", pygame.Rect(p_x * 60, p_y * 60, 60, 60),
                         2)
        if new_pl_board[p_x][p_y] == 'n':
            pygame.mixer.Channel(1).set_volume(0.2)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('./blaster.wav'))
            pygame.draw.line(screen, "red", [p_x * 60, p_y * 60],
                             [p_x * 60 + 60, p_y * 60 + 60])
            pygame.draw.line(screen, "red", [p_x * 60 + 60, p_y * 60],
                             [p_x * 60, p_y * 60 + 60])
        else:
            pygame.mixer.Channel(1).set_volume(0.2)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('./explosion2.wav'))
    else:
        board_moves(screen, computer_board)
    pygame.display.flip()
    return new_pl_board


# Funkcja wyswietlajaca statystyki graczy
def stats_show(screen, stats_player, stats_computer, move):
    font = pygame.font.SysFont("Arial", 30)
    if move == 0:
        text = font.render("Ruch Komputera", True, "white")
    else:
        text = font.render("Ruch Gracza", True, "white")
    screen.blit(text, [750 - text.get_width() / 2, 30])

    font = pygame.font.SysFont("Arial", 24)

    text = font.render("Statystyki gracza:", True, "white")
    screen.blit(text, [610, 110])
    text = font.render("Statystyki komputera:", True, "white")
    screen.blit(text, [610, 320])

    font = pygame.font.SysFont("Arial", 18)
    for i in range(4):
        if stats_player[3 - i] == i + 1:
            text = font.render(f"Zatopione statki {4 - i}-masztowe:"
                               f" {stats_player[3 - i]}", True, "green")
        else:
            text = font.render(f"Zatopione statki {4 - i}-masztowe:"
                               f" {stats_player[3 - i]}", True, "white")
        screen.blit(text, [610, 150 + i * 30])
    for i in range(4):
        if stats_computer[3 - i] == i + 1:
            text = font.render(f"Zatopione statki {4 - i}-masztowe:"
                               f" {stats_computer[3 - i]}", True, "red")
        else:
            text = font.render(f"Zatopione statki {4 - i}-masztowe:"
                               f" {stats_computer[3 - i]}", True, "white")
        screen.blit(text, [610, 360 + i * 30])
    pygame.display.flip()


# Funkcja menu rozstawiania statkow na planszy przez uzytkownika
def pregame(screen):
    running = True
    clock = pygame.time.Clock()
    ship4 = Ship(620, 10, 4, 1)
    ship3_1 = Ship(700, 10, 3, 2)
    ship3_2 = Ship(780, 10, 3, 3)
    ship2_1 = Ship(620, 280, 2, 4)
    ship2_2 = Ship(700, 280, 2, 5)
    ship2_3 = Ship(780, 280, 2, 6)
    ship1_1 = Ship(620, 430, 1, 7)
    ship1_2 = Ship(780, 430, 1, 8)
    ship1_3 = Ship(620, 520, 1, 9)
    ship1_4 = Ship(780, 520, 1, 10)
    ships = [ship4, ship3_1, ship3_2, ship2_1, ship2_2, ship2_3, ship1_1,
             ship1_2, ship1_3, ship1_4]
    border_x = pygame.Rect(600, 0, 1, 600)
    border_y = pygame.Rect(0, 600, 600, 1)
    all_on_board = False
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    allow = True
                    for s in ships:
                        if s.clicked:
                            allow = False
                    for s in ships:
                        if s.image.get_rect().move(s.x, s.y).\
                                collidepoint(mouse) and allow:
                            s.clicked = True
                            break
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for s in ships:
                        if s.clicked:
                            s.clicked = False
                            if mouse[0] < 600:
                                s.onboard = True
                                x_scale = int(mouse[0] / 60)
                                y_scale = int(mouse[1] / 60)
                                s.x = x_scale * 60
                                s.y = y_scale * 60
                            else:
                                s.onboard = False
                            for s2 in ships:
                                if s.id != s2.id and s2.onboard:
                                    if pygame.Rect.colliderect(
                                            s.image.get_rect().move(s.x, s.y),
                                            s2.image.get_rect().
                                            inflate(120, 120).move(s2.x, s2.y)):
                                        s.default_position()
                            if pygame.Rect.colliderect(
                                    s.image.get_rect().move(s.x, s.y),
                                    border_x) or pygame.Rect.colliderect(
                                    s.image.get_rect().move(s.x, s.y),
                                    border_y):
                                s.default_position()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    for s in ships:
                        if s.image.get_rect().move(s.x,
                                                   s.y).collidepoint(mouse)\
                                and s.onboard:
                            s.flip()
                            for s2 in ships:
                                if s.id != s2.id and s2.onboard:
                                    if pygame.Rect.colliderect(
                                            s.image.get_rect().move(s.x, s.y),
                                            s2.image.get_rect().
                                            inflate(120, 120).move(s2.x, s2.y)):
                                        s.default_position()
                                        s.flip()
                            if pygame.Rect.colliderect(
                                    s.image.get_rect().move(s.x, s.y),
                                    border_x) or pygame.Rect.colliderect(
                                    s.image.get_rect().move(s.x, s.y),
                                    border_y):
                                s.default_position()
                                s.flip()
                            break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 650 < mouse[0] < 850 and 500 < mouse[1] < 550\
                        and all_on_board:
                    player_board = create_player_board(ships)
                    computer_board = create_computer_board()
                    game(screen, player_board, computer_board)
        all_on_board = True
        for s in ships:
            if not s.onboard:
                all_on_board = False
        for s in ships:
            if s.clicked:
                s.x = mouse[0] - 30
                s.y = mouse[1] - 30
        screen.fill("black")
        if all_on_board:
            pygame.draw.rect(screen, "#006200", [650, 500, 200, 50])
            font = pygame.font.SysFont("Arial", 30)
            text = font.render("Start", True, "white")
            screen.blit(text, [750 - text.get_width() / 2, 506])
        screen.blit(pygame.transform.scale(
            pygame.image.load("stars_texture.png"), [600, 600]), [0, 0])
        board_lines(screen)
        for s in ships:
            screen.blit(s.image, [s.x, s.y])
        pygame.display.flip()
        clock.tick(60)


# Funkcja konca gry
def endgame(screen, player_wins):
    clock = pygame.time.Clock()
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 < mouse[0] < 550 and 375 < mouse[1] < 425:
                    pregame(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 < mouse[0] < 550 and 475 < mouse[1] < 525:
                    exit()
        screen.fill("black")
        screen.blit(pygame.transform.scale(
            pygame.image.load("galaxy.png"), [600, 600]), [150, 0])

        font = pygame.font.SysFont("Arial", 90)
        if player_wins:
            text = font.render("Zwycięstwo", True, "white")
        else:
            text = font.render("Porażka", True, "white")
        screen.blit(text, [450 - text.get_width() / 2, 100])

        pygame.draw.rect(screen, "#5F78FC", [300, 375, 300, 50])
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("Zagraj ponownie", True, "white")
        screen.blit(text, [450 - text.get_width() / 2, 380])

        pygame.draw.rect(screen, "red", [300, 475, 300, 50])
        text = font.render("Zakończ", True, "white")
        screen.blit(text, [450 - text.get_width() / 2, 480])

        pygame.display.flip()
        clock.tick(60)


# Funkcja glownej czesci gry w kosmiczne statki
def game(screen, player_board, computer_board):
    player_turn = random.randint(0, 1)
    running = True
    clock = pygame.time.Clock()
    ships_player = [0, 0, 0, 0]
    ships_computer = [0, 0, 0, 0]
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < mouse[0] < 600 and 0 < mouse[1] < 600 and player_turn:
                    x = int(mouse[0] / 60)
                    y = int(mouse[1] / 60)
                    if computer_board[x][y] == 'p':
                        pygame.mixer.Channel(1).set_volume(0.2)
                        pygame.mixer.Channel(1).play(
                            pygame.mixer.Sound('./blaster.wav'))
                        computer_board[x][y] = 'n'
                        board_show(screen, None, computer_board, None)
                        stats_show(screen, ships_player, ships_computer,
                                   player_turn)
                        player_turn = 0
                        pygame.time.delay(2000)
                    elif computer_board[x][y] != 'n' \
                            and computer_board[x][y] != 'p' \
                            and not re.search("t", computer_board[x][y]) \
                            and not re.search("z", computer_board[x][y]):
                        pygame.mixer.Channel(1).set_volume(0.2)
                        pygame.mixer.Channel(1).play(
                            pygame.mixer.Sound('./explosion2.wav'))
                        computer_board[x][y] = 't' + str(computer_board[x][y])
                        if ship_is_destroyed(computer_board,
                                             computer_board[x][y].
                                             replace('t', '')):
                            board, sp = ship_destroy(computer_board,
                                                     computer_board[x][y])
                            ships_player[sp - 1] += 1
                        board_show(screen, None, computer_board, None)
                        stats_show(screen, ships_player, ships_computer,
                                   player_turn)
                        if ships_computer == [4, 3, 2, 1] \
                                or ships_player == [4, 3, 2, 1]:
                            endgame(screen, player_turn)
                        player_turn = 0
                        pygame.time.delay(2000)

        if player_turn:
            board_show(screen, None, computer_board, None)
            stats_show(screen, ships_player, ships_computer, player_turn)
        else:
            board_show(screen, copy.deepcopy(player_board), None,
                       computer_make_move(player_board))
            board, sp = ship_destroy_computer(player_board)
            if sp != 0:
                ships_computer[sp - 1] += 1
                board_moves(screen, player_board)
                pygame.display.flip()
            stats_show(screen, ships_player, ships_computer, player_turn)
            pygame.time.delay(2000)
            if ships_computer == [4, 3, 2, 1] or ships_player == [4, 3, 2, 1]:
                endgame(screen, player_turn)
            player_turn = 1
        pygame.display.flip()
        clock.tick(60)
    pass


# Funkcja reprezentujaca menu glowne programu
def start():
    pygame.mixer.music.load('./Thrust Sequence.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    size = (900, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_icon(pygame.image.load("icon.png"))
    pygame.display.set_caption("Kosmiczne Statki")
    running = True
    clock = pygame.time.Clock()
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 < mouse[0] < 550 and 375 < mouse[1] < 425:
                    pregame(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 < mouse[0] < 550 and 475 < mouse[1] < 525:
                    exit()
        screen.blit(pygame.transform.scale(pygame.image.load("galaxy.png"),
                                           [600, 600]), [150, 0])

        font = pygame.font.SysFont("Arial", 90)
        text = font.render("Kosmiczne Statki", True, "white")
        screen.blit(text, [450 - text.get_width() / 2, 100])

        pygame.draw.rect(screen, "#5F78FC", [350, 375, 200, 50])
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("Start", True, "white")
        screen.blit(text, [450 - text.get_width() / 2, 380])

        pygame.draw.rect(screen, "red", [350, 475, 200, 50])
        text = font.render("Zamknij", True, "white")
        screen.blit(text, [450 - text.get_width() / 2, 480])

        pygame.display.flip()
        clock.tick(60)


def main():
    pygame.init()
    start()
    pygame.quit()

main()
