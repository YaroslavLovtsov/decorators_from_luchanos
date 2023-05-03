from random import randint
from Block3.MyTreasury.pseudo_graph import PseudoGraph as Pg


class Desk:
    def __init__(self, y, x):
        self.desk = [[0 for _ in range(8)] for _ in range(8)]
        self.desk[y][x] = 1
        self.current_y = y
        self.current_x = x
        self.start_y = y
        self.start_x = x
        self.forbidden_64 = []
        self.forbidden_64_fails = 0
        self.current_move = 1
        self.no_moves = False
        self.moves_archive = []
        self.success = False

    def scan_fields(self, yy, xx):
        h_list = [h_ind for h_ind in range(yy - 2, yy + 3) if h_ind * (7 - h_ind) >= 0]
        v_list = [v_ind for v_ind in range(xx - 2, xx + 3) if v_ind * (7 - v_ind) >= 0]

        result = []
        for elem in \
                [[(h_ind, v_ind) for v_ind in v_list if (h_ind - yy) ** 2 + (v_ind - xx) ** 2 == 5] for h_ind in h_list
                 ]:
            for elem02 in elem:
                if self.desk[elem02[0]][elem02[1]] == 0:
                    result.append((elem02[0], elem02[1]))

        return result

    def check_possible_move(self, check_list):
        self.moves_archive.append((self.current_y, self.current_x, check_list))
        self.current_move += 1

        min_value = 8
        scan_from_each_result = {}
        for elem2 in check_list:
            check_list_from = self.scan_fields(elem2[0], elem2[1])
            cur_lng = len(check_list_from)

            if cur_lng < min_value:
                min_value = cur_lng

            if cur_lng in scan_from_each_result.keys():
                scan_from_each_result[cur_lng].append((elem2[0], elem2[1]))
            else:
                scan_from_each_result[cur_lng] = []
                scan_from_each_result[cur_lng].append((elem2[0], elem2[1]))

        if min_value in scan_from_each_result.keys():
            ccl = scan_from_each_result[min_value]
            lng = len(ccl)
            if lng > 1:
                cur_num = randint(1, lng)
                return ccl[cur_num - 1]
            elif lng == 1:
                return ccl[0]
            else:
                return None
        else:
            return None

    def try_pass_all_desk(self, check_list=None):
        while not self.no_moves:
            if check_list is None:
                current_check_list = self.scan_fields(self.current_y, self.current_x)
            else:
                current_check_list = check_list.copy()
                check_list = None

            start_check_list = self.scan_fields(self.start_y, self.start_x)

            if len(start_check_list) == 1:
                self.forbidden_64 = (start_check_list[0][0], start_check_list[0][1])

            new_move = self.check_possible_move(current_check_list)

            if new_move is None:
                self.no_moves = True
            elif (len(self.forbidden_64) != 0) and (self.current_move < 64) and (new_move[0] == self.forbidden_64[0]) \
                    and (new_move[1] == self.forbidden_64[1]):
                new_move = current_check_list[0]
                self.desk[new_move[0]][new_move[1]] = self.current_move
                self.current_y = new_move[0]
                self.current_x = new_move[1]
                self.no_moves = True
            else:
                if self.desk[new_move[0]][new_move[1]] == 0:
                    self.desk[new_move[0]][new_move[1]] = self.current_move
                    self.current_y = new_move[0]
                    self.current_x = new_move[1]

                    if self.forbidden_64_fails == 10:
                        self.no_moves = True

                    if self.current_move == 64:
                        self.success = True
                else:
                    self.current_move -= 1
                    _ = self.moves_archive.pop()

    def undo_last_move(self):
        stop_test = False
        moves_ago = 0

        while not stop_test:
            self.current_move -= 1
            self.desk[self.current_y][self.current_x] = 0

            undo_y = self.current_y
            undo_x = self.current_x

            last_move = self.moves_archive[-1]
            self.current_y = last_move[0]
            self.current_x = last_move[1]

            moves_ago += 1
            _ = self.moves_archive.pop()
            undo_list = last_move[2]
            if len(undo_list) > 1:
                undo_list = \
                    [el_un for el_un in undo_list if ((el_un[0] != undo_y) or (el_un[1] != undo_x))]
                self.no_moves = False
                self.forbidden_64_fails = 0

                self.try_pass_all_desk(undo_list)
                stop_test = True
            else:
                stop_test = False

    def __str__(self):
        row_str_list = []
        hor_3 = Pg.HORIZONTAL * 3
        top = f'{Pg.HORIZONTAL * 3}{Pg.TOP}{Pg.HORIZONTAL * 3}'

        top_line = f" {Pg.LEFT_TOP}{hor_3}{top * 7}{hor_3}{Pg.RIGHT_TOP}"

        for elem03 in self.desk:
            row_str = f' {Pg.VERTICAL} '.join(list(map(lambda x: f' {x:2d} ', elem03)))
            row_str_list.append(f" {Pg.VERTICAL} {row_str} {Pg.VERTICAL} ")

        center = f'{hor_3}{Pg.CROSS}{hor_3}'
        center_line = f" {Pg.LEFT}{hor_3}{center * 7}{hor_3}{Pg.RIGHT}"
        bottom = f'{hor_3}{Pg.BOTTOM}{hor_3}'
        bottom_line = f" {Pg.LEFT_BOTTOM}{hor_3}{bottom * 7}{hor_3}{Pg.RIGHT_BOTTOM}"

        main_part = f'\n{center_line}\n'.join(row_str_list)
        return f"{top_line}\n{main_part}\n{bottom_line}"
