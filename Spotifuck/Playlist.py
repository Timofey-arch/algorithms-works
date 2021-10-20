"""Playlist class, realizing... music playlist?
    I don't know how to describe it by another way"""
from LinkedList import LinkedList


class PlayList(LinkedList):

    def __init__(self):
        super().__init__()
        self.current_composition = None

    def append_track(self, track, position, previous_track=None):
        """Append track in the position"""
        if position == "begin":
            self.append_left(track)
        if position == "middle":
            if previous_track is not None:
                self.insert(previous_track, track)
            else:
                raise AttributeError("Отсутствует параметр previous_track")
        if position == "end":
            self.append_right(track)

    def delete_track(self, track):
        """Delete track from the playlist"""
        self.remove(track)

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

