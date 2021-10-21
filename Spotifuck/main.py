from PyQt5.QtWidgets import QListWidgetItem

from Composition import Composition
from LinkedList import LinkedList
from Playlist import PlayList
from PyQt5 import QtWidgets
import sys
from Interface.SpotiFuckDesign import Ui_SpotiFuck
from Interface.AddPlaylistWindow import Ui_AddPlayListWindow


class AddPlaylistWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AddPlaylistWindow, self).__init__()
        self.ui = Ui_AddPlayListWindow()
        self.ui.setupUi(self)
        self.ui.Ok.clicked.connect(self.ok)
        self.ui.Cancel.clicked.connect(self.cancel)

    def ok(self):
        new_playlist = PlayList(None, None, None, None)
        new_playlist.playlist_name = self.ui.InputName
        new_playlist.playlist_author = self.ui.InputAuthor
        new_playlist.playlist_description = self.ui.InputDescr
        return new_playlist

    def cancel(self):
        self.exec()


class SpotiFuckMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SpotiFuckMainWindow, self).__init__()
        self.ui = Ui_SpotiFuck()
        self.ui.setupUi(self)
        # Buttons
        self.ui.AddPlaylist.clicked.connect(self.add_playlist)
        self.ui.DeletePlaylist.clicked.connect(self.delete_playlist)
        self.ui.AddMusicToPlaylist.clicked.connect(self.add_music_to_playlist)
        self.ui.DeleteMusicFromPlaylist.clicked.connect(self.delete_music_from_playlist)
        self.ui.InsertMusicToPlaylist.clicked.connect(self.insert_music_to_playlist)
        self.ui.Previous.clicked.connect(self.previous_track)
        self.ui.Next.clicked.connect(self.next_track)
        self.ui.PlayPause.clicked.connect(self.pause_play_track)
        self.ui.VolumeMinus.clicked.connect(self.volume_minus)
        self.ui.VolumeAbleDisable.clicked.connect(self.volume_able_disable)
        self.ui.VolumePlus.clicked.connect(self.volume_plus)
        # highlights
        # self.ui.PlayListList.itemClicked.connect(self.show_playlist_parameters(
        #    self.ui.PlayListList.itemClicked.))
        """self.ui.MusicFromPlaylistList.itemClicked.connect(self.show_track_parameters(
            self.ui.MusicFromPlaylistList.itemClicked.
        ))"""

    def add_playlist(self):
        add_playlist_window = AddPlaylistWindow()
        add_playlist_window.exec_()
        new_playlist = QListWidgetItem(add_playlist_window.ok())
        self.ui.PlayListList.addItem(new_playlist)

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

    def show_playlist_parameters(self, playlist):
        self.ui.PlayListDescription.setText(f"{playlist.playlist_author}, {playlist.length} tracks"
                                            f",{playlist.total_time()} seconds")
        self.ui.PlayListName.setText(playlist.playlist_name)
        self.ui.PlayListIcon.pixmap(playlist.icon)

    def show_track_parameters(self, composition):
        self.ui.MusicPicture.pixmap(composition.icon)
        self.ui.MusicName.setText(composition.music_name)
        self.ui.AuthorName.setText(composition.author)


def main():
    app = QtWidgets.QApplication([])
    application = SpotiFuckMainWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
