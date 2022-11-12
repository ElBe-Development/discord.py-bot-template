'''
Discord bot template.
© by ElBe.

Version: 1.9.2-R
'''

#Imports
import os
import discord
from discord import utils
import asyncio
import datetime
import time
import logging
import platform
import psutil

#Bot modules
import bot_functions
import command

#Start
print('Discord.py Bot')
print('----------------------------')
print('© by ElBe 2022.')
print('')
print('Start Informations')
print('------------------')
print('Discord version: ' + discord.__version__)
print('Bot version:     ' +
      bot_functions.json_module.get_config('Config')['Version'])
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
try:
    token = os.environ['token']
    version = bot_functions.json_module.get_config('Config')['Version']
    credits = bot_functions.json_module.get_config('Config')['Credits']
    footer = bot_functions.json_module.get_config('Config')['Footer']
    welcomeChannel = bot_functions.json_module.get_config('Channels')['Welcome']
    goodbyeChannel = bot_functions.json_module.get_config('Channels')['Goodbye']
    commands = bot_functions.json_module.get_config('Commands')
except Exception as e:
    print(bot_functions.console.error('Error while trying to get data from the config file.\n' + str(e)))

#Setup
logging.basicConfig(filename='log.txt', level=logging.INFO)
intents = discord.Intents.all()

#Create commands
try:
    if bot_functions.json_module.get_config('Created', 'command.json') == 0:
        command.run()
except Exception as e:
    print(bot_functions.console.error('Error while trying to create the commands.\n' + str(e)))

#Main
class Bot(discord.Client):
  '''Bot.'''

  async def on_connect(self):
    logging.info(
      str(datetime.datetime.now()) + ' Bot connected to the Discord API.')
    print(bot_functions.console.info('Bot connected to the Discord API.'))

  async def on_ready(self):
    logging.info(
      str(datetime.datetime.now()) + ' Bot logged in as ' + client.user.name +
      '.')
    print(
      bot_functions.console.info('Bot logged in as ' + client.user.name + '.'))
    print('')
    print('Log (Consolebased)')
    print('------------------')

    while True:
      await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f'/help for help.'))
      await asyncio.sleep(10)
      await client.change_presence(activity=discord.Game(
        name=f'Version {version}'))
      await asyncio.sleep(10)
      if credits:
        await client.change_presence(activity=discord.Game(
          name=' programmed by ElBe.'))
        await asyncio.sleep(10)

  async def on_resumed(self):
    logging.info(
      str(datetime.datetime.now().strftime('%d.%m.%Y %T')) +
      ' -- Bot resumed session.')
    print(bot_functions.console.log('Bot resumed a session.'))

  async def on_interaction(self, interaction):

    async def log(text: str):
      '''Log a text and save it in the logfile and the console.'''
      logging.info(
        str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' +
        str(text))
      print(bot_functions.console.log(str(text)))

    if interaction.type == discord.InteractionType.application_command:
      command_name = str(interaction.data['name'])
      await log('Command /' + command_name + ' was used by @' +
                str(interaction.user) + '.')

      if command_name == 'ping' and commands['ping']:
        pingEmbed = discord.Embed(title='Ping',
                                  description='Ping of the bot in ms.')
        pingEmbed.add_field(name='Latency: ',
                            value=str(round(client.latency * 1000)) + ' ms',
                            inline=False)
        pingEmbed.set_thumbnail(url=client.user.avatar.url)
        pingEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=pingEmbed,
                                                ephemeral=True)
      elif command_name == 'ping' and not commands['ping']:
        commandDisabledEmbed = discord.Embed(
          title='Command disabled',
          description=
          'This command was disabled in the bot config file. Ask a member with access to the bot to enable this command.'
        )
        commandDisabledEmbed.set_thumbnail(url=client.user.avatar.url)
        commandDisabledEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=commandDisabledEmbed,
                                                ephemeral=True)

      if command_name == 'info' and commands['info']:
        infoEmbed = discord.Embed(title='Information',
                                  description='Informations about the bot.')
        infoEmbed.add_field(name='Running on: ',
                            value=str(platform.system()) + ' ' +
                            str(platform.release()),
                            inline=False)
        infoEmbed.add_field(name='CPU usage: ',
                            value=str(psutil.cpu_percent(2)) + '%',
                            inline=False)
        infoEmbed.add_field(
          name='Uptime: ',
          value=str(
            datetime.timedelta(seconds=int(round(time.time() - starttime)))),
          inline=False)
        infoEmbed.set_thumbnail(url=client.user.avatar.url)
        infoEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=infoEmbed,
                                                ephemeral=True)
      elif command_name == 'info' and not commands['info']:
        commandDisabledEmbed = discord.Embed(
          title='Command disabled',
          description=
          'This command was disabled in the bot config file. Ask a member with access to the bot to enable this command.'
        )
        commandDisabledEmbed.set_thumbnail(url=client.user.avatar.url)
        commandDisabledEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=commandDisabledEmbed,
                                                ephemeral=True)

      if command_name == 'stop' and commands['stop']:
        if interaction.user.guild_permissions.administrator:
          await log('Client stoped.')
          exit()
        else:
          noPermissionsEmbed = discord.Embed(
            title='Missing permissions',
            description='You don\'t have permissions to do that.',
            color=discord.Color.red())
          noPermissionsEmbed.set_thumbnail(url=client.user.avatar.url)
          noPermissionsEmbed.set_footer(text=footer)
          await interaction.response.send_message(embed=noPermissionsEmbed,
                                                  ephemeral=True)
      elif command_name == 'stop' and not commands['stop']:
        commandDisabledEmbed = discord.Embed(
          title='Command disabled',
          description=
          'This command was disabled in the bot config file. Ask a member with access to the bot to enable this command.'
        )
        commandDisabledEmbed.set_thumbnail(url=client.user.avatar.url)
        commandDisabledEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=commandDisabledEmbed,
                                                ephemeral=True)

      if command_name == 'help' and commands['help']:
        helpEmbed = discord.Embed(
          title='Help',
          description='Help for commands and the usage of the bot.')
        helpEmbed.add_field(name='Ping',
                            value='Shows the ping of the bot in ms.',
                            inline=True)
        helpEmbed.add_field(name='Info',
                            value='Shows information about the bot.',
                            inline=True)
        helpEmbed.add_field(
          name='Help',
          value='Shows you help for commands and the usage of the bot.',
          inline=True)
        helpEmbed.add_field(name='Kick',
                            value='Kicks a member from the server.',
                            inline=True)
        helpEmbed.add_field(name='Ban',
                            value='Bans a member from the server.',
                            inline=True)
        helpEmbed.add_field(name='Unban',
                            value='Unbans a member from the server.',
                            inline=True)
        helpEmbed.add_field(
          name='more',
          value=
          'For more help write a direct message to <@!745695237380243457>.',
          inline=False)
        helpEmbed.set_thumbnail(url=client.user.avatar.url)
        helpEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=helpEmbed,
                                                ephemeral=True)

      if command_name == 'kick' and commands['kick']:
        options = interaction.data['options']
        if interaction.user.guild_permissions.administrator:
          member = options[0]['value']
          member = await interaction.guild.fetch_member(int(member))
          reason = options[1]['value']
          if reason == None:
            reason = 'Kicked by @' + str(
              interaction.user) + ' with the /kick command.'

          await member.kick(reason=reason)

          kickEmbed = discord.Embed(title='Kick',
                                    description='Succesfully kicked <@!' +
                                    options[0]['value'] + '>!')
          kickEmbed.set_thumbnail(url=client.user.avatar.url)
          kickEmbed.set_footer(text=footer)
          await interaction.response.send_message(embed=kickEmbed,
                                                  ephemeral=True)
        else:
          noPermissionsEmbed = discord.Embed(
            title='Missing permissions',
            description='You don\'t have permissions to do that.',
            color=discord.Color.red())
          noPermissionsEmbed.set_thumbnail(url=client.user.avatar.url)
          noPermissionsEmbed.set_footer(text=footer)
          await interaction.response.send_message(embed=noPermissionsEmbed,
                                                  ephemeral=True)
      elif command_name == 'kick' and not commands['kick']:
        commandDisabledEmbed = discord.Embed(
          title='Command disabled',
          description=
          'This command was disabled in the bot config file. Ask a member with access to the bot to enable this command.'
        )
        commandDisabledEmbed.set_thumbnail(url=client.user.avatar.url)
        commandDisabledEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=commandDisabledEmbed,
                                                ephemeral=True)

      if command_name == 'ban' and commands['ban']:
        options = interaction.data['options']
        if interaction.user.guild_permissions.administrator:
          member = options[0]['value']
          member = await interaction.guild.fetch_member(int(member))
          reason = options[1]['value']
          if reason == None:
            reason = 'Banned by @' + str(
              interaction.user) + ' with the /ban command.'

          await member.ban(reason=reason)

          banEmbed = discord.Embed(title='Ban',
                                   description='Succesfully banned <@!' +
                                   options[0]['value'] + '>!')
          banEmbed.set_thumbnail(url=client.user.avatar.url)
          banEmbed.set_footer(text=footer)
          await interaction.response.send_message(embed=banEmbed,
                                                  ephemeral=True)
        else:
          noPermissionsEmbed = discord.Embed(
            title='Missing permissions',
            description='You don\'t have permissions to do that.',
            color=discord.Color.red())
          noPermissionsEmbed.set_thumbnail(url=client.user.avatar.url)
          noPermissionsEmbed.set_footer(text=footer)
          await interaction.response.send_message(embed=noPermissionsEmbed,
                                                  ephemeral=True)
      elif command_name == 'ban' and not commands['ban']:
        commandDisabledEmbed = discord.Embed(
          title='Command disabled',
          description=
          'This command was disabled in the bot config file. Ask a member with access to the bot to enable this command.'
        )
        commandDisabledEmbed.set_thumbnail(url=client.user.avatar.url)
        commandDisabledEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=commandDisabledEmbed,
                                                ephemeral=True)

      if command_name == 'unban' and commands['unban']:
        options = interaction.data['options']
        if interaction.user.guild_permissions.administrator:
          member = options[0]['value']
          member = await client.fetch_user(int(member))
          reason = options[1]['value']
          if reason == None:
            reason = 'Unbanned by @' + str(
              interaction.user) + ' with the /unban command.'

          await interaction.guild.unban(member, reason=reason)

          unbanEmbed = discord.Embed(title='Unban',
                                     description='Succesfully unbanned <@!' +
                                     options[0]['value'] + '>!')
          unbanEmbed.set_thumbnail(url=client.user.avatar.url)
          unbanEmbed.set_footer(text=footer)
          await interaction.response.send_message(embed=unbanEmbed,
                                                  ephemeral=True)
        else:
          noPermissionsEmbed = discord.Embed(
            title='Missing permissions',
            description='You don\'t have permissions to do that.',
            color=discord.Color.red())
          noPermissionsEmbed.set_thumbnail(url=client.user.avatar.url)
          noPermissionsEmbed.set_footer(text=footer)
          await interaction.response.send_message(embed=noPermissionsEmbed,
                                                  ephemeral=True)
      elif command_name == 'unban' and not commands['unban']:
        commandDisabledEmbed = discord.Embed(
          title='Command disabled',
          description=
          'This command was disabled in the bot config file. Ask a member with access to the bot to enable this command.'
        )
        commandDisabledEmbed.set_thumbnail(url=client.user.avatar.url)
        commandDisabledEmbed.set_footer(text=footer)
        await interaction.response.send_message(embed=commandDisabledEmbed,
                                                ephemeral=True)

  async def on_member_join(self, member):

    async def log(text: str):
      '''Log a text and save it in the logfile and the console.'''
      logging.info(
        str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' +
        str(text))
      print(bot_functions.console.log(str(text)))

    if not member == client.user:
      channel = discord.utils.get(member.guild.text_channels,
                                  name=welcomeChannel)
      joinEmbed = discord.Embed(
        title='Welcome!',
        description='Hello  <@!' + str(member.id) +
        f'>! \nThank you for joining {member.guild.name}!')
      joinEmbed.set_thumbnail(url=member.avatar.url)
      joinEmbed.set_footer(text=footer)
      await channel.send(embed=joinEmbed)
      await member.add_roles(
        discord.utils.get(member.guild.roles, name='member'))
      await log('@' + str(member) + ' joined to ' + str(member.guild.name) +
                '.')

  async def on_member_remove(self, member):

    async def log(text: str):
      '''Log a text and save it in the logfile and the console.'''
      logging.info(
        str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- ' +
        str(text))
      print(bot_functions.console.log(str(text)))

    if not member == client.user:
      channel = discord.utils.get(member.guild.text_channels,
                                  name=goodbyeChannel)
      leaveEmbed = discord.Embed(title='Goodbye!',
                                 description='<@!' + str(member.id) +
                                 f'> left {member.guild.name}.')
      leaveEmbed.set_thumbnail(url=member.avatar.url)
      leaveEmbed.set_footer(text=footer)
      await channel.send(embed=leaveEmbed)
      await log('@' + str(member) + ' left ' + str(member.guild.name) + '.')

  async def on_disconnect(self):

    async def error(text: str):
      '''Send a error text and save it in the logfile.'''
      logging.info(
        str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + ' -- Error: ' +
        str(text))
      print(bot_functions.console.error(str(text)))

    await error('Bot disconected from discord.')


#Run
try:
    client = Bot(intents=intents, max_messages=None)
    client.run(token, log_handler=None)
except Exception as e:
    print(bot_functions.console.error('Error while trying to connect to discord.\n' + str(e)))