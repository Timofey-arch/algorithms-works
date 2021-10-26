"""Playlist class, realizing... music playlist?
    I don't know how to describe it by another way"""
import pygame.event

from LinkedList import LinkedList
import pygame

pygame.init()
STOPPED_PLAYING = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(STOPPED_PLAYING)


class PlayList(LinkedList):
    standard_playlist_icon = r"Interface\SpotiFuckButtonsImages\playlist_standard_icon.png"

    def __init__(self, playlist_name, playlist_author):
        super().__init__()
        self.current_composition = None
        self.__playlist_name = playlist_name
        self.__playlist_author = playlist_author
        self.total_time = 0

    @property
    def playlist_name(self):
        return self.__playlist_name

    @property
    def playlist_author(self):
        return self.__playlist_author

    @playlist_name.setter
    def playlist_name(self, playlist_name):
        if playlist_name:
            self.__playlist_name = playlist_name
        else:
            self.__playlist_name = "BORING_PLAYLIST_NAME"

    @playlist_author.setter
    def playlist_author(self, playlist_author):
        if playlist_author:
            self.__playlist_author = playlist_author
        else:
            self.__playlist_author = "BORING_PLAYLIST_AUTHOR"

    def set_icon(self, file_path):
        """Sets image.ico to playlist"""
        self.icon = file_path

    def count_of_tracks(self):
        """Return count of tracks in the playlist"""
        return self.length

    def append_track(self, track, position=None):
        """Append track in the position"""
        if self.length == 0:
            self.current_composition = track
        if position is None:
            self.append_right(track)
        else:
            self.insert(position, track)

    def delete_track(self, track):
        """Delete track from the playlist"""
        self.remove(track)

    def play_all(self, track):
        """Starts playing music from track"""
        self.current_composition = track
        pygame.mixer.music.load(self.current_composition.data.music)
        pygame.mixer.music.play()
        pygame.mixer.music.queue(self.current_composition.next_link.data.music)

    def next_track(self):
        """Starts next track"""
        self.current_composition = self.current_composition.next_link
        pygame.mixer.music.load(self.current_composition.data.music)
        pygame.mixer.music.play()

    def previous_track(self):
        """Starts previous track"""
        self.current_composition = self.current_composition.previous_link
        pygame.mixer.music.load(self.current_composition.data.music)
        pygame.mixer.music.play()

    def play_pause(self, current_composition):
        """Pause/Play track"""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def current(self):
        """Return current composition"""
        return self.current_composition
