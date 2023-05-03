from PIL import Image, ImageDraw
import random
import math


def random_colour():
    rgb = random.randint(0, 16 ** 6)
    b = rgb % 256
    rgb //= 256
    g = rgb % 256
    rgb //= 256
    r = rgb % 256

    return r, g, b


def draw_a_sun(draw, point_x, point_y, radius, rgb_from=None, rgb_to=None):
    if rgb_from is None:
        r1, g1, b1 = random_colour()
    else:
        r1, g1, b1 = rgb_from

    if rgb_to is None:
        r2, g2, b2 = random_colour()
    else:
        r2, g2, b2 = rgb_to

    for phi in range(2130):
        for ro in range(radius):
            draw.point((point_x + math.floor(ro * math.cos(phi / 339)),
                        point_y + math.floor(ro * math.sin(phi / 339))),
                       fill=(r1 + (ro * (r2 - r1))//radius, g1 + (ro * (g2 - g1))//radius,
                             b1 + (ro * (b2 - b1))//radius))


def draw_ground_and_heaven(draw, width, height, horizont_line, rgb_down_from=None, rgb_down_to=None,
                           rgb_up_from=None, rgb_up_to=None):
    semi_width = width // 2

    if rgb_down_from is None:
        r1, g1, b1 = random_colour()
    else:
        r1, g1, b1 = rgb_down_from

    if rgb_down_to is None:
        r2, g2, b2 = random_colour()
    else:
        r2, g2, b2 = rgb_down_to

    if rgb_up_from is None:
        r3, g3, b3 = random_colour()
    else:
        r3, g3, b3 = rgb_up_from

    if rgb_up_to is None:
        r4, g4, b4 = random_colour()
    else:
        r4, g4, b4 = rgb_up_to

    koeff = 3 * (1 + max(width, height) // 113)

    pi_nominator = 355 * koeff
    pi_denominator = 113 * koeff

    for phi in range(pi_nominator):
        cur_phi = phi / pi_denominator
        cur_cos = math.cos(cur_phi)
        cur_sin = math.sin(cur_phi)

        if phi == 0:
            curr_ro_down_max = semi_width
            curr_ro_up_max = semi_width
        else:
            curr_ro_down_max = math.floor(min(abs(semi_width / cur_cos), abs((height - horizont_line) / cur_sin)))
            curr_ro_up_max = math.floor(min(abs(semi_width / cur_cos), abs(horizont_line / cur_sin)))

        for ro_up in range(curr_ro_up_max):

            draw.point((semi_width - math.floor(ro_up * cur_cos), math.floor(ro_up * cur_sin)),
                       fill=(r3 + (ro_up * (r4 - r3)) // curr_ro_up_max,
                             g3 + (ro_up * (g4 - g3)) // curr_ro_up_max,
                             b3 + (ro_up * (b4 - b3)) // curr_ro_up_max))

        for ro_down in range(curr_ro_down_max):
            draw.point((semi_width + math.floor(ro_down * cur_cos), height - math.floor(ro_down * cur_sin)),
                       fill=(r1 + (ro_down * (r2 - r1)) // curr_ro_down_max,
                             g1 + (ro_down * (g2 - g1)) // curr_ro_down_max,
                             b1 + (ro_down * (b2 - b1)) // curr_ro_down_max))


def draw_simple_picture():
    WIDTH = 900
    HEIGHT = 600
    HORIZONT_LINE = 350

    RGB_DOWN_FROM = (48, 1, 16)  # (93, 214, 217)
    RGB_DOWN_TO = (45, 34, 45)  # (85, 13, 192)
    RGB_UP_FROM = (100, 144, 243)
    RGB_UP_TO = (111, 143, 171)  # (20, 94, 113)

    im3 = Image.new('RGB', (WIDTH, HEIGHT), (128, 128, 128))
    draw3 = ImageDraw.Draw(im3)
    draw_ground_and_heaven(draw3, WIDTH, HEIGHT, HORIZONT_LINE, RGB_DOWN_FROM, RGB_DOWN_TO, RGB_UP_FROM, RGB_UP_TO)
    draw_a_sun(draw3, 780, 120, 60, (232, 155, 45), (243, 200, 12))
    path_to_image = 'images/test_image.jpg'
    im3.save(path_to_image, quality=95)

    return path_to_image
