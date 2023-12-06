from collections import defaultdict
from typing import List, Dict, Tuple


class ParseSchematic:
    def __init__(self):
        self.matrix: List[List[str]] = []
        self.gear_ratios: List[List[List[int, List[int, int]]]] = []

    def parse(self, filename: str, objective: int) -> int:
        result = 0
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                self.matrix.append([])
                self.gear_ratios.append([])
                for char in line:
                    self.matrix[-1].append(char)
                    self.gear_ratios[-1].append([0, []])

        for y, line in enumerate(self.matrix):
            for x, _ in enumerate(line):
                if objective == 1:
                    result += self.parse_char_1(x, y, 0, False)
                else:
                    self.parse_char_2(x, y, 0, [])

        if objective == 2:
            for y in self.gear_ratios:
                for x in y:
                    if x[0] == 2:
                        result += x[1][0] * x[1][1]

        return result

    def parse_char_2(self, x: int, y: int, current_number: int, current_gears: List[Tuple[int, int]]):
        if x >= len(self.matrix[y]):
            if current_number and current_gears:
                for cx, cy in current_gears:
                    self.gear_ratios[cy][cx][0] += 1
                    self.gear_ratios[cy][cx][1].append(current_number)
            return

        char = self.matrix[y][x]
        if current_gears and not char.isnumeric():
            for cx, cy in current_gears:
                self.gear_ratios[cy][cx][0] += 1
                self.gear_ratios[cy][cx][1].append(current_number)
            return

        if not char.isnumeric():
            return

        self.matrix[y][x] = '.'
        current_number *= 10
        current_number += int(char)

        for xx in {x - 1, x, x + 1}:
            for yy in {y - 1, y, y + 1}:
                if (xx, yy) in current_gears:
                    continue
                if 0 <= xx < len(self.matrix[0]) and 0 <= yy < len(self.matrix):
                    if self.matrix[yy][xx] == '*':
                        current_gears.append((xx, yy))

        self.parse_char_2(x + 1, y, current_number, current_gears)

    def parse_char_1(self, x: int, y: int, current_number: int, valid: bool) -> int:
        if x >= len(self.matrix[y]):
            if valid:
                return current_number
            return 0

        # print(f'parse: {x}, {y}, {current_number}, {valid}')

        char = self.matrix[y][x]

        if valid and not char.isnumeric():
            return current_number

        if not char.isnumeric():
            return 0

        self.matrix[y][x] = '.'
        current_number *= 10
        current_number += int(char)

        if not valid:
            for xx in {x - 1, x, x + 1}:
                for yy in {y - 1, y, y + 1}:
                    if 0 <= xx < len(self.matrix[0]) and 0 <= yy < len(self.matrix):
                        if self.matrix[yy][xx] != '.' and not self.matrix[yy][xx].isnumeric():
                            valid = True
                            break

        return self.parse_char_1(x + 1, y, current_number, valid)


if __name__ == '__main__':
    gp = ParseSchematic()
    res1 = gp.parse('input', 1)
    res2 = gp.parse('input', 2)
    print(res1, res2)
