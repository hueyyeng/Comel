import os
from pathlib import Path

import darkdetect
from PySide6.QtWidgets import QMainWindow

PACKAGE_ROOT = Path(os.path.dirname(os.path.dirname(__file__)))
LIGHT_THEME = PACKAGE_ROOT / "comel/themes/light.qss"
DARK_THEME = PACKAGE_ROOT / "comel/themes/dark.qss"


class ComelMainWindowWrapper(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_light = darkdetect.isLight()
        self.apply_stylesheet()

    def toggle_theme(self):
        self.is_light = not self.is_light
        self.apply_stylesheet()

    def apply_stylesheet(self):
        theme = LIGHT_THEME if self.is_light else DARK_THEME
        with open(theme, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
