from abc import abstractmethod


class MinWindSubStringFinder:

    @abstractmethod
    def min_window(self, string: str, target: str) -> str:
        pass
