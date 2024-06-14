# Lab09A.py
# "The Modular Graphics Project"


from Graphics import *
from functions import *


def main():
    beginGrfx(1300,700)
    background()
    water()
    plant()
    fish()
    bubbles()
    drawFloor()
    tank()
    endGrfx()

if __name__ == "__main__":
    main()