# Задача 6
# Сами декораторы в модуле decorators.py
from decorators import password_simple_required_deco
from MyTreasury.MazeGenerator import MazeGrid


@password_simple_required_deco
def get_maze_grid(size_hor, size_vert):
    maze_grid = MazeGrid(size_hor, size_vert)
    maze_grid.generate()

    return maze_grid


print('-' * 175)
maze = get_maze_grid(159, 71)
print(maze)
