'''
Bot from The Guardians.
© by ElBe.

Version: 0.1.5
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
            await client.change_presence(activity=discord.Game(name=f'Version {version}'))
            await asyncio.sleep(10)
            if credits:
                await client.change_presence(activity=discord.Game(name=' programmed by ElBe.'))
                await asyncio.sleep(10)
        
    async def on_resumed(self):
        logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- Bot resumed seesion.')
        print(functions.console.log('Bot resumed a session.'))

    async def on_interaction(self, interaction):
        async def log(text: str):
            '''Log a text and save it in the logfile and the console.'''
            logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' + str(text))
            print(functions.console.log(str(text)))

        if interaction.type == discord.InteractionType.application_command:
            command_name = str(interaction.data['name'])
            print(str(interaction.data)) #DEBUG
            await log('Command /' + command_name + ' was used by @' + str(interaction.user) + '.')

            if command_name == 'ping':
                pingEmbed = discord.Embed(title='Ping', description='Ping of the bot in ms.')
                pingEmbed.add_field(name='Latency: ', value=str(round(client.latency * 1000)) + ' ms', inline=False)
                pingEmbed.set_thumbnail(url=client.user.avatar.url)
                pingEmbed.set_footer(text='Bot made by ElBe for The Guardians.')
                await interaction.response.send_message(embed=pingEmbed, ephemeral=True)

            if command_name == 'info':
                infoEmbed = discord.Embed(title='Information', description='Informations about the bot.')
                infoEmbed.add_field(name='Running on: ', value=str(platform.system()) + ' ' +  str(platform.release()), inline=False)
                infoEmbed.add_field(name='CPU usage: ', value=str(psutil.cpu_percent(2)) + '%', inline=False)
                infoEmbed.add_field(name='Uptime: ', value=str(datetime.timedelta(seconds=int(round(time.time()-starttime)))), inline=False)
                infoEmbed.set_thumbnail(url=client.user.avatar.url)
                infoEmbed.set_footer(text='Bot made by ElBe for The Guardians.')
                await interaction.response.send_message(embed=infoEmbed, ephemeral=True)

            if command_name == 'stop':
                await log('Client stoped.')
                exit()
            
            if command_name == 'help':
                helpEmbed = discord.Embed(title='Help', description='Help for commands and the usage of the bot.')
                helpEmbed.add_field(name='Ping', value='Shows the ping of the bot in ms.', inline=True)
                helpEmbed.add_field(name='Info', value='Shows information about the bot.', inline=True)
                helpEmbed.add_field(name='Help', value='Shows you help for commands and the usage of the bot.', inline=True)
                helpEmbed.add_field(name='Kick', value='Kicks a member from the server.', inline=True)
                helpEmbed.add_field(name='Ban', value='Bans a member from the server.', inline=True)
                helpEmbed.add_field(name='Unban', value='Unbans a member from the server.', inline=True)
                helpEmbed.add_field(name='more', value='For more help write a direct message to <@!745695237380243457>.', inline=False)
                helpEmbed.set_thumbnail(url=client.user.avatar.url)
                helpEmbed.set_footer(text='Bot made by ElBe for The Guardians.')
                await interaction.response.send_message(embed=helpEmbed, ephemeral=True)

            if command_name == ' kick':
                MISSING

            if command_name == 'ban':
                MISSING

            if command_name == 'unban':
                MISSING

    async def on_member_join(self, member):
        async def log(text: str):
            '''Log a text and save it in the logfile and the console.'''
            logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' + str(text))
            print(functions.console.log(str(text)))

        if not str(member) == client.user:
            channel = discord.utils.get(member.guild.text_channels, name='hi')
            joinEmbed = discord.Embed(title='Welcome!', description='Hello  <@!' + str(member.id) + f'>! \nThank you for joining {member.guild.name}!')
            joinEmbed.set_thumbnail(url=member.avatar.url)
            joinEmbed.set_footer(text='Bot made by ElBe for The Guardians.')
            await channel.send(embed=joinEmbed)
            await member.add_roles(discord.utils.get(member.guild.roles, name='member'))
            await log('@' + str(member) + ' joined to ' + str(member.guild.name) + '.')

    async def on_member_remove(self, member):
        async def log(text: str):
            '''Log a text and save it in the logfile and the console.'''
            logging.info(str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' + str(text))
            print(functions.console.log(str(text)))

        if not str(member) == client.user:
            channel = discord.utils.get(member.guild.text_channels, name='bye')
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
