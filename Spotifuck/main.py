from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QAction, QFileDialog

from Composition import Composition
from LinkedListItem import LinkedListItem
from Playlist import PlayList
from PyQt5 import QtWidgets
import sys
from Interface.SpotiFuckDesign import Ui_SpotiFuck
from Interface.AddPlaylistWindow import Ui_AddPlayListWindow
from Interface.ErrorWindow import Ui_ErrorWindow
from Interface.AddMusicWindow import Ui_AddMusicWindow


def show_playlist_items(playlist):
    for i in range(playlist.length):
        print(playlist[i].data.music_name)
    print("-----------------------------")


class AddPlaylistWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AddPlaylistWindow, self).__init__()
        self.ui = Ui_AddPlayListWindow()
        self.ui.setupUi(self)
        self.ui.Ok.clicked.connect(self.accept)
        self.ui.Cancel.clicked.connect(self.reject)
        self.ui.ChoosePath.clicked.connect(self.choose_path)

    def choose_path(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "PNG Files(*.png);;JPEG File(*.jpg);; All Files(*)")
        self.ui.FilePath.setText(filename)


class AddMusicWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AddMusicWindow, self).__init__()
        self.ui = Ui_AddMusicWindow()
        self.ui.setupUi(self)
        self.ui.Ok.clicked.connect(self.accept)
        self.ui.Cancel.clicked.connect(self.reject)
        self.ui.ChooseMusicFilePath.clicked.connect(self.choose_music_file_path)
        self.ui.ChoosePicturePath.clicked.connect(self.choose_picture_file_path)

    def choose_music_file_path(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "MP3 Files(*.mp3);;WAV File(*.wav);; All Files(*)")
        self.ui.MusicFilePath.setText(filename)

    def choose_picture_file_path(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "PNG Files(*.png);;JPEG File(*.jpg);; All Files(*)")
        self.ui.PictureFilePath.setText(filename)


class ErrorWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ErrorWindow, self).__init__()
        self.ui = Ui_ErrorWindow()
        self.ui.setupUi(self)
        self.ui.Ok.clicked.connect(self.accept)


class SpotiFuckMainWindow(QtWidgets.QMainWindow):
    PLAYLIST_ROLE = Qt.UserRole
    COMPOSITION_ROLE = Qt.UserRole + 1
    LINKED_LIST_ITEM_ROLE = Qt.UserRole + 2

    def __init__(self):
        super(SpotiFuckMainWindow, self).__init__()
        self.ui = Ui_SpotiFuck()
        self.ui.setupUi(self)
        window_icon = QIcon("Interface/SpotiFuckButtonsImages/SpotiFuckLogo.png")
        self.setWindowIcon(window_icon)
        # Actions
        self.delete = QAction()
        self.add = QAction()
        self.delete.setText("Delete playlist")
        self.add.setText("Add playlist")
        self.delete_track = QAction()
        self.add_track = QAction()
        self.insert_track = QAction()
        self.delete_track.setText("Delete track")
        self.add_track.setText("Add track")
        self.insert_track.setText("Insert new track after current")
        # Buttons
        self.ui.AddPlaylist.clicked.connect(self.add_playlist)
        self.ui.DeletePlaylist.clicked.connect(self.delete_playlist)
        self.ui.AddMusicToPlaylist.clicked.connect(self.add_music_to_playlist)
        self.ui.DeleteMusicFromPlaylist.clicked.connect(self.delete_music_from_playlist)
        self.ui.InsertMusicToPlaylist.clicked.connect(self.insert_music_to_playlist)
        self.ui.Previous.clicked.connect(self.previous_track)
        self.ui.Next.clicked.connect(self.next_track)
        self.ui.PlayPause.clicked.connect(self.pause_play_track)
        self.ui.PlayPause.clicked.connect(self.show_track_parameters)
        self.ui.VolumeMinus.clicked.connect(self.volume_minus)
        self.ui.VolumeAbleDisable.clicked.connect(self.volume_able_disable)
        self.ui.VolumePlus.clicked.connect(self.volume_plus)
        # Context menu actions
        self.add.triggered.connect(self.add_playlist)
        self.delete.triggered.connect(self.delete_playlist)
        self.add_track.triggered.connect(self.add_music_to_playlist)
        self.delete_track.triggered.connect(self.delete_music_from_playlist)
        self.insert_track.triggered.connect(self.insert_music_to_playlist)
        # Highlights
        self.ui.PlayListList.itemClicked.connect(self.show_playlist_parameters)

    def create_context_menu(self):
        self.ui.PlayListList.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.PlayListList.addAction(self.add)
        self.ui.PlayListList.addAction(self.delete)
        self.ui.MusicFromPlaylistList.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.MusicFromPlaylistList.addAction(self.add_track)
        self.ui.MusicFromPlaylistList.addAction(self.delete_track)
        self.ui.MusicFromPlaylistList.addAction(self.insert_track)

    @staticmethod
    def create_error_window(error_code):
        error_window = ErrorWindow()
        error_window.ui.ErrorCode.setText(error_code)
        error_window.exec()

    def add_playlist(self):
        add_playlist_window = AddPlaylistWindow()
        add_playlist_window.exec()

        new_playlist = PlayList(None, None)
        new_playlist.playlist_name = add_playlist_window.ui.InputName.text()
        new_playlist.playlist_author = add_playlist_window.ui.InputAuthor.text()
        if add_playlist_window.ui.FilePath.text():
            new_playlist.set_icon(add_playlist_window.ui.FilePath.text())
        else:
            new_playlist.set_icon(PlayList.standard_playlist_icon)

        list_widget_item = QListWidgetItem()
        list_widget_item.setData(self.PLAYLIST_ROLE, new_playlist)
        list_widget_item.setText(new_playlist.playlist_name)
        self.ui.PlayListList.addItem(list_widget_item)

    def delete_playlist(self):
        if not self.ui.PlayListList.currentItem():
            self.create_error_window("First, select a playlist to delete")
            return
        self.ui.PlayListList.takeItem(self.ui.PlayListList.currentRow())
        self.ui.PlayListIcon.clear()
        self.ui.PlayListName.setText("There is nothing...")
        self.ui.PlayListDescription.setText("...sounds of crickets...")
        self.ui.MusicFromPlaylistList.clear()

    def add_music_to_playlist(self):
        if not self.ui.PlayListList.currentItem():
            self.create_error_window("First, select a playlist to add music")
            return

        add_music_window = AddMusicWindow()
        add_music_window.exec()

        if add_music_window.ui.Ok.clicked and not add_music_window.ui.MusicFilePath.text():
            self.create_error_window("Choose music file")
            return

        playlist = self.ui.PlayListList.currentItem().data(self.PLAYLIST_ROLE)

        composition = Composition(add_music_window.ui.MusicFilePath.text())
        composition.music_name = add_music_window.ui.InputName.text()
        composition.author = add_music_window.ui.InputAuthor.text()
        if add_music_window.ui.PictureFilePath.text():
            composition.icon = add_music_window.ui.PictureFilePath.text()
        else:
            composition.icon = Composition.standard_composition_icon

        playlist_item = LinkedListItem(None, composition, None)
        music_from_playlist_item = QListWidgetItem()
        music_from_playlist_item.setData(self.LINKED_LIST_ITEM_ROLE, playlist_item)
        music_from_playlist_item.setText(composition.author + " - " + composition.music_name)
        playlist.append_right(playlist_item)
        show_playlist_items(playlist)
        self.ui.MusicFromPlaylistList.addItem(music_from_playlist_item)
        playlist_description = f"{playlist.playlist_author}, {playlist.length} track(s), {playlist.total_time} seconds"
        self.ui.PlayListDescription.setText(playlist_description)

    def delete_music_from_playlist(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            self.create_error_window("First, select a music to delete")
            return
        playlist = self.ui.PlayListList.currentItem().data(self.PLAYLIST_ROLE)
        linked_list_item = self.ui.MusicFromPlaylistList.currentItem().data(self.LINKED_LIST_ITEM_ROLE)
        playlist.delete_track(linked_list_item)
        self.ui.MusicFromPlaylistList.takeItem(self.ui.MusicFromPlaylistList.currentRow())
        self.ui.MusicPicture.clear()
        self.ui.MusicName.clear()
        self.ui.AuthorName.clear()
        self.show_playlist_parameters()

    def insert_music_to_playlist(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            self.create_error_window("First, select a music to insert")
            return
        playlist = self.ui.PlayListList.currentItem().data(self.PLAYLIST_ROLE)
        previous_item = self.ui.MusicFromPlaylistList.currentItem().data(self.LINKED_LIST_ITEM_ROLE)

        add_music_window = AddMusicWindow()
        add_music_window.exec()

        composition = Composition(add_music_window.ui.MusicFilePath.text())
        composition.music_name = add_music_window.ui.InputName.text()
        composition.author = add_music_window.ui.InputAuthor.text()
        if add_music_window.ui.PictureFilePath.text():
            composition.icon = add_music_window.ui.PictureFilePath.text()
        else:
            composition.icon = Composition.standard_composition_icon

        new_item = LinkedListItem(None, composition, None)
        music_from_playlist_item = QListWidgetItem()
        music_from_playlist_item.setData(self.LINKED_LIST_ITEM_ROLE, new_item)
        music_from_playlist_item.setText(composition.author + " - " + composition.music_name)
        playlist.append_track(previous_item, new_item)
        show_playlist_items(playlist)
        self.show_playlist_parameters()

    def pause_play_track(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            return

    def previous_track(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            return

    def next_track(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            return

    def volume_minus(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            return

    def volume_able_disable(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            return

    def volume_plus(self):
        if not self.ui.MusicFromPlaylistList.currentItem():
            return

    def show_playlist_parameters(self):
        self.ui.MusicFromPlaylistList.clear()
        playlist = self.ui.PlayListList.currentItem().data(self.PLAYLIST_ROLE)
        playlist_description = f"{playlist.playlist_author}, {playlist.length} track(s), {playlist.total_time} seconds"
        playlist_name = playlist.playlist_name
        self.ui.PlayListName.setText(playlist_name)
        self.ui.PlayListDescription.setText(playlist_description)
        icon = QPixmap(playlist.icon)
        self.ui.PlayListIcon.setPixmap(icon)
        for i in range(playlist.length):
            composition = QListWidgetItem()
            track = playlist[i]
            composition.setData(self.LINKED_LIST_ITEM_ROLE, track)
            composition.setText(track.data.music_name + " - " + track.data.author)
            self.ui.MusicFromPlaylistList.addItem(composition)

    def show_track_parameters(self):
        if self.ui.PlayPause.clicked and self.ui.MusicFromPlaylistList.currentItem():
            current_track = self.ui.MusicFromPlaylistList.currentItem().data(self.LINKED_LIST_ITEM_ROLE).data
            icon = QPixmap(current_track.icon)
            self.ui.MusicName.setText(current_track.music_name)
            self.ui.AuthorName.setText(current_track.author)
            self.ui.MusicPicture.setPixmap(icon)


def main():
    app = QtWidgets.QApplication([])
    application = SpotiFuckMainWindow()
    application.create_context_menu()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
