from __future__ import annotations

import random
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from comel.wrapper import ComelMainWindowWrapper
from widgets import HorizontalToolBar, VerticalToolBar


class TabPositionButton(QPushButton):
    def __init__(self, text: str, tab_pos: QTabWidget.TabPosition, parent: TabWidgetsApp):
        super().__init__(parent)
        self.parent_ = parent
        self.setText(text)
        self.tab_pos: QTabWidget.TabPosition = tab_pos

        self.clicked.connect(self._clicked)

    def _clicked(self):
        self.parent_.tab_widget.setTabPosition(self.tab_pos)


class TabWidgetsApp(ComelMainWindowWrapper):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tab Widgets App")
        self.setWindowIcon(QPixmap("icons/icons8-fat-cat-96.png"))

        self.setup_ui()
        self.setup_ui_menu_bar()

    def setup_ui(self):
        list_widget = QListWidget(self)
        list_widget.addItems(
            [
                "Foo",
                "Bar",
            ]
        )

        plaintextedit = QPlainTextEdit(self)
        plaintextedit.setPlaceholderText("Type something here")

        set_split_hori_btn = QPushButton("Horizontal")
        set_split_hori_btn.clicked.connect(self._set_splitter_horizontal)

        set_split_vert_btn = QPushButton("Vertical")
        set_split_vert_btn.clicked.connect(self._set_splitter_vertical)

        left_split_widget = VerticalToolBar(self)
        left_split_widget.addWidget(set_split_hori_btn)

        right_split_widget = VerticalToolBar(self)
        right_split_widget.addWidget(set_split_vert_btn)

        self.splitter = QSplitter(self)
        self.splitter.addWidget(left_split_widget)
        self.splitter.addWidget(right_split_widget)

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_widget.addTab(list_widget, "List")
        self.tab_widget.addTab(plaintextedit, "TextEdit")
        self.tab_widget.addTab(self.splitter, "Splitter")

        self.cat_action = QAction(QIcon("icons/icons8-fat-cat-96.png"), "Cat")
        self.cat_action.triggered.connect(self.toggle_theme)
        self.dog_action = QAction("Dog")
        self.dog_action.triggered.connect(self._dog)
        main_toolbar = QToolBar(self)
        main_toolbar.addAction(self.cat_action)
        main_toolbar.addAction(self.dog_action)
        self.addToolBar(main_toolbar)

        position_toolbar = HorizontalToolBar(self)
        north_btn = TabPositionButton("North", QTabWidget.TabPosition.North, self)
        south_btn = TabPositionButton("South", QTabWidget.TabPosition.South, self)
        east_btn = TabPositionButton("East", QTabWidget.TabPosition.East, self)
        west_btn = TabPositionButton("West", QTabWidget.TabPosition.West, self)
        position_toolbar.addWidget(north_btn)
        position_toolbar.addWidget(south_btn)
        position_toolbar.addWidget(east_btn)
        position_toolbar.addWidget(west_btn)

        central_widget = VerticalToolBar(self)
        central_widget.addWidget(position_toolbar)
        central_widget.addWidget(self.tab_widget)

        self.setCentralWidget(central_widget)

    def _set_splitter_horizontal(self):
        self.splitter.setOrientation(Qt.Orientation.Horizontal)

    def _set_splitter_vertical(self):
        self.splitter.setOrientation(Qt.Orientation.Vertical)

    def _dog(self):
        titles = [
            "Dog",
            "Doug",
            "Dawg",
            "Doggo",
            "Doggoneit",
            "Cat",
        ]
        existing_title = self.windowTitle()
        title = random.choice(titles)
        while title == existing_title:
            title = random.choice(titles)

        self.setWindowTitle(title)

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
    docking_app = TabWidgetsApp()
    docking_app.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
