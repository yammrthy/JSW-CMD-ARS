import time
import sys

class BootSequence:
    def run(self):
        lines = [
            "Initializing kernel modules...",
            "Loading encryption layer...",
            "Mounting virtual filesystem...",
            "Starting network simulation...",
            "Activating UI renderer...",
            "Boot sequence complete."
        ]

        print("\nSYSTEM BOOT INITIATED\n")

        for line in lines:
            print(line)
            time.sleep(0.7)

        print("\nWELCOME TO CYBER SIMULATOR v3.0\n")
