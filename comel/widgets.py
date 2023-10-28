from PySide6.QtWidgets import QCheckBox, QRadioButton


class CCheckBox(QCheckBox):
    DEFAULT_SIZE = 12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_size()

    def set_size(self, size: int = None):
        if not size:
            size = self.DEFAULT_SIZE

        self.setStyleSheet(
            f"""
                QCheckBox::indicator {{
                  width: {size}px;
                  height: {size}px;
                }}
            """
        )
        self.resize(self.DEFAULT_SIZE, self.DEFAULT_SIZE)


class CRadioButton(QRadioButton):
    DEFAULT_SIZE = 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_size()

    def set_size(self, size: int = None):
        if not size:
            size = self.DEFAULT_SIZE

        self.setStyleSheet(
            f"""
                QRadioButton::indicator {{
                  width: {size}px;
                  height: {size}px;
                }}
            """
        )
        self.resize(self.DEFAULT_SIZE, self.DEFAULT_SIZE)
