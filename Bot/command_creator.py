'''
Slash command creator for the discord.py The Guardians Bot.
© by ElBe.

Version: 0.1.0
'''

#Imports
import requests

#Variables
url = "https://discord.com/api/v10/applications/<INSERT APPLICATION ID HERE>/commands"
json = {
    "name": "<COMMAND NAME>",
    "type": 1,
    "description": "<COMMAND DESCRIPTION>"
}
headers = {
    "Authorization": "Bot <INSERT TOKEN HERE>"
}

#Request
try:
    r = requests.post(url, headers=headers, json=json)
    print('Command /' + str(json['name']) + ' was sucessfully created.')
except Exception as e:
    print('Error while trying to create the command /' + str(json['name']) + '.\n' + str(e))
