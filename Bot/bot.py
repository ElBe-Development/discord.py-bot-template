'''
Bot from The Guardians.
© by ElBe.

Version: 0.1.0
'''

#Imports
import discord
from discord import ui          
from discord import utils
from discord import app_commands
import asyncio
import datetime
import time
import logging
import platform
import psutil
from prettytable import PrettyTable
from random import randint, choice

#Bot modules
import functions

#Start
print('Discord.py The Guardians Bot')
print('-------------------')
print('© by ElBe 2022.')
print('')
print('Start Informations')
print('------------------')
print('Discord version: ' + discord.__version__)
print('Bot version:     ' + functions.json_module.get_config('Config')['Version'])
print('')
print('Starting')
print('--------')

#Variables
bold = '**'
italic = '*'
underline = '_'
stroke = '~~'
MISSING = utils.MISSING

#Starttime
starttime = time.time()
