from string import Template

from presets import Preset


def generate_light_qss():
    with open("base.qss", "r") as source:
        base_qss = Template(source.read())

    preset = Preset()
    with open("themes/light.qss", "w") as output:
        text = base_qss.substitute(**preset.light())
        output.write(text)


def generate_dark_qss():
    with open("base.qss", "r") as source:
        base_qss = Template(source.read())

    preset = Preset()
    with open("themes/dark.qss", "w") as output:
        text = base_qss.substitute(**preset.dark())
        output.write(text)


def main():
    generate_light_qss()
    generate_dark_qss()


if __name__ == '__main__':
    main()
