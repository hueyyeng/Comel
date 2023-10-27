import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from comel.widgets import CCheckBox
from comel.wrapper import ComelMainWindowWrapper


class TakusanApp(ComelMainWindowWrapper):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Takusan App")
        self.setWindowIcon(QPixmap("icons/icons8-fat-cat-96.png"))

        self.setup_ui()
        self.setup_ui_menu_bar()

    def setup_ui(self):
        # Main stuff
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        status_bar = QStatusBar()
        status_bar.showMessage("Status Bar Message: Ready")
        self.setStatusBar(status_bar)

        main_layout = QHBoxLayout()
        self.main_widget.setLayout(main_layout)

        side_layout = QVBoxLayout()
        main_layout.addLayout(side_layout)

        self.theme_label = QLabel("Light Theme" if self.is_light else "Dark Theme")
        side_layout.addWidget(self.theme_label)

        toggle_theme_btn = QPushButton("Toggle Theme")
        toggle_theme_btn.setDefault(True)
        toggle_theme_btn.clicked.connect(self.run_toggle_theme)
        side_layout.addWidget(toggle_theme_btn)

        select_color_btn = QPushButton("Select Color")
        select_color_btn.clicked.connect(self.show_color_dialog)
        side_layout.addWidget(select_color_btn)

        disabled_btn = QPushButton("Always Disabled")
        disabled_btn.setEnabled(False)
        side_layout.addWidget(disabled_btn)

        # Options Layout
        options_layout = QHBoxLayout()
        side_layout.addLayout(options_layout)

        combobox = QComboBox()
        combobox.addItems(
            [
                "Ramen",
                "Tempura",
                "Yakiniku",
            ]
        )
        options_layout.addWidget(combobox)

        bt1_radiobtn = QRadioButton("Radio 1")
        bt1_radiobtn.setChecked(True)
        options_layout.addWidget(bt1_radiobtn)
        bt2_radiobtn = QRadioButton("Radio 2")
        options_layout.addWidget(bt2_radiobtn)

        # QProgressBar
        progress_bar = QProgressBar()
        progress_bar.setMinimum(0)
        progress_bar.setMaximum(100)
        progress_bar.setValue(75)
        side_layout.addWidget(progress_bar)

        indeterminate_progress_bar = QProgressBar()
        indeterminate_progress_bar.setMinimum(0)
        indeterminate_progress_bar.setMaximum(0)
        side_layout.addWidget(indeterminate_progress_bar)

        # Input Layout
        input_layout = QFormLayout()
        side_layout.addLayout(input_layout)

        lineedit = QLineEdit()
        input_layout.addRow("QLineEdit:", lineedit)

        textedit = QTextEdit()
        input_layout.addRow("QTextEdit:", textedit)

        # QGroupBox
        groupbox = QGroupBox("GroupBox")
        side_layout.addWidget(groupbox)

        form_layout = QFormLayout()
        groupbox.setLayout(form_layout)

        name_lineedit = QLineEdit()
        form_layout.addRow("Name:", name_lineedit)

        age_spinbox = QSpinBox()
        form_layout.addRow("Age:", age_spinbox)

        knows_japanese_checkbox = CCheckBox()
        form_layout.addRow("Knows Japanese?", knows_japanese_checkbox)

        tab_layout = QVBoxLayout()
        main_layout.addLayout(tab_layout)

        tab_widget = QTabWidget()
        tab_layout.addWidget(tab_widget)
        tab1 = QWidget()
        tab_widget.addTab(tab1, "Tab 1")
        tab1_layout = QVBoxLayout()
        tab1.setLayout(tab1_layout)
        table_widget = QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.insertRow(0)
        ham = QTableWidgetItem("Ham")
        table_widget.setItem(0, 0, ham)
        tab1_layout.addWidget(table_widget)

        tab2 = QWidget()
        tab_widget.addTab(tab2, "Tab 2")
        tab2_layout = QVBoxLayout()
        tab2.setLayout(tab2_layout)
        list_widget = QListWidget()
        list_widget.addItems(
            [
                "JISHO FORM",
                "TE FORM",
                "NAI FORM",
                "MASU FORM",
            ]
        )
        tab2_layout.addWidget(list_widget)

    def setup_ui_menu_bar(self):
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&File", self.menu_bar)
        self.menu_bar.addMenu(file_menu)
        self.open_action = QAction("&Open", self.menu_bar)
        self.open_action.triggered.connect(self.run_open)
        file_menu.addAction(self.open_action)
        self.exit_action = QAction("E&xit", file_menu)
        self.exit_action.triggered.connect(self.close)
        file_menu.addAction(self.exit_action)

        help_menu = QMenu("&Help", self.menu_bar)
        self.menu_bar.addMenu(help_menu)
        self.about_action = QAction("&About", file_menu)
        self.about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(self.about_action)

    def run_toggle_theme(self):
        self.toggle_theme()
        text = "Light Theme" if self.is_light else "Dark Theme"
        self.theme_label.setText(text)

    def run_open(self):
        dialog = QFileDialog(self)
        dialog.setOption(QFileDialog.DontUseNativeDialog)
        if dialog.exec():
            print(dialog.selectedFiles())

    def show_color_dialog(self):
        color_dialog = QColorDialog(self)
        color_dialog.exec()

    def show_about_dialog(self):
        about_dialog = QDialog(self)
        about_dialog.setWindowTitle("About Takusan App")
        about_layout = QVBoxLayout()
        about_dialog.setLayout(about_layout)
        about_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        about_msg_label = QLabel("Example toggleable light/dark theme PySide6 app with various widgets.")
        about_layout.addWidget(about_msg_label)
        about_author_label = QLabel("By Huey Yeng")
        about_author_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        about_layout.addWidget(about_author_label)
        about_dialog.show()


def main():
    app = QApplication(sys.argv)
    takusan_app = TakusanApp()
    takusan_app.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
