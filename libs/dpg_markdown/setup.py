
def init_dpg_markdown(dpg,dpg_markdown,font_registry, size, default, bold, italic, bolditalic):
    def markdown_add_font(file, size, parent):
        with dpg.font(file, size, parent=parent) as font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Thai)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Vietnamese)

        return font
    

    dpg_markdown.set_font_registry(font_registry)
    dpg_markdown.set_add_font_function(markdown_add_font)
    markdown_font = dpg_markdown.set_font(font_size=14,default=str(default),bold=str(bold),italic=str(italic),italic_bold=str(bolditalic))

    return markdown_font