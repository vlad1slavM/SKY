'''https://cloud.mail.ru/home/test1.txt'''

from StateOfDirectory.currentState import State
import os
direction = r'C:\Users\dlach\Documents\GitHub\SKY\forTest1'
state = State(direction)
state.sync()
