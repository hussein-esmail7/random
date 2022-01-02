import sys
import time

for i in range(1, 4):
    sys.stdout.write(f"\rDoing thing {i}")
    time.sleep(1)
    sys.stdout.flush()
print()
