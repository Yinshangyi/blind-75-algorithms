from collections import deque

from src.strings.valid_parenthesis.parenthesis_validator import ParenthesisValidator


class ParenthesisValidatorImp(ParenthesisValidator):
    close_2_open_mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    def is_valid(self, string: str) -> bool:
        queue: deque[str] = deque()
        for char in string:
            if char not in self.close_2_open_mapping:
                queue.append(char)
            else:
                last_char = queue.pop()
                if self.close_2_open_mapping[char] != last_char:
                    return False
        return True

