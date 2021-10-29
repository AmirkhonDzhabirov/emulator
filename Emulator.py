import subprocess
# subprocess.call("cd C://Users//Amirkhon.Jobirov//AppData//Local//Android//Sdk//emulator & emulator -avd Pixel_2_API_28", shell=True)
# # subprocess.Popen("cd %ANDROID_HOME%\emulator")

# subprocess.call('appium.exe', cwd = "C://Users//Amirkhon.Jobirov//AppData//Local//Programs//Appium")
subprocess.run(["/Users/Amirkhon.Jobirov/AppData/Local/Android/Sdk/emulator/emulator","-avd", "Pixel_2_API_28"])
