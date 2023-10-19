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
        dark="rgb(49, 54, 59)",
    ))
    disabledFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="lightgray",
        dark="rgb(89, 94, 99)",
    ))
    disabledBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(240, 240, 240)",
        dark="rgb(49, 54, 59)",
    ))
    disabledCheckBoxBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(250, 250, 250)",
        dark="rgb(75, 80, 85)",
    ))
    viewSelectionBackgroundColor: PresetValue = field(default_factory=lambda: PresetValue(
        light="rgb(230, 239, 253)",
        dark="rgb(120, 135, 155)",
    ))
    viewSelectionDisabledBackgroundColor: PresetValue = field(default_factory=lambda: PresetValue(
        light="rgb(230, 239, 253)",
        dark="rgb(130, 140, 145)",
    ))
    hoverBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(215, 230, 240)",
        dark="rgb(130, 140, 145)",
    ))
    pressedBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(190, 200, 205)",
        dark="rgb(200, 210, 215)",
    ))
    tableHeaderBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="darkgray",
        dark="rgb(50, 50, 50)",
    ))
    tableHeaderGradientStartColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(235, 235, 235)",
        dark="rgb(105, 115, 125)",
    ))
    tableHeaderGradientEndColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(220, 220, 220)",
        dark="rgb(85, 95, 100)",
    ))
    tableHeaderDisabledGradientStartColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(240, 240, 240)",
        dark="rgb(60, 65, 70)",
    ))
    tableHeaderDisabledGradientEndColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(220, 220, 220)",
        dark="rgb(45, 50, 55)",
    ))
    tableHeaderHoverBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(230, 240, 255)",
        dark="rgb(130, 140, 145)",
    ))
    tableHeaderPressedBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(15, 15, 235)",
        dark="rgb(45, 85, 235)",
    ))
    tableHeaderPressedFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="white",
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
        dark="rgb(49, 54, 59)",
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
    defaultButtonBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(79, 139, 200)",
        dark="rgb(79, 139, 200)",
    ))
    defaultButtonHoverBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(106, 170, 234)",
        dark="rgb(106, 170, 234)",
    ))
    defaultButtonFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="white",
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
    scrollbarBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="transparent",
        dark="transparent",
    ))
    scrollbarHandleColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="lightgray",
        dark="darkgray",
    ))
    scrollbarBackgroundDisabledColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="transparent",
        dark="rgb(85, 90, 95)",
    ))
    scrollbarHandleDisabledColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="lightgray",
        dark="gray",
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
