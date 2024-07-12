""" ----------------------------- """
""" ---- BETA V4 PC-STAT-BOT ---- """
""" ----------------------------- """

import dearpygui.dearpygui as dpg
import libs.dpg_animations as dpg_animations
import libs.dpg_animator.dearpygui_animate as dpg_animator
import libs.dpg_theme as dpg_theme
from libs.dpg_addons.dpg_blur import WindowsWindowEffect, get_hwnd, MARGINS
import ctypes
import sys
import threading
import subprocess
import os
import time
import requests
import zipfile
big_let_start = 0x00C0
big_let_end = 0x00DF
small_let_end = 0x00FF
remap_big_let = 0x0410
alph_len = big_let_end - big_let_start + 1
alph_shift = remap_big_let - big_let_start
font_size = 15
is_menu_bar_clicked = False
dpg.create_context()
window_effect = WindowsWindowEffect()
def close():
    dpg.destroy_context()
    sys.exit(0)

def to_cyr(data_no_cyr):  
  out = [] 
  for i in range(0, len(data_no_cyr)):  
      if ord(data_no_cyr[i]) in range(big_let_start, small_let_end + 1):  
          out.append(chr(ord(data_no_cyr[i]) + alph_shift))  
      else:
          out.append(data_no_cyr[i])  
  return ''.join(out) 

def close_after_install():
    dpg.destroy_context()
    try:
        subprocess.Popen(["./pc-stat-bot/Pc-Stat-Bot.exe"])
    except subprocess.CalledProcessError as e:
        pass
    sys.exit(0)
def get_file_size(size_url):
    response = requests.get(size_url)
    response.raise_for_status()
    if response.status_code == 200:
        return float(response.text)
    else:
        return 60.8
def download_file(url, dest_folder, file_size):
    filename = "pc-stat-bot_latest.zip"
    filepath = os.path.join(dest_folder, filename)
    start_time = time.time()
    downloaded_size = 0
    download_speed = 0
    dpg.set_value("download_label", f"starting the download from {url}")
    with requests.get(url, stream=True) as r, open(filepath, 'wb') as file:
        for chunk in r.iter_content(chunk_size=1024):
            size = file.write(chunk)
            downloaded_size += size
            elapsed_time = time.time() - start_time
            download_speed = downloaded_size / elapsed_time if elapsed_time > 0 else 0
            dpg.set_item_label("download_label", f"{elapsed_time:.2f}sec | {(downloaded_size/1024/1024):.2f}/{file_size:.2f}MB | {(download_speed/1024/1024):.2f}MB/s")
            dpg.set_value("download_progress", (downloaded_size/1024/1024) / file_size / 1.1)
    
    return filepath
def unzip_file(filepath, dest_folder):
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
def main():
    global extract_folder
    dpg.set_item_label("install_button", " ")
    dpg.set_item_callback("install_button", passed_func)
    dpg.hide_item("download_label_latest_ver")
    dpg.show_item("download_progress")
    file_size_url = "https://raw.githubusercontent.com/Agzes/Pc-Stat-Bot/main/Installer/size" 
    file_url = "https://agzes.netlify.app/pc-stat-bot/pc-stat-bot_latest.zip"
    download_folder = ""
    extract_folder = "./pc-stat-bot"
    dpg.set_item_label("download_label", "receive file size")
    file_size = get_file_size(file_size_url)
    dpg.set_item_label("download_label", f'"pc-stat-bot_latest.zip" size: {file_size}')
    dpg.set_item_label("download_label", "starting the download")
    zip_filepath = download_file(file_url, download_folder, file_size)
    dpg.set_item_label("download_label", "downloaded")
    dpg.set_item_label("download_label", "unzipping")
    unzip_file(zip_filepath, extract_folder)
    dpg.set_item_label("download_label", "unzipped")
    dpg.set_value("download_progress", 1)
    dpg.set_item_label("download_label", 'deleting "pc-stat-bot_latest.zip"')
    dpg.set_item_label("download_label", 'Installed!')
    os.remove(zip_filepath)


    dpg.set_item_label("install_button", "Close")
    dpg.set_item_callback("install_button", close)
def passed_func():pass
def mouse_drag_callback(_, app_data):
    if is_menu_bar_clicked:
        _, drag_delta_x, drag_delta_y = app_data
        viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
        new_pos_x = viewport_pos_x + drag_delta_x
        new_pos_y = max(viewport_pos_y + drag_delta_y, 0)
        dpg.set_viewport_pos([new_pos_x, new_pos_y])
def mouse_click_callback():
    global is_menu_bar_clicked
    is_menu_bar_clicked = True if dpg.get_mouse_pos(local=False)[1] < 300 else False
with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)
    dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)
def _help(message):
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text("[i]", color=[255, 255, 255])
    with dpg.tooltip(t):
        dpg.add_text(message)
def Init_After_UI_Init():
    " BLUR ON "
    window_effect.setAeroEffect(get_hwnd())
    window_effect.setRoundedCorners(get_hwnd(), 10)
    " TRANSPARENT VIEWPORT "
    dwm = ctypes.windll.dwmapi
    margins = MARGINS(-1, -1, -1, -1)
    dwm.DwmExtendFrameIntoClientArea(get_hwnd(), margins) 
    threading.Thread(target=check_for_latest_ver).start()
def check_for_latest_ver():
    url = 'https://raw.githubusercontent.com/Agzes/Pc-Stat-Bot/main/version.txt'
    response = requests.get(url)
    if response.status_code == 200:
        response.text
        dpg.set_item_label("download_label_latest_ver", f"Last Version: {response.text}")
with dpg.theme() as transparent_button_for_text_in_center:
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
with dpg.theme() as border_with_transparent_button_for_text_element:
    with dpg.theme_component():
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, [25, 25, 25, 100])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [40,40,40,100])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [100,100,100,100])
with dpg.theme() as border_to_element:
    with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
with dpg.window(label="Pc-Stat-Bot", pos=(0,0), height=300, width=500, no_title_bar=True, no_resize=True, no_close=True, tag="UI", no_background=False, no_move=True, show=True, no_scroll_with_mouse=True, no_scrollbar=True):
    with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True, width=454):
        dpg.add_button(label="[Beta V4] Pc-Stat-Bot | Installer [v.1.0.1]",  pos=(7,2), width=440)
        dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
    dpg.add_button(label="x",  pos=(467,8), width=25, height=25, callback=close)
    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
    with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True,  pos=(7,115)):
        dpg.add_button(label="Click on the button below to install Pc-Stat-Bot",  pos=(7,2), width=456, tag="download_label")
        dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)

    with dpg.child_window(height=25, no_scrollbar=True, no_scroll_with_mouse=True,  pos=(7,145)):
        dpg.add_button(label="Last Version: loading",  pos=(7,2), width=456, tag="download_label_latest_ver")
        dpg.bind_item_theme(dpg.last_item(), transparent_button_for_text_in_center)
    dpg.add_progress_bar(default_value=0,height=25,width=484, show=False,  pos=(7,145), tag="download_progress")
    dpg.bind_item_theme(dpg.last_item(), border_to_element)
    dpg.add_button(label="Install", tag="install_button", pos=(7,267), width=485, height=25, callback=lambda: threading.Thread(target=main).start())
    dpg.bind_item_theme(dpg.last_item(), border_with_transparent_button_for_text_element)
dpg.bind_theme(dpg_theme.initialize())
dpg.set_frame_callback(20, Init_After_UI_Init)
dpg.create_viewport(title="Pc-Stat-Bot | Installer", width=500, height=300, decorated=False, resizable=False, clear_color=[0, 0, 0, 0])
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg_animator.run()
    dpg_animations.update()
    dpg.render_dearpygui_frame()
dpg.destroy_context()