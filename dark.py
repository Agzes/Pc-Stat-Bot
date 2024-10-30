""" ----------------------------- """
""" ---- BETA V4 PC-STAT-BOT ---- """
""" ----------------------------- """

import threading
import g4f
import subprocess
import pyautogui
import webbrowser
import os
import playsound
import time as time
from g4f import client
from lang.load import load_dark_translation

@staticmethod
def darksoundaction():
    playsound.playsound("Data\\sound\\dark-action.mp3")



class func_for_dark:
    def play_pause_track():
        pyautogui.press('playpause')
        darksoundaction()
    def screen_shot():
        SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshots')
        screenshot_path = os.path.join(SCREENSHOT_DIR, 'screenshot_temp.png')
        pyautogui.screenshot(screenshot_path)
        new_file_name = os.path.join(SCREENSHOT_DIR, f"screenshot_{int(time.time())}.png")
        os.rename(screenshot_path, new_file_name)
        darksoundaction()
    def next_track():
        pyautogui.press('nexttrack')
        darksoundaction()
    def prev_track():
        pyautogui.press('prevtrack')
        darksoundaction()
    def open_browser():
        webbrowser.open("https://www.google.com")
        darksoundaction()
    def click_enter():
        pyautogui.press('enter')
        darksoundaction()
    def open_facebook():
        webbrowser.open("https://www.facebook.com")
        darksoundaction()
    def open_yandex():
        webbrowser.open("https://yandex.com")
        darksoundaction()
    def open_twitter():
        webbrowser.open("https://twitter.com")
        darksoundaction()
    def open_instagram():
        webbrowser.open("https://www.instagram.com")
        darksoundaction()
    def open_amazon():
        webbrowser.open("https://www.amazon.com")
        darksoundaction()
    def open_netflix():
        webbrowser.open("https://www.netflix.com")
        darksoundaction()
    def open_reddit():
        webbrowser.open("https://www.reddit.com")
        darksoundaction()
    def open_whatsapp():
        webbrowser.open("https://www.whatsapp.com")
        darksoundaction()
    def open_pinterest():
        webbrowser.open("https://www.pinterest.com")
        darksoundaction()
    def open_vk():
        webbrowser.open("https://vk.com")
        darksoundaction()
    def open_spotify():
        webbrowser.open("https://www.spotify.com")
        darksoundaction()
    def open_sound_cloud():
        webbrowser.open("https://soundcloud.com")
        darksoundaction()
    def open_twitch():
        webbrowser.open("https://www.twitch.tv")
        darksoundaction()
    def open_google():
        webbrowser.open("https://www.google.com")
        darksoundaction()
    def open_youtube():
        webbrowser.open("https://www.youtube.com")
        darksoundaction()
    def click_left():
        pyautogui.leftClick()
        darksoundaction()
    def click_right():
        pyautogui.rightClick()
        darksoundaction()
    def show_desktop():
        pyautogui.hotkey('win', 'd')
        darksoundaction()
    def show_explorer():
        subprocess.call('explorer')
        darksoundaction()
    def close_window():
        pyautogui.hotkey('alt', 'f4')
        darksoundaction()
    def hibernation_pc():
        darksoundaction()
        subprocess.call('shutdown /h')
    def restart_pc():
        darksoundaction()
        subprocess.call('shutdown /r /t 0')
    def shut_down_pc():
        darksoundaction()
        subprocess.call('shutdown /l')
    def copy_text():
        pyautogui.hotkey('ctrl', 'c')
        darksoundaction()
    def paste_text():
        pyautogui.hotkey('ctrl', 'v')
        darksoundaction()
    def all_text():
        pyautogui.hotkey('ctrl', 'a')
        darksoundaction()
    def youtube_pause():
        pyautogui.press('space')
        darksoundaction()
    def youtube_mute():
        pyautogui.press('m')
        darksoundaction()
    def youtube_fullscreen():
        pyautogui.press('f')
        darksoundaction()
    def youtube_right():
        pyautogui.press('right')
        darksoundaction()
    def youtube_left():
        pyautogui.press('left')
        darksoundaction()
    def youtube_subtiter():
        pyautogui.press('c')
        darksoundaction()
    def press_backspace():
        pyautogui.press('backspace')
        darksoundaction()
    def launch_app_a(locate):
        subprocess.Popen(locate)
    def open_site(site):
        webbrowser.open(site)
    def cmd_command(command):
        subprocess.call("command")
    def dark_ai_answer(command):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{command}"}],
            provider=g4f.Provider.DuckDuckGo,
        )   
        mesage = response.choices[0].message.content

def dark_answer(command, lang, itsvoice=False, plugin_ai=False):
    dark_translates = load_dark_translation(lang)
    command = command.lower()
    if "dark" in command or itsvoice is False:
        dark_check_ = False
        if plugin_ai is True and any(keyword in command for keyword in ("ai","ии")):
            playsound.playsound("Data\\sound\\dark-request.mp3")
            return command
        if any(keyword in command for keyword in ("привет","hi","hello")):
            dark_check_ = True
            return dark_translates["hi"]
        if any(keyword in command for keyword in ("пока","bye","goodbye")):
            dark_check_ = True
            return dark_translates["bye"]
        if any(keyword in command for keyword in ("пауза","stop","pause","start","turn","disable","enable","включи","останови")):
            threading.Thread(target=func_for_dark.play_pause_track).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("назад","back","last","past","прошлый")):
            threading.Thread(target=func_for_dark.prev_track).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("следующий","next","вперёд")):
            threading.Thread(target=func_for_dark.next_track).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("cкрин", "скриншот", "screen", "screenshot", "снимок")):
            threading.Thread(target=func_for_dark.screen_shot).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("вк", "vk", "вконтакте")):
            threading.Thread(target=func_for_dark.open_vk).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("браузер", "browser")):
            threading.Thread(target=func_for_dark.open_browser).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("твич", "twitch", "твитч")):
            threading.Thread(target=func_for_dark.open_twitch).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("соунд", "клауд", "sound", "cloud")):
            threading.Thread(target=func_for_dark.open_sound_cloud).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("спотифай", "spotify")):
            threading.Thread(target=func_for_dark.open_spotify).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("пинтерест", "pinterest")):
            threading.Thread(target=func_for_dark.open_pinterest).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("whatsapp", "ватсап")):
            threading.Thread(target=func_for_dark.open_whatsapp).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("facebook", "фейсбук")):
            threading.Thread(target=func_for_dark.open_facebook).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("yandex", "яндекс")):
            threading.Thread(target=func_for_dark.open_yandex).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("instagram", "инстаграмм", "инста")):
            threading.Thread(target=func_for_dark.open_instagram).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("amazon", "амазон")):
            threading.Thread(target=func_for_dark.open_amazon).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("netflix", "нетфликс")):
            threading.Thread(target=func_for_dark.open_netflix).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("reddit", "редит", "реддит")):
            threading.Thread(target=func_for_dark.open_reddit).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("google", "гугл")):
            threading.Thread(target=func_for_dark.open_google).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("youtube", "ютуб")):
            threading.Thread(target=func_for_dark.open_youtube).start()   
            dark_check_ = True
            return "processed_status_200"   
        if any(keyword in command for keyword in ("enter", "ентер")):
            threading.Thread(target=func_for_dark.click_enter).start()      
            dark_check_ = True
            return "processed_status_200"
        elif any(keyword in command for keyword in ("backspace")):
            threading.Thread(target=func_for_dark.press_backspace).start()   
            dark_check_ = True
            return "processed_status_200" 
        elif any(keyword in command for keyword in ("нажми", "click", "button")) and any(keyword in command for keyword in ("пкм","правая","right","правой")):
            threading.Thread(target=func_for_dark.click_right).start()   
            dark_check_ = True
            return "processed_status_200"
        elif any(keyword in command for keyword in ("нажми", "click", "button")) and any(keyword in command for keyword in ("лкм", "левая","left", "левой")):
            threading.Thread(target=func_for_dark.click_left).start()     
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("show", "покажи")) and any(keyword in command for keyword in ("рабочий","desktop","стол")):
            threading.Thread(target=func_for_dark.show_desktop).start()   
            dark_check_ = True
            return "processed_status_200"
        elif any(keyword in command for keyword in ("сверни", "minimize")) and any(keyword in command for keyword in ("окна","windows","window","all","все")):
            threading.Thread(target=func_for_dark.show_desktop).start()   
            dark_check_ = True
            return "processed_status_200"  
        if any(keyword in command for keyword in ("проводник","explorer","finder","files","файлы")):
            threading.Thread(target=func_for_dark.show_explorer).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("закрой", "close")) and any(keyword in command for keyword in ("окно","windows","window","program","app","программу","приложение")):
            threading.Thread(target=func_for_dark.close_window).start()     
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("спящий","гибернации","гибернация","сна","сон","hibernation","sleep")):
            threading.Thread(target=func_for_dark.hibernation_pc).start()   
            dark_check_ = True
            return "processed_status_200" 
        if any(keyword in command for keyword in ("пк","компьютер","computer","pc")) and any(keyword in command for keyword in ("перезагрузи", "перезагрузка", "reboot")):
            threading.Thread(target=func_for_dark.restart_pc).start()    
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("пк","компьютер","computer","pc")) and any(keyword in command for keyword in ("выключи","выключение","завершение работы","turn off","shutdown")):
            threading.Thread(target=func_for_dark.shut_down_pc).start()     
            dark_check_ = True
            return "processed_status_200"  
        if any(keyword in command for keyword in ("скопируй", "копировать", "копируй", "copy")):
            threading.Thread(target=func_for_dark.copy_text).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("вставить", "вставляй", "paste")):
            threading.Thread(target=func_for_dark.paste_text).start()
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("беззвук", "без звук", "без звука", "mute","unmute")):
            threading.Thread(target=func_for_dark.youtube_mute).start() 
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("экран", "screen", "fullscreen")) and  any(keyword in command for keyword in ("полный","fullscreen","full","полноэкранный","весь")):
            threading.Thread(target=func_for_dark.youtube_fullscreen).start()   
            dark_check_ = True
            return "processed_status_200"
        if any(keyword in command for keyword in ("субтитры", "subtitles")) and  any(keyword in command for keyword in ("включи","выключи","покажи","спрячь","отобрази","turn on","turn off","show","hide","display")):
            threading.Thread(target=func_for_dark.youtube_subtiter).start()   
            dark_check_ = True
            return "processed_status_200"   
        if any(keyword in command for keyword in ("перемотай", "rewind")) and any(keyword in command for keyword in ("дальше","next")):
            threading.Thread(target=func_for_dark.youtube_left).start()   
            dark_check_ = True
            return "processed_status_200"  
        if any(keyword in command for keyword in ("перемотай", "rewind")) and any(keyword in command for keyword in ("назад","back")):
            threading.Thread(target=func_for_dark.youtube_right).start()
            dark_check_ = True
            return "processed_status_200"
        else:
            if itsvoice is False:
                return dark_translates["not_recognized"]
    else:
        return "null_status_200"
