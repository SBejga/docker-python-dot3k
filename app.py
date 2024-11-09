#!/usr/bin/env python

import sys
import time

import dot3k.backlight as backlight
import dot3k.joystick as nav
import dot3k.lcd as lcd
from dot3k.menu import Menu, MenuOption

from graph import IPAddress
from cpu import GraphCPU
from clock import Clock

print("""
This example uses automation to advance through each menu item.
You should see each menu item appear in turn. However use-input will not be accepted.

Press CTRL+C to exit.
""")

myCPU = GraphCPU()

menu = Menu(structure={
        'CPU': myCPU,
        'Clock': Clock(),
        'IP': IPAddress(),
    },
    lcd=lcd,
    idle_handler=myCPU,
    idle_time=3,
)

REPEAT_DELAY = 0.5
REPEAT_DATE = 0.99

@nav.on(nav.UP)
def handle_up(pin):
    menu.up()
    nav.repeat(nav.UP, menu.up, REPEAT_DELAY, 0.99)


@nav.on(nav.DOWN)
def handle_down(pin):
    menu.down()
    nav.repeat(nav.DOWN, menu.down, REPEAT_DELAY, 0.99)


@nav.on(nav.LEFT)
def handle_left(pin):
    menu.left()
    nav.repeat(nav.LEFT, menu.left, REPEAT_DELAY, 0.99)


@nav.on(nav.RIGHT)
def handle_right(pin):
    menu.right()
    nav.repeat(nav.RIGHT, menu.right, REPEAT_DELAY, 0.99)


@nav.on(nav.BUTTON)
def handle_button(pin):
    menu.select()

while 1:
    menu.redraw()
    time.sleep(0.05)
