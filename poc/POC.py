import time
import threading
from gpiozero import Button


class SkrabbleButton(Button):
    def __init__(self, name, pin, on_click, on_press, pull_up=True, threshold=2):
        super().__init__(pin, pull_up=pull_up)
        self.name = name
        self._threshold = threshold
        self._on_click = on_click
        self._on_press = on_press

    def wait_for_press(self):
        super().wait_for_press()
        begin = time.time()
        print(f'{self.name} down')
        super().wait_for_release()
        press_duration = time.time() - begin
        print(f'{self.name} was pressed for {press_duration} seconds')

        if press_duration < self._threshold:
            self._on_click()
        else:
            self._on_press()

    def get_thread(self):
        print(f'Adding {self.name}')
        return threading.Thread(target=self.wait_for_press)


start_button = SkrabbleButton("Start", 6, lambda: print('Changement de mode'),
                              lambda: print('Changement de mode (appui long)'))
next_button = SkrabbleButton("Next", 16, lambda: print('Clic'), lambda: print('Press'), pull_up=False)


class ButtonHandler:
    def __init__(self, *args):
        self._buttons = args

    def wait_any(self):
        threads = []

        for button in self._buttons:
            threads.append(button.get_thread())
            threads[-1].start()

        while True:
            for (index, t) in enumerate(threads):
                if not t.is_alive:
                    print(f'Restarting {self._buttons[index].name}')
                    threads[index] = self._buttons[index].get_thread()
                    threads[index].start()


Handler = ButtonHandler(start_button, next_button)
Handler.wait_any()
