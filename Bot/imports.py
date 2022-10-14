'''
Module importer for the discord.py Bot.

© by ElBe.

Version: 0.1.2

NOTE: Only execute once. Only works on windows (for now).
'''

#Imports
import os
import subprocess

#Executable
executable = os.path.expanduser('~') + r'\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\python.exe'

#Main
try:
    subprocess.check_call([executable, '-m', 'pip', 'install', 'discord.py'])
    subprocess.check_call([executable, '-m', 'pip', 'install', 'asyncio'])
    subprocess.check_call([executable, '-m', 'pip', 'install', 'datetime'])
    subprocess.check_call([executable, '-m', 'pip', 'install', 'psutil'])

    print('Packages installed successfully!')

except subprocess.CalledProcessError:
    print('Error while trying to install the packages.')
