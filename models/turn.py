from typing import List


class Solution:

    def __init__(self, score: str, words: List[str]):
        self.score: str = score
        self.words: List[str] = words

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return f"Score: {self.score}, Words: {self.words}"


class Turn:

    def __init__(self, entry: str, solutions: List[Solution]):
        self.entry: str = entry
        self.solutions: List[Solution] = solutions

    def __repr__(self):
        return f"Entry: {self.entry}, Solutions: {self.solutions}"
