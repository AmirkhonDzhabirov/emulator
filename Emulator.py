import os
def ept():
    result = os.system('cd %ANDROID_HOME%/emulator & emulator -avd Pixel_2_API_28')
    return result

ept()
