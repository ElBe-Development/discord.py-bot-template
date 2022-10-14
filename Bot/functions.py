'''
Functions for the discord.py Bot.
© by ElBe.

Version: 0.1.1
'''

#Imports
import json
import os
import colorama
import datetime
import re

class variables():
    '''All variables used in this module.'''
    standart_config_file = 'config.json'
    standart_datetime_format = datetime.date.isoformat

class json_module():
    def get_config(name: str, file = variables.standart_config_file):
        '''Returns a value from the given/standart JSON file.'''
        with open(file, 'r') as f:
            return json.load(f)[name]

    def write_json(data, show_text = False, file = variables.standart_config_file):
        '''Writes the text to the given/standart JSON file.'''
        with open(file, 'w') as f:
            json.dump(data, f)
            f.close()

            if show_text:
                print(console.log('Data ' + str(data) + ' added to ' + str(file) + '.'))

class console():
    def info(text: str):
        '''Returns a info text.'''
        i = 0
        if len(re.findall('\n', text)) > 1:
            text = '\n' + text
        search = len(re.findall('\n', text))

        if search > 1:
            for i in range(search):
                text = text.replace('\n', '//n[' + colorama.Fore.LIGHTBLUE_EX + str(i + 1) + colorama.Style.RESET_ALL + '] ', 1)
                i = i + 1
            text = text.replace('//n', '\n')
        return colorama.Fore.LIGHTBLUE_EX + str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + colorama.Style.RESET_ALL + ' [' + colorama.Fore.GREEN + 'INFO' + colorama.Style.RESET_ALL + ']    ' + text

    def error(text: str):
        '''Returns a error text.'''
        i = 0
        if len(re.findall('\n', text)) > 1:
            text = '\n' + text
        search = len(re.findall('\n', text))

        if search > 1:
            for i in range(search):
                text = text.replace('\n', '//n[' + colorama.Fore.LIGHTBLUE_EX + str(i + 1) + colorama.Style.RESET_ALL + '] ', 1)
                i = i + 1
            text = text.replace('//n', '\n')
        return colorama.Fore.LIGHTBLUE_EX + str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + colorama.Style.RESET_ALL + ' [' + colorama.Fore.RED + 'ERROR' + colorama.Style.RESET_ALL + ']   ' + text

    def warn(text: str):
        '''Returns a warn text.'''
        i = 0
        if len(re.findall('\n', text)) > 1:
            text = '\n' + text
        search = len(re.findall('\n', text))

        if search > 1:
            for i in range(search):
                text = text.replace('\n', '//n[' + colorama.Fore.LIGHTBLUE_EX + str(i + 1) + colorama.Style.RESET_ALL + '] ', 1)
                i = i + 1
            text = text.replace('//n', '\n')
        return colorama.Fore.LIGHTBLUE_EX + str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + colorama.Style.RESET_ALL + ' [' + colorama.Fore.YELLOW + 'WARNING' + colorama.Style.RESET_ALL + '] ' + text

    def log(text: str):
        '''Returns a log text.'''
        i = 0
        if len(re.findall('\n', text)) > 1:
            text = '\n' + text
        search = len(re.findall('\n', text))

        if search > 1:
            for i in range(search):
                text = text.replace('\n', '//n[' + colorama.Fore.LIGHTBLUE_EX + str(i + 1) + colorama.Style.RESET_ALL + '] ', 1)
                i = i + 1
            text = text.replace('//n', '\n')
        return colorama.Fore.LIGHTBLUE_EX + str(datetime.datetime.now().strftime('%d.%m.%Y %T')) + colorama.Style.RESET_ALL + ' [LOG]     ' + text

    def clear():
        '''Clear the console.'''
        os.system('cls')

    def crusor_up():
        '''Changes the position of the crusor to the line above.'''
        print('\x1b[1A')

    def erase_line():
        '''Erases the current line.'''
        print('\x1b[2K')

    def erase_last():
        '''Erases the last line.'''
        print('\x1b[1A' + '\x1b[2K' + '\x1b[1A')
