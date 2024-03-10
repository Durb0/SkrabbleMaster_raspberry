from core import Service
from models.turn import Turn
from .board import Board

@Service
class TurnService:
    def __init__(self):
        self._turns:List[Turn] = []

    def addTurn(self, turn:Turn):
        self._turns.append(turn)

    def getTurns(self):
        return self._turns

    def cleanCache(self):
        self._turns = []
        print('cache cleaned')

    def removeLastTurn(self):
        if self._turns:
            self._turns.pop()
            print('last turn removed')
        else:
            print('no turn to remove')

