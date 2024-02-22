import itertools
import time
import sys


def spinner(duration=3):
    spinner = itertools.cycle(["-", "/", "|", "\\"])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write("\r" + next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\rLoading complete!   ")
