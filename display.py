import os

class Display:
    def banner(self):
        print("=" * 60)
        print("      CYBER SIMULATION TERMINAL (SAFE DEMO)")
        print("=" * 60)

    def show(self, text):
        print(f"> {text}")
