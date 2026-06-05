import time
from display import Display
from events import EventGenerator
from logger import Logger

class CyberEngine:
    def __init__(self):
        self.display = Display()
        self.events = EventGenerator()
        self.logger = Logger()
        self.running = True

    def start(self):
        self.display.banner()

        while self.running:
            event = self.events.get_event()
            self.logger.log(event)
            self.display.show(event)
            time.sleep(0.4)
