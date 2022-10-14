'''
Module importer for the discord.py Bot.

© by ElBe.

Version: 0.1.0

NOTE: Only execute once.
'''

#Imports
import sys
import subprocess

#Main
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord.py'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'asyncio'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'datetime'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'logging'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'platform'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])

print('Packages installed successfully!')
