'''
Slash command creator for the discord.py Bot.
© by ElBe.

Version: 0.1.4
'''

#Imports
import requests
import functions

#Variables
url = 'https://discord.com/api/v10/applications/' + str(functions.json_module.get_config('Config')['Application ID']) + '/commands'
headers = {
    'Authorization': 'Bot ' + str(functions.json_module.get_config('Config')['Token'])
}

#Example Command
json = {
    'name': 'ping',
    'type': 1,
    'description': 'Shows you the ping of the bot.'
}

#Function
def create_command(json):
    try:
        r = requests.post(url, headers=headers, json=json)
        print('Command /' + str(json['name']) + ' was sucessfully created.')
    except Exception as e:
        print('Error while trying to create the command /' + str(json['name']) + '.\n' + str(e))
