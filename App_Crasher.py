import os
import sys
cwd=os.getcwd()
os.system('cd '+cwd)
p1t=sys.platform
if p1t=='win32' or 'win64':
    os.system('taskkill /im python.exe /f')

