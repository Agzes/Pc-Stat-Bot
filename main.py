""" ----------------------------- """
""" ---- BETA V4 PC-STAT-BOT ---- """
""" ----------------------------- """
version = """pre-4.0.0
"""


" DearPyGui | UI | Addons "
import dearpygui.dearpygui as dpg
from g4f.client import Client
import libs.dpg_animations as dpg_animations
import libs.dpg_animator.dearpygui_animate as dpg_animator
import libs.dpg_markdown as dpg_markdown
import libs.dpg_theme as dpg_theme
# Blur
import ctypes.wintypes
" Standart LIBS"
from datetime import datetime
import time as time
import webbrowser
import sys
import json
import threading

" For Get PC Info "
import psutil
from libs.sys_info.sys_info import SystemInfo
from libs.dpg_addons.dpg_blur import WindowsWindowEffect, get_hwnd, MARGINS

" For Bot "
from tg_bot import telegram_bot

" Dark "
from dark import dark_answer, darksoundaction
import speech_recognition as sr

import requests
" Discord Extention " 

" TEMP "
UI_user_name = "Agzes"
client = Client()

" GLOBAL FUNCTION "
def load_from_json(filename):
    with open(filename, 'r') as json_file:
        DATAfromCFG = json.load(json_file)
    return DATAfromCFG
" GLOBAL INFO"
Font_Path = "Data/Fonts/base.ttf"
big_let_start = 0x00C0
big_let_end = 0x00DF
small_let_end = 0x00FF
remap_big_let = 0x0410
alph_len = big_let_end - big_let_start + 1
alph_shift = remap_big_let - big_let_start
font_size = 15
default_font_path = 'Data/Fonts/base.ttf'
bold_font_path = 'Data/Fonts/bold.ttf'
italic_font_path = 'Data/Fonts/italic.ttf'
italic_bold_font_path = 'Data/Fonts/bolditalic.ttf'
is_menu_bar_clicked = False
is_terms_of_use_open = False
is_notify_open = False
is_info_open = False
is_dark_on = False
is_theme_picker_open = False
auto_thread_statistics = None
current_tab = "Home_Tab"
""" JSON CONFIG LOADER """
data_for_preload = load_from_json("Config/main_data.json")
"main"
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
"statistics"
auto_update_statistics = False
auto_update_statistics_time = 5
"plugins"
" for Dark "
ai_function_for_dark = False
" for telegram bot "
ai_function_for_telegram = False
mouse_move_for_telegram = False
keyboard_move_for_telegram = False
data_function_for_telegram = False
" other plugins "
monitoring_pc_other = False
try:
    main_name = data_for_preload["main"]["main_name"]
except:  # noqa: E722
    pass
try:
    main_token = data_for_preload["main"]["main_token"]
except:  # noqa: E722
    pass
try:
    main_id = data_for_preload["main"]["main_id"]
except:  # noqa: E722
    pass
try:
    main_webhook = data_for_preload["main"]["main_webhook"]
except:  # noqa: E722
    pass
try:
    main_token_ds = data_for_preload["main"]["main_token_ds"]
except:  # noqa: E722
    pass
try:
    is_main_autoscreen = data_for_preload["main"]["is_main_autoscreen"]
except:  # noqa: E722
    pass
try:
    main_autoscreen_time = data_for_preload["main"]["main_autoscreen_time"]
except:  # noqa: E722
    pass
try:
    is_main_autoinformation = data_for_preload["main"]["is_main_autoinformation"]
except:  # noqa: E722
    pass
try:
    main_autosinformation_time = data_for_preload["main"]["main_autosinformation_time"]
except:  # noqa: E722
    pass
try:
    main_login = data_for_preload["main"]["main_login"]
except:  # noqa: E722
    pass
try:
    main_password = data_for_preload["main"]["main_password"]
except:  # noqa: E722
    pass
try:
    main_language = data_for_preload["main"]["main_language"]
except:  # noqa: E722
    pass
try:
    auto_update_statisticks_info = data_for_preload["statistics"]["auto_update_statistics"]
except:  # noqa: E722
    pass
try:
    auto_update_statisticks_time_info = data_for_preload["statistics"]["auto_update_statistics_time"]
except:  # noqa: E722
    pass
try:
    ai_function_for_dark = data_for_preload["plugins"]["dark"]["ai_function_for_dark"]
except:  # noqa: E722
    pass
try:
    ai_function_for_telegram = data_for_preload["plugins"]["telegram"]["ai_function_for_telegram"]
except:  # noqa: E722
    pass
try:
    mouse_move_for_telegram = data_for_preload["plugins"]["telegram"]["mouse_move_for_telegram"]
except:  # noqa: E722
    pass
try:
    keyboard_move_for_telegram = data_for_preload["plugins"]["telegram"]["keyboard_move_for_telegram"]
except:  # noqa: E722
    pass
try:
    data_function_for_telegram = data_for_preload["plugins"]["telegram"]["data_function_for_telegram"]
except:  # noqa: E722
    pass
try:
    monitoring_pc_other = data_for_preload["plugins"]["other"]["monitoring_pc_other"]
except:  # noqa: E722
    pass
try:
    is_dark_on = data_for_preload["dark"]["dark_on"]
except:  # noqa: E722
    pass
lang = main_language

"Init UI"
dpg.create_context()

""" PC INFO AND BLUR """
system_info = SystemInfo()
window_effect = WindowsWindowEffect()


def close():
    dpg.destroy_context()
    sys.exit(0)

" FONT WITH CYRILIC SUPPORT "
def to_cyr(data_no_cyr):  
  out = [] 
  for i in range(0, len(data_no_cyr)):  
      if ord(data_no_cyr[i]) in range(big_let_start, small_let_end + 1):  
          out.append(chr(ord(data_no_cyr[i]) + alph_shift))  
      else:
          out.append(data_no_cyr[i])  
  return ''.join(out) 
with dpg.font_registry() as font_registry:
  with dpg.font(Font_Path, 15) as default_font:
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
def markdown_add_font(file, size, parent):
  with dpg.font(file, size, parent=parent) as font:
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
  return font
dpg_markdown.set_font_registry(font_registry)
dpg_markdown.set_add_font_function(markdown_add_font)
markdown_font = dpg_markdown.set_font(
    font_size=font_size,
    default=str(default_font_path),
    bold=str(bold_font_path),
    italic=str(italic_font_path),
    italic_bold=str(italic_bold_font_path)
)
" MOVE WINDOW "
def mouse_drag_callback(_, app_data):
    if is_menu_bar_clicked:
        _, drag_delta_x, drag_delta_y = app_data
        viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
        new_pos_x = viewport_pos_x + drag_delta_x
        new_pos_y = max(viewport_pos_y + drag_delta_y, 0)
        dpg.set_viewport_pos([new_pos_x, new_pos_y])
def mouse_click_callback():
    global is_menu_bar_clicked
    is_menu_bar_clicked = True if dpg.get_mouse_pos(local=False)[1] < 31 else False
with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)
    dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)
" ASSETS AND LOGO AND FONT FOR UI "
lw,lh,lc,ld = dpg.load_image("Data/logo/full-logo.png")
dw,dh,dc,dd = dpg.load_image("Data/assets/dark.png")
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=lw, height=lh, default_value=ld, tag="logo")
    dpg.add_static_texture(width=dw, height=dh, default_value=dd, tag="dark")
with dpg.font("Data/Fonts/namefont.ttf", 20, parent=font_registry) as NameFont:  
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
""" TAB WORKING """
def change_tab(tab):
    global current_tab, is_notify_open
    if is_terms_of_use_open is True:
        licens_window("close")
    if is_notify_open:
        ui_notify_close()
    dpg_animator.add("opacity", current_tab, 1, 0, [.57, .06, .61, .86], 100)
    dpg.bind_item_theme(f"{tab}_Button", picked_tab_color)
    dpg_animator.add("opacity", tab, 0, 1, [.57, .06, .61, .86], 100)
    dpg.bind_item_theme(f"{current_tab}_Button", unpicked_tab_color)
    current_tab = tab


""" 'DARK' """

    
def dark_checker(text, command=""):
    if text == "processed_status_200":
        dark_add("**[Дарк]:** выполнено!" if lang == "ru" else "**[Dark]:** done!")
    elif text == command.lower():
        dark_add("**[Дарк]:** Думаю..." if lang == "ru" else "**[Dark]:** Think...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{text}"}],
        )
        mesage = response.choices[0].message.content
        dark_add(f"**[Дарк]:** {mesage}" if lang == "ru" else f"**[Dark]:** {mesage}")
        darksoundaction()
    elif any(keyword in text for keyword in ("Привет!", "Hi!", "Пока!", "Bye!")):
        dark_add(f"**[Дарк]:** {text}" if lang == "ru" else f"**[Dark]:** {text}")
    elif text ==  "Команда или речь не распознана :c" or text == "Command or speech is not recognized :c":
        dark_add(f"**[Дарк]:** {text}" if lang == "ru" else f"**[Dark]:** {text}")
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
            dark_add(f"**[Вы][Голос]:** {dark_recognize}" if lang == "ru" else f"**[You][Voice]:** {dark_recognize}")
            return dark_recognize
        else:
            return "yous_dont_say_anything_code_200"
    except sr.UnknownValueError:
        return "Ошибка распознования голоса" if lang == "ru" else "Error with recognize Voice"
    except sr.RequestError:
        return "Ошибка в запросе на распознование голоса" if lang == "ru" else "Error with respone to recognize Voice"
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
    dark_add(f"**[Вы]:** {to_cyr(temp_msg)}" if lang == "ru" else f"**[You]:** {to_cyr(temp_msg)}")
    dpg.set_value("dark_chat_value", "")
    dark_checker(dark_answer(to_cyr(temp_msg), lang=main_language, itsvoice=False, plugin_ai=ai_function_for_dark), to_cyr(temp_msg))



""" UI USE """
def terminall_add(text, status, desc=""):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if "info" in  status:
        text = f'<font color="[255, 255, 255, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Tab")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)
        
    elif "error" in status:
        text = f'<font color="[173, 48, 38, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Tab")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)

    elif "status" in  status:
        text = f'<font color="[135, 173, 241, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Tab")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)
        
    elif "warning" in status:
        text = f'<font color="[187, 74, 13, 255]">{text}</font>'
        group = dpg.add_group(horizontal=True, parent="Terminal_Tab")
        dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
        t = dpg_markdown.add_text(text, parent=group, wrap=435)
        with dpg.tooltip(t):
            dpg.add_text(current_time)
        
    
    if desc != "":
        t = dpg.add_text("[больше]" if lang == "ru" else "[more]", parent=group, color=[200, 200, 200])
        with dpg.tooltip(t):
            dpg.add_text(desc)
def licens_window(move):
    global current_tab, is_terms_of_use_open
    if move == "open" and is_terms_of_use_open is False:
        is_terms_of_use_open = True
        dpg.show_item("Licens_Window")
        dpg_animator.add("opacity", "Home_Tab", 1, 0, [.57, .06, .61, .86], 100)
        dpg_animator.add("position", "Licens_Window", [7,-700], [7,37], [.23, .07, .53, 1], 100)
    else:
        is_terms_of_use_open = False
        dpg_animator.add("opacity", "Home_Tab", 0, 1, [.57, .06, .61, .86], 100)
        dpg_animator.add("position", "Licens_Window", [7,37], [7,-700], [.23, .07, .53, 1.30], 100)
def start_statistics_auto_update():
    global auto_thread_statistics
    while True:
        data_for_preload = load_from_json("Config/main_data.json")
        try:
            auto_update_statisticks_info = data_for_preload["statistics"]["auto_update_statistics"]
        except:  # noqa: E722
            pass
            time.sleep(1)
        try:
            auto_update_statisticks_time_info = data_for_preload["statistics"]["auto_update_statistics_time"]
        except:  # noqa: E722
            pass
            time.sleep(1)
        if auto_update_statisticks_info is False:
            pass
            time.sleep(1)
        elif auto_update_statisticks_info is True:
            if auto_update_statisticks_time_info <= 0:
                pass
                time.sleep(1)
            else:
                statistics_update()
                time.sleep(auto_update_statisticks_time_info)
def statistics_update():
    global programm_start
    info = system_info.get_formatted_info()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    " cpu "
    dpg.set_value("statistics_tab_cpu_label", f"ЦП: {info['cpu']}%" if lang == "ru" else f"CPU: {info['cpu']}%")
    temp_stat_cpu = dpg.get_value("statistics_tab_cpu_plot")
    temp_stat_cpu.append(info['cpu'])
    dpg.set_value("statistics_tab_cpu_plot", temp_stat_cpu)
    dpg.set_value("statistics_tab_cpu_cores_label", f"Ядра ЦП: {info['total_cores']}" if lang == "ru" else f"CPU cores: {info['total_cores']}")
    dpg.set_value("statistics_tab_cpu_cores", f"{info['cpu_cores_rus']}" if lang == "ru" else f"{info['cpu_cores_eng']}")

    " memory "
    dpg.set_value("statistics_tab_ram_occupied_label", f"Занято ОЗУ: {info['occupied_ram']:.2f} ГБ" if lang == "ru" else f"Occupied RAM: {info['occupied_ram']:.2f} GB")
    temp_stat_ocupied_ram = dpg.get_value("statistics_tab_ram_occupied")
    temp_stat_ocupied_ram.append(info['occupied_ram'])
    dpg.set_value("statistics_tab_ram_occupied", temp_stat_ocupied_ram)

    dpg.set_value("statistics_tab_ram_free_label", f"Свободно ОЗУ: {info['free_ram']:.2} ГБ" if lang == "ru" else f"Free RAM: {info['free_ram']:.2} GB")
    temp_stat_free_ram = dpg.get_value("statistics_tab_ram_free")
    temp_stat_free_ram.append(info['free_ram'])
    dpg.set_value("statistics_tab_ram_free", temp_stat_free_ram)

    dpg.set_value("statistics_tab_ram_total", f"{info['total_ram']:.2f} ГБ" if lang == "ru" else f"{info['total_ram']:.2f} GB")

    " gpu "
    dpg.set_value("statistics_tab_gpu_label", f"ГП: {info['gpu_info']}"if lang == "ru" else  f"GPU: {info['gpu_info']}")
    temp_stat_gpu = dpg.get_value("statistics_tab_gpu")
    temp_stat_gpu.append(info['gpu'])
    dpg.set_value("statistics_tab_gpu", temp_stat_gpu)

    " other "
    dpg.set_value("statistics_tab_other_time", f"Время: {current_time}"if lang == "ru" else f"Time: {current_time}")
    uptime = datetime.now() - programm_start
    dpg.set_value("statistics_tab_other_online", f"Программа включена: {uptime}" if lang == "ru" else f"Total online: {uptime}")
def _help(message):
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text("[i]", color=[255, 255, 255])
    with dpg.tooltip(t):
        dpg.add_text(message)

def information_open(text):
    global current_tab, is_info_open
    if is_info_open:
        information_close()
    is_info_open = True
    dpg.set_value("info_text", text)
    dpg_animator.add("opacity", "tab_in_ui", 1, 0, [.57, .06, .61, .86], 30)
    dpg_animator.add("position", "info_window", [5, -300], [7,37], [.23, .07, .53, 1], 100)
    dpg_animator.add("position", current_tab, [7,37], [7,190], [.23, .07, .53, 1.63], 100)
    dpg_animator.add("opacity", "info_window", 0, 1, [.57, .06, .61, .86], 100)
    dpg_animator.add("opacity", "info_text", 0, 1, [.64, .12, .72, .86], 100, timeoffset=10 / 60)
def information_close():
    global is_info_open
    if is_info_open is False:
        return
    elif is_info_open is True:
        is_info_open = False
    dpg_animator.add("opacity", "tab_in_ui", 0, 1, [.57, .06, .61, .86], 100)
    dpg_animator.add("position", "info_window", [7,37], [5, -300], [.23, .07, .53, 1], 100)
    dpg_animator.add("position", current_tab, [7, 190], [7,37], [.23, .07, .53, 1], 100)
    dpg_animator.add("opacity", "info_window", 1, 0, [.57, .06, .61, .86], 100)
    dpg_animator.add("opacity", "info_text", 1, 0, [.64, .12, .72, .86], 100, timeoffset=10 / 60)
def ui_notify_close(code=""):
    global is_notify_open
    if is_notify_open is False:
        return
    elif is_notify_open is True:
        is_notify_open = False
    dpg_animator.add("opacity", "tab_in_ui", 0, 1, [.57, .06, .61, .86], 100)
    dpg_animator.add("position", "notify_window", [7,37], [5, -300], [.23, .07, .53, 1], 100)
    dpg_animator.add("position", current_tab, [7, 140], [7,37], [.23, .07, .53, 1], 100)
    dpg_animator.add("opacity", "notify_window", 1, 0, [.57, .06, .61, .86], 100)
    dpg_animator.add("opacity", "notify_text", 1, 0, [.64, .12, .72, .86], 100, timeoffset=10 / 60)
def ui_notify_start(text, duraction):
    global current_tab, is_notify_open
    if is_notify_open:
        ui_notify_close()
    is_notify_open = True
    dpg.set_value("notify_text", text)
    dpg_animator.add("opacity", "tab_in_ui", 1, 0, [.57, .06, .61, .86], 30)
    dpg_animator.add("position", "notify_window", [5, -300], [7,37], [.23, .07, .53, 1], 100)
    dpg_animator.add("position", current_tab, [7,37], [7,140], [.23, .07, .53, 1.63], 100)
    dpg_animator.add("opacity", "notify_window", 0, 1, [.57, .06, .61, .86], 100)
    dpg_animator.add("opacity", "notify_text", 0, 1, [.64, .12, .72, .86], 100, timeoffset=10 / 60)
    time.sleep(duraction)
    ui_notify_close()
def ui_notify(text, duraction):
    threading.Thread(target=ui_notify_start,args=(text,duraction,)).start()
"""
def theme_window_open():
    global current_tab, is_theme_picker_open
    if is_theme_picker_open:
        theme_window_close()
    is_theme_picker_open = True
    dpg_animator.add("opacity", "tab_in_ui", 1, 0, [.57, .06, .61, .86], 30)
    dpg_animator.add("position", "pick_a_theme_window", [5, -300], [7,37], [.23, .07, .53, 1], 100)
    dpg_animator.add("position", current_tab, [7,37], [7,137], [.23, .07, .53, 1.63], 100)
    dpg_animator.add("opacity", "pick_a_theme_window", 0, 1, [.57, .06, .61, .86], 100)
def theme_window_close(code=""):
    global is_theme_picker_open
    if is_theme_picker_open is False:
        return
    elif is_theme_picker_open is True:
        is_theme_picker_open = False
    dpg_animator.add("opacity", "tab_in_ui", 0, 1, [.57, .06, .61, .86], 100)
    dpg_animator.add("position", "pick_a_theme_window", [7,37], [5, -300], [.23, .07, .53, 1], 100)
    dpg_animator.add("position", current_tab, [7, 137], [7,37], [.23, .07, .53, 1], 100)
    dpg_animator.add("opacity", "pick_a_theme_window", 1, 0, [.57, .06, .61, .86], 100)
"""

""" SAVE SETTINGS """
def data_update(whatsupdate, more=""):
    global statistics_thread

    data_for_preload = load_from_json("Config/main_data.json")
    "main"
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
    "statistics"
    auto_update_statistics = False
    auto_update_statistics_time = 5
    "plugins"
    " for Dark "
    ai_function_for_dark = False
    " for telegram bot "
    ai_function_for_telegram = False
    mouse_move_for_telegram = False
    keyboard_move_for_telegram = False
    data_function_for_telegram = False
    " other plugins "
    monitoring_pc_other = False
    "dark"
    dark_on = False
    try:
        main_name = data_for_preload["main"]["main_name"]
    except:  # noqa: E722
        pass
    try:
        main_token = data_for_preload["main"]["main_token"]
    except:  # noqa: E722
        pass
    try:
        main_id = data_for_preload["main"]["main_id"]
    except:  # noqa: E722
        pass
    try:
        main_webhook = data_for_preload["main"]["main_webhook"]
    except:  # noqa: E722
        pass
    try:
        main_token_ds = data_for_preload["main"]["main_token_ds"]
    except:  # noqa: E722
        pass
    try:
        is_main_autoscreen = data_for_preload["main"]["is_main_autoscreen"]
    except:  # noqa: E722
        pass
    try:
        main_autoscreen_time = data_for_preload["main"]["main_autoscreen_time"]
    except:  # noqa: E722
        pass
    try:
        is_main_autoinformation = data_for_preload["main"]["is_main_autoinformation"]
    except:  # noqa: E722
        pass
    try:
        main_autosinformation_time = data_for_preload["main"]["main_autosinformation_time"]
    except:  # noqa: E722
        pass
    try:
        main_login = data_for_preload["main"]["main_login"]
    except:  # noqa: E722
        pass
    try:
        main_password = data_for_preload["dark"]["main_password"]
    except:  # noqa: E722
        pass
    try:
        main_language = data_for_preload["main"]["main_language"]
    except:  # noqa: E722
        pass
    try:
        auto_update_statistics = data_for_preload["statistics"]["auto_update_statistics"]
    except:  # noqa: E722
        pass
    try:
        auto_update_statistics_time = data_for_preload["statistics"]["auto_update_statistics_time"]
    except:  # noqa: E722
        pass
    try:
        ai_function_for_dark = data_for_preload["plugins"]["dark"]["ai_function_for_dark"]
    except:  # noqa: E722
        pass
    try:
        ai_function_for_telegram = data_for_preload["plugins"]["telegram"]["ai_function_for_telegram"]
    except:  # noqa: E722
        pass
    try:
        mouse_move_for_telegram = data_for_preload["plugins"]["telegram"]["mouse_move_for_telegram"]
    except:  # noqa: E722
        pass
    try:
        keyboard_move_for_telegram = data_for_preload["plugins"]["telegram"]["keyboard_move_for_telegram"]
    except:  # noqa: E722
        pass
    try:
        data_function_for_telegram = data_for_preload["plugins"]["telegram"]["data_function_for_telegram"]
    except:  # noqa: E722
        pass
    try:
        monitoring_pc_other = data_for_preload["plugins"]["other"]["monitoring_pc_other"]
    except:  # noqa: E722
        pass
    try:
        dark_on = data_for_preload["dark"]["dark_on"]
    except:  # noqa: E722
        pass


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
            ui_notify("Ошибка: Имя пустое!" if lang == "ru" else "Error: Name is null!", 3)
            return
        if main_token == "":
            ui_notify("Ошибка: Нет токена!" if lang == "ru" else "Error: No token!", 3)
            return
        else:
            if ":" in main_token:
                pass
            else:
                ui_notify("Ошибка: Токен не правильного формата!" if lang == "ru" else "Error: The token is not in the right format!", 3)
                return
        if id == "":
            ui_notify("Ошибка: Нет id!" if lang == "ru" else "Error: id not entered!", 3)
            return
        if is_main_autoscreen is True:
            if main_autoscreen_time <= 0:
                ui_notify("Ошибка: Время в Авто-Скриншотах указанно не верно!\nИспользуйте значения от 1 до 999" if lang == "ru" else "Error: The time in Auto-Screenshots is not correct!\nUse values from 1 to 999", 3)
                return
        if is_main_autoinformation is True:
            if main_autosinformation_time <= 0:
                ui_notify("Ошибка: Время в Авто-Статистике указанно не верно!\nИспользуйте значения от 1 до 999" if lang == "ru" else "Error: The time in Auto-Statistics is not correct!\nUse values from 1 to 999", 3)
                return
    if whatsupdate == "stat":
        auto_update_statistics = dpg.get_value("statistics_tab_settings_checkbox")
        auto_update_statistics_time = dpg.get_value("statistics_tab_settings_time")

        if auto_update_statistics_time <= 0 or auto_update_statistics_time >=1000:
            ui_notify("Ошибка!\nВремя для обновления должно быть от 1 до 999" if lang == "ru" else "Mistake!\nThe time for the update should be from 1 to 999", 5)
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
            "auto_update_statistics": auto_update_statistics,
            "auto_update_statistics_time": auto_update_statistics_time
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
        ui_notify("Сохранено!" if lang == "ru" else "Saved!", 3)

def start_telegram_bot():
    global tg_bot
    threading.Thread(target=start_check_tg_status).start()
    tg_bot = telegram_bot()

total_message_in_tg_bot = 0
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
                        terminall_add(message,status,desc)
                        total_message_in_tg_bot += 1
        time.sleep(0.1)





def check_for_update():
    url = 'https://raw.githubusercontent.com/Agzes/Pc-Stat-Bot/main/version.txt'
    response = requests.get(url)
    if response.status_code == 200:
        file_content = response.text
        if file_content != version:
            information_open(f"Доступна новая версия! Последняя версия: {file_content}, ваша версия: {version}" if lang == "ru" else f"A new version is available! Latest version: {file_content}, your version: {version}")
    else:
        information_open(f"Не удалось наличие обновлений. Ответ от сервера: {response.status_code}" if lang == "ru" else f"Error with check for update. Response from server: {response.status_code}")
def Init_After_UI_Init():
    global recognizer, microphone, statistics_thread
    " BLUR ON "
    window_effect.setAeroEffect(get_hwnd())
    window_effect.setRoundedCorners(get_hwnd(), 10)
    " TRANSPARENT VIEWPORT "
    dwm = ctypes.windll.dwmapi
    margins = MARGINS(-1, -1, -1, -1)
    dwm.DwmExtendFrameIntoClientArea(get_hwnd(), margins) 
    " FONT "
    with dpg.font(Font_Path, 15, parent=font_registry) as input_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        biglet = remap_big_let
        for i1 in range(big_let_start, big_let_end + 1):
            dpg.add_char_remap(i1, biglet)
            dpg.add_char_remap(i1 + alph_len, biglet + alph_len)
            biglet += 1
    dpg.bind_item_font("dark_chat_value", input_font)
    dpg.bind_item_font("settings_name", input_font)
    dpg_animator.add("opacity", "Home_Tab", 0, 1, [.57, .06, .61, .86], 100)
    dpg.bind_item_theme("Home_Tab_Button", picked_tab_color)
    " "
    statistics_thread = threading.Thread(target=start_statistics_auto_update).start()
    
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    threading.Thread(target=dark_start).start()
    threading.Thread(target=check_for_update).start()
    threading.Thread(target=start_telegram_bot).start()
""" UI """
with dpg.theme() as unpicked_tab_color:
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_Button, [18, 18, 18, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [188, 177, 226, 140])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [208, 197, 246, 140])
with dpg.theme() as picked_tab_color:
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 0, 75, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [37, 0, 75, 140])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [37, 0, 75, 140])
with dpg.theme() as key_button_color:
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 0, 75, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [37, 0, 75, 140])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [37, 0, 75, 140])
with dpg.theme() as key_button_color_with_border:
    with dpg.theme_component():
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 0, 75, 255])
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

with dpg.window(label="Pc-Stat-Bot", pos=(0,0), height=750, width=500, no_title_bar=True, no_resize=True, no_close=True, tag="UI", no_background=False, no_move=True, show=True, no_scroll_with_mouse=True, no_scrollbar=True):
    with dpg.group(horizontal=True):
        dpg.add_image("logo", width=20,height=20, pos=(7, 6))
        dpg.add_text('''Pc-Stat-Bot''', pos=(33,2))
        dpg.bind_item_font(dpg.last_item(), NameFont)
        dpg.add_button(label='-', pos=(430, 6), height=20, width=20, callback=lambda: dpg.minimize_viewport())
        dpg.add_button(label='X', pos=(453, 6), height=20, width=40, callback=close)
    dpg_markdown.add_text("---", pos=(0,24))

    """ UI TOOLS """
    with dpg.child_window(height=670,width=485, tag="Licens_Window", show=False, pos=(7,-700), indent=1):
        with dpg.child_window(height=600):
            dpg_markdown.add_text("""## Условия использования Pc-Stat-Bot
---        
## Введение
**Pc-Stat-Bot** - это многофункциональный бот для узнавания 
разной информации пк удалённо. Он позволяет управлять музыкой,
видео, звуком, мышкой, клавиатурой и другимифункциями ПК через 
телеграм-бота. Он также имеет графический интерфейс 
пользователя (UI), который показывает статистику ПК, такую как 
загрузка ЦП, загрузка ГП, загрузку ОП и т.д. **Pc-Stat-Bot** 
разработан и принадлежит Agzes. Это приложение является 
бесплатным и c открытым исходным кодом, который вы можете 
найти на **github**.Вы можете использовать приложение 
**Pc-Stat-Bot** только в личных и не коммерческих целях. 
Вы не можете продавать,сдавать в аренду, распространять или 
передавать приложение или его части третьим лицам.

---
## Область применения
Вы можете модифицировать исходный код приложения соответствии 
с лицензией **GNU General Public License v3.0**, которая 
доступна на **github**. Вы должны сохранять все авторские права.
Вы несете полную ответственность за любые действия, которые вы 
совершаете с помощью приложения **Pc-Stat-Bot**.

---
## Отказ от ответственности
Мы предоставляем вам приложение **Pc-Stat-Bot** **как есть** без 
каких-либо гарантий или обязательств. Мы не гарантируем, что 
приложение будет работать без ошибок, сбоев или прерываний. 
Мы также не гарантируем, что приложение будет соответствовать 
вашим потребностям или ожиданиям.Мы не несем ответственности за 
любые убытки или ущерб,который может возникнуть в связи с 
использованием или невозможностью использования приложения 
Pc-Stat-Bot. Это включает, но не ограничивается, потерей 
данных, прибыли, репутации, деловой информации или другими 
не материальными убытками. Мы также не несем ответственности 
за любые претензии или  требования третьих лиц, связанные с 
вашим использованием приложения **Pc-Stat-Bot**. 

---
## Изменение условий использования
Мы оставляем за собой право изменять эти условия использования
в любое время по нашему усмотрению. Мы будем уведомлять вас о 
любых существенных изменениях через приложение или другие 
доступные каналы. Ваше продолжение использования приложения 
после такого уведомления будет означать ваше согласие с 
измененными условиями использования.""" if lang == "ru" else """## Pc-Stat-Bot: Terms of Use

---
## Introduction
**Pc-Stat-Bot** is a multifunctional bot for recognizing different 
pc information remotely. It allows you to control music, video, 
sound, mouse, keyboard and other PC functions via telegram bot. 
It also has a graphical user interface (UI) that shows PC
statistics such as CPU utilization, GPU utilization, OP 
utilization, etc. **Pc-Stat-Bot** is developed and owned by Agzes. 
This application is free and open source which you can find on 
**github**. You can use **Pc-Stat-Bot** application only for 
personal and non commercial purposes. You may not sell, rent, 
lease, distribute or transfer the application or parts of it 
to third parties.

---
## Application Scope
You may modify the source code of the application under the 
**GNU General Public License v3.0**, which is available on 
**github**. You must retain all copyrights.You are solely 
responsible for any actions you take with the **Pc-Stat-Bot** 
application.

---
## Disclaimer
We provide you with the **Pc-Stat-Bot** application **as is** 
*as is* without any warranty or guarantee. We do not guarantee
that the application will be error, crash or interruption free. 
We also do not warrant that the application will meet your 
needs or expectations.We will not be liable for any loss or 
damage that may arise from the use or inability to use the 
Pc-Stat-Bot application. This includes, but is not limited to, 
loss of data, profits, reputation, business information or other 
non-tangible damages. We are also not responsible for any third 
party claims or demands arising from your use of the 
**Pc-Stat-Bot application**.

---
## Change of Terms of Use
We reserve the right to change these terms of use at any time 
at our discretion. We will notify you of any material changes
through the app or other available channels. Your continued 
use of the app after such notification will constitute your 
acceptance of the modified terms of use.""")
        dpg.add_button(label="Закрыть" if lang == "ru" else "Close", width=468, height=50, callback= lambda: licens_window("close"))

    """ UI TABS """
    with dpg.child_window(height=670, tag="Home_Tab", show=True, pos=(7,37)):
        text_for_greetings = f"## Здравствуйте, {main_name}" if lang == "ru" else f"## Hello, {main_name}"
        dpg_markdown.add_text(text_for_greetings, pos=((500-(len(text_for_greetings)*11))/2,150))
        with dpg.group(horizontal=True, pos=(7,587)):
            dpg.add_button(label="Обратная Связь" if lang == "ru" else 'Feedback', width=233, height=30, callback=lambda: webbrowser.open("https://t.me/agzes0"))
            dpg.add_button(label="Страница Проекта" if lang == "ru" else 'Project Page', width=233, height=30, callback=lambda: webbrowser.open("https://github.com/Agzes/Pc-Stat-Bot"))
        dpg.add_button(label="Лицензионное соглашение" if lang == "ru" else "License Agreement", width=471, pos=(7,620), height=42,  callback=lambda: licens_window("open")) 
        dpg.bind_item_theme(dpg.last_item(), key_button_color) 
    with dpg.child_window(height=670,width=485, tag="Terminal_Tab", show=True, pos=(7,37)):
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="Терминал" if lang == "ru" else "Terminal",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg_markdown.add_text("---")
    with dpg.child_window(height=670,width=485, tag="Statistics_Tab", show=True, pos=(7,37)):
        
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="Статистика" if lang == "ru" else "Statistics",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()
        " CPU "
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=316, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text("ЦП: " if lang == "ru" else "CPU: ", pos=(7,3), tag="statistics_tab_cpu_label")
                dpg.add_simple_plot(height=100, default_value=(0,100,), tag="statistics_tab_cpu_plot")
                dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=148, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text("Ядра ЦП: " if lang == "ru" else "CPU cores: ", pos=(7,3), tag="statistics_tab_cpu_cores_label")
                with dpg.child_window(height=100):
                    dpg.add_text("", tag="statistics_tab_cpu_cores", pos=(7,3))
        
        dpg.add_separator()
        " RAM "
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=170, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text("Занято ОЗУ: " if lang == "ru" else "Occupied RAM: ", pos=(7,3), tag="statistics_tab_ram_occupied_label")
                dpg.add_simple_plot(height=100, width=170, default_value=(0,psutil.virtual_memory().total / (1024 ** 3)), tag="statistics_tab_ram_occupied")
                dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=170, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text("Свободно ОЗУ: " if lang == "ru" else "Free RAM: ", pos=(7,3), tag="statistics_tab_ram_free_label")
                dpg.add_simple_plot(height=100, width=170, default_value=(0,psutil.virtual_memory().total / (1024 ** 3)), tag="statistics_tab_ram_free")
                dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)
            with dpg.group(horizontal=False):
                with dpg.child_window(height=25, width=119, no_scrollbar=True, no_scroll_with_mouse=True):
                    dpg.add_text("Всего ОЗУ: " if lang == "ru" else "Total RAM:", pos=(7,3), tag="statistics_tab_ram_total_label")
                with dpg.child_window(height=100):
                    dpg.add_text("", tag="statistics_tab_ram_total")
           
        dpg.add_separator()
        " GPU "
        with dpg.child_window(height=25, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_text("ГП: " if lang == "ru" else "GPU: ", pos=(7,3), tag="statistics_tab_gpu_label")
        dpg.add_simple_plot(height=100, width=470, default_value=(0,100,), tag="statistics_tab_gpu")
        dpg.bind_item_theme(dpg.last_item(), simple_plot_theme)

        dpg.add_separator()
        " OTHER "
        with dpg.child_window(height=25, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_text("Прочее: " if lang == "ru" else "Other: ", pos=(7,3))
        with dpg.child_window(height=70, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_text("Программа включена: "if lang == "ru" else "Total online: ", tag="statistics_tab_other_online")
            dpg.add_text("Время: "if lang == "ru" else "Time: ", tag="statistics_tab_other_time")

        dpg.add_separator()
        " SETTINGS "
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="автоматическое обновление статистики" if lang == "ru" else "automatic statistics update",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        with dpg.child_window(height=34, width=470, no_scrollbar=True, no_scroll_with_mouse=True):
            with dpg.group(horizontal=True):
                dpg.add_checkbox(pos=(6,6), tag="statistics_tab_settings_checkbox", default_value=auto_update_statisticks_info)
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                dpg.add_button(label="сохранить"  if lang == "ru" else "save", width=325, callback=lambda: data_update("stat"))
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                dpg.add_input_int(width=100, tag="statistics_tab_settings_time", default_value=auto_update_statisticks_time_info)
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
        
        dpg.add_separator()
        " UPDATE "
        dpg.add_button(label="обновить"  if lang == "ru" else "update",height=30, width=470, callback=statistics_update)
        dpg.bind_item_theme(dpg.last_item(), key_button_color_with_border)
    with dpg.child_window(height=670,width=485, tag="Plugins_Tab", show=True, pos=(7,37)):
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="Плагины" if lang == "ru" else "Plugins",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()

        with dpg.child_window(height=82):
            with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
                dpg.add_button(label='Для "Дарка"' if lang == "ru" else 'For "Dark"',  pos=(7,2), width=456)
                dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="ai_functions_for_dark_ui", default_value=ai_function_for_dark, callback=lambda: data_update("plugins","ai_function_for_dark"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label='Функции ИИ*' if lang == "ru" else 'AI Functions*',  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label="Подробнее" if lang == "ru" else "More", width=100, callback=lambda: information_open("""Функции ИИ (для "Дарка")
Версия: 1.1.0 | Тип: Дополнение для "Дарка" 
Добавляет функции ИИ для "Дарка"
""" if lang == "ru" else """AI Functions (for “Dark”)
Version: 1.1.0 | Type: Add-on for "Dark"
Adds AI functions for "Dark"
"""))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)

        dpg.add_spacer(height=5)
        with dpg.child_window(height=208):
            with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
                dpg.add_button(label='Для Телеграмм Бота' if lang == "ru" else 'For Telegram Bot',  pos=(7,2), width=456)
                dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="mouse_move_for_telegram_ui", default_value=mouse_move_for_telegram, callback=lambda: data_update("plugins","mouse_move_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label='Управление Мышкой' if lang == "ru" else 'Mouse Control',  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label="Подробнее" if lang == "ru" else "More", width=100, callback=lambda: information_open("""Управление Мышкой
Версия: 1.1.0 | Тип: Дополнение для Telegram
Добавляет функции управление мышкой в телеграмм бота
""" if lang == "ru" else """Mouse Control
Version: 1.1.0 | Type: Add-on for Telegram
Adds mouse control functions to Telegram bot
"""))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="keyboard_move_for_telegram_ui", default_value=keyboard_move_for_telegram, callback=lambda: data_update("plugins","keyboard_move_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label='Управление Клавиатурой' if lang == "ru" else 'Keyboard Control',  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label="Подробнее" if lang == "ru" else "More", width=100, callback=lambda: information_open("""Управление Клавиатурой
Версия: 2.0 | Тип: Дополнение для Telegram
Добавляет функции управление клавиатурой для Телеграмм бота
""" if lang == "ru" else """Keyboard Control
Version: 2.0 | Type: Add-on for Telegram
Adds keyboard control functions for Telegram bot
"""))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="ai_function_for_telegram_ui", default_value=ai_function_for_telegram, callback=lambda: data_update("plugins","ai_function_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label='Функции ИИ*' if lang == "ru" else 'AI Functions*',  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label="Подробнее" if lang == "ru" else "More", width=100, callback=lambda: information_open("""Функции ИИ (для Телеграмм бота)
Версия: 1.1.0 | Тип: Дополнение для Telegram
Добавляет функции ИИ для телеграмм бота
""" if lang == "ru" else """AI Functions (for Telegram bot)
Version: 1.1.0 | Type: Add-on for Telegram
Adds AI functions for Telegram bot
"""))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="data_function_for_telegram_ui", default_value=data_function_for_telegram, callback=lambda: data_update("plugins","data_function_for_telegram"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label='Управление Файлами' if lang == "ru" else 'Files Control',  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label="Подробнее" if lang == "ru" else "More", width=100, callback=lambda: information_open("""Управление Файлами
Версия: 1.1.0 | Тип: Дополнение для Telegram 
Добавляет управлением файлами
""" if lang == "ru" else """Files Control
Version: 1.1.0 | Type: Add-on for Telegram
Adds files control for Telegram bot
"""))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)

        dpg.add_spacer(height=5)
        with dpg.child_window(height=82):
            with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
                dpg.add_button(label='Прочее' if lang == "ru" else 'Other',  pos=(7,2), width=456)
                dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
            with dpg.child_window(height=37, no_scrollbar=True, no_scroll_with_mouse=True):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(pos=(7,7), tag="monitoring_pc_other_ui", default_value=monitoring_pc_other, callback=lambda: data_update("plugins","monitoring_pc_other"))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_button(label='Мониторинг ПК' if lang == "ru" else 'PC Monitoring',  width=305)
                    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
                    dpg.add_button(label="Подробнее" if lang == "ru" else "More", width=100, callback=lambda: information_open("""Мониторинг ПК
Версия: 1.0.0 | Тип: Прочее
Мониторинг ПК и всё...
""" if lang == "ru" else """PC Monitoring
Version: 1.0.0 | Type: Other
PC Monitoring and all
"""))
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)      
    with dpg.child_window(height=670,width=485, tag="Dark_Tab", show=True, pos=(7,37)): 
        with dpg.group(horizontal=True):
            dpg.add_button(label="   ", height=51, width=27, callback=change_mic_checker, tag="dark_mic_status")
            if is_dark_on:
                dpg.bind_item_theme(dpg.last_item(), dark_mic_up)
            else:
                dpg.bind_item_theme(dpg.last_item(), dark_mic_off)
            dpg.add_image("dark", width=400, height=51, tag="dark_ui_logo")
            dpg.add_button(label="Нас\nтро\nйки"if lang=="ru" else "Set\ntin\ngs", height=51, width=32, callback=lambda: information_open('На данный момент у "Дарка" нету настроек'if lang == "ru" else 'At the moment, "Dark" has no settings'))
        dpg.add_separator()
        with dpg.child_window(height=553, tag="dark_chat"):
            dpg_markdown.add_text("""# Warning!\n**dark is now in alpha (+_+)**""")
        with dpg.child_window():
            with dpg.group(horizontal=True):
                dpg.add_input_text(width=423, tag="dark_chat_value", callback=dark_send_msg, on_enter=True)
                dpg.add_button(label="->", callback=dark_send_msg)
    with dpg.child_window(height=670,width=485, tag="Panel_Tab", show=True, pos=(7,37)):
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="v4 | Pc-Stat-Bot | Панель" if lang == "ru" else "v4 | Pc-Stat-Bot | Panel",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()

        dpg_markdown.add_text("\n\n\n\n# будет доступно в v.4.1 " if lang == "ru" else "\n\n\n\n# comming soon in v.4.1")
    with dpg.child_window(height=670,width=485, tag="Settings_Tab", show=True, pos=(7,37)):
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="Настройки" if lang == "ru" else "Settings",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()
        dpg_markdown.add_text("## Основное:" if lang == "ru" else "## Main:")
        dpg.add_combo(["ru","en"], tag="settings_language", pos=(427,43),width=50, default_value=main_language)
        with dpg.child_window(height=90):
            dpg.add_input_text(hint="Имя (как вас можно называть) " if lang == "ru" else "Name (what to call you)", width=453, tag="settings_name", default_value=main_name)
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            dpg.add_input_text(hint="Токен" if lang == "ru" else "Token", width=453, tag="settings_token", default_value=main_token)
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            dpg.add_input_text(hint="Телеграмм ID" if lang == "ru" else "Telegram ID", width=453, tag="settings_id", default_value=main_id)
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
        
        dpg_markdown.add_text("## Дополнительно:" if lang == "ru" else "## Additionally:")
        with dpg.child_window(height=64):
            dpg.add_input_text(hint="Веб-Хук" if lang == "ru" else "Web-hook", width=453, tag="settings_webhook", default_value=main_webhook)
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
            dpg.add_input_text(hint="Discord токен" if lang == "ru" else "Discord token", width=453, tag="settings_token-ds", default_value=main_token_ds)
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
        with dpg.group(horizontal=True):
            dpg_markdown.add_text("## Функции:" if lang == "ru" else "## Functions:")
            dpg_markdown.add_text("## Безопаность:" if lang == "ru" else "## Security:", pos=(213,263))
        with dpg.group(horizontal=True):
            with dpg.child_window(height=64, width=200, pos=(9,294)):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(tag="settings_autoscreen_value", default_value=is_main_autoscreen)
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_input_int(width=100, tag="settings_autoscreen_time", default_value=main_autoscreen_time)
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    _help("авто-скриншоты" if lang == "ru" else "auto-screen")
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(tag="settings_autoinfo_value", default_value=is_main_autoinformation)  
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    dpg.add_input_int(width=100, tag="settings_autoinfo_time", default_value=main_autosinformation_time)
                    dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                    _help("авто-информация" if lang == "ru" else "auto-info")
            
            with dpg.child_window(height=64):
                dpg.add_input_text(hint="Логин" if lang == "ru" else "Login", width=247, tag="settings_sec_login", default_value=main_login)
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)
                dpg.add_input_text(hint="Пароль" if lang == "ru" else "Password", width=247, tag="settings_sec_pass", default_value=main_password)
                dpg.bind_item_theme(dpg.last_item(), border_with_button_element)

        dpg_markdown.add_text("## Интерфейс:" if lang == "ru" else "## Interface:")
        with dpg.child_window(height=64):
            dpg.add_button(label="Тема" if lang == "ru" else "Theme", width=453, height=47, callback=lambda: ui_notify(text="Скоро в версии 4.1" if lang == "ru" else "Soon in v.4.1", duraction=3))
            dpg.bind_item_theme(dpg.last_item(), border_with_button_element)

        dpg.add_separator()

        dpg.add_spacer(height=139)
        dpg.add_button(label="Сохранить" if lang == "ru" else "Save", width=470, height=55, callback=lambda: data_update("main"))
        dpg.bind_item_theme(dpg.last_item(), key_button_color) 


    with dpg.group(tag="tab_in_ui"):
        dpg_markdown.add_text("---", pos=(0,706))
        with dpg.group(horizontal=True, pos=(7,720)):
            dpg.add_button(label=" Главная " if lang == "ru" else "  Home  ", tag="Home_Tab_Button", callback=lambda: change_tab("Home_Tab")); dpg.bind_item_theme(dpg.last_item(), picked_tab_color)  # noqa: E702
            dpg.add_button(label="Терминал" if lang == "ru" else "Terminal", tag="Terminal_Tab_Button", callback=lambda: change_tab("Terminal_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)  # noqa: E702
            dpg.add_button(label="Статистика" if lang == "ru" else "Statistics", tag="Statistics_Tab_Button", callback=lambda: change_tab("Statistics_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)  # noqa: E702
            dpg.add_button(label="Плагины" if lang == "ru" else "Plugins", tag="Plugins_Tab_Button", callback=lambda: change_tab("Plugins_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)  # noqa: E702
            dpg.add_button(label='"Дарк"' if lang == "ru" else ' "Dark" ', tag="Dark_Tab_Button", callback=lambda: change_tab("Dark_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)  # noqa: E702
            dpg.add_button(label="Панель" if lang == "ru" else "Panel*", tag="Panel_Tab_Button", callback=lambda: change_tab("Panel_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)  # noqa: E702
            dpg.add_button(label="Настройки" if lang == "ru" else "Settings", tag="Settings_Tab_Button", callback=lambda: change_tab("Settings_Tab")); dpg.bind_item_theme(dpg.last_item(), unpicked_tab_color)  # noqa: E702
    """
    with dpg.child_window(label="Выберите тему" if lang == "ru" else "Choose a theme", tag="pick_a_theme_window", height=97,width=485, show=True, pos=(7,37)):
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="Выберите тему" if lang == "ru" else "Choose a theme",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()
        dpg_theme.add_theme_picker(tag="theme_picker_in_ui", width=470)
        dpg.add_button(label="Закрыть & Сохранить" if lang == "ru" else "Close & Save",width=470, callback=theme_window_close)
    """
    with dpg.child_window(label="Уведомление!" if lang == "ru" else "Notification!", tag="notify_window", height=100,width=485, show=True, pos=(7,37)):
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="Уведомление!" if lang == "ru" else "Notification!",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()
        dpg.add_text("", tag="notify_text", color=[255, 255, 255, 0],wrap=475)
        dpg.add_spacer(height=5)
    with dpg.child_window(label="Информация" if lang == "ru" else "Information", tag="info_window", height=150,width=485, show=True, pos=(7,37)):
        with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True):
            dpg.add_button(label="Информация" if lang == "ru" else "Information",  pos=(7,2), width=456)
            dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
        dpg.add_separator()
        dpg.add_text("", tag="info_text", color=[255, 255, 255, 0],wrap=475)
        dpg.add_spacer(height=5)
        dpg.add_button(label="закрыть" if lang == "ru" else "close",  pos=(7,119), width=470, callback=information_close)
        dpg.bind_item_theme(dpg.last_item(), border_with_button_element)



""" HIDE UI """
dpg_animator.add("position", "Licens_Window", [0,0], [7,-700], [.23, .07, .53, 1.63], 1)
dpg_animator.add("position", "notify_window", [0,0], [7,-300], [.23, .07, .53, 1.63], 1)
dpg_animator.add("position", "info_window", [0,0], [7,-300], [.23, .07, .53, 1.63], 1)
dpg_animator.add("opacity", "Home_Tab", 1, 0, [.57, .06, .61, .86], 1)
dpg_animator.add("opacity", "Terminal_Tab", 1, 0, [.57, .06, .61, .86], 1)
dpg_animator.add("opacity", "Statistics_Tab", 1, 0, [.57, .06, .61, .86], 1)
dpg_animator.add("opacity", "Plugins_Tab", 1, 0, [.57, .06, .61, .86], 1)
dpg_animator.add("opacity", "Dark_Tab", 1, 0, [.57, .06, .61, .86], 1)
dpg_animator.add("opacity", "Panel_Tab", 1, 0, [.57, .06, .61, .86], 1)
dpg_animator.add("opacity", "Settings_Tab", 1, 0, [.57, .06, .61, .86], 1)

programm_start = datetime.now()

dpg.bind_theme(dpg_theme.initialize())
dpg.bind_font(default_font)
dpg.set_frame_callback(20, Init_After_UI_Init)
dpg.create_viewport(title="Pc-Stat-Bot | V4", width=500, height=750, decorated=False, resizable=False, clear_color=[0, 0, 0, 0], small_icon="Data\\logo\\mini-logo.ico", large_icon="Data\\logo\\full-logo.ico")
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg_animator.run()
    dpg_animations.update()
    dpg.render_dearpygui_frame()
dpg.destroy_context()



















