"""Playlist class, realizing... music playlist?
    I don't know how to describe it by another way"""
from LinkedList import LinkedList


class PlayList(LinkedList):

    def __init__(self, playlist_name, playlist_description, playlist_author, icon=None):
        super().__init__()
        self.current_composition = None
        self.__playlist_name = playlist_name
        self.__playlist_author = playlist_author
        self.__playlist_description = playlist_description
        self.icon = icon
        self.total_time = 0

    @property
    def playlist_name(self):
        return self.__playlist_name

    @property
    def playlist_author(self):
        return self.__playlist_author

    @property
    def playlist_description(self):
        return self.__playlist_description

    @playlist_name.setter
    def playlist_name(self, playlist_name):
        if playlist_name:
            self.__playlist_name = playlist_name
        else:
            raise NameError("Поле названия плейлиста пустое")

    @playlist_author.setter
    def playlist_author(self, playlist_author):
        if playlist_author:
            self.__playlist_author = playlist_author
        else:
            raise NameError("Поле автора плейлиста пустое")

    @playlist_description.setter
    def playlist_description(self, playlist_description):
        if playlist_description:
            self.__playlist_description = playlist_description
        else:
            raise NameError("Поле описания плейлиста пустое")

    def total_time(self):
        """Return total time of the playlist"""
        return self.total_time

    def count_of_tracks(self):
        """Return count of tracks in the playlist"""
        return self.length

    def append_track(self, track, position, previous_track=None):
        """Append track in the position"""
        if position == "begin":
            self.append_left(track)
            self.total_time += track.time()
        if position == "middle":
            if previous_track is not None:
                self.insert(previous_track, track)
                self.total_time += track.time()
            else:
                raise AttributeError("Отсутствует параметр previous_track")
        if position == "end":
            self.append_right(track)
            self.total_time += track.time()

    def delete_track(self, track):
        """Delete track from the playlist"""
        self.remove(track)
        self.total_time -= track.time()

    def play_all(self, track):
        """Starts playing music from track"""
        pass

    def next_track(self):
        """Starts next track"""
        self.current_composition = self.current_composition.next_link
        self.current_composition.data.play()

    def previous_track(self):
        """Starts previous track"""
        self.current_composition = self.current_composition.previous_link
        self.current_composition.data.play()

    def pause_track(self):
        """Pause/Play track"""
        pause_flag = False
        if not pause_flag:
            self.current_composition.data.pause()
        else:
            self.current_composition.data.unpause()

    def current(self):
        """Return current composition"""
        return self.current_composition
