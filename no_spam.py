# types where the cursor is placed after running the code

import pyautogui as pg
from time import sleep as sl

f = 0
keep_going = True
while keep_going:
    sl(3)
    f += 1
    pg.write("you online?")
    pg.press("enter")
    if f > 10:
        keep_going = False
