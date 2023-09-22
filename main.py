import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
#from app_functions import SharePoint
import config
import os
import logging
import logging.handlers
from app_modules import *
from shareplum import Site, Office365, folder
from shareplum.site import Version

folder_name = 'folder1'

dir_path = "D:\TAA1"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        SharePoint.initShareData(self)
        self.show()

        #self.ui.browseButton.clicked.connect(lambda: Exporter.open_file_dialog(self))
        self.ui.exportButton.clicked.connect(lambda: SharePoint.upload_folder(self,folder_name, dir_path ))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    logFolder = os.getenv('APPDATA')
    if logFolder is None:
        logFolder = os.environ['USERPROFILE']
            
    logFolder = logFolder + "\\ShareUpload\\Logs\\"
    if not os.path.exists(os.path.dirname(logFolder)):
       os.makedirs(os.path.dirname(logFolder))
    handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", logFolder + "AppLogs.log"))
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    root.addHandler(handler)
    window = MainWindow()
    sys.exit(app.exec_())