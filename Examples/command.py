'''
Example command for the discord.py Bot.
© by ElBe.
Version: 1.0
'''
#Imports
import discord
import functions

#Main
async def __init__(interaction: discord.Interaction, *args):
    '''Example command cog.
    
    Usage:
        `/example`

    Args:
        interaction (discord.Interaction): Interaction provided by on_interaction.
    '''
    
    if interaction.data['name'] == 'example':
        functions.log('Command /example was used by @' + str(interaction.user) + '.')
        if functions.json_module.get_config('Commands')['example']:
            print('This is an example!')
        else:
            commandDisabledEmbed = discord.Embed(title='Command disabled', description='This command was disabled in the bot config file. Ask a member with access to the bot to enable this command.')
            commandDisabledEmbed.set_thumbnail(url=interaction.client.user.avatar.url)
            commandDisabledEmbed.set_footer(text=functions.json_module.get_config('Config')['Footer'])
            await interaction.response.send_message(embed=commandDisabledEmbed, ephemeral=True)
