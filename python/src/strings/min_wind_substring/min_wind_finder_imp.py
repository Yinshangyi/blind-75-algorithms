from collections import Counter

from src.strings.min_wind_substring.min_wind_finder import MinWindSubStringFinder


class MinWindSubStringFinderImp(MinWindSubStringFinder):
    def min_window(self, string: str, target: str) -> str:
        str_counter, target_counter = Counter(), Counter(target)
        left_min_window, right_min_window = -1, -1
        width_window = float("infinity")
        left_pt = 0
        need_count, target_count = 0, len(target_counter)

        for right_pt in range(len(string)):
            curr_char = string[right_pt]
            str_counter[curr_char] = 1 + str_counter.get(curr_char, 0)

            if curr_char in target_counter and str_counter[curr_char] == target_counter[curr_char]:
                need_count += 1

            while need_count == target_count:
                curr_window = (right_pt - left_pt) + 1
                if curr_window < width_window:
                    left_min_window, right_min_window = left_pt, right_pt
                    width_window = curr_window
                str_counter[string[left_pt]] -= 1
                if string[left_pt] in target_counter and str_counter[string[left_pt]] < target_counter[
                    string[left_pt]]:
                    need_count -= 1
                left_pt += 1
        return string[left_min_window:right_min_window + 1] if width_window < float("infinity") else ""
