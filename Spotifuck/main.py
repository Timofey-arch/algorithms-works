from Composition import Composition
from LinkedList import LinkedList
from PyQt5 import QtWidgets
import sys
from Interface.SpotiFuckDesign import Ui_SpotiFuck
from Interface.AddPlaylistWindow import Ui_AddPlayListWindow


class SpotiFuckMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SpotiFuckMainWindow, self).__init__()
        self.ui = Ui_SpotiFuck()
        self.ui.setupUi(self)
        self.ui.AddPlaylist.connect(self.add_playlist)
        self.ui.DeletePlaylist.connect(self.delete_playlist)
        self.ui.AddMusicToPlaylist.connnect(self.add_music_to_playlist)
        self.ui.DeleteMusicFromPlaylist.connect(self.delete_music_from_playlist)
        self.ui.InsertMusicToPlaylist.connect(self.insert_music_to_playlist)
        self.ui.Previous.connect(self.previous_track)
        self.ui.Next.connect(self.next_track)
        self.ui.PlayPause.connect(self.pause_play_track)
        self.ui.VolumeMinus.connect(self.volume_minus)
        self.ui.VolumeAbleDisable.connect(self.volume_able_disable)
        self.ui.VolumePlus.connect(self.volume_plus)


    def add_playlist(self):
        pass

    def delete_playlist(self):
        pass

    def add_music_to_playlist(self):
        pass

    def delete_music_from_playlist(self):
        pass

    def insert_music_to_playlist(self):
        pass

    def pause_play_track(self):
        pass

    def previous_track(self):
        pass

    def next_track(self):
        pass

    def volume_minus(self):
        pass

    def volume_able_disable(self):
        pass

    def volume_plus(self):
        pass


class AddPlaylistWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddPlaylistWindow, self).__init__()
        self.ui = Ui_AddPlayListWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication([])
    application = SpotiFuckMainWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
