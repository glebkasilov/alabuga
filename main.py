import os
import time
import inquirer
import random
import curses


class programmer():
    def __init__(self, health=10, intelligence=4, level=0, money=100, mind=10) -> None:
        self.health = health
        self.intelligence = intelligence
        self.level = level
        self.money = money
        self.mind = mind
        self.sleep_time = 15
        self.money_for_work = 0
        self.work_shift = 0
        self.dead = False

    def stats(self) -> None:
        print(f"Его стата:\nЗдоровье - {self.health}\nУровень интелекта - {self.intelligence}\nГрейд - {
              self.get_level()}\nКоличество денег - {self.money} руб.\nДуховное здровье - {self.mind}\n")

    def get_level(self) -> str:
        if self.level == 0:
            return "Junior"
        elif self.level == 1:
            return "Middle"
        elif self.level == 2:
            return "Senior"

    def add_health(self):
        self.health = min(self.health + 2, 10)

    def reading_book(self):
        beautiful_print("Ваш персонаж слишком глупый, чтобы сам выбрать книгу")
        beautiful_print("Предложите её ему:")
        book = input()
        add_intelligence = random.randint(1, 3)
        self.intelligence += add_intelligence

        print()

        if add_intelligence == 3:
            beautiful_print(
                "Книга, предложенная песонажу, была чрезвычайно гениальна")

        elif add_intelligence == 2:
            beautiful_print(
                "Книга, предложенная песонажу, была средничком, много знаний с нее он не получил, но хоть что-то узнал")

        elif add_intelligence == 1:
            beautiful_print(
                "Даже для Вашего персонажа эта книга была очень не очень")

        print(f"Уровень интелекта Вашего понднялся на {add_intelligence}")
        print(f"Его интелект теперь на уровене {self.intelligence}")

        time.sleep(1.5)

    def do_meditation(self):
        clear_console()
        beautiful_print("Расслабьтесь и оглягнитесь по сторонам")
        beautiful_print("Если вокруг Вас, кто-то есть - не оглядывайтесь")
        beautiful_print("Войдите в зону комфорта и забудьте обо всем")
        beautiful_print("В целом мире остались только Вы и Ваше спокойствие")
        beautiful_print(
            "Хорошая новость: Вы отдохнули;\n Другая хорошая новость, что Ваш персонаж - нет")
        time.sleep(1.5)
        clear_console()

        beautiful_print(
            "Персонаж пошел заниматься медитацией и обретать душевный покой:")
        for i in range(30, 0, -1):
            clear_console()
            print(f"Ваш песонаж занимается йогой еще {i} секунд")
            time.sleep(1)

        clear_console()

        beautiful_print("Ваш персонаж отдохнул")
        self.mind = min(self.mind + 3, 10)
        print(f"Уровень его душевного сознания поднялся до {self.mind}")
        time

    def sleep(self):
        for i in range(self.sleep_time, 0, -1):
            print(f"Ваш песонаж спит еще {i} секунд")
            time.sleep(1)
            clear_console()
        self.sleep_time += 15
        self.add_health()

    def serch_work(self):
        if self.level == 0:
            self.money_for_work = random.randint(100, 500)
        elif self.level == 1:
            self.money_for_work = random.randint(400, 1200)
        elif self.level == 2:
            self.money_for_work = random.randint(1000, 10000)
        for i in range(random.randint(10, 30), 0, -1):
            print(f"Он продлиться еще {i} секунд")
            time.sleep(1)
            clear_console()

    def working(self):
        for i in range(12, 0, -1):
            clear_console()
            print(f"Ваш песонаж работает еще {i} секунд")
            time.sleep(1)
        clear_console()
        self.health -= 1
        print(f"У Вас осталось {self.health} HP")
        self.money += self.money_for_work
        print(f"Теперь ваш баланс {self.money}")
        self.work_shift += 1
        time.sleep(2)
        clear_console()

    def do_work(self):
        if self.work_shift == 0:
            beautiful_print("Поздравляем Вас с первой рабочей сменой!")
            beautiful_print("Вы чувствуете себя хорошо")
            beautiful_print("Но есть один минус(")
            beautiful_print("От работы кони дохнут")
            beautiful_print("Вы хоть и не конь, наверно")
            beautiful_print("Хотя от куда я знаю, кто играет в мою игру?",
                            right_interval=0.04, left_interval=0.01, revese=True, wait_time=0.2)
            beautiful_print("ПРЕДУПРЕЖДЕНИЕ:")
            beautiful_print(
                "НЕ ПЕРЕУСРЕДСВУЙТЕ НА РАБОТЕ, ЕСТЬ СТРАХ УМЕРЕТЬ!")
            beautiful_print(
                "Будьте внимательны, и хорошего Вам первого рабочего дня)")
            beautiful_print(
                "Ps. Чтобы вам не ждать 12 часов, ваша компания сократила рабочий день до 12 секунд, но это только для Вас")
            beautiful_print("Вас же работник работает так же 12 часов)")
            self.working()

        else:
            beautiful_print("Поздравляем Вас с очередной рабочей сменой!")
            print(f"Она у Вас уже: {player.work_shift}")
            self.working()
            if self.health == 0:
                beautiful_print("Хорошая новость, Вы сдохли!")
                self.dead = True


player = None
player_grisha = programmer()
player_seresa = programmer(6, 6, 1, 600, 6)
player_kesha = programmer(2, 10, 2, 10000, 3)


def beautiful_print(text, revese=False, right_interval=0.08, left_interval=0.07, wait_time=1.2):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(right_interval)
    time.sleep(wait_time)
    if not revese:
        print("\n")

    else:
        for i in range(len(text), -1, -1):
            print('\r' + text[:i], end=' ', flush=False)
            time.sleep(left_interval)
        print("\r", end="")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter():
    print("Нажмите 'Enter' чтобы продолжить")
    while input() != "":
        pass
    clear_console()


def chess():
    WHITE = 1
    BLACK = 2

    def correct_coords(row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def opponent(color):
        if color == WHITE:
            return BLACK
        else:
            return WHITE

    class Black():
        def __eq__(self, other):
            return isinstance(other, Black)

        def opponent(self):
            return White()

        def is_black(self):
            return True

        def is_white(self):
            return False

    class White():
        def __eq__(self, other):
            return isinstance(other, White)

        def opponent(self):
            return Black()

        def is_black(self):
            return False

        def is_white(self):
            return True

    class Knight:
        def __init__(self, color) -> None:
            self.color = color

        def can_move(self, row, col, row1, col1, board):
            if not (0 <= row1 < 8 and 0 <= col1 < 8) or not board:
                return False
            if abs(row - row1) * abs(col - col1) != 2 or not board:
                return False
            return True

        def set_position(self, row1, col1):
            self.row = row1
            self.col = col1

        def get_color(self):
            return self.color

        def char(self):
            return 'N'

        def is_king(self):
            return False

    class King:
        def __init__(self, color) -> None:
            self.color = color
            self.new = True

        def can_move(self, row, col, row1, col1, board):
            if row + 1 == row1 or \
                    row - 1 == row1 or \
                    row - 1 == row1 and col + 1 == col1 or \
                    row + 1 == row1 and col + 1 == col1 or \
                    row + 1 == row1 and col - 1 == col1 or \
                    row - 1 == row1 and col - 1 == col1 or \
                    col - 1 == col1 or \
                    col + 1 == col1 and board:
                self.new = False
                return True
            else:
                return False

        def set_position(self, row1, col1):
            self.row = row1
            self.col = col1

        def get_color(self):
            return self.color

        def is_king(self):
            return True

        def char(self):
            return 'K'

    class Queen:
        def __init__(self, color) -> None:
            self.color = color

        def can_move(self, row, col, row1, col1, board):
            if not correct_coords(row1, col1):
                return False
            piece1 = board[row1][col1]
            if not (piece1 is None) and piece1.get_color() == self.color:
                return False
            if row == row1 or col == col1:
                step = 1 if (row1 >= row) else -1
                for r in range(row + step, row1, step):
                    if not (board[r][col] is None):
                        return False
                step = 1 if (col1 >= col) else -1
                for c in range(col + step, col1, step):
                    if not (board[row][c] is None):
                        return False
                self.new = False
                return True
            if row - col == row1 - col1:
                step = 1 if (row1 >= row) else -1
                for r in range(row + step, row1, step):
                    c = col - row + r
                    if not (board[r][c] is None):
                        return False
                self.new = False
                return True
            if row + col == row1 + col1:
                step = 1 if (row1 >= row) else -1
                for r in range(row + step, row1, step):
                    c = row + col - r
                    if not (board[r][c] is None):
                        return False
                self.new = False
                return True
            return False

        def can_attack(self, board, row, col, row1, col1):
            return self.can_move(self, board, row, col, row1, col1)

        def set_position(self, row1, col1):
            self.row = row1
            self.col = col1

        def get_color(self):
            return self.color

        def char(self):
            return 'Q'

        def is_king(self):
            return False

    class Pawn:
        def __init__(self, color) -> None:
            self.color = color

        def set_position(self, row, col):
            self.row = row
            self.col = col

        def char(self):
            return 'P'

        def get_color(self):
            return self.color

        def can_move(self, row, col, row1, col1, board):
            # Пешка может сделать из начального положения ход на 2 клетки
            # вперёд, поэтому поместим индекс начального ряда в start_row.
            if self.color == WHITE:
                direction = 1
                start_row = 1
            else:
                direction = -1
                start_row = 6

            # ход на 1 клетку
            if row + direction == row1 and board[row1][col1] is None:
                return True

            # ход на 2 клетки из начального положения
            if row == start_row and board[row1][col1] is None:
                return True

            if row + direction == row1 and (col + 1 == col1 or col - 1 == col1) \
                    and board[row1][col1]:
                if board[row1][col1].get_color() != self.color:
                    return True

            return False

        def is_king(self):
            return False

    class Bishop:
        def __init__(self, color) -> None:
            self.color = color

        def can_move(self, row, col, row1, col1, board):
            if not (0 <= row1 < 8 and 0 <= col1 < 8) or not board:
                return False
            if abs(row1 - row) != abs(col1 - col) or not board:
                return False
            return True

        def set_position(self, row1, col1):
            self.row = row1
            self.col = col1

        def get_color(self):
            return self.color

        def char(self) -> str:
            return 'B'

        def is_king(self):
            return False

    class Rook:
        def __init__(self, color) -> None:
            self.color = color
            self.new = True

        def set_position(self, row, col):
            self.row = row
            self.col = col

        def char(self):
            return 'R'

        def get_color(self):
            return self.color

        def can_move(self, row, col, row1, col1, board):
            # Невозможно сделать ход в клетку, которая не лежит в том же ряду
            # или столбце клеток.
            if row != row1 and col != col1:
                return False

            self.new = False
            return True

        def is_king(self):
            return False

    class Board:
        def __init__(self):
            self.color = WHITE
            self.field = [[None] * 8 for i in range(8)]

            for col in range(8):
                self.field[6][col] = Pawn(BLACK)
                self.field[1][col] = Pawn(WHITE)

            self.field[0][0] = Rook(WHITE)
            self.field[0][1] = Knight(WHITE)
            self.field[0][2] = Bishop(WHITE)
            self.field[0][3] = Queen(WHITE)
            self.field[0][4] = King(WHITE)
            self.field[0][5] = Bishop(WHITE)
            self.field[0][6] = Knight(WHITE)
            self.field[0][7] = Rook(WHITE)

            self.field[7][0] = Rook(BLACK)
            self.field[7][1] = Knight(BLACK)
            self.field[7][2] = Bishop(BLACK)
            self.field[7][3] = Queen(BLACK)
            self.field[7][4] = King(BLACK)
            self.field[7][5] = Bishop(BLACK)
            self.field[7][6] = Knight(BLACK)
            self.field[7][7] = Rook(BLACK)

        def current_player_color(self):
            return self.color

        def cell(self, row, col):
            piece = self.field[row][col]
            if piece is None:
                return '  '
            color = piece.get_color()
            c = 'w' if color == WHITE else 'b'
            return c + piece.char()

        def move_piece(self, row, col, row1, col1):
            def is_path_clear():
                delta_row = 1 if row1 > row else -1 if row1 < row else 0
                delta_col = 1 if col1 > col else -1 if col1 < col else 0

                check_row, check_col = row + delta_row, col + delta_col
                while check_row != row1 or check_col != col1:
                    if self.field[check_row][check_col] is not None:
                        return False
                    check_row += delta_row
                    check_col += delta_col
                return True

            if not correct_coords(row, col) or not correct_coords(row1, col1):
                return False
            if row == row1 and col == col1:
                return False  # нельзя пойти в ту же клетку
            piece = self.field[row][col]
            if piece is None:
                return False
            if piece.get_color() != self.color:
                return False
            if isinstance(piece, King) and not is_path_clear():
                return False
            if not piece.can_move(row, col, row1, col1, self.field):
                return False

            self.field[row][col] = None  # Снять фигуру.
            self.field[row1][col1] = piece  # Поставить на новое место.
            piece.set_position(row1, col1)
            self.color = opponent(self.color)
            return True

        def move_and_promote_pawn(self, row, col, row1, col1, char):
            if not isinstance(self.field[row][col], Pawn):
                return False
            if not self.move_piece(row, col, row1, col1):
                return False
            if char == 'Q':
                self.field[row1][col1] = Queen(self.field[row1][col1].color)
            elif char == 'N':
                self.field[row1][col1] = Knight(self.field[row1][col1].color)
            elif char == 'B':
                self.field[row1][col1] = Bishop(self.field[row1][col1].color)
            elif char == 'R':
                self.field[row1][col1] = Rook(self.field[row1][col1].color)
            return True

        def castling0(self):
            active_colour = (1 if self.color == 2 else 0) * 7
            if isinstance(self.field[active_colour][4], King) and isinstance(self.field[active_colour][0], Rook):
                if isinstance(self.field[active_colour][4], King) and \
                        isinstance(self.field[active_colour][0], Rook):
                    if self.field[active_colour][4].new and self.field[active_colour][0].new and \
                            not any((
                                self.field[active_colour][1],
                                self.field[active_colour][2],
                                self.field[active_colour][3]
                            )):
                        self.field[active_colour][2] = self.field[active_colour][4]
                        self.field[active_colour][4] = None

                        self.field[active_colour][3] = self.field[active_colour][0]
                        self.field[active_colour][0] = None

                        self.color = opponent(self.color)
                        return True
            return False

        def castling7(self):
            active_colour = (1 if self.color == 2 else 0) * 7
            if isinstance(self.field[active_colour][4], King) and isinstance(self.field[active_colour][7], Rook):
                if isinstance(self.field[active_colour][4], King) and isinstance(self.field[active_colour][7], Rook):
                    if self.field[active_colour][4].new and self.field[active_colour][7].new and \
                            not any((self.field[active_colour][6], self.field[active_colour][5])):
                        self.field[active_colour][6] = self.field[active_colour][4]
                        self.field[active_colour][4] = None

                        self.field[active_colour][5] = self.field[active_colour][7]
                        self.field[active_colour][7] = None

                        self.color = opponent(self.color)
                        return True
            return False

        def get_piece(self, row, col):
            if correct_coords(row, col):
                return self.field[row][col]
            else:
                return None

        def is_under_attack(self, row, col, color):
            mass = []
            for i in range(8):
                for j in range(8):
                    piece = self.field[i][j]
                    if piece is not None and piece.get_color() == color:
                        if piece.can_move(row, col, self.field):
                            for k in range(8):
                                for n in range(8):
                                    if piece.can_move(k, n, self.field):
                                        mass.append((k, n))
            if (row, col) in mass:
                return True
            else:
                return False

        def checkmate(self, color):
            for i in range(8):
                for j in range(8):
                    if self.field[i][j] is not None:
                        if self.field[i][j].get_color() == color and self.field[i][j].is_king():
                            return False
            return True

        def __str__(self):
            print('     +----+----+----+----+----+----+----+----+')
            for row in range(7, -1, -1):
                print(' ', row, end='  ')
                for col in range(8):
                    print('|', self.cell(row, col), end=' ')
                print('|')
                print('     +----+----+----+----+----+----+----+----+')
            print(end='        ')
            for col in range(8):
                print(col, end='    ')
            return '\n'

    board = Board()
    print("\n     Начальная доска:\n")
    print(board)

    while True:
        print("\n     Ход белых:")
        while True:
            row = int(input('     Введите строку откуда: '))
            col = int(input('     Введите столбец откуда: '))
            row1 = int(input('     Введите строку куда: '))
            col1 = int(input('     Введите столбец куда: '))
            if board.move_piece(row, col, row1, col1):
                print(board)
                break
            else:
                print(board)
                print("\n     Неверные координаты!\n")
                print("     Введите координаты еще раз:\n")

        if board.checkmate(2):
            print("     Белые победили!")
            break

        print("\n     Ход черных:")
        while True:
            row = int(input('     Введите строку откуда: '))
            col = int(input('     Введите столбец откуда: '))
            row1 = int(input('     Введите строку куда: '))
            col1 = int(input('     Введите столбец куда: '))
            if board.move_piece(row, col, row1, col1):
                print(board)
                break
            else:
                print(board)
                print("     Неверные координаты!\n\n")
                print("     Введите координаты еще раз:\n")

        if board.checkmate(1):
            print("     Черные победили!")
            break


def snake() -> bool:
    s = curses.initscr()
    curses.curs_set(0)
    sh, sw = s.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], ord('0'))

    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 1),
                    random.randint(1, sw - 1)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], ord('0'))
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
            break

        if len(snake) == 8:
            curses.endwin()
            return True

    curses.endwin()

    return False


def start():
    beautiful_print("Добро пожаловать в Жизнь!", revese=True)
    beautiful_print("Ха-ха-ха, ладно, просто играть в жизнь - скучно!!!")
    beautiful_print("А вот побыть в шкуре программиста - это уже другое")

    beautiful_print(
        "Так давайте погрузимся и узнаем какого быть программистом на самом деле???")

    while True:
        questions = [
            inquirer.List('choice',
                          message="Хотите ли Вы погрузиться в незабываемое путешествие?",
                          choices=['Да', 'Нет', 'Выход'])
        ]

        choice = inquirer.prompt(questions)['choice']

        if choice == 'Да':
            introduction_into_situation()
            break

        elif choice == 'Нет':
            clear_console()
            beautiful_print("Знаешь чей ответ?", right_interval=0.04,
                            left_interval=0.01, revese=True, wait_time=0.2)

            beautiful_print(
                "Ты ТОЧНО хочешь остаться в этом скучном, отвратном, невыносимом мире?!")
            questions_no = [
                inquirer.List('choice',
                              message="А если подумать, ты передумаешь?",
                              choices=['Да', 'Нет'])
            ]
            choice = inquirer.prompt(questions_no)['choice']

            if choice == 'Да':
                beautiful_print("Люблю тебя <3")
                introduction_into_situation()

            if choice == 'Нет':
                beautiful_print(
                    "НУ И ОСТАВАЙСЯ ОДИН В ЭТОМ ОМЕРЗИЕТЛЬНОМ МИРЕ, А ТЫ ВЕДЬ МОГ ОТПРАВИТСЯ СО МНОЙ В ТАКОЕ ПУТЕШЕСВИЕ!", right_interval=0.04)

            break

        elif choice == 'Выход':
            clear_console()
            print("Ну а зачем я тогда старался?\n")

            questions_no = [
                inquirer.List('choice',
                              message="Может ты передумаешь?",
                              choices=['Да', 'Нет'])
            ]
            choice = inquirer.prompt(questions_no)['choice']

            if choice == 'Да':
                beautiful_print(
                    "Люблю тебя <3, но не так сильно, как того, кто сразу нажал 'Да'")
                introduction_into_situation()

            if choice == 'Нет':
                print("Я обиделся...")

            break


def introduction_into_situation():
    global player
    clear_console()
    beautiful_print("Ну, чтож ты тут, а это значит, что игра началась:\n")

    players = ['Гриша', 'Сережа', 'Иннокентий']
    while True:
        questions = [
            inquirer.List('choice',
                          message="Давай для начала выберем кем ты хочешь быть?",
                          choices=players)
        ]
        choice = inquirer.prompt(questions)['choice']

        if choice == 'Гриша':
            clear_console()
            beautiful_print(
                "Гриша - это настоящий 'Кент', всегда здоров, разум его крепок, здоровье велико, но одна проблема - в айтишке он полный джун(")
            player_grisha.stats()

            questions_grisha = [
                inquirer.List('choice',
                              message="Берем Гришу?)",
                              choices=['Да', 'Нет'])
            ]
            choice = inquirer.prompt(questions_grisha)['choice']

            if choice == "Да":
                player = player_grisha
                explanation_of_goals()
                break

            else:
                clear_console()
                choice = None
                if len(players) > 2:
                    players.pop(players.index('Гриша'))
                else:
                    beautiful_print(
                        "Не обезсудь, но ты Гришаня по душе и никак больше, поэтому будешь им)")
                    player = player_grisha
                    explanation_of_goals()
                    break
                continue

        elif choice == 'Сережа':
            clear_console()
            beautiful_print("Сережа - это тот самый чел, который за минуту до волны хайпа айтишки начал ей заниматься(поэтому уже успел подкачаться),\nон, конечно, уже не огурец, но и не мудрец, в общем, не трепи мозги и вот")
            player_seresa.stats()

            print("Ps. Смотря на его статы, мне иногда кажется, что он шестерка...")

            questions_seresa = [
                inquirer.List('choice',
                              message="Берем Сережу?)",
                              choices=['Да', 'Нет'])
            ]
            choice = inquirer.prompt(questions_seresa)['choice']

            if choice == "Да":
                beautiful_print(
                    "А ведь может быть, что Гриша и Кеша обидятся(")
                player = player_seresa
                explanation_of_goals()
                break

            else:
                beautiful_print("Ну и правильно, туда этого Сережу")
                clear_console()
                choice = None
                if len(players) > 2:
                    players.pop(players.index('Сережа'))
                else:
                    beautiful_print(
                        "Не обезсудь, но с Сережей у тебя судьба, ты будешь им)")
                    player = player_seresa
                    explanation_of_goals()
                    break
                continue

        elif choice == 'Иннокентий':
            clear_console()
            beautiful_print("Иннокентий полностью оправдывает свое название. Тот самы чел, который родился с книжкой по си в руках.\nВ 10 лет он уже разработал свою операционую систему, но подумал, что это по позерски и перешел на линукс\nВстречайте, Кеша!:")
            player_kesha.stats()

            print("Ps. Смотря на него становится страшно, ведь ты вспоминаешь, что это человек, а не чищеный компьютер только в последнюю очередь")

            questions_kesha = [
                inquirer.List('choice',
                              message="Согласен стать Кешей?)",
                              choices=['Да', 'Нет'])
            ]
            choice = inquirer.prompt(questions_kesha)['choice']

            if choice == "Да":
                clear_console()
                beautiful_print(
                    "Извини, но Кеша слишком идеален для тебя, но из-за твоего старания, ты похож на Сережу, так что будешь им)")
                player_seresa.stats()
                player = player_seresa
                explanation_of_goals()
                break

            else:
                beautiful_print("Это был глупый поступок, даже очень глупый")
                clear_console()
                choice = None
                if len(players) > 2:
                    players.pop(players.index('Иннокентий'))
                else:
                    beautiful_print(
                        "Учитывая твой выбор, ты определенно Гриша, так что, вот его характеристики и запомни, что Кеша - лучший")
                    player_grisha.stats()
                    player = player_grisha
                    explanation_of_goals()
                    break

                continue


def explanation_of_goals():
    beautiful_print(
        "Ну, чтож, когда мы определились с нашим персонажем можно переходить к основной игре:")
    beautiful_print(
        "Наша цель - стать натсоящим прогером, заработать море деняг и создать то, что не создавал никто")
    beautiful_print(
        "Теперь, надо поднять характеристики, ведь какие мы прогеры без звания Сеньера?")
    time.sleep(1.5)
    clear_console()
    hub()


def hub():
    global player
    while True:
        if player.dead:
            break
        points = [
            inquirer.List('choice',
                          message="Выбери действие",
                          choices=["Статистика персонажа", "Отдохнуть", "Пойти прокачиваться", "Работа"])
        ]

        choice = inquirer.prompt(points)['choice']

        if choice == "Статистика персонажа":
            clear_console()
            player.stats()
            press_enter()

        elif choice == "Отдохнуть":
            if player.sleep_time == 15:
                clear_console()
                beautiful_print("Механика сна очень простая:")
                beautiful_print(
                    "Когда ты спишь - ты востанавливаешь силы, но согласись, что просто так спать нельзя")
                beautiful_print("Поэтому постоянно спать - нельзя")
                beautiful_print("И твой сон входит в привычку...")
                time.sleep(2)
                clear_console()
            player.sleep()

        elif choice == "Пойти прокачиваться":
            leveling_uping()

        elif choice == "Работа":
            while True:
                if player.dead:
                    break

                clear_console()
                if player.money_for_work == 0:
                    mass = ["Искать работу", "Выйти"]
                else:
                    mass = ["Сведенья о работе", "Пойти на работу",
                            "Сметить работу", "Уволится с работы", "Выйти"]

                work_points = [
                    inquirer.List('choice',
                                  message="Выбери действие",
                                  choices=mass)
                ]
                choice_work = inquirer.prompt(work_points)['choice']

                if choice_work == "Выйти":
                    clear_console()
                    break

                elif choice_work == "Искать работу":
                    clear_console()
                    beautiful_print(
                        "Вы ищите работу, этот процесс не стабильный...")
                    player.serch_work()

                elif choice_work == "Сведенья о работе":
                    clear_console()
                    beautiful_print("Работа у Вас достаточно хорошая")
                    print(f"На ней Ваша зарабатная плата равняется: {
                          player.money_for_work} руб.\n")
                    press_enter()

                elif choice_work == "Уволится с работы":
                    work_no = [
                        inquirer.List('choice',
                                      message="Вы точно хотите уволиться с работы?",
                                      choices=["Да", "Нет"])
                    ]
                    choice_work_no = inquirer.prompt(work_no)['choice']
                    if choice_work_no == "Да":
                        player.money_for_work = 0
                        clear_console()
                        beautiful_print("Вы теперь безработный!")
                        time.sleep(1.5)
                    else:
                        clear_console()

                elif choice_work == "Сметить работу":
                    beautiful_print(
                        "Происходит процесс смены работы, это процесс не стабильный...")
                    player.serch_work()
                    continue

                elif choice_work == "Пойти на работу":
                    clear_console()
                    player.do_work()

                choice_work = None


def leveling_uping():
    global player
    while True:
        clear_console()
        if player.dead:
            break

        points = [
            inquirer.List('choice',
                          message="Выбери действие",
                          choices=["Прокачка интелекта", "Медитации", "Повышение квалификации", "Выйти"])
        ]

        choice = inquirer.prompt(points)['choice']

        if choice == "Выйти":
            clear_console()
            break

        elif choice == "Повышение квалификации":
            while True:
                clear_console()
                if player.level == 0:
                    beautiful_print("Твой следующий уровень - 'Middle'")
                    beautiful_print(
                        "Для того чтобы им стать тебе минимум нужны характеристики:")
                    print("Интелект - 6")
                    print("Сознание - 6\n")
                    if player.intelligence >= 6 and player.mind >= 6:
                        up_points = [
                            inquirer.List('choice',
                                          message="Ты хочешь им стать?",
                                          choices=["Да", "Нет"])
                        ]

                        up_choice = inquirer.prompt(up_points)['choice']

                        if up_choice == "Да":
                            up_choice = None
                            player.level = 1
                            clear_console()
                            beautiful_print("Поздравляю, Вы стали Middleом!")
                            break

                        else:
                            up_choice = None
                            clear_console()
                            break

                    else:
                        print()
                        press_enter()
                        break

                elif player.level == 1:
                    beautiful_print("Твой следующий уровень - 'Senior'")
                    beautiful_print(
                        "Для того чтобы им стать тебе минимум нужны характеристики:\n")
                    print("Интелект - 10")
                    print("Сознание - 8\n")
                    if player.intelligence >= 10 and player.mind >= 8:
                        up_points = [
                            inquirer.List('choice',
                                          message="Ты хочешь им стать?",
                                          choices=["Да", "Нет"])
                        ]

                        up_choice = inquirer.prompt(up_points)['choice']

                        if up_choice == "Да":
                            up_choice = None
                            player.level = 1
                            clear_console()
                            beautiful_print(
                                "Поздравляю, Вы прошли игру и стали первоклассным Seniorом!")
                            time.sleep(10)
                            player.dead = True
                            break

                        else:
                            up_choice = None
                            clear_console()
                            break

                    else:
                        print()
                        press_enter()
                        break

        elif choice == "Медитации":
            clear_console()
            beautiful_print("Стоимость одной медитации равняется 800 руб.")
            points_meditation = [
                inquirer.List('choice',
                              message="Пойдете ли Вы на медитацию?",
                              choices=["Да", "Нет", "Подумаю"])
            ]

            choice_meditation = inquirer.prompt(points_meditation)['choice']

            if choice_meditation == "Да":
                if player.money >= 800:
                    player.do_meditation()
                    player.money -= 800

                else:
                    beautiful_print("Извините, но бедных не берем(")
                    time.sleep(1.5)
                    clear_console()

            elif choice_meditation == "Нет":
                clear_console()
                beautiful_print("Наверно, тебе жалко деняг, бедный игрок(")
                clear_console()

            elif choice_meditation == "Подумаю":
                clear_console()
                beautiful_print(
                    "Ой, ну ты, как мама, всегда подумаю, а потом все равно нет(")
                clear_console()

            choice_meditation = None

        elif choice == "Прокачка интелекта":
            choice = None
            while True:
                clear_console()
                intelligece_point = [
                    inquirer.List('choice',
                                  message="Выбери каким способом хочешь прокачать интелект",
                                  choices=["Чтение книги", "Игра в змейку", "Игра в шахматы", "Выйти"])
                ]

                intelligece_choice = inquirer.prompt(
                    intelligece_point)['choice']

                if intelligece_choice == "Выйти":
                    clear_console()
                    break

                elif intelligece_choice == "Чтение книги":
                    clear_console()
                    player.reading_book()

                elif intelligece_choice == "Игра в шахматы":
                    clear_console()

                    beautiful_print(
                        "В этой игре, есть один подвох, что вы будете играть в шахматы сам с собой")
                    beautiful_print("Вы скажите: 'Зачем сам с собой!?'")
                    beautiful_print("Все просто!")
                    beautiful_print(
                        "Ваш персонаж - программист!, не забывайте это")
                    beautiful_print(
                        "Был бы он каким-нибудь сварщиком я бы еще понял, но он же программист!")
                    beautiful_print(
                        "Не смотря на его звание, я все-таки должен спросить у Вас")
                    beautiful_print(
                        "Хотите ли Вы сыграть в шахматы сами с собой?")
                    beautiful_print(
                        "Да, конечно, это круто, чтобы быстро повысить интелект Вашего песонажа, но это игра принесет ему таже большой вред")
                    beautiful_print("Ведь, его кукуха может уехать сама собой")
                    chess_point = [
                        inquirer.List('choice',
                                      message="Ты уверен в своем решении и есть ли у тебя 1000 руб.?",
                                      choices=["Да, кончено", "Нет, но подумаю"])
                    ]

                    chess_choice = inquirer.prompt(chess_point)['choice']

                    if chess_choice == "Да, кончено":
                        if player.money >= 1000:
                            chess()
                            player.money -= 1000
                            player.intelligence += 5
                            player.mind -= 3
                            beautiful_print(
                                "Поздравляем, ты выйграл в шахматах!", wait_time=2)
                            print(f"Ваши мозги на {
                                  player.intelligence} уровне")
                            print(f"А ваш баланс {player.money} руб.")
                            print(f"Ваше сознание на {player.mind}")
                            clear_console()

                        else:
                            beautiful_print("Извините, но бедных не берем(")
                            time.sleep(1.5)
                            clear_console()

                    elif chess_choice == "Нет, но подумаю":
                        clear_console()
                        beautiful_print(
                            "Наверно, ты исправишь свое решение, когда подумаешь")
                        clear_console()

                elif intelligece_choice == "Игра в змейку":
                    clear_console()
                    beautiful_print(
                        "Это та самая страя и добрая игра в змейку")
                    beautiful_print(
                        "Ваша задача просто собрать змейку из 8 частей")
                    beautiful_print("Одна попытка - 600 руб.")

                    snake_point = [
                        inquirer.List('choice',
                                      message="Поехали?",
                                      choices=["Yes", "Нет, я не умею играть в змеюку"])
                    ]

                    snake_choice = inquirer.prompt(snake_point)['choice']

                    if snake_choice == "Yes":
                        if player.money >= 600:
                            win = snake()
                            player.money -= 600
                            if win:
                                clear_console()
                                beautiful_print(
                                    "Поздравляем, Вы прошли игру!)")
                                player.intelligence += 3
                                print(f"Ваши мозги на {
                                      player.intelligence} уровне")
                            else:
                                beautiful_print("Повезет в следующий раз!")
                                beautiful_print(
                                    "Не расстраивайся, возможно, ты просто неудачник!)")
                            print(f"А ваш баланс {player.money} руб.")

                            time.sleep(4)
                            clear_console()

                        else:
                            beautiful_print("Извините, но идите работать(")
                            time.sleep(1.5)
                            clear_console()

                    elif snake_choice == "Нет, я не умею играть в змеюку":
                        clear_console()
                        beautiful_print(
                            "Наверно, тебе стоит больше тренировать(")
                        clear_console()

                intelligece_choice = None

        choice = None


if __name__ == "__main__":
    snake()
