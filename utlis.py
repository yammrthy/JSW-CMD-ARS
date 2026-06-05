import random

def fake_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))
