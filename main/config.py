import configparser
from os.path import exists
import os

class Config(configparser.ConfigParser):
    '''Project configuration class'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._settings_file = 'settings.ini'
        self._settings_folder = 'main/settings'

        self._file_path = '%s/%s' % (self._settings_folder,
                                     self._settings_file)

        #configuration file check
        if not exists(self._file_path):
            self._create_config()
        else:
            self.read(self._file_path)
        

    def _create_config(self):
        self.add_section('data_base_settings')
        self.set('data_base_settings', 'host', os.environ.get('db', 'not_db'))
        self.set('data_base_settings', 'database', 'test_app')
        self.set('data_base_settings', 'user', 'test_app_admin')
        self.set('data_base_settings', 'password', 'test_app_admin')

        with open(self._file_path, 'w') as file:
            self.write(file)
