import os
import sys
from configparser import ConfigParser


def singleton(cls):
    def inner(*args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            __instance = cls(*args, **kwargs)
            cls.__instance = __instance
            return __instance
    return inner


@singleton
class Configuration(ConfigParser):
    def __init__(self):
        super().__init__()

        if hasattr(sys, 'frozen'):
            configFile = os.path.dirname(os.path.abspath(sys.executable))
        else:
            configFile = os.path.dirname(os.path.abspath(__file__))
        self.configFile = os.path.join(configFile, 'config.ini')

        # we use this for writing a new file, or repairing damaged entries
        self.defaults = {
            'default': {
                'style': 'dark',
                'gameroot': '',
                'currentskin': 'default'
            }
        }

        self.validValues = {
            'default': {
                'style': ['light', 'dark'],
                'gameroot': 'string',
                'currentskin': 'string'
            }
        }

        read = self.read(self.configFile)
        if not read:
            # config file doesn't exist, write defaults
            self.writeDefaults()
        else:
            if self.repairConfig():
                # save the fixed config
                self.saveConfig()


    def writeDefaults(self):
        for key, value in self.defaults.items():
            self[key] = value

        self.saveConfig()

    def saveConfig(self):
        with open(self.configFile, 'w') as confile:
            self.write(confile)

    def repairConfig(self):
        # did we repair anything?
        dirtyConfig = False

        # verify integrity of options, and if not exist, then reset the option
        for k1, v1 in self.defaults.items():
            if k1 in self:
                for k2, v2 in self[k1].items():
                    if isinstance(self.validValues[k1][k2], list):
                        # make sure it is one of the allowed values
                        if self[k1][k2] not in self.validValues[k1][k2]:
                            self[k1][k2] = self.defaults[k1][k2]
                            dirtyConfig = True
                    elif isinstance(self.validValues[k1][k2], str):
                        # value can be anything, but it must be of a certain type
                        if self.validValues[k1][k2] == 'string':
                            # i don't care what the string is
                            if not isinstance(self[k1][k2], str):
                                self[k1][k2] = self.defaults[k1][k2]
                                dirtyConfig = True
                        elif self.validValues[k1][k2] == 'number':
                            # the number is represented in a string,
                            # so verify the string is essentially a number
                            try:
                                int(self[k1][k2])
                            except ValueError:
                                self[k1][k2] = self.defaults[k1][k2]
                                dirtyConfig = True
                        elif self.validValues[k1][k2] == 'bool':
                            # this is also a string
                            if self[k1][k2].lower() not in ('true', 'false'):
                                self[k1][k2] = self.defaults[k1][k2]
                                dirtyConfig = True

        # fill in any possible gaps with default values
        # in this way we'll never have a KeyError, no matter
        # if the real config file is damaged
        for k1, v1 in self.defaults.items():
            if k1 not in self:
                self[k1] = v1
                dirtyConfig = True
            else:
                for k2, v2 in v1.items():
                    if k2 not in self[k1]:
                        self[k1][k2] = v2
                        dirtyConfig = True

        return dirtyConfig
