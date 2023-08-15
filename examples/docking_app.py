import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from comel.wrapper import ComelMainWindowWrapper


class DockingApp(ComelMainWindowWrapper):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Docking App")
        self.setWindowIcon(QPixmap("icons/icons8-fat-cat-96.png"))
        self.setDockNestingEnabled(True)

        self.setup_ui()
        self.setup_ui_menu_bar()

    def setup_ui(self):
        dock = QDockWidget("List Widget", self)
        w = QWidget(dock)
        dock.setWidget(w)
        w.setMinimumHeight(200)
        w_layout = QVBoxLayout()
        w.setLayout(w_layout)
        list_label = QLabel("Foobar:")
        w_layout.addWidget(list_label)
        list_widget = QListWidget()
        list_widget.addItems(
            [
                "Foo",
                "Bar",
            ]
        )
        w_layout.addWidget(list_widget)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        docker = QDockWidget("LineEdit Widget", self)
        ww = QWidget(docker)
        docker.setWidget(ww)
        ww_layout = QVBoxLayout()
        ww.setLayout(ww_layout)
        name_lineedit = QLineEdit()
        name_lineedit.setPlaceholderText("Type something here")
        ww_layout.addWidget(name_lineedit)
        groupbox = QGroupBox()
        ww_layout.addWidget(groupbox)
        btn = QPushButton("OK")
        btn.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        btn2 = QPushButton("Emergency Exit!")
        btn2.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        btn2.clicked.connect(lambda: QMessageBox.warning(self, "Emergency!", "There is no escape!"))
        layout = QHBoxLayout()
        groupbox.setLayout(layout)
        layout.addWidget(btn)
        layout.addWidget(btn2)
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, docker)

        dockerer = QDockWidget("PlainTextEdit Widget", self)
        www = QWidget(dockerer)
        dockerer.setWidget(www)
        www_layout = QVBoxLayout()
        www.setLayout(www_layout)
        plaintextedit = QPlainTextEdit()
        plaintextedit.setPlaceholderText("Type something here")
        www_layout.addWidget(plaintextedit)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dockerer)

    def setup_ui_menu_bar(self):
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        file_menu = QMenu("File", self.menu_bar)
        self.menu_bar.addMenu(file_menu)

        self.toggle_theme_action = QAction("Toggle Theme", file_menu)
        self.toggle_theme_action.triggered.connect(self.toggle_theme)
        file_menu.addAction(self.toggle_theme_action)

        self.exit_action = QAction("Exit", file_menu)
        self.exit_action.triggered.connect(self.close)
        file_menu.addAction(self.exit_action)


def main():
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Comel")
    docking_app = DockingApp()
    docking_app.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
