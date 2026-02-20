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
        self.list_widget = QListWidget(self)
        self.list_widget.addItems(
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
        self.tab_widget.addTab(self.list_widget, "List")
        self.tab_widget.addTab(plaintextedit, "TextEdit")
        self.tab_widget.addTab(self.splitter, "Splitter")

        self.cat_action = QAction(QIcon("icons/icons8-fat-cat-96.png"), "Cat")
        self.cat_action.triggered.connect(self.toggle_theme)
        self.dog_action = QAction("Dog")
        self.dog_action.triggered.connect(self._dog)
        self.bird_action = QAction("Bird")
        self.bird_action.triggered.connect(self._bird)
        main_toolbar = QToolBar(self)
        main_toolbar.addAction(self.cat_action)
        main_toolbar.addAction(self.dog_action)
        main_toolbar.addAction(self.bird_action)
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

    def _bird(self):
        # The following birb species name is not verified!
        birds = [
            "African Grey Parrot", "Albatross", "American Crow", "American Goldfinch", "American Kestrel",
            "American Robin", "Anhinga", "Anna's Hummingbird", "Arctic Tern", "Atlantic Puffin",
            "Australian King Parrot", "Bald Eagle", "Baltimore Oriole", "Barn Owl", "Barn Swallow",
            "Barred Owl", "Belted Kingfisher", "Black Vulture", "Black-capped Chickadee", "Black-headed Gull",
            "Blue Grosbeak", "Blue Jay", "Blue Tit", "Blue-footed Booby", "Bobolink",
            "Bohemian Waxwing", "Brown Creeper", "Brown Pelican", "Budgerigar", "Buff-breasted Sandpiper",
            "Canada Goose", "Canvasback", "Carolina Chickadee", "Carolina Wren", "Caspian Tern",
            "Cattle Egret", "Cedar Waxwing", "Chipping Sparrow", "Clark's Nutcracker", "Common Blackbird",
            "Common Eider", "Common Grackle", "Common Kingfisher", "Common Loon", "Common Merganser",
            "Common Nighthawk", "Common Redpoll", "Common Tern", "Cooper's Hawk", "Corncrake",
            "Crested Auklet", "Crested Caracara", "Dark-eyed Junco", "Downy Woodpecker", "Eastern Bluebird",
            "Eastern Meadowlark", "Eastern Phoebe", "Eastern Screech Owl", "Eurasian Blackcap", "Eurasian Blue Tit",
            "Eurasian Collared Dove", "Eurasian Eagle-Owl", "Eurasian Jay", "Eurasian Nuthatch", "Eurasian Sparrowhawk",
            "European Goldfinch", "European Greenfinch", "European Robin", "Evening Grosbeak", "Ferruginous Hawk",
            "Florida Scrub Jay", "Forster's Tern", "Galah", "Gannet", "Golden Eagle",
            "Golden-crowned Kinglet", "Goldcrest", "Gray Catbird", "Gray Heron", "Gray Jay",
            "Great Blue Heron", "Great Crested Flycatcher", "Great Egret", "Great Gray Owl", "Great Horned Owl",
            "Great Kiskadee", "Great Skua", "Greater Flamingo", "Greater Roadrunner", "Greater Sage-Grouse",
            "Green Heron", "Green Jay", "Green Woodpecker", "Grey Parrot", "Gyrfalcon",
            "Harlequin Duck", "Harris's Hawk", "Herring Gull", "Hoatzin", "Horned Grebe",
            "Horned Lark", "House Finch", "House Sparrow", "House Wren", "Hudsonian Godwit",
            "Indigo Bunting", "Ivory Gull", "Jackdaw", "Jabiru", "Juniper Titmouse",
            "Kea", "Kestrel", "Killdeer", "King Eider", "King Penguin",
            "King Vulture", "Lapland Longspur", "Lark Bunting", "Laughing Kookaburra", "Lazuli Bunting",
            "Lesser Black-backed Gull", "Little Egret", "Loggerhead Shrike", "Long-tailed Duck", "Long-tailed Jaeger",
            "Magnolia Warbler", "Mallard", "Mandarin Duck", "Marbled Godwit", "Marsh Harrier",
            "Merlin", "Mountain Bluebird", "Mute Swan", "Northern Cardinal", "Northern Flicker",
            "Northern Gannet", "Northern Goshawk", "Northern Harrier", "Northern Mockingbird", "Northern Pintail",
            "Northern Shoveler", "Northern Shrike", "Olive-backed Sunbird", "Olive Warbler", "Osprey",
            "Pacific Loon", "Painted Bunting", "Palm Warbler", "Peregrine Falcon", "Phainopepla",
            "Pileated Woodpecker", "Pink-footed Goose", "Pine Grosbeak", "Pine Siskin", "Plain Chachalaca",
            "Plumbeous Vireo", "Pomarine Jaeger", "Purple Finch", "Purple Gallinule", "Purple Martin",
            "Red Crossbill", "Red Knot", "Red Phalarope", "Red-bellied Woodpecker", "Red-breasted Merganser",
            "Red-eyed Vireo", "Red-footed Booby", "Red-headed Woodpecker", "Red-shouldered Hawk", "Red-tailed Hawk",
            "Red-throated Loon", "Ring-billed Gull", "Ring-necked Duck", "Rock Dove", "Rock Ptarmigan",
            "Rock Wren", "Rose-breasted Grosbeak", "Rose-ringed Parakeet", "Ross's Gull", "Royal Tern",
            "Ruby-crowned Kinglet", "Ruby-throated Hummingbird", "Ruddy Duck", "Ruff", "Sandhill Crane",
            "Sanderling", "Savannah Sparrow", "Scarlet Ibis", "Scarlet Macaw", "Scissor-tailed Flycatcher",
            "Snow Bunting", "Snow Goose", "Snowy Egret", "Snowy Owl", "Song Sparrow",
            "Spotted Dove", "Spotted Owl", "Starling", "Steller's Jay", "Surf Scoter",
            "Swainson's Hawk", "Swainson's Thrush", "Tree Swallow", "Trumpeter Swan", "Tufted Duck",
            "Tufted Titmouse", "Turkey Vulture", "Ural Owl", "Varied Thrush", "Verdin",
            "Vermilion Flycatcher", "Virginia Rail", "Western Bluebird", "Western Grebe", "Western Meadowlark",
            "Western Tanager", "White Ibis", "White Pelican", "White Stork", "White-throated Sparrow",
            "Whooping Crane", "Wild Turkey", "Willow Ptarmigan", "Wilson's Phalarope", "Winter Wren",
            "Wood Duck", "Wood Thrush", "Yellow Warbler", "Yellow-bellied Sapsucker", "Yellow-billed Cuckoo",
            "Yellow-breasted Chat", "Yellow-eyed Penguin", "Yellow-rumped Warbler", "Zebra Finch", "Zenaida Dove"
        ]
        self.list_widget.addItems(birds)

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
