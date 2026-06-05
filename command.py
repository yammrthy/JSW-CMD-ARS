import random
from utils import fake_ip

class CommandHandler:
    def __init__(self):
        self.history = []

    def execute(self, cmd: str):
        self.history.append(cmd)

        if cmd == "help":
            return self.help()

        elif cmd == "scan":
            return self.scan()

        elif cmd == "status":
            return self.status()

        elif cmd == "ip":
            return f"Current simulated IP: {fake_ip()}"

        else:
            return "Unknown command. Type 'help'."

    def help(self):
        return (
            "AVAILABLE COMMANDS:\n"
            "  help   - show commands\n"
            "  scan   - simulate scan\n"
            "  status - system status\n"
            "  ip     - show fake IP"
        )

    def scan(self):
        targets = ["node-A", "node-B", "node-C", "node-D"]
        result = random.choice(targets)
        return f"Scanning... found activity in {result}"

    def status(self):
        return "SYSTEM: STABLE | CPU: 32% | MEMORY: 48% | FIREWALL: ACTIVE"
