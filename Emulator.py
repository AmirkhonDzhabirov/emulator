import os
import time
def ept():
    result = os.system('cd %ANDROID_HOME%/emulator & emulator -list-avds')
    print(result)

ept()

