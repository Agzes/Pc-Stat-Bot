"""

  Pc-Stat-Bot data loader addon
            v.1.0.0

"""

def load_data(JSON):
    global main_name,main_token,main_id,main_webhook,main_token_ds,is_main_autoscreen,main_autoscreen_time,is_main_autoinformation,main_autosinformation_time,main_login,main_password,main_language,auto_update_statistics,auto_update_statistics_time,ai_function_for_dark,ai_function_for_telegram,mouse_move_for_telegram,keyboard_move_for_telegram,data_function_for_telegram,monitoring_pc_other,auto_update_statistics_info,auto_update_statistics_time_info,is_dark_on,lang
    " main "
    main_name = "User"
    main_token = ""
    main_id = 0
    main_webhook = ""
    main_token_ds = ""
    is_main_autoscreen = False
    main_autoscreen_time = 0
    is_main_autoinformation = False
    main_autosinformation_time = 0
    main_login = ""
    main_password = ""
    main_language = "en"
    " statistics "
    auto_update_statistics = False
    auto_update_statistics_time = 5
    auto_update_statistics_info = False
    auto_update_statistics_time_info = 5
    " plugins "
    " for Dark "
    ai_function_for_dark = False
    " for telegram bot "
    ai_function_for_telegram = False
    mouse_move_for_telegram = False
    keyboard_move_for_telegram = False
    data_function_for_telegram = False
    " other plugins "
    monitoring_pc_other = False
    is_dark_on = False
    try:
        main_name = JSON["main"]["main_name"]
    except:  
        pass
    try:
        main_token = JSON["main"]["main_token"]
    except:   
        pass
    try:
        main_id = JSON["main"]["main_id"]
    except:   
        pass
    try:
        main_webhook = JSON["main"]["main_webhook"]
    except:   
        pass
    try:
        main_token_ds = JSON["main"]["main_token_ds"]
    except:   
        pass
    try:
        is_main_autoscreen = JSON["main"]["is_main_autoscreen"]
    except:   
        pass
    try:
        main_autoscreen_time = JSON["main"]["main_autoscreen_time"]
    except:   
        pass
    try:
        is_main_autoinformation = JSON["main"]["is_main_autoinformation"]
    except:   
        pass
    try:
        main_autosinformation_time = JSON["main"]["main_autosinformation_time"]
    except:   
        pass
    try:
        main_login = JSON["main"]["main_login"]
    except:   
        pass
    try:
        main_password = JSON["main"]["main_password"]
    except:   
        pass
    try:
        main_language = JSON["main"]["main_language"]
    except:   
        pass
    try:
        auto_update_statistics_info = JSON["statistics"]["auto_update_statistics"]
    except:   
        pass
    try:
        auto_update_statistics_time_info = JSON["statistics"]["auto_update_statistics_time"]
    except:   
        pass
    try:
        ai_function_for_dark = JSON["plugins"]["dark"]["ai_function_for_dark"]
    except:   
        pass
    try:
        ai_function_for_telegram = JSON["plugins"]["telegram"]["ai_function_for_telegram"]
    except:   
        pass
    try:
        mouse_move_for_telegram = JSON["plugins"]["telegram"]["mouse_move_for_telegram"]
    except:   
        pass
    try:
        keyboard_move_for_telegram = JSON["plugins"]["telegram"]["keyboard_move_for_telegram"]
    except:   
        pass
    try:
        data_function_for_telegram = JSON["plugins"]["telegram"]["data_function_for_telegram"]
    except:   
        pass
    try:
        monitoring_pc_other = JSON["plugins"]["other"]["monitoring_pc_other"]
    except:   
        pass
    try:
        is_dark_on = JSON["dark"]["dark_on"]
    except:   
        pass
    lang = main_language
    
    return main_name,main_token,main_id,main_webhook,main_token_ds,is_main_autoscreen,main_autoscreen_time,is_main_autoinformation,main_autosinformation_time,main_login,main_password,main_language,auto_update_statistics,auto_update_statistics_time,ai_function_for_dark,ai_function_for_telegram,mouse_move_for_telegram,keyboard_move_for_telegram,data_function_for_telegram,monitoring_pc_other,auto_update_statistics_info,auto_update_statistics_time_info,is_dark_on,lang
    