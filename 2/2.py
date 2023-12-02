import re
import math
from typing import Dict, Tuple


class GameParser:
    def parse_file(self, filename: str, cubes_available: Dict[str, int]) -> Tuple[int, int]:
        res1, res2 = 0, 0
        with open(filename, 'r') as f:
            for line in f.readlines():
                res1 += self.parse_line_first_question(line, cubes_available)
                res2 += self.parse_line_second_question(line)

        return res1, res2

    @staticmethod
    def parse_line_first_question(line: str, cubes_available: Dict[str, int]) -> int:
        match = re.match(r'Game (\d*):(.*)', line)
        game_id = int(match.groups()[0])
        game_data = match.groups()[1]

        for sub_game in game_data.split(';'):
            for color, amount in cubes_available.items():
                match = re.search(rf'(\d*) {color}', sub_game)
                if match and int(match.groups(0)[0]) > amount:
                    return 0
        return game_id

    @staticmethod
    def parse_line_second_question(line: str) -> int:
        match = re.match(r'Game (\d*):(.*)', line)
        game_data = match.groups()[1]

        d: Dict[str, int] = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for sub_game in game_data.split(';'):
            for color in d.keys():
                if match := re.search(rf'(\d*) {color}', sub_game):
                    d[color] = max(d[color], int(match.groups()[0]))

        return math.prod(d.values())


if __name__ == '__main__':
    gp = GameParser()
    cubes_available = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    res1, res2 = gp.parse_file('input', cubes_available)
    print(res1, res2)