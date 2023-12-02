from collections import defaultdict
from typing import Dict, List

FWD_MATCHES: Dict[str, int] = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
REV_MATCHES: Dict[str, int] = {
    k[::-1]: v for k, v in FWD_MATCHES.items()
}


class ParseInput:
    def __init__(self) -> None:
        self.current_options : Dict[int, List[str]] = defaultdict(list)

    def parse_file(self, file: str) -> int:
        result = 0
        with open(file, 'r') as f:
            while line := f.readline():
                n1 = self.parse_line(line, FWD_MATCHES) * 10
                n2 = self.parse_line(line[::-1], REV_MATCHES)
                result += n1 + n2
        return result

    def parse_line(self, line: str, matches: Dict[str, int]) -> int:
        self.current_options.clear()
        for i, c in enumerate(line):
            if result := self.parse_char(matches, i, c):
                return result
        print('ERROR: should not happen')
        return 0

    def parse_char(self, matches: Dict[str, int], pos: int, c: str) -> int:
        if c.isnumeric():
            return int(c)

        tmp_options : Dict[int, List[str]] = defaultdict(list)

        for k, v in self.current_options.items():
            for curstr in v:
                newstr = curstr + c
                if newstr in matches:
                    return matches[newstr]

                tmp_options[k].append(newstr)
        tmp_options[pos].append(c)

        self.current_options = tmp_options


if __name__ == '__main__':
    parse = ParseInput()
    res = parse.parse_file('input')
    print(res)