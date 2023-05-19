import winreg
import os
# Disable proxy server and port number
registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings", 0, winreg.KEY_WRITE)
winreg.SetValueEx(registry_key, "ProxyEnable", 0, winreg.REG_DWORD, 0)

# Close registry key
winreg.CloseKey(registry_key)

os.system("taskkill /f /im pyprox_HTTPS_v1.0.exe")
