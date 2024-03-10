from typing import List

class Solution:

    def __init__(self, word:str, score:str, definition:str):
        self.word:str = word
        self.score:str = score
        self.definition:str = definition

class Turn:

    def __init__(self, entry:str, solutions: List[Solution]):
        self.entry:str = entry
        self.solutions:List[Solution] = solutions