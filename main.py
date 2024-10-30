""" ----------------------------- """
""" ---- BETA V4 PC-STAT-BOT ---- """
""" ----------------------------- """
fps_unlocker = False
version = """4.0.0
"""

# DearPyGui | UI | Addons 
import dearpygui.dearpygui as dpg  
from g4f.client import Client 
import libs.dpg_animations as dpg_animations  
import libs.dpg_animator.dearpygui_animate as dpg_animator 
import libs.dpg_markdown as dpg_markdown  
import libs.dpg_theme as dpg_theme  
from libs.addons.data_loader import load_data
from libs.dpg_addons.cyr_support import init_font_with_cyr_support, to_cyr
from libs.dpg_markdown.setup import init_dpg_markdown
from libs.dpg_addons.drag_window import drag_window_setup
from libs.addons.basic_func import load_from_json
from libs.addons.animations import start_animations, init_all_element
from libs.dpg_addons.assets_loader import load_assets, load_themes
from Data.LICENSE import License_EN, License_RU
import ctypes.wintypes    
# Standard LIBS
from datetime import datetime    
import time as time    
import webbrowser    
import sys    
import os
import json    
import threading    
import requests  
# For Get PC Info
import psutil    
from libs.sys_info.sys_info import SystemInfo    
from libs.dpg_addons.dpg_blur import WindowsWindowEffect, get_hwnd, MARGINS    
# For Telegram Bot 
from tg_bot import telegram_bot    
# Dark 
from dark import dark_answer, darksoundaction    
import speech_recognition as sr    
from lang.load import load_translation

client = Client() # G4F Load
total_message_in_tg_bot = 0 # telegram total msg (for terminal work) 

# Variables for interface 
is_terms_of_use_open = False
is_notify_open = False
is_info_open = False
is_theme_picker_open = False
auto_thread_statistics = False
current_tab = "Home_Tab"

main_name,main_token,main_id,main_webhook,main_token_ds,is_main_autoscreen,main_autoscreen_time,is_main_autoinformation,main_autosinformation_time,main_login,main_password,main_language,auto_update_statistics,auto_update_statistics_time,ai_function_for_dark,ai_function_for_telegram,mouse_move_for_telegram,keyboard_move_for_telegram,data_function_for_telegram,monitoring_pc_other,auto_update_statistics_info,auto_update_statistics_time_info,is_dark_on,lang = load_data(load_from_json("Config/main_data.json")) # Config Loader
translations,telegram_translates,parameters = load_translation(main_language)

dpg.create_context() # DearPyGUI initializing
system_info = SystemInfo() # sys_info initializing
window_effect = WindowsWindowEffect() # dpg_blur initializing
def close(): dpg.destroy_context(); sys.exit(0) # Close UI and Program function
with dpg.font_registry() as font_registry: #  Create a font registry for markdown and creating fonts
  with dpg.font("Data/Fonts/base.ttf", 15) as default_font: # Basic font
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
  with dpg.font("Data/Fonts/namefont.ttf", 20, parent=font_registry) as NameFont: dpg.add_font_range_hint(dpg.mvFontRangeHint_Default) # Font for Pc-Stat-Bot tittle
init_dpg_markdown(dpg,dpg_markdown,font_registry,15,'Data/Fonts/base.ttf','Data/Fonts/bold.ttf','Data/Fonts/italic.ttf','Data/Fonts/bolditalic.ttf') # initializing dpg_markdown
drag_window_setup(dpg,37) # Make window movable
load_assets(dpg) # Load Pc-Stat-Bot and "Dark" icon
unpicked_tab_color,picked_tab_color,key_button_color,key_button_color_with_border,simple_plot_theme,border_to_element,border_with_button_element,border_with_transparent_button_for_text_element, transparent_button_for_text_in_center,notify_window_back,dark_mic_off,dark_mic_up,logo_bg = load_themes(dpg) # Load themes for UI and UX
def change_tab(tab): # Function for tabs working (animation/change color)
    global current_tab, is_notify_open
    if is_terms_of_use_open is True:
        license_window("close")
    if is_notify_open:
        ui_notify_close()
    if tab == current_tab:
        return
    old_tab = current_tab
    dpg_animator.add("opacity", current_tab, 1, 0, [.57, .06, .61, .86], 45, callback_data=old_tab, callback=hide_item)
    dpg.bind_item_theme(f"{tab}_Button", picked_tab_color)
    dpg.show_item(tab)
    dpg_animator.add("opacity", tab, 0, 1, [.57, .06, .61, .86], 45)
    dpg.bind_item_theme(f"{current_tab}_Button", unpicked_tab_color)
    current_tab = tab

def hide_item(sender, old_tab):
    dpg.hide_item(old_tab)

    
    
def hide_item2(sender, item):
    dpg.hide_item(item)

# "Dark"
def dark_checker(text, command=""):
    if text == "processed_status_200":
        dark_add(translations["dark_assistant"]["done"])
    elif text == command.lower():
        dark_add(translations["dark_assistant"]["think"])
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{text}"}],
        )
        mesage = response.choices[0].message.content
        dark_add(translations["dark_assistant"]["msg"].format(mesage=mesage))
        darksoundaction()
    elif any(keyword in text for keyword in ("Привет!", "Hi!", "Пока!", "Bye!")):
        dark_add(translations["dark_assistant"]["msg"].format(mesage=text))
    elif translations["dark_assistant"]["command_not_recognized"]:
        dark_add(translations["dark_assistant"]["msg"].format(mesage=text))
def dark_add(text):
    if text != "null_status_200":
        dpg_markdown.add_text(text, parent='dark_chat', wrap=450)
def dark_listen():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source) 
    try:
        dark_recognize = recognizer.recognize_google(audio, language="ru-RU")
        dark_recognize = dark_recognize.lower()
        if "dark" in dark_recognize or "дарк" in dark_recognize:
            dark_add(translations["dark_assistant"]["you_voice"].format(dark_recognize=dark_recognize))
            return dark_recognize
        else:
            return "yous_dont_say_anything_code_200"
    except sr.UnknownValueError:
        return translations["dark_assistant"]["error_speech_recognize"]
    except sr.RequestError:
        return translations["dark_assistant"]["error_with_response"]
def dark_start():
    while True:
        command = dark_listen()
        dark_checker(dark_answer(to_cyr(command), lang=main_language, itsvoice=True, plugin_ai=ai_function_for_dark), to_cyr(command))
def change_mic_checker():
    global is_dark_on
    if is_dark_on:
        is_dark_on = False
        dpg.bind_item_theme("dark_mic_status", dark_mic_off)
    else: 
        is_dark_on = True
        dpg.bind_item_theme("dark_mic_status", dark_mic_up)
    data_update("dark")
def dark_send_msg():
    temp_msg = dpg.get_value("dark_chat_value")
    dark_add(translations["dark_assistant"]["you"].format(temp_msg=to_cyr(temp_msg)))
    dpg.set_value("dark_chat_value", "")
    dark_checker(dark_answer(to_cyr(temp_msg), lang=main_language, itsvoice=False, plugin_ai=ai_function_for_dark), to_cyr(temp_msg))

# UI Functions (terminal work / license window / notify / information window / more data label) 
def terminal_add(text, status, desc=""):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if "info" in  status:
        text = f'<font color="[255, 255, 255, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Output")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)
        
    elif "error" in status:
        text = f'<font color="[173, 48, 38, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Output")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)

    elif "status" in  status:
        text = f'<font color="[135, 173, 241, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Output")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)
        
    elif "warning" in status:
        text = f'<font color="[187, 74, 13, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Output")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)
        
    if desc != "":
        t = dpg.add_text(translations["ui_tools"]["more"], parent=group, color=[200, 200, 200])
        with dpg.tooltip(t):
            dpg.add_text(desc)
def license_window(move):
    global current_tab, is_terms_of_use_open
    if move == "open" and is_terms_of_use_open is False:
        is_terms_of_use_open = True
        dpg.show_item("License_Window")
        dpg_animator.add("opacity", "Home_Tab", 1, 0, [.57, .06, .61, .86], 45, callback_data="Home_Tab" , callback=hide_item2)
        dpg_animator.add("position", "License_Window", [7,-700], [7,40], [.23, .07, .53, 1], 45)
    else:
        is_terms_of_use_open = False
        dpg.show_item("Home_Tab")
        dpg_animator.add("opacity", "Home_Tab", 0, 1, [.57, .06, .61, .86], 45)
        dpg_animator.add("position", "License_Window", [7,40], [7,-700], [.23, .07, .53, 1.30], 45)
def information_open(text):
    global current_tab, is_info_open
    if is_info_open:
        information_close()
    is_info_open = True
    dpg.set_value("info_text", text)
    dpg_animator.add("opacity", "tab_in_ui", 1, 0, [.57, .06, .61, .86], 15)
    dpg_animator.add("position", "info_window", [5, -300], [7,40], [.23, .07, .53, 1], 45)
    dpg_animator.add("position", current_tab, [7,40], [7,193], [.23, .07, .53, 1.63], 45)
    dpg_animator.add("opacity", "info_window", 0, 1, [.57, .06, .61, .86], 45)
    dpg_animator.add("opacity", "info_text", 0, 1, [.64, .12, .72, .86], 45, timeoffset=10 / 60)
def information_close():
    global is_info_open
    if is_info_open is False:
        return
    elif is_info_open is True:
        is_info_open = False
    dpg_animator.add("opacity", "tab_in_ui", 0, 1, [.57, .06, .61, .86], 45)
    dpg_animator.add("position", "info_window", [7,40], [5, -300], [.23, .07, .53, 1], 45)
    dpg_animator.add("position", current_tab, [7, 193], [7,40], [.23, .07, .53, 1], 45)
    dpg_animator.add("opacity", "info_window", 1, 0, [.57, .06, .61, .86], 45)
    dpg_animator.add("opacity", "info_text", 1, 0, [.64, .12, .72, .86], 45, timeoffset=10 / 60)
def ui_notify_close(code=""):
    global is_notify_open
    if is_notify_open is False:
        return
    elif is_notify_open is True:
        is_notify_open = False
    dpg_animator.add("opacity", "tab_in_ui", 0, 1, [.57, .06, .61, .86], 45)
    dpg_animator.add("position", "notify_window", [7,40], [5, -300], [.23, .07, .53, 1], 45)
    dpg_animator.add("position", current_tab, [7, 143], [7,40], [.23, .07, .53, 1], 45)
    dpg_animator.add("opacity", "notify_window", 1, 0, [.57, .06, .61, .86], 45)
    dpg_animator.add("opacity", "notify_text", 1, 0, [.64, .12, .72, .86], 45, timeoffset=10 / 60)
def ui_notify_start(text, duration):
    global current_tab, is_notify_open
    if is_notify_open:
        ui_notify_close()
    is_notify_open = True
    dpg.set_value("notify_text", text)
    dpg_animator.add("opacity", "tab_in_ui", 1, 0, [.57, .06, .61, .86], 15)
    dpg_animator.add("position", "notify_window", [5, -300], [7,40], [.23, .07, .53, 1], 45)
    dpg_animator.add("position", current_tab, [7,40], [7,143], [.23, .07, .53, 1.63], 45)
    dpg_animator.add("opacity", "notify_window", 0, 1, [.57, .06, .61, .86], 45)
    dpg_animator.add("opacity", "notify_text", 0, 1, [.64, .12, .72, .86], 45, timeoffset=10 / 60)
    time.sleep(duration)
    ui_notify_close()

def ui_notify(text, duration):
    threading.Thread(target=ui_notify_start,args=(text,duration,)).start()
def _help(message):
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text("[i]", color=[255, 255, 255])
    with dpg.tooltip(t):
        dpg.add_text(message)

# statistics
def start_statistics_auto_update():
    global auto_thread_statistics
    while True:
        data_for_preload = load_from_json("Config/main_data.json")
        try:
            auto_update_statistics_info = data_for_preload["statistics"]["auto_update_statistics"]
        except:   
            pass
            time.sleep(1)
        try:
            auto_update_statistics_time_info = data_for_preload["statistics"]["auto_update_statistics_time"]
        except:   
            pass
            time.sleep(1)
        if auto_update_statistics_info is False:
            pass
            time.sleep(1)
        elif auto_update_statistics_info is True:
            if auto_update_statistics_time_info <= 0:
                pass
                time.sleep(1)
            else:
                statistics_update()
                time.sleep(auto_update_statistics_time_info)
def statistics_update():
    global program_start
    info = system_info.get_formatted_info()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    " cpu "
    dpg.set_value("statistics_tab_cpu_label", translations["statistics"]["cpu"].format(info=info['cpu']))
    temp_stat_cpu = dpg.get_value("statistics_tab_cpu_plot")
    temp_stat_cpu.append(info['cpu'])
    dpg.set_value("statistics_tab_cpu_plot", temp_stat_cpu)
    dpg.set_value("statistics_tab_cpu_cores_label", translations["statistics"]["cpu_core"].format(data=info['total_cores']))
    temp_text = ""
    for i in info["cpu_cores_i"]:
        temp_text += translations["statistics"]["cpu_core_i"].format(i=i+1, percent=info["cpu_cores_percent"][i]) + "\n"
    dpg.set_value("statistics_tab_cpu_cores", temp_text)

    " memory "
    
    dpg.set_value("statistics_tab_ram_occupied_label", translations["statistics"]["memory_occupied"].format(data=round(info['occupied_ram'],2)))
    temp_stat_occupied_ram = dpg.get_value("statistics_tab_ram_occupied")
    temp_stat_occupied_ram.append(info['occupied_ram'])
    dpg.set_value("statistics_tab_ram_occupied", temp_stat_occupied_ram)

    dpg.set_value("statistics_tab_ram_free_label", translations["statistics"]["memory_free"].format(data=round(info['free_ram'], 2)))
    temp_stat_free_ram = dpg.get_value("statistics_tab_ram_free")
    temp_stat_free_ram.append(info['free_ram'])
    dpg.set_value("statistics_tab_ram_free", temp_stat_free_ram)

    dpg.set_value("statistics_tab_ram_total", translations["statistics"]["memory_total"].format(data=round(info['total_ram'], 2)))

    " gpu "
    dpg.set_value("statistics_tab_gpu_label", translations["statistics"]["gpu"].format(data=info['gpu_info']))
    temp_stat_gpu = dpg.get_value("statistics_tab_gpu")
    temp_stat_gpu.append(info['gpu'])
    dpg.set_value("statistics_tab_gpu", temp_stat_gpu)

    " other "
    dpg.set_value("statistics_tab_other_time", translations["statistics"]["time"].format(data=current_time))
    uptime = datetime.now() - program_start
    dpg.set_value("statistics_tab_other_online", translations["statistics"]["program_on"].format(data=uptime))

# Settings Saver
def data_update(whatsupdate, more=""):
    global statistics_thread

    main_name,main_token,main_id,main_webhook,main_token_ds,is_main_autoscreen,main_autoscreen_time,is_main_autoinformation,main_autosinformation_time,main_login,main_password,main_language,auto_update_statistics,auto_update_statistics_time,ai_function_for_dark,ai_function_for_telegram,mouse_move_for_telegram,keyboard_move_for_telegram,data_function_for_telegram,monitoring_pc_other,auto_update_statistics_info,auto_update_statistics_time_info,is_dark_on,lang = load_data(load_from_json("Config/main_data.json"))
    dark_on = is_dark_on
    
    if whatsupdate == "main":
        main_name = dpg.get_value("settings_name")
        main_token = dpg.get_value("settings_token")
        main_id = dpg.get_value("settings_id")
        main_webhook = dpg.get_value("settings_webhook")
        main_token_ds = dpg.get_value("settings_token-ds")
        is_main_autoscreen = dpg.get_value("settings_autoscreen_value")
        main_autoscreen_time = dpg.get_value("settings_autoscreen_time")
        is_main_autoinformation = dpg.get_value("settings_autoinfo_value")
        main_autosinformation_time = dpg.get_value("settings_autoinfo_time")
        main_login = dpg.get_value("settings_sec_login")
        main_password = dpg.get_value("settings_sec_pass")
        main_language = dpg.get_value("settings_language")

        if main_name == "":
            ui_notify(translations["ui_tools"]["error_name"], 3)
            return
        if main_token == "":
            ui_notify(translations["ui_tools"]["error_token"], 3)
            return
        else:
            if ":" in main_token:
                pass
            else:
                ui_notify(translations["ui_tools"]["error_token_incorrect"], 3)
                return
        if id == "":
            ui_notify(translations["ui_tools"]["error_id"], 3)
            return
        if is_main_autoscreen is True:
            if main_autoscreen_time <= 0:
                ui_notify(translations["ui_tools"]["error_auto-screen_time"], 3)
                return
        if is_main_autoinformation is True:
            if main_autosinformation_time <= 0:
                ui_notify(translations["ui_tools"]["error_auto-information_time"], 3)
                return
    if whatsupdate == "stat":
        auto_update_statistics_info = dpg.get_value("statistics_tab_settings_checkbox")
        auto_update_statistics_time_info = dpg.get_value("statistics_tab_settings_time")

        if auto_update_statistics_time_info <= 0 or auto_update_statistics_time_info >=1000:
            ui_notify(translations["ui_tools"]["error_time"], 5)
            return
    if whatsupdate == "plugins":
        if more == "ai_function_for_dark":
            ai_function_for_dark = dpg.get_value("ai_functions_for_dark_ui")

        if more == "ai_function_for_telegram":
            ai_function_for_telegram = dpg.get_value("ai_function_for_telegram_ui")
        if more == "mouse_move_for_telegram":
            mouse_move_for_telegram = dpg.get_value("mouse_move_for_telegram_ui")
        if more == "keyboard_move_for_telegram":
            keyboard_move_for_telegram = dpg.get_value("keyboard_move_for_telegram_ui")
        if more == "data_function_for_telegram":
            data_function_for_telegram = dpg.get_value("data_function_for_telegram_ui")

        if more == "monitoring_pc_other":
            monitoring_pc_other = dpg.get_value("monitoring_pc_other_ui")
    if whatsupdate == "dark":
        if is_dark_on:
            dark_on = False
        else:
            dark_on = True


    


    settings = {
        "main": {
            "main_name": main_name,
            "main_token": main_token,
            "main_id": main_id,
            "main_webhook": main_webhook,
            "main_token_ds": main_token_ds,
            "is_main_autoscreen": is_main_autoscreen,
            "main_autoscreen_time": main_autoscreen_time,
            "is_main_autoinformation": is_main_autoinformation,
            "main_autosinformation_time": main_autosinformation_time,
            "main_login": main_login,
            "main_password": main_password,
            "main_language": main_language
        },
        "statistics": {
            "auto_update_statistics": auto_update_statistics_info,
            "auto_update_statistics_time": auto_update_statistics_time_info
        }, 
        "plugins": {
            "dark": {
                "ai_function_for_dark": ai_function_for_dark
            },
            "telegram": {
                "ai_function_for_telegram": ai_function_for_telegram,
                "mouse_move_for_telegram": mouse_move_for_telegram,
                "keyboard_move_for_telegram": keyboard_move_for_telegram,
                "data_function_for_telegram": data_function_for_telegram
            },
             "other": {
                 "monitoring_pc_other": monitoring_pc_other
             },
        },
        "dark": {
            "dark_on": dark_on
        }
    }

    with open("Config/main_data.json", "w") as file:
        json.dump(settings, file, indent=4, sort_keys=True)
    if whatsupdate == "stat" or whatsupdate == "main":
        ui_notify(translations["ui_tools"]["saved"], 3)

# Telegram Bot
def start_telegram_bot():
    global tg_bot
    threading.Thread(target=start_check_tg_status).start()
    tg_bot = telegram_bot()
def start_check_tg_status():
    global total_message_in_tg_bot
    while True:
        if 'tg_bot' in globals():
            tot_msg, msg_data = tg_bot.get_data()
            if tot_msg == total_message_in_tg_bot:pass   
            else:
                for data in msg_data:
                    id_msg = data['id']
                    if id_msg < total_message_in_tg_bot: pass   
                    else:
                        message = data['text']
                        status = data['status']
                        desc = data['desc']
                        if status == "code":
                            if message == "off_bot_and_program":close()
                            if message == "off_bot_and_program_and_shutdown": os.system('shutdown -s')
                            if message == "off_bot_and_program_and_hibernate": os.system("shutdown /h")
                            if message == "off_bot_and_program_and_reboot": os.system('reboot now')
                            pass
                        terminal_add(message,status,desc)
                        total_message_in_tg_bot += 1
        time.sleep(0.1)

# Update Checker
def check_for_update():
    url = 'https://raw.githubusercontent.com/Agzes/Pc-Stat-Bot/main/version.txt'
    response = requests.get(url)
    if response.status_code == 200:
        file_content = response.text
        if file_content != version:
            information_open(translations["ui_tools"]["new_update"].format(file_content=file_content,version=version))
    else:
        information_open(translations["ui_tools"]["error_check_update"].format(data=response.status_code))

# After UI start Functions 
def hide_show_ui_close_button(sender, data): # Function for start animation (make fake close button for close (because DearPyGUI restrictions))
    dpg.show_item("PSB_Close_Button") # Display of a drawn button (which can detect pressing the right mouse button, but cannot be animated)
    dpg.hide_item("PSB_Fake_Close_Button") # Hiding a real button (which was used for animation)
def Init_Before_UI_Init(): # start thread (for UI/UX and start animations)
    window_effect.setAeroEffect(get_hwnd()) # Enable acrylic effect for background
    window_effect.setRoundedCorners(get_hwnd(), 10) # Enable rounding for windows 11 
    input_font = init_font_with_cyr_support(dpg=dpg, font_path="Data/Fonts/base.ttf", font_registry=font_registry) # Creating font for input with cyr support
    dpg.bind_item_font("dark_chat_value", input_font) # bind input font to "dark" > chat input
    dpg.bind_item_font("settings_name", input_font) # bind input font to settings > name input
    start_animations(lang,parameters,hide_show_ui_close_button,dpg_animator) # start animation on program opening
def Init_After_UI_Init(): # start thread (for telegram bot/auto-statistics/and other...)
    global recognizer, microphone, statistics_thread
    
    recognizer = sr.Recognizer() # create Recognizer
    microphone = sr.Microphone() # create Microphone for Recognizer
    
    statistics_thread = threading.Thread(target=start_statistics_auto_update).start() # start Statistics auto update
    threading.Thread(target=dark_start).start() # start "Dark"
    threading.Thread(target=check_for_update).start() # check for update
    threading.Thread(target=start_telegram_bot).start() # start Telegram Bot

    # clean RAM
    handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, psutil.Process().pid)
    if handle:
        ctypes.windll.psapi.EmptyWorkingSet(handle)
        ctypes.windll.kernel32.CloseHandle(handle)

# 2 function close button
def hovered_close_button(sender, app_data, user_data):
    mouse_pos_temp = dpg.get_mouse_pos(local=False)
    if mouse_pos_temp[0] <= 490 and mouse_pos_temp[0] >= 465 and mouse_pos_temp[1] <= 31 and mouse_pos_temp[1] >= 7:
        dpg.configure_item("PSB_Close_Button", fill=(97, 108, 146, 140))
    else:
        dpg.configure_item("PSB_Close_Button", fill=(25, 25, 25, 100))
def close_from_ui(sender, app_data, user_data):
    mouse_pos_temp = dpg.get_mouse_pos(local=False)
    if mouse_pos_temp[0] <= 490 and mouse_pos_temp[0] >= 465 and mouse_pos_temp[1] <= 31 and mouse_pos_temp[1] >= 7:
        if app_data == dpg.mvMouseButton_Right:
            dpg.minimize_viewport()
        elif app_data == dpg.mvMouseButton_Left:
            close()

# Main UI
with dpg.window(label="Pc-Stat-Bot", pos=(0,-2), height=752, width=499, no_title_bar=True, no_resize=True, no_close=True, tag="UI", no_background=False, no_move=True, show=True, no_scroll_with_mouse=True, no_scrollbar=True): # Creating main window
    with dpg.drawlist(width=500, height=100, tag="PSB_Close_Button_p1"): # Create drawlist for 2funcButton
        dpg.draw_rectangle([457, 1], [483, 26],rounding=3, color=[108, 97, 146, 140], fill=[25, 25, 25, 100], show=False, tag="PSB_Close_Button") # Drawing 2funcButton
        with dpg.handler_registry(): # Add handler for mouse move and click
            dpg.add_mouse_move_handler(callback=hovered_close_button, user_data="PSB_Close_Button")
            dpg.add_mouse_release_handler(callback=close_from_ui, user_data="PSB_Close_Button")
    dpg.add_button(height=25, width=26, tag="PSB_Fake_Close_Button", pos=(465, 9)) # Create fake 2funcButton button for animations 
    dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme to fake button
    dpg_markdown.add_text("""<font size=28 color="(108, 97, 146, 255)">x</font>""", pos=(471, 2), tag="PSB_Close_Button_p2") # create X on 2funcButton
    with dpg.child_window(height=25,width=25, pos=(7, 9), no_scroll_with_mouse=True,no_scrollbar=True, tag="PSB_Logo_UI_BG"): # Logo
        dpg.bind_item_theme(dpg.last_item(), logo_bg)
        dpg.add_image("logo", width=25,height=25, pos=(0, 0))
    dpg.bind_item_theme(dpg.last_item(), border_to_element) # The stylization of the logo so that it is similar to other elements
    with dpg.child_window(height=25,width=423, pos=(37, 9), no_scroll_with_mouse=True,no_scrollbar=True, tag="PSB_Title_UI_BG"): # Tittle
        dpg.add_text('''Pc-Stat-Bot''', pos=(153,-3), tag="PSB_Title_UI")
        dpg.bind_item_font(dpg.last_item(), NameFont)
        pass
    dpg.bind_item_theme(dpg.last_item(), border_to_element) # bind theme for Tittle

    # UI Tools
    with dpg.child_window(height=670,width=485, tag="License_Window", show=False, pos=(7,-700), indent=1): # License Window
        with dpg.child_window(height=600):
            dpg_markdown.add_text(  markdown_text=License_RU if lang == "ru" else License_EN) # License
        dpg.add_button(label=translations["ui_tools"]["close"], width=468, height=50, callback= lambda: license_window("close"))

    # UI Tabs
    with dpg.child_window(height=670, tag="Home_Tab", show=True, pos=(7,40)): # Home Tab child Window
        greetings_temp = translations["user"]["greeting"].format(UserName=main_name)
        text_for_greetings = f"## {greetings_temp}" # make Greetings text
        dpg_markdown.add_text(text_for_greetings, pos=((500-(len(text_for_greetings)*11))/2,150)) # calculate position and show Greetings text
        with dpg.group(horizontal=True, pos=(7,587)): # Group for buttons under child_window
            dpg.add_button(label=translations["home_tab"]["feedback"], width=233, height=30, callback=lambda: webbrowser.open("https://t.me/agzes0")) # Feedback
            dpg.add_button(label=translations["home_tab"]["project_page"], width=233, height=30, callback=lambda: webbrowser.open("https://github.com/Agzes/Pc-Stat-Bot")) # GitHub page
        dpg.add_button(label=translations["home_tab"]["license_agreement"], width=471, pos=(7,620), height=42,  callback=lambda: license_window("open"), tag="License_Button") # License
        dpg.bind_item_theme(dpg.last_item(), key_button_color) # bind style for License color
    with dpg.child_window(height=670,width=485, tag="Terminal_Tab", show=True, pos=(7,40)): # Terminal Tab child Window
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label 
            dpg.add_button(label=translations["tab_bar"]["terminal"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        with dpg.child_window(tag="Terminal_Output"): # Terminal Data (output)
            pass
    with dpg.child_window(height=670,width=485, tag="Statistics_Tab", show=True, pos=(7,40)): # Statistics Tab child Window
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
            dpg.add_button(label=translations["tab_bar"]["statistics"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator() # Line
        
        # CPU
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=316, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text(translations["statistics_tab"]["cpu"], pos=(7,3), tag="statistics_tab_cpu_label")
                dpg.add_simple_plot(height=100, default_value=(0,100,), tag="statistics_tab_cpu_plot")
                dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=148, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text(translations["statistics_tab"]["GPU_Cores"], pos=(7,3), tag="statistics_tab_cpu_cores_label")
                with dpg.child_window(height=100):
                    dpg.add_text("", tag="statistics_tab_cpu_cores", pos=(7,3))
        dpg.add_separator() # Line
        
        # RAM
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=170, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text(translations["statistics_tab"]["ram_occupied"], pos=(7,3), tag="statistics_tab_ram_occupied_label")
                dpg.add_simple_plot(height=100, width=170, default_value=(0,psutil.virtual_memory().total / (1024 ** 3)), tag="statistics_tab_ram_occupied")
                dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=170, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text(translations["statistics_tab"]["free_ram"], pos=(7,3), tag="statistics_tab_ram_free_label")
                dpg.add_simple_plot(height=100, width=170, default_value=(0,psutil.virtual_memory().total / (1024 ** 3)), tag="statistics_tab_ram_free")
                dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=119, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text(translations["statistics_tab"]["total_ram"], pos=(7,3), tag="statistics_tab_ram_total_label")
                with dpg.child_window(height=100):
                    dpg.add_text("", tag="statistics_tab_ram_total") 
        dpg.add_separator() # Line
        
        # GPU
        with dpg.child_window(height=25, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_text(translations["statistics_tab"]["gpu"], pos=(7,3), tag="statistics_tab_gpu_label")
        dpg.add_simple_plot(height=100, width=470, default_value=(0,100,), tag="statistics_tab_gpu")
        dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)
        dpg.add_separator() # Line
        
        # OTHER
        with dpg.child_window(height=25, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_text(translations["statistics_tab"]["other"], pos=(7,3))
        with dpg.child_window(height=70, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_text(translations["statistics_tab"]["total_online"], tag="statistics_tab_other_online")
            dpg.add_text(translations["statistics_tab"]["time"], tag="statistics_tab_other_time")
        dpg.add_separator() # Line
        
        # SETTINGS (auto-update statistics)
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label=translations["statistics_tab"]["auto_stat_update"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        with dpg.child_window(height=34, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            with dpg.group(horizontal=True):
                dpg.add_checkbox(pos=(6,6), tag="statistics_tab_settings_checkbox", default_value=auto_update_statistics_info)
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                dpg.add_button(label=translations["statistics_tab"]["save"], width=325, callback=lambda: data_update("stat"))
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                dpg.add_input_int(width=100, tag="statistics_tab_settings_time", default_value=auto_update_statistics_time_info)
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
        dpg.add_separator()
        
        # UPDATE statistics button
        dpg.add_button(label=translations["statistics_tab"]["update"],height=30, width=470, callback=statistics_update)
        dpg.bind_item_theme(dpg.last_item(), key_button_color_with_border) # bind theme for button
    with dpg.child_window(height=670,width=485, tag="Plugins_Tab", show=True, pos=(7,40)): # Plugins Tab child Window
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
            dpg.add_button(label=translations["tab_bar"]["plugins"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator() # Line

        # Plugins for "Dark"
        with dpg.child_window(height=82):
            with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
                dpg.add_button(label=translations["plugins_tab"]["for_dark"],  pos=(7,2), width=456)
                dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True): # Plugin
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="ai_functions_for_dark_ui", default_value=ai_function_for_dark, callback=lambda: data_update("plugins","ai_function_for_dark"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label=translations["plugins_tab"]["ai_functions_dark"],  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label=translations["plugins_tab"]["more"], width=100, callback=lambda: information_open(translations["ui_back"]["info_about_ai_functions_dark"]))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
        dpg.add_spacer(height=5)
        
        # Plugins for Telegram Bot
        with dpg.child_window(height=208):
            with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
                dpg.add_button(label=translations["plugins_tab"]["for_telegram_bot"],  pos=(7,2), width=456)
                dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True): # Plugin
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="mouse_move_for_telegram_ui", default_value=mouse_move_for_telegram, callback=lambda: data_update("plugins","mouse_move_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label=translations["plugins_tab"]["mouse_control"],  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label=translations["plugins_tab"]["more"], width=100, callback=lambda: information_open(translations["ui_back"]["info_about_mouse_control"]))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True): # Plugin
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="keyboard_move_for_telegram_ui", default_value=keyboard_move_for_telegram, callback=lambda: data_update("plugins","keyboard_move_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label=translations["plugins_tab"]["keyboard_control"],  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label=translations["plugins_tab"]["more"], width=100, callback=lambda: information_open(translations["ui_back"]["info_about_keyboard_control"]))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True): # Plugin
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="ai_function_for_telegram_ui", default_value=ai_function_for_telegram, callback=lambda: data_update("plugins","ai_function_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label=translations["plugins_tab"]["ai_functions_dark"],  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label=translations["plugins_tab"]["more"], width=100, callback=lambda: information_open(translations["ui_back"]["info_about_ai_functions"]))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True): # Plugin
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="data_function_for_telegram_ui", default_value=data_function_for_telegram, callback=lambda: data_update("plugins","data_function_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label=translations["plugins_tab"]["files_control"],  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label=translations["plugins_tab"]["more"], width=100, callback=lambda: information_open(translations["ui_back"]["info_about_data_functions"]))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
        dpg.add_spacer(height=5)
        
        # Plugins | Other 
        with dpg.child_window(height=82):
            with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
                dpg.add_button(label=translations["plugins_tab"]["other"],  pos=(7,2), width=456)
                dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True): # Plugin
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="monitoring_pc_other_ui", default_value=monitoring_pc_other, callback=lambda: data_update("plugins","monitoring_pc_other"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label=translations["plugins_tab"]["pc_monitoring"],  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label=translations["plugins_tab"]["more"], width=100, callback=lambda: information_open(translations["ui_back"]["info_about_monitoring_pc"]))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)      
    with dpg.child_window(height=670,width=485, tag="Dark_Tab", show=True, pos=(7,40)): # Dark Tab child Window 
        with dpg.group(horizontal=True): # Top bar of "Dark"
            dpg.add_button(label="   ", height=51, width=27, callback=change_mic_checker, tag="dark_mic_status") # "Dark" status bar
            if is_dark_on:
                dpg.bind_item_theme(dpg.last_item(), dark_mic_up)
            else:
                dpg.bind_item_theme(dpg.last_item(), dark_mic_off)
            dpg.add_image("dark", width=400, height=51, tag="dark_ui_logo") # "Dark" tittle [ maybe logo idk ]
            dpg.add_button(label=translations["dark_tab"]["settings"], height=51, width=32, callback=lambda: information_open(translations["ui_back"]["dark_have_no_settings"])) # Settings Button
        dpg.add_separator() # Line
        with dpg.child_window(height=553, tag="dark_chat"): # Chat
            dpg_markdown.add_text(translations["dark_tab"]["info"]) # Warning
        with dpg.child_window(): # Chat Input
            with dpg.group(horizontal=True):
                dpg.add_input_text(width=423, tag="dark_chat_value", callback=dark_send_msg, on_enter=True) # Input
                dpg.add_button(label="->", callback=dark_send_msg) # Send Button
    with dpg.child_window(height=670,width=485, tag="Panel_Tab", show=True, pos=(7,40)): # Panel Tab child Window
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
            dpg.add_button(label=translations["panel_tab"]["label"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator() # Line

        dpg_markdown.add_text(translations["panel_tab"]["in_dev"], pos=(145,200)) # in dev...
        dpg_markdown.add_text(translations["panel_tab"]["soon_ver410"], pos=(165,230))
    with dpg.child_window(height=670,width=485, tag="Settings_Tab", show=True, pos=(7,40)): # Settings Tab child Window
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
            dpg.add_button(label=translations["tab_bar"]["settings"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator() # Line
        dpg_markdown.add_text(translations["settings_tab"]["main"]) # Main text
        dpg.add_combo(["ru","en"], tag="settings_language", pos=(427,43),width=50, default_value=main_language) # change language combo
        with dpg.child_window(height=90): # main group
            dpg.add_input_text(hint=translations["settings_tab"]["name"], width=453, tag="settings_name", default_value=main_name) # Name
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
            dpg.add_input_text(hint=translations["settings_tab"]["token"], width=453, tag="settings_token", default_value=main_token) # telegram Token
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
            dpg.add_input_text(hint=translations["settings_tab"]["telegram_id"], width=453, tag="settings_id", default_value=main_id) # telegram ID
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
        dpg_markdown.add_text(translations["settings_tab"]["additionally"]) # Additionally text
        with dpg.child_window(height=64): # additionally group
            dpg.add_input_text(hint=translations["settings_tab"]["web_hook"], width=453, tag="settings_webhook", default_value=main_webhook) # web-hook
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
            dpg.add_input_text(hint=translations["settings_tab"]["discord_token"], width=453, tag="settings_token-ds", default_value=main_token_ds) # discord-token
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
        with dpg.group(horizontal=True): # Functions and Security text group
            dpg_markdown.add_text(translations["settings_tab"]["functions"], pos=(8,263)) # Functions text
            dpg_markdown.add_text(translations["settings_tab"]["security"], pos=(213,263)) # Security text
        with dpg.group(horizontal=True): # Functions and Security group
            with dpg.child_window(height=64, width=200, pos=(9,294)):
                with dpg.group(horizontal=True): # Auto-Screen
                    dpg.add_checkbox(tag="settings_autoscreen_value", default_value=is_main_autoscreen) # auto-screenshots checkbox
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
                    dpg.add_input_int(width=100, tag="settings_autoscreen_time", default_value=main_autoscreen_time) # auto-screenshots time
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
                    _help(translations["settings_tab"]["auto_screen"]) # auto-screen text
                with dpg.group(horizontal=True): # Auto-Info
                    dpg.add_checkbox(tag="settings_autoinfo_value", default_value=is_main_autoinformation) # auto-information checkbox
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
                    dpg.add_input_int(width=100, tag="settings_autoinfo_time", default_value=main_autosinformation_time) # auto-information time
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
                    _help(translations["settings_tab"]["auto_info"]) # auto-info text
            
            with dpg.child_window(height=64): # Security group
                dpg.add_input_text(hint=translations["settings_tab"]["login"], width=247, tag="settings_sec_login", default_value=main_login) # Login
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
                dpg.add_input_text(hint=translations["settings_tab"]["password"], width=247, tag="settings_sec_pass", default_value=main_password) # Password
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme
        dpg_markdown.add_text(translations["settings_tab"]["interface"]) # Interface text 
        with dpg.child_window(height=64): # Interface group
            dpg.add_button(label=translations["settings_tab"]["theme"], width=453, height=47, callback=lambda: ui_notify(text=translations["panel_tab"]["in_dev"], duration=3)) # theme button
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme

        dpg.add_separator() # Line
        dpg.add_spacer(height=139) # Space
        
        dpg.add_button(label=translations["settings_tab"]["save"], width=470, height=55, callback=lambda: data_update("main")) # Save button
        dpg.bind_item_theme(dpg.last_item(), key_button_color) # bind theme


    with dpg.group(tag="tab_in_ui"): # Tabs
        with dpg.group(horizontal=True, pos=(7,716)): # Tabs group
            dpg.add_button(height=25, pos=(7,716), label=translations["tab_bar"]["home"], tag="Home_Tab_Button", callback=lambda: change_tab("Home_Tab")); dpg.bind_item_theme(dpg.last_item(), picked_tab_color)  # home
            dpg.add_button(height=25, pos=(parameters["tab_weight"]["terminal"] ,716),label=translations["tab_bar"]["terminal"], tag="Terminal_Tab_Button", callback=lambda: change_tab("Terminal_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)  # terminal
            dpg.add_button(height=25, pos=(parameters["tab_weight"]["statistics"],716),label=translations["tab_bar"]["statistics"], tag="Statistics_Tab_Button", callback=lambda: change_tab("Statistics_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color) # statistics  
            dpg.add_button(height=25, pos=(parameters["tab_weight"]["plugins"],716),label=translations["tab_bar"]["plugins"], tag="Plugins_Tab_Button", callback=lambda: change_tab("Plugins_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)   # plugins
            dpg.add_button(height=25, pos=(parameters["tab_weight"]["dark"],716),label=translations["tab_bar"]["dark"], tag="Dark_Tab_Button", callback=lambda: change_tab("Dark_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)   #"Dark"
            dpg.add_button(height=25, pos=(parameters["tab_weight"]["panel"],716), label=translations["tab_bar"]["panel"], tag="Panel_Tab_Button", callback=lambda: change_tab("Panel_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)   # panel
            dpg.add_button(height=25, pos=(parameters["tab_weight"]["settings"],716),label=translations["tab_bar"]["settings"], tag="Settings_Tab_Button", callback=lambda: change_tab("Settings_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color) # settings
            
    
    
    with dpg.child_window(label=translations["ui_tools"]["ui_notification"], tag="notify_window", height=100,width=485, show=True, pos=(7,40)): # Notification window
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
            dpg.add_button(label=translations["ui_tools"]["ui_notification"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()  # Line
        dpg.add_text("", tag="notify_text", color=[255, 255, 255, 0],wrap=475) # Text
        dpg.add_spacer(height=5)  # Space
    with dpg.child_window(label=translations["ui_tools"]["ui_information"], tag="info_window", height=150,width=485, show=True, pos=(7,40)): # Information window
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True): # Label
            dpg.add_button(label=translations["ui_tools"]["ui_information"],  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator() # Line
        dpg.add_text("", tag="info_text", color=[255, 255, 255, 0],wrap=475) # Text
        dpg.add_spacer(height=5)  # Space
        dpg.add_button(label=translations["ui_tools"]["close"],  pos=(7,119), width=470, callback=information_close) # Close button
        dpg.bind_item_theme(dpg.last_item(), border_with_button_element) # bind theme






time.sleep(0.1) # ! This line makes UI 100% launched ! # 
init_all_element(dpg_animator) # hide element (for notify/information and start animation) 
dpg.bind_theme(dpg_theme.initialize()) # Initialize dpg_theme
dpg.bind_font(default_font) # bind font for UI
dpg.set_frame_callback(200, Init_After_UI_Init) # set callback after 200 frame make
dpg.set_frame_callback(10, Init_Before_UI_Init) # set callback after 10  frame make
dpg.create_viewport(title="Pc-Stat-Bot | V4", width=499, height=746, decorated=False, resizable=False, clear_color=[0, 0, 0, 0], small_icon="Data\\logo\\mini-logo.ico", large_icon="Data\\logo\\full-logo.ico") # Create Window 
dpg.setup_dearpygui() # dearpygui 
dpg.show_viewport() # show window
program_start = datetime.now() # start time
desired_fps = 61 # fps limit
frame_time = 1.0 / desired_fps # fps time
ctypes.windll.dwmapi.DwmExtendFrameIntoClientArea(get_hwnd(), MARGINS(-1, -1, -1, -1)) # Make window transparent
dpg_animator.run() # miss the 1st stage of animation before drawing UI (So that the interface does not appear in the 1st Frame)
dpg_animations.update() # miss the 1st stage of animation before drawing UI
if fps_unlocker: 
    while dpg.is_dearpygui_running(): # start render dearpygui and animations without lock
        dpg_animator.run() # animation
        dpg_animations.update() # animations
        dpg.render_dearpygui_frame() # render frame
else:
    while dpg.is_dearpygui_running(): # start render dearpygui and animations 
        dpg_animator.run() # animation
        dpg_animations.update() # animations
        start_time = time.time() # before frame render 
        dpg.render_dearpygui_frame() # render frame
        elapsed_time = time.time() - start_time # calculate time to sleep before next frame (so that there are 60 frames per second)
        time_to_sleep = max(frame_time - elapsed_time, 0) # calculate time to sleep before next frame (so that there are 60 frames per second)
        time.sleep(time_to_sleep) # time to sleep while
dpg.destroy_context() # dearpygui 

