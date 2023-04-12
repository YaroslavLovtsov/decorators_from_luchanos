import random
from Block3.MyTreasury.pseudo_graph import PseudoGraph as Pg
from colorama import init as cl_init, Fore as clFore, Back as clBack


class MazeGrid:
    def __init__(self, size_x, size_y):
        self.RIGHT = 0
        self.UP = 1
        self.LEFT = 2
        self.DOWN = 3

        self.width = size_x
        self.height = size_y

        self.horizontal_direction = True
        self.vertical_direction = True

        self.current_direction = self.RIGHT
        self.grid = [['#' for _ in range(size_x)] for _ in range(size_y)]

        self.start_x = 1
        self.start_y = 3

        self.current_x = 1
        self.current_y = 3

        self.destination_x = self.width - 2
        self.destination_y = self.height - 4

        self.no_moves = False
        self.finish_is_reached = False

        self.start_system = [(self.current_y, self.current_x)]
        self.finish_system = [(self.destination_y, self.destination_x)]

        self.grid[3][0] = ' '
        self.grid[3][1] = ' '
        self.grid[-4][-1] = ' '
        self.grid[-4][-2] = ' '

        self.start_finish_system = 0
        self.first_insertion_complete = False

        self.cur_trav_dir = None

    def __str__(self):
        result_array = []
        for line_numb, row in enumerate(self.grid):
            array_to_print = []

            for col_numb, curr_el in enumerate(row):
                if curr_el == ' ':
                    array_to_print.append(f'{clBack.LIGHTBLUE_EX}{curr_el}{clBack.RESET}')
                elif curr_el != '#':
                    array_to_print.append(f'{clFore.RED}{clBack.LIGHTYELLOW_EX}{curr_el}{clBack.RESET}{clFore.RESET}')
                else:

                    if line_numb == 0:
                        up_wall = False
                    else:
                        up_wall = self.grid[line_numb - 1][col_numb] == '#'

                    if line_numb == self.height - 1:
                        down_wall = False
                    else:
                        down_wall = self.grid[line_numb + 1][col_numb] == '#'

                    if col_numb == 0:
                        left_wall = False
                    else:
                        left_wall = self.grid[line_numb][col_numb - 1] == '#'

                    if col_numb == self.width - 1:
                        right_wall = False
                    else:
                        right_wall = self.grid[line_numb][col_numb + 1] == '#'

                    array_to_print.append(Pg.border_element(up_wall, left_wall, right_wall, down_wall))

            result_array.append(''.join(array_to_print))
        return '\n'.join(result_array)

    def move(self, directions):
        lng = len(directions)
        if lng == 0:
            self.no_moves = True
            return
        else:
            if (self.current_y, self.current_x) in self.start_system:
                self.start_finish_system = 0
            elif (self.current_y, self.current_x) in self.start_system:
                self.start_finish_system = 1
            else:
                self.start_finish_system = 2

            drc, mov = directions[random.randint(1, lng)-1]
            if drc == self.RIGHT:
                self.move_horizontal(self.current_x, self.current_x + mov)
            elif drc == self.UP:
                self.move_vertical(self.current_y, self.current_y - mov)
            elif drc == self.LEFT:
                self.move_horizontal(self.current_x, self.current_x - mov)
            elif drc == self.DOWN:
                self.move_vertical(self.current_y, self.current_y + mov)
            else:
                pass

    def move_horizontal(self, x_from, x_to):
        if x_to > x_from:
            cur_range = range(x_from + 1, x_to + 1)
        else:
            cur_range = range(x_from - 1, x_to - 1, -1)

        for ind_s in cur_range:
            self.grid[self.current_y][ind_s] = ' '
            if self.start_finish_system == 0:
                self.start_system.append((self.current_y, ind_s))
            else:
                self.finish_system.append((self.current_y, ind_s))

        self.current_x = x_to
        self.horizontal_direction = False
        self.vertical_direction = True

    def move_vertical(self, y_from, y_to):
        if y_to > y_from:
            cur_range = range(y_from + 1, y_to + 1)
        else:
            cur_range = range(y_from - 1, y_to - 1, -1)

        for ind_s in cur_range:
            self.grid[ind_s][self.current_x] = ' '
            if self.start_finish_system == 0:
                self.start_system.append((ind_s, self.current_x))
            else:
                self.finish_system.append((ind_s, self.current_x))

        self.current_y = y_to
        self.horizontal_direction = True
        self.vertical_direction = False

    def scan_directions(self, left_direction=False, right_direction=False):
        result = []

        if left_direction:
            x_to_left = self.current_x - 2
            while x_to_left > 0:
                if self.grid[self.current_y][x_to_left] != ' ':
                    result.append((self.LEFT, self.current_x - x_to_left))
                    x_to_left -= 2
                else:
                    x_to_left = -1

            x_to_right = self.current_x + 2
            while x_to_right < self.width:
                if self.grid[self.current_y][x_to_right] != ' ':
                    result.append((self.RIGHT, x_to_right - self.current_x))
                    x_to_right += 2
                else:
                    x_to_right = self.width + 1

        if right_direction:
            y_to_up = self.current_y - 2
            while y_to_up > 0:
                if self.grid[y_to_up][self.current_x] != ' ':
                    result.append((self.UP, self.current_y - y_to_up))
                    y_to_up -= 2
                else:
                    y_to_up = -1

            y_to_down = self.current_y + 2
            while y_to_down < self.height:
                if self.grid[y_to_down][self.current_x] != ' ':
                    result.append((self.DOWN, y_to_down - self.current_y))
                    y_to_down += 2
                else:
                    y_to_down = self.height + 1

        return result

    def scan_insertion_place(self):
        result = []

        grd = self.grid

        for el_y in range(1, self.height, 2):
            for el_x in range(1, self.width, 2):
                test = grd[el_y][el_x] == '#' and grd[el_y][el_x - 1] == '#' and grd[el_y][el_x + 1] == '#'\
                    and grd[el_y-1][el_x] == '#' and grd[el_y-1][el_x - 1] == '#' and grd[el_y-1][el_x + 1] == '#' \
                    and grd[el_y + 1][el_x - 1] == '#' and grd[el_y + 1][el_x + 1] == '#' \
                    and grd[el_y + 1][el_x + 1] == '#'

                if test:
                    if el_x > 1 and grd[el_y][el_x - 2] == ' ':
                        result.append(((el_y, el_x - 1), (el_y, el_x), True, (el_y, el_x - 2)))

                    if el_x < self.width - 2 and grd[el_y][el_x + 2] == ' ':
                        result.append(((el_y, el_x + 1), (el_y, el_x), True, (el_y, el_x + 2)))

                    if el_y > 1 and grd[el_y - 2][el_x] == ' ':
                        result.append(((el_y - 1, el_x), (el_y, el_x), False, (el_y - 2, el_x)))

                    if el_y < self.height - 2 and grd[el_y + 2][el_x] == ' ':
                        result.append(((el_y + 1, el_x), (el_y, el_x), False, (el_y + 2, el_x)))

        return result

    def generate(self):
        scanned_directions = self.scan_directions(True, True)
        self.move(scanned_directions)

        stop_test_global = False

        while not stop_test_global:
            while not self.no_moves:
                scanned_directions = self.scan_directions(self.horizontal_direction, self.vertical_direction)
                self.move(scanned_directions)

            ins_var_list = self.scan_insertion_place()
            ins_var_lng = len(ins_var_list)

            if not self.first_insertion_complete:
                self.no_moves = False
                self.current_y = self.destination_y
                self.current_x = self.destination_x

                self.horizontal_direction = True
                self.vertical_direction = True

                self.first_insertion_complete = True
            else:
                if ins_var_lng < 1:
                    stop_test_global = True
                else:
                    if ins_var_lng == 1:
                        ins_pts = ins_var_list[0]
                    else:
                        ins_ind = random.randint(1, ins_var_lng)
                        ins_pts = ins_var_list[ins_ind - 1]

                    self.grid[ins_pts[0][0]][ins_pts[0][1]] = ' '
                    self.grid[ins_pts[1][0]][ins_pts[1][1]] = ' '
                    self.current_y = ins_pts[1][0]
                    self.current_x = ins_pts[1][1]

                    self.horizontal_direction = ins_pts[2]
                    self.vertical_direction = not ins_pts[2]
                    self.no_moves = False

                    if ins_pts[3] in self.start_system:
                        self.start_system.append(ins_pts[0])
                        self.start_system.append(ins_pts[1])
                    else:
                        self.finish_system.append(ins_pts[0])
                        self.finish_system.append(ins_pts[1])

        connection_points = self.scan_points_for_connection()
        conn_lng = len(connection_points)
        conn_ind = random.randint(0, conn_lng - 1)
        conn_y, conn_x = connection_points[conn_ind]
        self.grid[conn_y][conn_x] = ' '

    def scan_points_for_connection(self):
        result_array = []

        for row_ind in range(2, self.height - 2):
            for col_ind in range(2, self.width - 2):
                if self.grid[row_ind][col_ind] == ' ':
                    in_start_sys = (row_ind, col_ind) in self.start_system
                    if self.grid[row_ind - 1][col_ind] == '#' and self.grid[row_ind - 2][col_ind] == ' ':
                        in_finish_sys = (row_ind - 2, col_ind) in self.finish_system
                        rests = (((row_ind - 1) % 2 != 0) or (col_ind % 2 != 0)) and (in_start_sys == in_finish_sys)
                        if rests and not (row_ind - 1, col_ind) in result_array:
                            result_array.append((row_ind - 1, col_ind))

                    if self.grid[row_ind + 1][col_ind] == '#' and self.grid[row_ind + 2][col_ind] == ' ':
                        in_finish_sys = (row_ind + 2, col_ind) in self.finish_system
                        rests = (((row_ind + 1) % 2 != 0) or (col_ind % 2 != 0)) and (in_start_sys == in_finish_sys)
                        if rests and not (row_ind + 1, col_ind) in result_array:
                            result_array.append((row_ind + 1, col_ind))

                    if self.grid[row_ind][col_ind - 1] == '#' and self.grid[row_ind][col_ind - 2] == ' ':
                        in_finish_sys = (row_ind, col_ind - 2) in self.finish_system
                        rests = ((row_ind % 2 != 0) or ((col_ind - 1) % 2 != 0)) and (in_start_sys == in_finish_sys)
                        if rests and not (row_ind, col_ind - 1) in result_array:
                            result_array.append((row_ind, col_ind - 1))

                    if self.grid[row_ind][col_ind + 1] == '#' and self.grid[row_ind][col_ind + 2] == ' ':
                        in_finish_sys = (row_ind, col_ind + 2) in self.finish_system
                        rests = ((row_ind % 2 != 0) or ((col_ind + 1) % 2 != 0)) and (in_start_sys == in_finish_sys)
                        if rests and not (row_ind, col_ind + 1) in result_array:
                            result_array.append((row_ind, col_ind + 1))

        return result_array

    def travers(self):
        stop_test_traversal = False

        stop_number = 0

        self.current_y = self.start_y
        self.current_x = self.start_x - 1

        self.cur_trav_dir = self.RIGHT
        self.grid[self.current_y][self.current_x] = "*"

        while not stop_test_traversal:
            self.grid[self.current_y][self.current_x] = "*"

            if (self.current_y == self.destination_y) and (self.current_x == self.destination_x):
                stop_test_traversal = True
                self.current_x += 1
                self.grid[self.current_y][self.current_x] = "*"
                continue
            elif (self.current_y == self.start_y) and (self.current_x == self.start_x) \
                    and self.cur_trav_dir == self.LEFT:
                stop_test_traversal = True
                self.current_x -= 1
                self.grid[self.current_y][self.current_x] = "*"
                continue
            elif self.move_turn_right_if_possible():
                stop_number += 1
                # print(stop_number, "НАПРАВО")
                continue
            elif self.move_in_same_direction_if_possible():
                stop_number += 1
                # print(stop_number, "ПРЯМО")
                continue
            elif self.move_turn_left_if_possible():
                stop_number += 1
                # print(stop_number, "НАЛЕВО")
                continue
            elif self.move_in_reverse_direction_if_possible():
                stop_number += 1
                # print(stop_number, "НАЗАД")
                continue
            else:
                stop_test_traversal = True
                continue

    def move_turn_right_if_possible(self):
        cur_y_up = self.current_y - 1
        cur_y = self.current_y
        cur_y_down = self.current_y + 1

        cur_x_left = self.current_x - 1
        cur_x = self.current_x
        cur_x_right = self.current_x + 1

        if self.cur_trav_dir == self.RIGHT and self.grid[cur_y_down][cur_x] != "#":

            curr_y_incr = 1
            curr_x_incr = 0
            new_direction = self.DOWN

        elif self.cur_trav_dir == self.DOWN and self.grid[cur_y][cur_x_left] != "#":

            curr_y_incr = 0
            curr_x_incr = -1
            new_direction = self.LEFT

        elif self.cur_trav_dir == self.LEFT and self.grid[cur_y_up][cur_x] != "#":

            curr_y_incr = -1
            curr_x_incr = 0
            new_direction = self.UP

        elif self.cur_trav_dir == self.UP and self.grid[cur_y][cur_x_right] != "#":

            curr_y_incr = 0
            curr_x_incr = 1
            new_direction = self.RIGHT

        else:

            return False

        if self.grid[self.current_y + curr_y_incr][self.current_x + curr_x_incr] == '*':
            self.grid[self.current_y][self.current_x] = ' '

        self.current_y += curr_y_incr
        self.current_x += curr_x_incr
        self.grid[self.current_y][self.current_x] = '*'
        self.cur_trav_dir = new_direction

        if (self.current_y == (self.height - 1)) or (self.current_x == (self.width - 1)):
            return None

        return True

    def move_in_same_direction_if_possible(self):
        cur_y_up = self.current_y - 1
        cur_y = self.current_y
        cur_y_down = self.current_y + 1

        cur_x_left = self.current_x - 1
        cur_x = self.current_x
        cur_x_right = self.current_x + 1

        if self.cur_trav_dir == self.RIGHT and self.grid[cur_y][cur_x_right] != "#":

            curr_y_incr = 0
            curr_x_incr = 1

        elif self.cur_trav_dir == self.DOWN and self.grid[cur_y_down][cur_x] != "#":

            curr_y_incr = 1
            curr_x_incr = 0

        elif self.cur_trav_dir == self.LEFT and self.grid[cur_y][cur_x_left] != "#":

            curr_y_incr = 0
            curr_x_incr = -1

        elif self.cur_trav_dir == self.UP and self.grid[cur_y_up][cur_x] != "#":

            curr_y_incr = -1
            curr_x_incr = 0

        else:

            return False

        if self.grid[self.current_y + curr_y_incr][self.current_x + curr_x_incr] == '*':
            self.grid[self.current_y][self.current_x] = ' '

        self.current_y += curr_y_incr
        self.current_x += curr_x_incr
        self.grid[self.current_y][self.current_x] = '*'

        if (self.current_y == (self.height - 1)) or (self.current_x == (self.width - 1)):
            return None

        return True

    def move_turn_left_if_possible(self):
        cur_y_up = self.current_y - 1
        cur_y = self.current_y
        cur_y_down = self.current_y + 1

        cur_x_left = self.current_x - 1
        cur_x = self.current_x
        cur_x_right = self.current_x + 1

        if self.cur_trav_dir == self.RIGHT and self.grid[cur_y_up][cur_x] != "#":

            curr_y_incr = -1
            curr_x_incr = 0
            new_direction = self.UP

        elif self.cur_trav_dir == self.DOWN and self.grid[cur_y][cur_x_right] != "#":

            curr_y_incr = 0
            curr_x_incr = 1
            new_direction = self.RIGHT

        elif self.cur_trav_dir == self.LEFT and self.grid[cur_y_down][cur_x] != "#":

            curr_y_incr = 1
            curr_x_incr = 0
            new_direction = self.DOWN

        elif self.cur_trav_dir == self.UP and self.grid[cur_y][cur_x_left] != "#":

            curr_y_incr = 0
            curr_x_incr = -1
            new_direction = self.LEFT

        else:

            return False

        if self.grid[self.current_y + curr_y_incr][self.current_x + curr_x_incr] == '*':
            self.grid[self.current_y][self.current_x] = ' '

        self.current_y += curr_y_incr
        self.current_x += curr_x_incr
        self.grid[self.current_y][self.current_x] = '*'
        self.cur_trav_dir = new_direction

        if (self.current_y == (self.height - 1)) or (self.current_x == (self.width - 1)):
            return None

        return True

    def move_in_reverse_direction_if_possible(self):
        cur_y_up = self.current_y - 1
        cur_y = self.current_y
        cur_y_down = self.current_y + 1

        cur_x_left = self.current_x - 1
        cur_x = self.current_x
        cur_x_right = self.current_x + 1

        if self.cur_trav_dir == self.RIGHT and self.grid[cur_y][cur_x_left] != "#":

            curr_y_incr = 0
            curr_x_incr = -1
            new_direction = self.LEFT

        elif self.cur_trav_dir == self.DOWN and self.grid[cur_y_up][cur_x] != "#":

            curr_y_incr = -1
            curr_x_incr = 0
            new_direction = self.UP

        elif self.cur_trav_dir == self.LEFT and self.grid[cur_y][cur_x_right] != "#":

            curr_y_incr = 0
            curr_x_incr = 1
            new_direction = self.RIGHT

        elif self.cur_trav_dir == self.UP and self.grid[cur_y_down][cur_x] != "#":

            curr_y_incr = 1
            curr_x_incr = 0
            new_direction = self.DOWN

        else:

            return False

        if self.grid[self.current_y + curr_y_incr][self.current_x + curr_x_incr] == '*':
            self.grid[self.current_y][self.current_x] = ' '

        self.current_y += curr_y_incr
        self.current_x += curr_x_incr
        self.grid[self.current_y][self.current_x] = '*'
        self.cur_trav_dir = new_direction

        if (self.current_y == (self.height - 1)) or (self.current_x == (self.width - 1)):
            return None

        return True


cl_init()
