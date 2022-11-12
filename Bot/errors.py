'''
Errors for the discord.py Bot.
© by ElBe.

Version: 1.0
'''
#Imports
import functions

#Error
class error():
    def __init__(self, name: str, text: str):
        functions.console.error(name + '\n' + text)
        exit()

#API error
class APIError(error):
    def __init__(self, text: str):
        super().__init__('API error', text)

#OutdatedVersionError
class OutdatedVersionError():
    def __init__(self, outdated: str, version: str, download: str):
        functions.console.warn('Outdated version\nYou installed an outdated version of ' + outdated + '. Please install version ' + version + ' from ' + download + '.')