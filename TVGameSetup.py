import subprocess
import os

f = open('C:/Users/Mason/Documents/TVGameSetup/settings.txt', 'r+')
message = f.read()



if message == '0':
    os.popen('C:/Users/Mason/Documents/TVGameSetup/MultiMonitorTool.exe /SetPrimary 1')
    os.popen('C:/Users/Mason/Documents/TVGameSetup/nircmd setdefaultsounddevice "TV" 1')
    f.truncate()
    f = open('C:/Users/Mason/Documents/TVGameSetup/settings.txt', 'w')
    f.write('1')
    f.close()
else:
    os.popen('C:/Users/Mason/Documents/TVGameSetup/MultiMonitorTool.exe /SetPrimary 4')
    os.popen('C:/Users/Mason/Documents/TVGameSetup/nircmd setdefaultsounddevice "Headphones (PC)" 1')
    f.truncate()
    f = open('C:/Users/Mason/Documents/TVGameSetup/settings.txt', 'w')
    f.write('0')
    f.close()

