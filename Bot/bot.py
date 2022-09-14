'''
Bot from The Guardians.
© by ElBe.

Version: 0.1.3
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

#JSON data
token = functions.json_module.get_config('Config')['Token']
version = functions.json_module.get_config('Config')['Version']
credits = functions.json_module.get_config('Config')['Credits']
icon = functions.json_module.get_config('Images')['Logo']
commands = functions.json_module.get_config('Commands')

#Setup
logging.basicConfig(filename='log.txt', level=logging.INFO)
intents = discord.Intents.all()

#Main
class TheGuardiansBot(discord.Client):
    '''Bot.'''

    async def on_connect(self):
        logging.info(str(datetime.datetime.now()) + 'Bot connected to the Discord API.')
        print(functions.console.info('Bot connected to the Discord API.'))

    async def on_ready(self):
        logging.info(str(datetime.datetime.now()) + 'Bot logged in as ' + client.user.name + '.')
        print(functions.console.info('Bot logged in as ' + client.user.name + '.'))
        print('')
        print('Log (Consolebased)')
        print('------------------')

        while True:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'/help for help.'))
            await asyncio.sleep(10)
            await client.change_presence(activity=discord.Game(name=' with The Guardians on 6b6t.'))
            await asyncio.sleep(10)
            if credits:
                await client.change_presence(activity=discord.Game(name=' programmed by ElBe.'))
                await asyncio.sleep(10)
        
    async def on_resumed(self):
        logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- Bot resumed seesion.')
        print(functions.console.log('Bot resumed a session.'))

    #Commands

    async def on_member_join(self, member):
        async def log(text: str):
            '''Log a text and save it in the logfile and the console.'''
            logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' + str(text))
            print(functions.console.log(str(text)))

        if not str(member) == client.user:
            channel = discord.utils.get(member.guild.text_channels, name="hi")
            joinEmbed = discord.Embed(title='Welcome!', description='Hello  <@!' + str(member.id) + f'>! \nThank you for joining {member.guild.name}!')
            joinEmbed.set_thumbnail(url=member.avatar.url)
            joinEmbed.set_footer(text='Bot made by ElBe for The Guardians.')
            await channel.send(embed=joinEmbed)
            await member.add_roles(discord.utils.get(member.guild.roles, name="member"))
            await log('@' + str(member) + ' joined to ' + str(member.guild.name) + '.')

    async def on_member_remove(self, member):
        async def log(text: str):
            '''Log a text and save it in the logfile and the console.'''
            logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' + str(text))
            print(functions.console.log(str(text)))

        if not str(member) == client.user:
            channel = discord.utils.get(member.guild.text_channels, name="bye")
            joinEmbed = discord.Embed(title='Goodbye!', description='<@!' + str(member.id) + f'> left {member.guild.name}.')
            joinEmbed.set_thumbnail(url=member.avatar.url)
            joinEmbed.set_footer(text='Bot made by ElBe for The Guardians.')
            await channel.send(embed=joinEmbed)
            await log('@' + str(member) + ' left ' + str(member.guild.name) + '.')

    async def on_disconnect(self):
        async def error(text: str):
            '''Send a error text and save it in the logfile.'''
            logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- Error: ' + str(text))
            print(functions.console.error(str(text)))

        await error('Bot disconected from discord.')


#Run
client = TheGuardiansBot(intents = intents, max_messages=None)
client.run(token)#, log_handler=None)
