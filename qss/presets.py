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
    # TODO: Check on QComboBox and QTableView border color?
    # TODO: Replace all specific widgets border/bg color
    baseBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(184, 184, 184)",
        dark="rgb(128, 128, 128)",
    ))
    baseDisabledBorderColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(211, 211, 211)",
        dark="rgb(80, 80, 80)",
    ))
    disabledFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(211, 211, 211)",
        dark="rgb(89, 94, 99)",
    ))
    disabledBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(240, 240, 240)",
        dark="rgb(49, 54, 59)",
    ))
    radioBtnOnImageFile: PresetValue = field(default_factory=lambda: PresetValue(
        light="radio-on.png",
        dark="dark-radio-on.png",
    ))
    radioBtnOffImageFile: PresetValue = field(default_factory=lambda: PresetValue(
        light="radio-off.png",
        dark="dark-radio-off.png",
    ))
    radioBtnOnDisabledImageFile: PresetValue = field(default_factory=lambda: PresetValue(
        light="dark-radio-on.png",
        dark="radio-on.png",
    ))
    radioBtnOffDisabledImageFile: PresetValue = field(default_factory=lambda: PresetValue(
        light="dark-radio-off.png",
        dark="radio-off.png",
    ))
    checkboxImageFile: PresetValue = field(default_factory=lambda: PresetValue(
        light="checked.png",
        dark="dark-checked.png",
    ))
    checkboxDisabledImageFile: PresetValue = field(default_factory=lambda: PresetValue(
        light="checked-disabled.png",
        dark="dark-checked-disabled.png",
    ))
    checkboxBackgroundColor: PresetValue = field(default_factory=lambda: PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    checkboxDisabledBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
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
        light="rgb(96, 159, 250)",
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
    sectionBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(250, 250, 250)",
        dark="#474f56",
    ))
    viewBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    defaultButtonBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(79, 139, 200)",
        dark="rgb(79, 139, 200)",
    ))
    defaultButtonDisabledBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(188, 200, 212)",
        dark="rgb(77, 99, 121)",
    ))
    defaultButtonHoverBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(106, 170, 234)",
        dark="rgb(106, 170, 234)",
    ))
    defaultButtonFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="white",
    ))
    defaultButtonDisabledFontColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(240, 240, 240)",
        dark="rgb(150, 150, 150)",
    ))
    progressbarBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
    ))
    progressbarChunkBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(182, 227, 255)",
        dark="rgb(25, 63, 140)",
    ))
    comboboxBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="white",
        dark="rgb(85, 90, 95)",
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
    tabBackgroundColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(220, 220, 220)",
        dark="rgb(58, 63, 68)",
    ))
    tabSelectedBackgroundGradientStartColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(255, 255, 255)",
        dark="rgb(125, 135, 145)",
    ))
    tabSelectedBackgroundGradientEndColor: PresetValue = field(default_factory=lambda:PresetValue(
        light="rgb(224, 224, 224)",
        dark="rgb(105, 115, 125)",
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
