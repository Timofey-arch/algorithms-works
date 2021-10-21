"""Composition class, containing music file"""


class Composition:

    def __init__(self, music, music_name, description, author, icon=None):
        self.music = music
        self.__music_name = music_name
        self.__description = description
        self.__author = author
        self.icon = icon

    @property
    def music_name(self):
        return self.__music_name

    @property
    def description(self):
        return self.__description

    @property
    def author(self):
        return self.__author

    @music_name.setter
    def music_name(self, name):
        if name:
            self.__music_name = name
        else:
            raise NameError("Поле имени пустое")

    @description.setter
    def description(self, description):
        if description:
            self.__description = description
        else:
            raise NameError("Поле описания пустое")

    @author.setter
    def author(self, author):
        if author:
            self.__author = author
        else:
            raise NameError("Поле автор пустой")
