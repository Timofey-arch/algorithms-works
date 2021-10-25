"""Composition class, containing music file"""
from PyQt5.QtCore import QUrl
from pygame import mixer


class Composition:
    composition_number = 0
    standard_composition_icon = r"C:\Users\user\Desktop\
                                Алгоритмы\Spotifuck\Interface\SpotiFuckButtonsImage\composition_standard_icon.png"

    def __init__(self, music, music_name=None, author=None):
        self.music = mixer.Sound(music)
        self.__music_name = music_name
        self.__author = author
        self.icon = Composition.standard_composition_icon
        Composition.composition_number += 1

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
            self.__music_name = "STANDARD_MUSIC_NAME"

    @author.setter
    def author(self, author):
        if author:
            self.__author = author
        else:
            self.__author = "SPOTIFUCK"
