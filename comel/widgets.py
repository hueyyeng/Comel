from PySide6.QtWidgets import QCheckBox


class CCheckBox(QCheckBox):
    DEFAULT_SIZE = 12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCheckBoxSize()

    def setCheckBoxSize(self, size: int = None):
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
