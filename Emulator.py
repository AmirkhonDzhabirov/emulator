import os
import time
def ept():
    result = os.system('emulator -list-avds')
    print(result)

ept()

