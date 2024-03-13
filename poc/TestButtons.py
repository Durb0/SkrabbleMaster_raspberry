from service import Board

if __name__ == '__main__':
    board = Board()
    board.mode_button.on_press.connect(lambda e: print(f'Mode button pressed for {e} seconds'))
    board.action_button.on_press.connect(lambda e: print(f'Action button pressed for {e} seconds'))
    input('Press enter to exit')
    print('Exiting')
