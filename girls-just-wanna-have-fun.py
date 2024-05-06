import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Some boys take a beautiful girl", 0.10),
        ("And hide her away from the rest of the world", 0.08),
        ("I wanna be the one to walk in the sun", 0.08),
        ("Oh, girls, they wanna have fun", 0.08),
        ("Oh, girls just wanna have fun", 0.08),
        (" ", 150),
    ]

    delays = [0.1, 1, 0.5, 0.7, 0.5, 0]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()