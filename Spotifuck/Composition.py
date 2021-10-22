"""Composition class, containing music file"""


class Composition:
    standard_composition_icon = r"C:\Users\user\Desktop\
                                Алгоритмы\Spotifuck\Interface\SpotiFuckButtonsImage\composition_standard_icon.png"

    def __init__(self, music, music_name, author):
        self.music = music
        self.__music_name = music_name
        self.__author = author
        self.icon = Composition.standard_composition_icon

    @property
    def music_name(self):
        return self.__music_name

    @property
    def author(self):
        return self.__author

    @music_name.setter
    def music_name(self, name):
        if name:
            self.__music_name = name
        else:
            raise NameError("Поле имени пустое")

    @author.setter
    def author(self, author):
        if author:
            self.__author = author
        else:
            raise NameError("Поле автор пустой")
