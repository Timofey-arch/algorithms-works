from PyQt5.QtWidgets import QListWidgetItem

from Composition import Composition
from LinkedListItem import LinkedListItem
from Playlist import PlayList
from PyQt5 import QtWidgets
import sys
from Interface.SpotiFuckDesign import Ui_SpotiFuck
from Interface.AddPlaylistWindow import Ui_AddPlayListWindow
from Interface.DeletePlayListWindow import Ui_DeletePlaylistWindow
from Interface.ErrorWindow import Ui_ErrorWindow


class AddPlaylistWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AddPlaylistWindow, self).__init__()
        self.ui = Ui_AddPlayListWindow()
        self.ui.setupUi(self)
        self.ui.Ok.clicked.connect(self.accept)
        self.ui.Cancel.clicked.connect(self.reject)
        self.ui.ChoosePath.clicked.connect(self.choose_path)

    def choose_path(self):
        pass


class DeletePlaylistWindow(QtWidgets.QDialog):
    def __init__(self):
        super(DeletePlaylistWindow, self).__init__()
        self.ui = Ui_DeletePlaylistWindow()
        self.ui.setupUi(self)
        self.ui.Ok.clicked.connect(self.accept)
        self.ui.Cancel.clicked.connect(self.reject)


class ErrorWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ErrorWindow, self).__init__()
        self.ui = Ui_ErrorWindow()
        self.ui.setupUi(self)
        self.ui.Ok.clicked.connect(self.accept)


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
        # Highlights
        # self.ui.PlayListList.itemClicked.connect(self.show_playlist_parameters())
        self.ui.MusicFromPlaylistList.itemClicked.connect(self.show_track_parameters)

    # Works
    def add_playlist(self):
        # Window show
        add_playlist_window = AddPlaylistWindow()
        add_playlist_window.exec()
        # Creating new playlist
        new_playlist = PlayList(None, None)
        new_playlist.playlist_name = add_playlist_window.ui.InputName.text()
        new_playlist.playlist_author = add_playlist_window.ui.InputAuthor.text()
        new_playlist.set_icon(add_playlist_window.ui.FilePath.text())
        # Adding new playlist to PlayListList
        list_widget_item = QListWidgetItem()
        list_widget_item.setData(new_playlist.playlist_number, new_playlist)
        self.ui.PlayListList.addItem(str(new_playlist.playlist_number) + " - " +
                                     list_widget_item.data(new_playlist.playlist_number).playlist_name)
        PlayList.playlist_number += 1

    # Not works yet
    def delete_playlist(self):
        delete_playlist_window = DeletePlaylistWindow()
        delete_playlist_window.exec()
        self.ui.PlayListList.removeItemWidget(self.ui.PlayListList.itemFromIndex(
            int(delete_playlist_window.ui.InputName.text())))

    def add_music_to_playlist(self, composition):
        new_composition = LinkedListItem(None, composition, None)

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
        playlist_information = f"{playlist.playlist_author}, " \
                               f"{playlist.length} track(s), " \
                               f"{playlist.total_time()} seconds"
        self.ui.PlayListDescription.setText(playlist_information)
        self.ui.PlayListName.setText(playlist.playlist_name)

    def show_track_parameters(self):
        pass


def main():
    app = QtWidgets.QApplication([])
    application = SpotiFuckMainWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
