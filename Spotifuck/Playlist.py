"""Playlist class, realizing... music playlist?
    I don't know how to describe it by another way"""
from LinkedList import LinkedList


class PlayList(LinkedList):

    def __init__(self):
        super().__init__()
        self.current_composition = None

    def append_track(self, track, position, previous_track=None):
        if position == "begin":
            self.append_left(track)
        if position == "middle":
            self.insert(previous_track, track)
        if position == "end":
            self.append_right(track)

    def delete_track(self, track):
        self.remove(track)

    def play_all(self, track):
        pass

    def next_track(self):
        self.current_composition = self.current_composition.get_next_link()
        self.current_composition.data.play()

    def previous_track(self):
        self.current_composition = self.current_composition.get_previous_link()
        self.current_composition.data.play()

    def pause_track(self):
        pause_flag = False
        if not pause_flag:
            self.current_composition.data.pause()
        else:
            self.current_composition.data.unpause()

    def current(self):
        return self.current_composition

