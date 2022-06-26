#!/usr/bin/env python

import I2C_LCD_driver
import time
import random

mylcd = I2C_LCD_driver.lcd()

#adding the spaces after each word is just a jank way of making sure the screen is clear every time run_display executes
#deleted all lines besides one for privacy

firstLineData = ["hello               ",
        ]

secondLineData = ["fella             ",
        ]

"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",


### this is the original stuff to make the time and date display
# while True:
#     mylcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
#     mylcd.lcd_display_string(time.strftime('%a:%b:%d 20%y'), 2)

#function to make sure another function only runs once
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper



@run_once
def run_display():
#         while True:
            listItemCorrelator = random.randint(231,232)
            #we use list(list)[number] to grab the list item w/ the same index as each other in both lists
            mylcd.lcd_display_string(list(firstLineData)[listItemCorrelator], 1)
            mylcd.lcd_display_string(list(secondLineData)[listItemCorrelator], 2)
#             time.sleep(10)

#right now this only clears the display once.
#Find a way to clear the display after every time run_display executes
def clear_display():
    mylcd.lcd_display_string("", 1)
    mylcd.lcd_display_string("", 2)
                       
run_display()
clear_display()
