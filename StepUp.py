"""
File: StepUp.py
Name: 陳俊義
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *

# 本來只會move、left、pick一個、put一個 四種動作，其他要自己定義


def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_99_beepers()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
