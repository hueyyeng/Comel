from pathlib import Path
from string import Template

from presets import Preset


def generate_light_qss():
    with open("base.qss", "r") as source:
        base_qss = Template(source.read())

    preset = Preset()
    text = base_qss.substitute(**preset.light())

    qss = Path("themes/light.qss")
    qss.parent.mkdir(exist_ok=True)
    qss.write_text(text)

    export_qss = Path("../comel/themes/light.qss")
    export_qss.write_text(text)


def generate_dark_qss():
    with open("base.qss", "r") as source:
        base_qss = Template(source.read())

    preset = Preset()
    text = base_qss.substitute(**preset.dark())

    qss = Path("themes/dark.qss")
    qss.parent.mkdir(exist_ok=True)
    qss.write_text(text)

    export_qss = Path("../comel/themes/dark.qss")
    export_qss.write_text(text)


def main():
    generate_light_qss()
    generate_dark_qss()


if __name__ == '__main__':
    main()
