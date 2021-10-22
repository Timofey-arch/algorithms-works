"""Playlist class, realizing... music playlist?
    I don't know how to describe it by another way"""
from LinkedList import LinkedList


class PlayList(LinkedList):
    playlist_number = 1
    standard_icon_path = r"C:\Users\user\Desktop\Алгоритмы\Spotifuck\Interface\SpotiFuckButtonsImages" \
                         "\playlist_standart_icon.png"

    def __init__(self, playlist_name, playlist_author, icon=None):
        super().__init__()
        self.current_composition = None
        self.__playlist_name = playlist_name
        self.__playlist_author = playlist_author
        self.icon = icon
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
        if file_path:
            self.icon = file_path
        else:
            self.icon = self.standard_icon_path

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
