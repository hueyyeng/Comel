from dataclasses import dataclass, fields, field


@dataclass
class PresetValue:
    light: str
    dark: str


@dataclass
class Preset:
    baseFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="#555555",
        dark="#ffffff",
    ))
    baseBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(240, 240, 240)",
        dark="#31363b",
    ))
    disabledFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="gray",
        dark="lightgray",
    ))
    disabledBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="lightgray",
        dark="gray",
    ))
    hoverBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(215, 230, 240)",
        dark="rgb(130, 140, 145)",
    ))
    pressedBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(190, 200, 205)",
        dark="rgb(200, 210, 215)",
    ))
    tableHeaderHoverBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(215, 230, 240)",
        dark="rgb(130, 140, 145)",
    ))
    tableHeaderPressedBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(170, 170, 170)",
        dark="rgb(160, 160, 160)",
    ))
    tooltipBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(240, 240, 240)",
        dark="rgb(240, 240, 240)",
    ))
    tooltipFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="#555555",
        dark="#555555",
    ))
    menubarBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="lightgray",
        dark="darkgray",
    ))
    menuItemBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(240, 240, 240)",
        dark="#31363b",
    ))
    menuItemSelectedColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="black",
    ))
    menuItemSelectedBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="dodgerblue",
        dark="lightsteelblue",
    ))
    menuBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="lightgray",
        dark="darkgray",
    ))
    sectionBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(250, 250, 250)",
        dark="#474f56",
    ))
    viewBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    buttonBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="gray",
    ))
    progressbarBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    progressbarBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="darkgray",
    ))
    progressbarChunkBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="powderblue",
        dark="rgb(30, 50, 75)",
    ))
    comboboxBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    comboboxBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="darkgray",
    ))
    comboboxSelectionBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="lightskyblue",
        dark="dodgerblue",
    ))
    spinboxBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    textInputBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    textInputBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="gray",
    ))
    tabwidgetBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="darkgray",
    ))
    tabBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="darkgray",
    ))
    statusbarBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="darkgray",
    ))

    def light(self) -> dict:
        data = {}
        for f in fields(self):
            value: PresetValue = getattr(self, f.name)
            data[f.name] = value.light

        return data

    def dark(self) -> dict:
        data = {}
        for f in fields(self):
            value: PresetValue = getattr(self, f.name)
            data[f.name] = value.dark

        return data
