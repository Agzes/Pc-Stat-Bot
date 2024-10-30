

def init_all_element(dpg_animator):
    dpg_animator.add("position", "PSB_Title_UI_BG", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "PSB_Logo_UI_BG", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "PSB_Fake_Close_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "PSB_Close_Button_p2", [0,0], [37,-300], [.23, .07, .53, 1], 1)

    dpg_animator.add("position", "License_Window", [0,0], [7,-700], [.23, .07, .53, 1.63], 1)
    dpg_animator.add("position", "notify_window", [0,0], [7,-300], [.23, .07, .53, 1.63], 1)
    dpg_animator.add("position", "info_window", [0,0], [7,-300], [.23, .07, .53, 1.63], 1)
    dpg_animator.add("opacity", "Home_Tab", 1, 0, [.57, .06, .61, .86], 1)
    dpg_animator.add("opacity", "Terminal_Tab", 1 , 0, [.57, .06, .61, .86], 1)
    dpg_animator.add("opacity", "Statistics_Tab", 1, 0, [.57, .06, .61, .86], 1)
    dpg_animator.add("opacity", "Plugins_Tab", 1, 0, [.57, .06, .61, .86], 1)
    dpg_animator.add("opacity", "Dark_Tab", 1, 0, [.57, .06, .61, .86], 1)
    dpg_animator.add("opacity", "Panel_Tab", 1, 0, [.57, .06, .61, .86], 1)
    dpg_animator.add("opacity", "Settings_Tab", 1, 0, [.57, .06, .61, .86], 1)

    dpg_animator.add("position", "Home_Tab_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "Terminal_Tab_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "Statistics_Tab_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "Plugins_Tab_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "Dark_Tab_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "Panel_Tab_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    dpg_animator.add("position", "Settings_Tab_Button", [0,0], [37,-300], [.23, .07, .53, 1], 1)
    

def start_animations(lang,parameters,hide_show_ui_close_button,dpg_animator):
    dpg_animator.add("opacity", "Home_Tab", 0, 1, [1,-0.03,.55,.65], 200)
    dpg_animator.add("position", "PSB_Title_UI_BG", [37,-60], [37, 9], [.23, .07, .53, 1.06], 100)
    dpg_animator.add("position", "PSB_Fake_Close_Button", [465,-60], [465, 9], [.23, .07, .53, 1.06], 175, callback=hide_show_ui_close_button)
    dpg_animator.add("position", "PSB_Close_Button_p2", [471,-60], [471, 2], [.23, .07, .53, 1.06], 175)
    
    dpg_animator.add("position", "PSB_Logo_UI_BG", [7,-60], [7, 9], [.23, .07, .53, 1.06], 175)
    dpg_animator.add("position", "Home_Tab_Button",       [7  ,800], [7  ,716], [.23, .07, .53, 1], 135)
    dpg_animator.add("position", "Terminal_Tab_Button",   [parameters["tab_weight"]["terminal"],800], [parameters["tab_weight"]["terminal"],716], [.23, .07, .53, 1], 105)
    dpg_animator.add("position", "Statistics_Tab_Button", [parameters["tab_weight"]["statistics"],800], [parameters["tab_weight"]["statistics"],716], [.23, .07, .53, 1], 75)
    dpg_animator.add("position", "Plugins_Tab_Button",    [parameters["tab_weight"]["plugins"],800], [parameters["tab_weight"]["plugins"],716], [.23, .07, .53, 1], 60)
    dpg_animator.add("position", "Dark_Tab_Button",       [parameters["tab_weight"]["dark"],800], [parameters["tab_weight"]["dark"],716], [.23, .07, .53, 1], 90)
    dpg_animator.add("position", "Panel_Tab_Button",      [parameters["tab_weight"]["panel"],800], [parameters["tab_weight"]["panel"],716], [.23, .07, .53, 1], 120)
    dpg_animator.add("position", "Settings_Tab_Button",   [parameters["tab_weight"]["settings"],800], [parameters["tab_weight"]["settings"],716], [.23, .07, .53, 1], 150)