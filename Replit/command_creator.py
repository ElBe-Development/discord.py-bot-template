'''
Slash command creator for the discord.py Bot.
© by ElBe.

Version: 0.1.5
'''

#Imports
import os
import requests

#Variables
url = 'https://discord.com/api/v10/applications/' + str(os.environ['application_id']) + '/commands'
headers = {
    'Authorization': 'Bot ' + str(os.environ['token'])
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
