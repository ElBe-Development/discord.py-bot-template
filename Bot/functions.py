'''
Functions for the discord.py Bot.
© by ElBe.
Version: 1.2
'''

#Imports
import json
import os
import colorama
import datetime
import re

#Bot modules
import errors

class variables():
    '''All variables used in this module.'''
    standart_config_file = 'config.json'
    standart_datetime_format = datetime.date.isoformat

class json_module():
    def get_config(name: str, file = variables.standart_config_file):
        '''Returns a value from the given/standart JSON file.'''
        try:
            with open(file, 'r') as f:
                return json.load(f)[name]
        except Exception as e:
            errors.DataLoadingError(e.__cause__)

    def write_json(data, show_text = False, file = variables.standart_config_file):
        '''Writes the text to the given/standart JSON file.'''
        try:
            with open(file, 'w') as f:
                json.dump(data, f)
                f.close()

                if show_text:
                    print(console.log('Data ' + str(data) + ' added to ' + str(file) + '.'))
        except Exception as e:
            errors.DataWritingError(e.__cause__)

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

class translate_text():
    def __init__(category: str, text: str):
        language = str(json_module.get_config('Config')['Language'])
        if category == 'B':
            return json_module.get_config('Bot', 'data/lang/' + language + '/bot.json')[text]
        elif category == 'C':
            return json_module.get_config('Commands', 'data/lang/' + language + '/commands.json')[text]
        elif category == 'CC':
            return json_module.get_config('Command creator', 'data/lang/' + language + '/command_creator.json')[text]
        elif category == 'E':
            return json_module.get_config('Error', 'data/lang/' + language + '/errors.json')[text]
        elif category == 'F':
            return json_module.get_config('Functions', 'data/lang/' + language + '/functions.json')[text]
        elif category == 'R':
            with open(r'data/lang/' + json_module.get_config('Config')['Language'] + r'/rules.txt', 'r') as f:
                return f.read()
        else:
            errors.UnexpectedValueError('B, C, CC, E, F, R', category)
