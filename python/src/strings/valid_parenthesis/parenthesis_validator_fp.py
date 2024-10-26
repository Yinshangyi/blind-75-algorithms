from collections import deque
from typing import List

from src.strings.valid_parenthesis.parenthesis_validator import ParenthesisValidator


class ParenthesisValidatorFP(ParenthesisValidator):
    close_2_open_mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    def is_valid(self, string: str) -> bool:
        # @formatter:off
        def helper(chars: List[str], queue: deque[str]) -> bool:
            match chars:
                case []: return len(queue) == 0
                case [head, *tail]:
                    if head not in self.close_2_open_mapping:
                        return helper(tail, deque(list(queue) + [head]))
                    if self.close_2_open_mapping[head] != queue.pop():
                        return False
                    return helper(tail, queue)
        return helper(list(string), deque())