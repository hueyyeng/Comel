import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from comel.wrapper import ComelMainWindowWrapper


class BareboneApp(ComelMainWindowWrapper):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Barebone App")
        self.setWindowIcon(QPixmap("icons/icons8-fat-cat-96.png"))

        self.setup_ui()
        self.setup_ui_menu_bar()

    def setup_ui(self):
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout()
        self.main_widget.setLayout(layout)

        self.theme_label = QLabel("Light Theme" if self.is_light else "Dark Theme")
        self.theme_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.theme_label)

        toggle_theme_btn = QPushButton("Toggle Theme")
        toggle_theme_btn.clicked.connect(self.run_toggle_theme)
        layout.addWidget(toggle_theme_btn)

    def setup_ui_menu_bar(self):
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        file_menu = QMenu("File", self.menu_bar)
        self.menu_bar.addMenu(file_menu)
        self.exit_action = QAction("Exit", file_menu)
        self.exit_action.triggered.connect(self.close)
        file_menu.addAction(self.exit_action)

    def run_toggle_theme(self):
        self.toggle_theme()
        text = "Light Theme" if self.is_light else "Dark Theme"
        self.theme_label.setText(text)


def main():
    app = QApplication(sys.argv)
    barebone_app = BareboneApp()
    barebone_app.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
