import random

class EventGenerator:
    def __init__(self):
        self.events = [
            "Scanning virtual network nodes...",
            "Checking system integrity...",
            "Simulating packet routing...",
            "Loading security dashboard...",
            "Analyzing fake traffic data...",
            "Refreshing system logs...",
        ]

    def get_event(self):
        return random.choice(self.events)
