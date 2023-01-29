'''
Functions for the discord.py Bot.
© by ElBe.
Version: 1.6

NOTE: Async functions in this file cause errors and should not be created.
'''

#Imports
import discord

import colorama
import datetime
import json
import logging
import os
import platform
import prettytable
import requests
import sqlite3
import typing

#Bot modules
import errors

#Setup
colorama.init()

#Variables
class variables():
    '''All variables used in this module.'''

    standard_logging_file: typing.Final[str] = 'data\\log\\' + str(datetime.datetime.today()) + '.txt'
    standard_datetime_format: typing.Final[str] = '%Y-%m-%d %H:%M:%S'
    standard_logging_format: typing.Final[str] = colorama.Fore.LIGHTBLUE_EX + '{timestamp}' + colorama.Style.RESET_ALL + ' [{color}{level}' + colorama.Style.RESET_ALL + '] {name} {message}'
    standard_config_file: typing.Final[str] = 'data\\config.json'
    standard_database_file: typing.Final[str] = 'data\\bot.db'
    standard_intents: typing.Final[discord.Intents] = discord.Intents.all()

class json_module():
    '''Module for dealing with JSON files.'''

    def __init__(self, file: str = variables.standard_config_file) -> None:
        '''Sets a file to be read.

        Args:
            file (str, optional): File to read. Defaults to variables.standard_config_file.

        Returns:
            None
        '''

        self.file = file

    def get_value(name: str, file: str = variables.standard_config_file) -> object: #TODO: Change all occurrences
        '''Returns a value parsed from a JSON config file.

        Args:
            name (str): Name of the key to be parsed.
            file (str, optional): Relative path to the json config file. Default to 'data\\config.json'.

        Returns:
            object: Object parsed from the JSON file.
        '''
        try:
            with open(file, 'r') as f:
                return json.load(f)[name]
        except Exception as e:
            return errors.DataLoadingError(e.__cause__)

    def write_json(data: object, file: str) -> None:
        '''Writes data to a JSON file.

        Args:
            data (object): Data to insert.
            file (str): Relative path to the json file.
        '''
        try:
            with open(file, 'w') as f:
                json.dump(data, f)
                f.close()
        except Exception as e:
            return errors.DataWritingError(e.__cause__)

    def __str__(self) -> str:
        '''Returns contents of the file as a string.

        Returns:
            str: Contents of the file.
        '''

        with open(self.file, 'r') as f:
            return str(f.read())

class database():
    '''Still in beta!'''
    def __init__(self, database: str = variables.standard_database_file) -> None:
        self.database = sqlite3.connect(database)
        self.cursor = database.cursor()
        
    def get_value(self, key: str, table: str, whereKey: str, whereValue: str) -> object:
        self.cursor.execute('SELECT ' + key + ' FROM ' + table + ' WHERE ' + whereKey + ' = ' + whereValue)
        return self.cursor.fetchall()
    
    def insert_value(self, key: str) -> object:
        pass

class console():
    def clear() -> None:
        '''Clear the console.'''
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def cursor_up() -> None:
        '''Changes the position of the cursor to the line above.'''
        print('\x1b[1A')

    def erase_line() -> None:
        '''Erases the current line.'''
        print('\x1b[2K')

    def erase_last() -> None:
        '''Erases the last line.'''
        print('\x1b[1A' + '\x1b[2K' + '\x1b[1A')

class translate_text():
    def __init__(category: str, text: str) -> str: #TODO: Add language system (LATER)
        '''MODULE IS TURNED OFF'''
        return        
        
        #language = str(json_module.get_config('Config')['Language'])
        #if category == 'B':
        #    return json_module.get_config('Bot', 'data/lang/' + language + '/bot.json')[text]
        #elif category == 'C':
        #    return json_module.get_config('Commands', 'data/lang/' + language + '/commands.json')[text]
        #elif category == 'CC':
        #    return json_module.get_config('Command creator', 'data/lang/' + language + '/command_creator.json')[text]
        #elif category == 'E':
        #    return json_module.get_config('Error', 'data/lang/' + language + '/errors.json')[text]
        #elif category == 'F':
        #    return json_module.get_config('Functions', 'data\\lang\\' + language + '\\functions.json')[text]
        #elif category == 'R':
        #    with open('data\\lang\\' + json_module.get_config('Config')['Language'] + '\\rules.txt', 'r') as f:
        #        return f.read()
        #else:
        #    errors.UnexpectedValueError('B, C, CC, E, F, R', category)

class formation():
    def format_table(table: prettytable.PrettyTable):
        '''Format prettytable.PrettyTables to look better.

        Args:
            table (prettytable.PrettyTable): Table to format.

        Returns:
            table: Formatted table.
        '''        
        
        table.vertical_char = '│'
        table.horizontal_char = '─'
        table.junction_char = '┼'
        table.left_junction_char = '├'
        table.right_junction_char = '┤'
        table.top_left_junction_char = '┌'
        table.top_right_junction_char = '┐'
        table.top_junction_char = '┬'
        table.bottom_left_junction_char = '└'
        table.bottom_right_junction_char = '┘'
        table.bottom_junction_char = '┴'
        
        return table

class create_command():
    def __init__(self, json: dict) -> None:
        '''Creates a command with given json data.

        Args:
            json (dict): Json data to use when creating the command.
            
        Returns:
            None
        '''

        self.json = json

        try:
            requests.post('https://discord.com/api/v10/applications/' + str(json_module.get_config('Config')['Application ID']) + '/commands', headers={'Authorization': 'Bot ' + str(json_module.get_config('Config')['Token'])}, json=json)
        except Exception as e:
            print('Error while trying to create the command /' + str(json['name']) + '.\n' + str(e))

    def __str__(self) -> str:
        '''String representation of the command creator.
        
        Returns:
            str: The string representation of the command creator.
        '''

        return 'Trying to create command /' + self.json['name'] + ' with json:' + str(self.json)

class log():
    def __init__(self, message: str, level: str) -> None:
        '''Logs a message on the given level.

        Args:
            message (str): Message to log.
            level (str): Level to log with. Has to be 'CRITICAL','ERROR','WARNING','INFO' or'DEBUG'. Defaults to 'DEBUG'.
    
        Returns:
            None
        '''

        self.message = message
        self.level = level if level is not None else self.default_level


    def setup(self, format: str = variables.standard_logging_format, default_level: str = 'DEBUG', default_name: str = 'ROOT') -> None:
        '''Sets up logging with the given format, a default level and a default name for unnamed loggers.

        Args:
            format (str, optional): Format for logging. Has to contain '{message}', '{level}' and '{timestamp}'. Can contain '{name}' and '{color}'. Defaults to variables.standard_logging_format.
            default_level (str, optional): Default logging level. Has to be 'CRITICAL','ERROR','WARNING','INFO' or'DEBUG'. Defaults to 'DEBUG'.
            default_name (str, optional): Default logger name. Each function can have its own logger or logger. Defaults to 'ROOT'.

        Returns:
            None
        '''

        self.format = format
        self.default_level = default_level
        self.default_name = default_name

    def __str__(self):
        '''String representation of the logged message.
        
        Returns:
            str: The string representation of the logged message.
        '''

        return #TODO: add return value

class download():
    def __init__(url: str, file: str) -> None:
        '''ATTENTION: The download function is still in experimental state! Errors are expected and should be reported.
        
        Downloads a file from the specified url to the specified file in the download directory.

        Args:
            url (str): URL to download file from.
            file (str): File name to write to. Don't include path.

        Returns:
            None
        '''
        
        if os.path.splitext(url)[1] == os.path.splitext(file)[1]:
            if os.path.exists(os.path.expanduser('~\\Downloads\\' + file)): 
                raise FileExistsError('File ' + file + ' already exists')
            else:
                with open(os.path.expanduser('~\\Downloads\\' + file), 'x') as f:
                    for line in str(str(requests.get(url).content).replace('b\'', '')).split('\\n')[:-1]:
                        f.write(line + '\n')
        else:
            errors.FileExtensionError('File extension from ' + url + ' is not the same as the file extension from ' + file + '.')
