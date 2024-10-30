

def load_assets(dpg):
    lw,lh,lc,ld = dpg.load_image("Data/logo/full-logo.png")
    dw,dh,dc,dd = dpg.load_image("Data/assets/dark.png")
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=lw, height=lh, default_value=ld, tag="logo")
        dpg.add_static_texture(width=dw, height=dh, default_value=dd, tag="dark")
        
def load_themes(dpg):
    with dpg.theme() as unpicked_tab_color:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, [18, 18, 18, 100])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [188, 177, 226, 140])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [208, 197, 246, 140])
    with dpg.theme() as picked_tab_color:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 0, 75, 100])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [37, 0, 75, 140])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [37, 0, 75, 140])
    with dpg.theme() as key_button_color:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 0, 75, 170])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [37, 0, 75, 140])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [37, 0, 75, 140])
    with dpg.theme() as key_button_color_with_border:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 0, 75, 170])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [37, 0, 75, 140])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [37, 0, 75, 140])
    with dpg.theme() as simple_plot_theme:
        with dpg.theme_component():
                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
    with dpg.theme() as border_to_element:
        with dpg.theme_component():
                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
    with dpg.theme() as border_with_button_element:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, [25, 25, 25, 100])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [97, 108, 146, 140])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [18, 18, 18, 255])
    with dpg.theme() as border_with_transparent_button_for_text_element:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, [0,0,0,0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0,0,0,0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0,0,0,0])
    with dpg.theme() as transparent_button_for_text_in_center:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
    with dpg.theme() as notify_window_back:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [33, 33, 33, 255])
    with dpg.theme() as dark_mic_up:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_Button, [39, 163, 39, 255])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [39, 163, 39, 140])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [39, 163, 39, 140])
    with dpg.theme() as dark_mic_off:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_Button, [148, 0, 0, 255])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [148, 0, 0, 140])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [148, 0, 0, 140])
    with dpg.theme() as logo_bg:
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [18, 18, 18, 255])

    return unpicked_tab_color,picked_tab_color,key_button_color,key_button_color_with_border,simple_plot_theme,border_to_element,border_with_button_element,border_with_transparent_button_for_text_element, transparent_button_for_text_in_center,notify_window_back,dark_mic_off,dark_mic_up,logo_bg