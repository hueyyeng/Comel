import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QSizePolicy as QSP

from comel.wrapper import ComelMainWindowWrapper


class VerticalGroupBox(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setSizePolicy(
            QSP.Policy.MinimumExpanding,
            QSP.Policy.MinimumExpanding,
        )

    def layout(self) -> QVBoxLayout:
        return super().layout()

    def addWidget(self, w: QWidget):
        self.layout().addWidget(w)


    def addStretch(self):
        self.layout().addStretch()


class HorizontalLayoutWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

    def layout(self) -> QHBoxLayout:
        return super().layout()

    def addWidget(self, w: QWidget):
        self.layout().addWidget(w)


class GreatestHitGroupBox(VerticalGroupBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text_label = QLabel("Text Label")
        self.addWidget(self.text_label)

        self.unchecked_checkbox = QCheckBox("Unchecked")
        self.addWidget(self.unchecked_checkbox)

        self.checked_checkbox = QCheckBox("Checked")
        self.checked_checkbox.setChecked(True)
        self.addWidget(self.checked_checkbox)

        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Lineedit")
        self.addWidget(self.lineedit)

        self.combobox = QComboBox()
        self.combobox.addItems(
            [
                "Ringo",
                "Mogire",
                "Beam",
            ]
        )
        self.addWidget(self.combobox)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            [
                "Foo",
                "Bar",
            ]
        )
        items = [
            "Milk Tea",
            "Oolong Tea",
            "Jasmine Tea",
            "Green Tea",
            "Bubble Tea",
            "Americano",
            "Cappuccino",
            "Espresso",
            "Frappucino",
            "Ipoh White Coffee",
            "Iced Coffee",
            "Plain Water",
        ]
        for item in items:
            item_ = QStandardItem(item)
            self.model.appendRow(item_)

        self.model.setItem(0, 1, QStandardItem("Chocolate"))
        self.model.setItem(1, 1, QStandardItem("Orange"))
        self.model.setItem(2, 1, QStandardItem("Strawberry"))
        self.model.setItem(3, 1, QStandardItem("A very long name for an unknown flavor"))

        self.listview = QListView()
        self.listview.setModel(self.model)
        self.addWidget(self.listview)

        self.treeview = QTreeView()
        self.treeview.setModel(self.model)
        self.addWidget(self.treeview)

        self.tableview = QTableView()
        self.tableview.setModel(self.model)
        self.addWidget(self.tableview)

        self.addStretch()


class CheckDisabledStateApp(ComelMainWindowWrapper):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Check Disabled State App")
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

        default_btn = QPushButton("Default Button")
        default_btn.setDefault(True)
        layout.addWidget(default_btn)

        default_disabled_btn = QPushButton("Default Button Disabled")
        default_disabled_btn.setDefault(True)
        default_disabled_btn.setEnabled(False)
        layout.addWidget(default_disabled_btn)

        self.compare_widget = HorizontalLayoutWidget(self)
        layout.addWidget(self.compare_widget)

        self.normal_groupbox = GreatestHitGroupBox("Normal State")
        self.compare_widget.addWidget(self.normal_groupbox)

        self.disabled_groupbox = GreatestHitGroupBox("Disabled State")
        self.disabled_groupbox.setDisabled(True)
        self.compare_widget.addWidget(self.disabled_groupbox)

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
    barebone_app = CheckDisabledStateApp()
    barebone_app.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
