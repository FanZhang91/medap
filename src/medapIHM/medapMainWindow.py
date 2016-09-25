from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MedapMainWindow(QFrame):

    def __init__(self, parent=None):
        super(MedapMainWindow, self).__init__(parent)

        # ----------------------------------------------------------
        # positioning the Graphical tool in the middle of the screen
        # ----------------------------------------------------------
        self.desktop = QApplication.desktop()
        width = self.desktop.width()
        height = self.desktop.height()
        self.appWidth = 0.95 * width
        self.appHeight = 0.85 * height
        self.setMinimumWidth(self.appWidth)
        self.setMinimumHeight(self.appHeight)
        self.setGeometry((width - self.appWidth) / 3, (height - self.appHeight) / 3, self.appWidth, self.appHeight)
        self.normalSize = True
        self.mouseStat = True

        # ----------------------------------------------------------
        # configure the appearance of the graphic tool
        # ----------------------------------------------------------
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        self.setWindowOpacity(0.97)
        self.setMouseTracking(True)
        self.setAutoFillBackground(True)
        self.draw_background()

        # ----------------------------------------------------------
        # initialise the principal components of the graphic tool
        # ----------------------------------------------------------
        #self.analyserTitleBar = TitleBarOfAnalyseur(self)
        #self.analyserToolBar = ToolBarOfAnalyseur(self)
        #self.analyserMainOperatingWidget = MainOperatingWidget(self)
        #self.analyserStatusBar = StatusBar(self)
        #self.analyserMediator = None

        # ----------------------------------------------------------
        # generate a vertical layout to contains all the component upon
        # ----------------------------------------------------------
        self.analyserMainLayout = QVBoxLayout(self)
        #self.analyserMainLayout.addWidget(self.analyserTitleBar)
        #self.analyserMainLayout.addWidget(self.analyserToolBar)
        #self.analyserMainLayout.addWidget(self.analyserMainOperatingWidget)
        #self.analyserMainLayout.addWidget(self.analyserStatusBar)
        self.analyserMainLayout.setSpacing(0)
        self.analyserMainLayout.setContentsMargins(0, 0, 0, 0)
        self.analyserMainLayout.setMargin(0)
        self.analyserMainLayout.setAlignment(Qt.AlignCenter)

    def draw_background(self):
        """
            - configure the background and the size of the graphical tool
        """
        pixmap = QPixmap(":/background.png")
        palette = self.palette()
        if self.normalSize:
            palette.setBrush(QPalette.Background, QBrush(
                pixmap.scaled(QSize(self.appWidth, self.appHeight), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        else:
            palette.setBrush(QPalette.Background, QBrush(
                pixmap.scaled(QSize(self.desktop.width(), self.desktop.height()), Qt.IgnoreAspectRatio,
                              Qt.SmoothTransformation)))

        self.setPalette(palette)
        self.setMask(pixmap.mask())
        self.setAutoFillBackground(True)