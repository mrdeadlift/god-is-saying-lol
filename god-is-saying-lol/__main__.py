import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDesktopWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import leagueofevents

class VideoPlayer(QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path
        self.initUI()
        self.initVideo()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Video Player")
        screen_resolution = QDesktopWidget().screenGeometry()
        self.setGeometry(screen_resolution)
        self.setWindowOpacity(0.7)

        self.video_widget = QVideoWidget(self)
        self.video_widget.setGeometry(screen_resolution)


        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setVolume(25)
        self.media_player.stateChanged.connect(self.on_media_state_changed)

    def initVideo(self):
        # 動画のパスを取得
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_path)))
        self.media_player.play()

    def on_media_state_changed(self, state):
        if state == QMediaPlayer.StoppedState: 
            self.media_player.stop()
            self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.media_player.stop()
            self.close()

def onDeath():
    app = QApplication(sys.argv)
    # 動画のパスを取得
    file_path = resource_path(r'video\Elshaddai_GodIsSaying_720p.mp4')
    if not os.path.exists(file_path):
        print("File does not exist:", file_path)
        return
    player = VideoPlayer(file_path)
    player.show()
    app.exec_()

def onGameJoin():
    app = QApplication(sys.argv)
    # 動画のパスを取得
    file_path = resource_path(r'video\Elshaddai_ItsOkNoProblem_720p.mp4')
    if not os.path.exists(file_path):
        print("File does not exist:", file_path)
        return
    player = VideoPlayer(file_path)
    player.show()
    app.exec_()
    
def onRespawn():
    app = QApplication(sys.argv)
    # 動画のパスを取得
    file_path = resource_path(r'video\Elshaddai_TheBestOnePlease_720p.mp4')
    if not os.path.exists(file_path):
        print("File does not exist:", file_path)
        return
    player = VideoPlayer(file_path)
    player.show()
    app.exec_()
    
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    leagueofevents.subscribe_to_event("onGameJoin", onGameJoin)
    leagueofevents.subscribe_to_event("onDeath", onDeath)
    leagueofevents.subscribe_to_event("onRespawn", onRespawn)
    

