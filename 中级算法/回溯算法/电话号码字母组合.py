# ！ -*- coding: utf-8 -*-


def letterCombinations(digits: str):
    """
    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
    :param digits:
    :return:
    """
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
         "7": "pqrs", "8": "tuv", "9": "wxyz"}

    results = []
    for digit in digits:
        letter = d[digit]
        if not results:
            results.extend(list(letter))
            continue
        new_results = []
        for l in letter:
            for res in results:
                new_results.append(res + l)
        results = new_results
    return results
