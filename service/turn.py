from core.service import Service
from models.turn import Turn
from .board import Board
from core.inject import inject
from .componentservice import ComponentService

MAX_TURNS = 6

@Service
@inject('_routing', ComponentService)
class TurnService:
    def __init__(self):
        self._turns:List[Turn] = []
        self._selected_index = None

    def addTurn(self, turn:Turn):
        self._turns.append(turn)
        self._selected_index = 0


    @property
    def turns(self):
        return self._turns

    @property
    def selected_index(self):
        return self._selected_index

    @property
    def selected_turn(self):
        if self._selected_index is not None:
            return self._turns[self._selected_index]
        else:
            return None

    def cleanCache(self):
        self._turns = []
        self._selected_index = None
        print('cache cleaned')

    def nextIndex(self):
        if self._selected_index is not None:
            self._selected_index = (self._selected_index + 1) % len(self._turns)
            print('next turn')
        else:
            print('no turn selected')
        return self._selected_index

    def previousIndex(self):
        if self._selected_index is not None:
            self._selected_index = (self._selected_index - 1) % len(self._turns)
            print('previous turn')
        else:
            print('no turn selected')
        return self._selected_index

    def removeLastTurn(self):
        if self._turns:
            self._turns.pop()
            self._selected_index = 0 if self._turns else None
            print('last turn removed')
        else:
            print('no turn to remove')

