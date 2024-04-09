"""
File: Steeplechase.py
Name: 陳俊義
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(7):
        while front_is_clear():
            move()
        jump()


def jump():
    """
    pre-condition:Karel is on the left side of the world, facing East.
    post-condition:Karel is on the right side of the world.
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is on the left side of the world, facing East.
    post-condition:Karel is facing East.
    """
    turn_left()
    # Facing North
    while not right_is_clear():
        move()
    turn_right()


def cross():
    """
    pre-condition:Karel is facing East.
    post-condition:Karel is facing South.
    """
    move()
    turn_right()


def down():
    """
    pre-condition: Karel is facing South.
    post-condition:Karel is facing East.
    """
    move()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
