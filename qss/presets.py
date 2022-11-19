from dataclasses import dataclass, fields


@dataclass
class PresetValue:
    light: str
    dark: str


@dataclass
class Preset:
    baseFontColor: PresetValue = PresetValue(
        light="#555555",
        dark="#ffffff",
    )
    baseBackgroundColor: PresetValue = PresetValue(
        light="rgb(240, 240, 240)",
        dark="#31363b",
    )
    disabledFontColor: PresetValue = PresetValue(
        light="gray",
        dark="lightgray",
    )
    disabledBackgroundColor: PresetValue = PresetValue(
        light="lightgray",
        dark="gray",
    )
    tooltipBackgroundColor: PresetValue = PresetValue(
        light="rgb(240, 240, 240)",
        dark="rgb(240, 240, 240)",
    )
    tooltipFontColor: PresetValue = PresetValue(
        light="#555555",
        dark="#555555",
    )
    menubarBorderColor: PresetValue = PresetValue(
        light="lightgray",
        dark="darkgray",
    )
    menuItemBackgroundColor: PresetValue = PresetValue(
        light="rgb(240, 240, 240)",
        dark="#31363b",
    )
    menuItemSelectedColor: PresetValue = PresetValue(
        light="white",
        dark="black",
    )
    menuItemSelectedBackgroundColor: PresetValue = PresetValue(
        light="dodgerblue",
        dark="lightsteelblue",
    )
    menuBorderColor: PresetValue = PresetValue(
        light="lightgray",
        dark="darkgray",
    )
    sectionBackgroundColor: PresetValue = PresetValue(
        light="rgb(250, 250, 250)",
        dark="#474f56",
    )
    viewBackgroundColor: PresetValue = PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    )
    buttonBorderColor: PresetValue = PresetValue(
        light="darkgray",
        dark="gray",
    )
    progressbarBackgroundColor: PresetValue = PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    )
    progressbarBorderColor: PresetValue = PresetValue(
        light="darkgray",
        dark="darkgray",
    )
    progressbarChunkBackgroundColor: PresetValue = PresetValue(
        light="powderblue",
        dark="rgb(30, 50, 75)",
    )
    comboboxBackgroundColor: PresetValue = PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    )
    comboboxBorderColor: PresetValue = PresetValue(
        light="darkgray",
        dark="darkgray",
    )
    comboboxSelectionBackgroundColor: PresetValue = PresetValue(
        light="lightskyblue",
        dark="dodgerblue",
    )
    spinboxBackgroundColor: PresetValue = PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    )
    textInputBackgroundColor: PresetValue = PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    )
    textInputBorderColor: PresetValue = PresetValue(
        light="darkgray",
        dark="gray",
    )
    tabwidgetBorderColor: PresetValue = PresetValue(
        light="darkgray",
        dark="darkgray",
    )
    tabBorderColor: PresetValue = PresetValue(
        light="darkgray",
        dark="darkgray",
    )
    statusbarBorderColor: PresetValue = PresetValue(
        light="darkgray",
        dark="darkgray",
    )

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
