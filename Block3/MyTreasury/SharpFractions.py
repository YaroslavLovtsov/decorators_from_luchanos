from math import floor


class SharpFloat:
    def __init__(self, nomin=0, denomin=1, sixtets_quantity=1667):
        array = []

        if nomin == 0 and denomin == 1:
            self.array = [0 for _ in range(sixtets_quantity)]

        for ind in range(sixtets_quantity):
            nomin *= 1000000
            cur_el = floor(nomin / denomin)
            array.append(cur_el)
            nomin %= denomin

        self.sixtets_quantity = sixtets_quantity
        self.array = array

    def is_zero(self):
        for el in self.array:
            if el != 0:
                return False

        return True

    def __add__(self, other):
        result = SharpFloat(sixtets_quantity=self.sixtets_quantity)
        result_array = [0 for _ in range(self.sixtets_quantity)]
        cur_trans_from_child = 0

        for ind in range(self.sixtets_quantity - 1, -1, -1):
            cur_el = cur_trans_from_child + self.array[ind] + other.array[ind]

            if ind == 0:
                result_array[ind] = cur_el
            else:
                result_array[ind] = cur_el % 1000000
                cur_trans_from_child = cur_el // 1000000

        result.array = result_array
        return result

    def __sub__(self, other):
        result = SharpFloat(sixtets_quantity=self.sixtets_quantity)
        result_array = [0 for _ in range(self.sixtets_quantity)]
        cur_trans_from_child = 0

        for ind in range(self.sixtets_quantity - 1, -1, -1):
            cur_el = self.array[ind] - other.array[ind] - cur_trans_from_child
            if cur_el < 0:
                cur_el += 1000000
                cur_trans_from_child = 1
            else:
                cur_trans_from_child = 0

            result_array[ind] = cur_el

        result.array = result_array
        return result

    def __rmul__(self, other):
        result = SharpFloat(sixtets_quantity=self.sixtets_quantity)
        result_array = [0 for _ in range(self.sixtets_quantity)]
        cur_trans_from_child = 0

        for ind in range(self.sixtets_quantity - 1, -1, -1):
            cur_el = cur_trans_from_child + self.array[ind] * other

            if ind == 0:
                result_array[ind] = cur_el
            else:
                result_array[ind] = cur_el % 1000000
                cur_trans_from_child = cur_el // 1000000

        result.array = result_array
        return result

    def __truediv__(self, other):
        current_dec = 0
        result = SharpFloat(sixtets_quantity=self.sixtets_quantity)
        cur_ind = 0
        for el in self.array:
            cur_el = (1000000 * current_dec + el) // other
            current_dec = (1000000 * current_dec + el) % other
            result.array[cur_ind] = cur_el
            cur_ind += 1

        return result

    def __str__(self):
        def lmb(en):
            return new_str if en[0] % 30 == 29 else "" + "{:06d}".format(en[1])

        whole_part = self.array[0] // 1000000
        self.array[0] %= 1000000
        new_str = "\n "
        return f'{whole_part}.{" ".join(map(lmb, enumerate(self.array)))}'
