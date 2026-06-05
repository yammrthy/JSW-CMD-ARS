import random
from datetime import datetime

class SecurityLogs:
    def __init__(self):
        self.events = [
            "Firewall check completed",
            "Encrypted packet received",
            "System integrity verified",
            "Background scan running",
            "No threats detected",
        ]

    def generate(self):
        time = datetime.now().strftime("%H:%M:%S")
        event = random.choice(self.events)
        return f"[{time}] {event}"
