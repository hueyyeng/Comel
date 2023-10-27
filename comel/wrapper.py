import os
from pathlib import Path

import darkdetect
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QMainWindow

PACKAGE_ROOT = Path(os.path.dirname(os.path.dirname(__file__)))
LIGHT_THEME = PACKAGE_ROOT / "comel/themes/light.qss"
DARK_THEME = PACKAGE_ROOT / "comel/themes/dark.qss"


class ComelMainWindowWrapper(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.set_icons_search_path()
        self.is_light = darkdetect.isLight()
        self.apply_stylesheet()

    def set_icons_search_path(self):
        # Using "cicons" to avoid potential name clashing for
        # project that already uses "icons" prefix
        QDir.addSearchPath(
            "cicons",
            os.path.join(self.root, "icons")
        )

    def toggle_theme(self):
        self.is_light = not self.is_light
        self.apply_stylesheet()

    def apply_stylesheet(self):
        theme = LIGHT_THEME if self.is_light else DARK_THEME
        with open(theme, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
