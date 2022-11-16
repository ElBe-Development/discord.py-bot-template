'''
Command creator for the discord.py Bot.

© by ElBe.

Version: 0.1.6

NOTE: Only execute once.
'''

#Imports
import command_creator
import bot_functions

class run():
    def __init__(self):  
        #Stop command
        json = {
            'name': 'stop',
            'type': 1,
            'description': 'Stops the bot.'
        }
        command_creator.create_command(json)

        #Help command
        json = {
            'name': 'help',
            'type': 1,
            'description': 'Shows you help about the bot.'
        }
        command_creator.create_command(json)

        #Ping command
        json = {
            'name': 'ping',
            'type': 1,
            'description': 'Shows you the ping of the bot in ms.'
        }
        command_creator.create_command(json)

        #Info command
        json = {
            'name': 'info',
            'type': 1,
            'description': 'Shows you information about the bot.'
        }
        command_creator.create_command(json)

        #Kick command
        json = {
            'name': 'kick',
            'type': 1,
            'description': 'Kicks a member from the server.',
            "options": [
                {
                    "name": "member",
                    "description": "The member to kick.",
                    "type": 6,
                    "required": True
                },
                {
                    "name": "reason",
                    "description": "Reason for the kick.",
                    "type": 3,
                    "required": False
                }
            ]
        }
        command_creator.create_command(json)

        #Ban command
        json = {
            'name': 'ban',
            'type': 1,
            'description': 'Bans a member from the server.',
            "options": [
                {
                    "name": "member",
                    "description": "The member to ban.",
                    "type": 6,
                    "required": True
                },
                {
                    "name": "reason",
                    "description": "Reason for the ban.",
                    "type": 3,
                    "required": False
                }
            ]
        }
        command_creator.create_command(json)

        #Unban command
        json = {
            'name': 'unban',
            'type': 1,
            'description': 'Unbans a member from the server.',
            "options": [
                {
                    "name": "member",
                    "description": "The member to unban.",
                    "type": 6,
                    "required": True
                },
                {
                    "name": "reason",
                    "description": "Reason for the unban.",
                    "type": 3,
                    "required": False
                }
            ]
        }
        command_creator.create_command(json)

        #File
        bot_functions.json_module.write_json({"Created": 1}, False, 'command.json')