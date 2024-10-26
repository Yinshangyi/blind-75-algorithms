from src.strings.valid_anagram.AnagramValidator import AnagramValidator


class AnagramValidatorImp(AnagramValidator):

    def is_anagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        return sorted_str1 == sorted_str2
