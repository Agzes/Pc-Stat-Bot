""" ----------------------------- """
""" ---- BETA V4 PC-STAT-BOT ---- """
""" ----------------------------- """

import g4f.Provider
import g4f.providers
import telebot 
import os
import json
import time as time
from libs.sys_info.sys_info import get_system_info
from libs.addons.keyboards import keyboard_click
import subprocess
import ctypes
import keyboard as keyboard
import pyautogui
import psutil
import g4f
from g4f.client import Client
from telebot import types
import threading
from lang.load import load_translation
g4f.debug.version_check = False
def load_from_json(filename):
    with open(filename, 'r') as json_file:
        DATAfromCFG = json.load(json_file)
    return DATAfromCFG
def get_current_keyboard_language():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    hwnd = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(hwnd, None)
    klid = user32.GetKeyboardLayout(thread_id)
    lid = klid & 0xFFFF
    return lid
def get_language_name(lid):
    lang_map = {
        0x0419: "RU",  
        0x0409: "EN",  
        0x0809: "EN",  
    }
    return lang_map.get(lid, "Unknown")

class telegram_bot:
    def __init__(self):
        threading.Thread(target=self.start).start()

    def start(self):
        self.tot_msg = 0
        self.msg = [] 
        data_for_bot_init = load_from_json("Config/main_data.json")
        try:
            self.main_language = data_for_bot_init["main"]["main_language"]
        except:   
            pass
        main_translations,translations,parameters = load_translation(self.main_language)
        self.translations = translations
        self.send_data(translations["main"]["initialization"], "status")
        self.send_data(translations["main"]["checking_data"], "info") 
        self.client = Client()
        try:
            self.main_name = data_for_bot_init["main"]["main_name"]
        except:   
            pass
        try:
            self.main_token = data_for_bot_init["main"]["main_token"]
        except:   
            pass
        try:
            self.main_id = data_for_bot_init["main"]["main_id"]
        except:   
            pass
        try:
            self.main_login = data_for_bot_init["main"]["main_login"]
        except:   
            pass
        try:
            self.main_password = data_for_bot_init["main"]["main_password"]
        except:   
            pass
        try:
            self.main_language = data_for_bot_init["main"]["main_language"]
        except:   
            pass
        try:
            self.ai_function_for_telegram = data_for_bot_init["plugins"]["telegram"]["ai_function_for_telegram"]
        except:   
            pass
        try:
            self.mouse_move_for_telegram = data_for_bot_init["plugins"]["telegram"]["mouse_move_for_telegram"]
        except:   
            pass
        try:
            self.keyboard_move_for_telegram = data_for_bot_init["plugins"]["telegram"]["keyboard_move_for_telegram"]
        except:   
            pass
        try:
            self.data_function_for_telegram = data_for_bot_init["plugins"]["telegram"]["data_function_for_telegram"]
        except:   
            pass
        
        self.send_data(translations["main"]["entering_data"], "info") 
        self.authorized_ids = [int(self.main_id)]
        self.bot = telebot.TeleBot(self.main_token)
        lang = self.main_language

        

        self.send_data(translations["main"]["init_keyboard0"], "info") 
        self.main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        main_bot = types.KeyboardButton(translations["keyboards"]["main_keyboard"]["bot_management"])
        main_music = types.KeyboardButton(translations["keyboards"]["main_keyboard"]["music_management"])
        main_video = types.KeyboardButton(translations["keyboards"]["main_keyboard"]["video_management"])
        main_volume = types.KeyboardButton(translations["keyboards"]["main_keyboard"]["sound_management"])
        main_pc = types.KeyboardButton(translations["keyboards"]["main_keyboard"]["pc_management"])
        main_plugin = types.KeyboardButton(translations["keyboards"]["main_keyboard"]["plugins"])
        self.main_keyboard.row(main_bot)
        self.main_keyboard.row(main_music)
        self.main_keyboard.row(main_video)
        self.main_keyboard.row(main_volume)
        self.main_keyboard.row(main_pc)
        self.main_keyboard.row(main_plugin)
        self.bot.send_message(self.main_id, translations["main"]["greetings"].format(name=self.main_name), reply_markup=self.main_keyboard)
        self.bot_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        bot_control_info = types.KeyboardButton(translations["keyboards"]["bot_control_keyboard"]["information"])
        bot_control_off = types.KeyboardButton(translations["keyboards"]["bot_control_keyboard"]["shutdown"])
        bot_control_back = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back_to_main"])
        self.bot_control_keyboard.row(bot_control_info)
        self.bot_control_keyboard.row(bot_control_off)
        self.bot_control_keyboard.row(bot_control_back)
        self.send_data(translations["main"]["init_keyboard1"], "info") 
        self.music_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        music_control_back = types.KeyboardButton('⏮️')
        music_control_pause_play = types.KeyboardButton('⏯️')
        music_control_next = types.KeyboardButton('⏭️')
        music_control_back_kb = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back_to_main"])
        self.music_control_keyboard.row(music_control_back, music_control_pause_play, music_control_next)
        self.music_control_keyboard.row(music_control_back_kb)
        self.send_data(translations["main"]["init_keyboard2"], "info") 
        self.video_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        video_control_back = types.KeyboardButton('⏪')
        video_control_pause_play = types.KeyboardButton('⏸▶️')
        video_control_next = types.KeyboardButton('⏩')
        video_control_back_kb = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back_to_main"])
        self.video_control_keyboard.row(video_control_back, video_control_pause_play, video_control_next)
        self.video_control_keyboard.row(video_control_back_kb)
        self.send_data(translations["main"]["init_keyboard3"], "info") 
        self.volume_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        volume_control_minus = types.KeyboardButton('🔉')
        volume_control_off_on = types.KeyboardButton('🔇')
        volume_control_plus = types.KeyboardButton('🔊')
        volume_control_back_kb = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back_to_main"])
        self.volume_control_keyboard.row(volume_control_minus, volume_control_off_on, volume_control_plus)
        self.volume_control_keyboard.row(volume_control_back_kb)
        self.send_data(translations["main"]["init_keyboard4"], "info") 
        self.pc_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        
        pc_control_sleep = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["hibernation"])
        pc_control_shutdown = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["shutdown"])
        pc_control_restart = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["reboot"])

        pc_control_block = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["lock"])
        pc_control_info = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["statistics"])
        pc_control_explorer = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["explorer"])

        pc_control_close_wd = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["close_window"])
        pc_control_screenshot = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["screenshot"])
        pc_control_collapse_all = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["collapse_all"])

        pc_control_enter = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["enter"])
        pc_control_battery = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["battery"])
        pc_control_basket_clean = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["clear_cart"])

        pc_control_test = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["list_of_program"])

        pc_control_back = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back_to_main"])
        self.pc_control_keyboard.row(pc_control_sleep, pc_control_shutdown, pc_control_restart)
        self.pc_control_keyboard.row(pc_control_block, pc_control_info, pc_control_screenshot)
        self.pc_control_keyboard.row(pc_control_enter, pc_control_close_wd, pc_control_collapse_all)
        self.pc_control_keyboard.row(pc_control_explorer, pc_control_battery, pc_control_basket_clean)
        self.pc_control_keyboard.row(pc_control_test, pc_control_back)

        self.plugin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        if self.keyboard_move_for_telegram is True:
            self.send_data(translations["main"]["init_keyboard5"], "info") 
            plugin_keyboard_1 = types.KeyboardButton(translations["keyboards"]["plugin_keyboard"]["keyboard"])
            self.plugin_keyboard.row(plugin_keyboard_1)
        if self.mouse_move_for_telegram is True:
            self.send_data(translations["main"]["init_keyboard6"], "info") 
            plugin_keyboard_2 = types.KeyboardButton(translations["keyboards"]["plugin_keyboard"]["mouse"])
            self.plugin_keyboard.row(plugin_keyboard_2)
        if self.data_function_for_telegram is True:
            self.send_data(translations["main"]["init_keyboard7"], "info") 
            plugin_keyboard_3 = types.KeyboardButton(translations["keyboards"]["plugin_keyboard"]["data"])
            self.plugin_keyboard.row(plugin_keyboard_3)
        if self.ai_function_for_telegram is True:
            self.send_data(translations["main"]["init_keyboard8"], "info") 
            plugin_keyboard_4 = types.KeyboardButton(translations["keyboards"]["plugin_keyboard"]["ai"])
            self.plugin_keyboard.row(plugin_keyboard_4)

        plugin_keyboard_back = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back_to_main"])
        self.plugin_keyboard.row(plugin_keyboard_back)
        if self.mouse_move_for_telegram is True:
            self.mouse_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            mouse_control_keyboard_left = types.KeyboardButton('⬅️')
            mouse_control_keyboard_left_top = types.KeyboardButton('↖️')
            mouse_control_keyboard_top = types.KeyboardButton('⬆️')
            mouse_control_keyboard_right_top = types.KeyboardButton('↗️')
            mouse_control_keyboard_right = types.KeyboardButton('➡️')
            mouse_control_keyboard_right_bottom = types.KeyboardButton('↘️')
            mouse_control_keyboard_bottom = types.KeyboardButton('⬇️')
            mouse_control_keyboard_left_bottom = types.KeyboardButton('↙️')
            mouse_control_keyboard_click = types.KeyboardButton('⏺️')
            mouse_control_keyboard_screenshot = types.KeyboardButton(translations["keyboards"]["pc_keyboard"]["screenshot"])
            mouse_control_keyboard_click_left = types.KeyboardButton(translations["keyboards"]["mouse_keyboard"]["click_left"])
            mouse_control_keyboard_click_right = types.KeyboardButton(translations["keyboards"]["mouse_keyboard"]["click_right"]) 
            mouse_control_keyboard_back = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back"])
            self.mouse_control_keyboard.row(mouse_control_keyboard_left_top, mouse_control_keyboard_top,mouse_control_keyboard_right_top)
            self.mouse_control_keyboard.row(mouse_control_keyboard_left, mouse_control_keyboard_click,mouse_control_keyboard_right)
            self.mouse_control_keyboard.row(mouse_control_keyboard_left_bottom, mouse_control_keyboard_bottom,mouse_control_keyboard_right_bottom)
            self.mouse_control_keyboard.row(mouse_control_keyboard_click_left, mouse_control_keyboard_click_right)
            self.mouse_control_keyboard.row(mouse_control_keyboard_screenshot)
            self.mouse_control_keyboard.row(mouse_control_keyboard_back)
        if self.keyboard_move_for_telegram is True:
            self.kb_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            keys = [
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                'z', 'x', 'c', 'v', 'b', 'n', 'm',
                'space',
                translations["keyboards"]["plugin_keyboard_keyboard"]["write"], translations["keyboards"]["pc_keyboard"]["screenshot"],
                translations["keyboards"]["plugin_keyboard_keyboard"]["change_language"],
                '{', '|', '}', '!', '"', '#', '$', '%',
                '&', "'", '*', '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>', '?', '@', '[',
                ']', '^', '_', '`', '~', '(', ')',
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
                'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
                'num0', 'num1', 'num2', 'num3', 'num4',
                'num5', 'num6', 'num7', 'num8', 'num9',
                'alt', 'altleft', 'altright', 'capslock',
                'ctrl', 'ctrlleft', 'ctrlright', 'del',
                'delete', 'down', 'end', 'enter', 'esc',
                'fn', 'home', 'insert', 'left', 'pagedown',
                'pageup', 'printscreen', 'right',
                'shift', 'shiftleft', 'shiftright', 'space',
                'stop', 'up', 'win', 'scrolllock',
            ]

            keyboard_buttons = [types.KeyboardButton(key) for key in keys]
            keyboard_rows = []
            row = []
            row_count = [10, 10, 9, 7, 1, 3, 1, 8, 8, 8, 7, 6, 6, 5, 5, 4, 4, 5, 4, 4, 4, 4]
            current_row_index = 0

            for button in keyboard_buttons:
                row.append(button)
                if len(row) == row_count[current_row_index]:
                    keyboard_rows.append(row)
                    row = []
                    current_row_index = (current_row_index + 1) % len(row_count)

            if row:
                keyboard_rows.append(row)

            for i, row in enumerate(keyboard_rows):
                if i == 3:
                    padding_left = '   '
                    padding_right = '   '
                    modified_row = [types.KeyboardButton(padding_left)] + row + [types.KeyboardButton(padding_right)]
                    self.kb_control_keyboard.row(*modified_row)
                else:
                    self.kb_control_keyboard.row(*row)

            kb_control_keyboard_BACK = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back"])
            self.kb_control_keyboard.row(kb_control_keyboard_BACK)

            self.kb_control_keyboard_rus = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            keys = [
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',
                'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',
                'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'ю',
                'space',
                translations["keyboards"]["plugin_keyboard_keyboard"]["write"], translations["keyboards"]["pc_keyboard"]["screenshot"],
                translations["keyboards"]["plugin_keyboard_keyboard"]["change_language"],
                '{', '|', '}', '!', '"', '#', '$', '%',
                '&', "'", '*', '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>', '?', '@', '[',
                ']', '^', '_', '`', '~', '(', ')',
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
                'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
                'num0', 'num1', 'num2', 'num3', 'num4',
                'num5', 'num6', 'num7', 'num8', 'num9',
                'alt', 'altleft', 'altright', 'capslock',
                'ctrl', 'ctrlleft', 'ctrlright', 'del',
                'delete', 'down', 'end', 'enter', 'esc',
                'fn', 'home', 'insert', 'left', 'pagedown',
                'pageup', 'printscreen', 'right',
                'shift', 'shiftleft', 'shiftright', 'space',
                'stop', 'up', 'win', 'scrolllock',
            ]

            keyboard_buttons = [types.KeyboardButton(key) for key in keys]
            keyboard_rows = []
            row = []
            row_count = [10, 12, 11, 8, 1, 3, 1, 8, 8, 8, 7, 6, 6, 5, 5, 4, 4, 5, 4, 4, 4, 4]
            current_row_index = 0

            for button in keyboard_buttons:
                row.append(button)
                if len(row) == row_count[current_row_index]:
                    keyboard_rows.append(row)
                    row = []
                    current_row_index = (current_row_index + 1) % len(row_count)

            if row:
                keyboard_rows.append(row)

            for i, row in enumerate(keyboard_rows):
                if i == 3:
                    padding_left = '   '
                    padding_right = '   '
                    modified_row = [types.KeyboardButton(padding_left)] + row + [types.KeyboardButton(padding_right)]
                    self.kb_control_keyboard_rus.row(*modified_row)
                else:
                    self.kb_control_keyboard_rus.row(*row)

            kb_control_keyboard_rus_BACK = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back"])
            self.kb_control_keyboard_rus.row(kb_control_keyboard_BACK)

            self.kb_control_keyboard_inkog = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            kb_control_keyboard_inkog_change = types.KeyboardButton(translations["keyboards"]["plugin_keyboard_keyboard"]["change_language"])
            kb_control_keyboard_inkog_back = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back"])
            self.kb_control_keyboard_inkog.row(kb_control_keyboard_inkog_change)
            self.kb_control_keyboard_inkog.row(kb_control_keyboard_inkog_back)
        if self.data_function_for_telegram is True:
            self.data_tools_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            data_tools_keyboard_disk = types.KeyboardButton(translations["keyboards"]["data_keyboards"]["files"])
            data_tools_keyboard_upload = types.KeyboardButton(translations["keyboards"]["data_keyboards"]["download"])
            data_tools_keyboard_download = types.KeyboardButton(translations["keyboards"]["data_keyboards"]["upload"])
            data_tools_keyboard_back = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back"])
            self.data_tools_keyboard.row(data_tools_keyboard_disk)
            self.data_tools_keyboard.row(data_tools_keyboard_upload)
            self.data_tools_keyboard.row(data_tools_keyboard_download)
            self.data_tools_keyboard.row(data_tools_keyboard_back)
        if self.ai_function_for_telegram is True:
            self.g4f_tool_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            g4f_tool_keyboard_respond = types.KeyboardButton(translations["keyboards"]["ai_keyboards"]["ask"])
            g4f_tool_keyboard_back = types.KeyboardButton(translations["keyboards"]["keyboard_need"]["back"])
            self.g4f_tool_keyboard.row(g4f_tool_keyboard_respond)
            self.g4f_tool_keyboard.row(g4f_tool_keyboard_back)
        self.send_data(translations["main"]["initialized"], "status")
        self.send_data(translations["main"]["initialization_command"], "info")
        @self.bot.message_handler(commands=['start'])
        def start(message):
            if message.from_user.id in self.authorized_ids:
                self.bot.send_message(self.main_id, translations["main"]["greetings"].format(name=self.main_name), reply_markup=self.main_keyboard)
            else:
                self.bot.send_message(message.chat.id, translations["main"]["log_in"])
                self.send_data(translations["main"]["warning"].format(id=message.from_user.id), "warning")
        @self.bot.message_handler(commands=['login'])
        def login(message):
            if message.from_user.id in self.authorized_ids:
                self.bot.send_message(message.chat.id, translations["main"]["already_login"])
            else:
                self.send_data(translations["main"]["checking_data_from_user"].format(id=message.from_user.id), "info")
                words = message.text.split()
                if len(words) >= 3:
                    login_check = words[1]
                    password_check = words[2]
                    if login_check == self.main_login and password_check == self.main_password:
                        self.authorized_ids.append(message.from_user.id)
                        self.send_data(translations["main"]["successful_login_terminal"].format(id=message.from_user.id), "info")
                        self.bot.send_message(message.chat.id,translations["main"]["successful_login"],reply_markup=self.main_keyboard)
                        return
                    else:
                        self.send_data(translations["main"]["incorrect_data"].format(id=message.from_user.id), "warning")
                        self.bot.send_message(message.chat.id,translations["main"]["incorrect_pass_or_login"])
                        return
                else:
                    self.send_data(translations["main"]["incorrect_data"].format(id=message.from_user.id), "warning")
                    self.bot.send_message(message.chat.id,translations["main"]["incorrect_no_data"])
                    return
        @self.bot.message_handler(commands=['off_bot'])
        def off(message):
            if message.from_user.id in self.authorized_ids:
                self.send_data("off_bot_and_program", "code")
                self.send_data(" ", "info")
        @self.bot.message_handler(commands=['shutdown'])
        def shutdown(message):
            if message.from_user.id in self.authorized_ids:
                self.send_data("off_bot_and_program_and_shutdown", "code")
                self.send_data(" ", "info")
        @self.bot.message_handler(commands=['hibernation'])
        def hibernate(message):
            if message.from_user.id in self.authorized_ids:
                self.send_data("off_bot_and_program_and_hibernate", "code")
                self.send_data(" ", "info")
        @self.bot.message_handler(commands=['reboot'])
        def reboot(message):
            if message.from_user.id in self.authorized_ids:
                self.send_data("off_bot_and_program_and_reboot", "code")
                self.send_data(" ", "info")

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            if call.message.chat.id in self.authorized_ids:
                if call.data[0] == 'Y':
                    self.send_data(translations["data_plugin"]["decided_download"].format(id=call.message.from_user.id), "info") 
                    file_path = call.data[1:]
                    if os.path.isfile(file_path):
                        with open(file_path, 'rb') as file:
                            self.bot.send_document(call.message.chat.id, file)
                elif call.data[0] == 'N':
                    self.send_data(translations["data_plugin"]["decided_not_download_terminal"].format(id=call.message.from_user.id), "info") 
                    self.bot.send_message(call.message.chat.id, translations["data_plugin"]["decided_not_download"])
                if call.data[0] == 'D':
                    self.send_data(translations["data_plugin"]["walks_in_directories"].format(id=call.message.from_user.id), "info", "info") 
                    dir_path = call.data[1:]
                    if os.path.isdir(dir_path):
                        markup = types.InlineKeyboardMarkup()
                        for item in os.listdir(dir_path):
                            item_path = os.path.join(dir_path, item)
                            if os.path.isdir(item_path):
                                markup.add(types.InlineKeyboardButton(text=item, callback_data='D' + item_path))
                            else:
                                markup.add(types.InlineKeyboardButton(text=item, callback_data='F' + item_path))
                        self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=translations["main"]["pc-stat-bot"],reply_markup=markup)
                elif call.data[0] == 'F':
                    self.send_data(translations["data_plugin"]["click_to_file"].format(id=call.message.from_user.id), "info") 
                    file_path = call.data[1:]
                    if os.path.isfile(file_path):
                        markup = types.InlineKeyboardMarkup()
                        markup.add(types.InlineKeyboardButton(text='👍', callback_data='Y' + file_path))
                        markup.add(types.InlineKeyboardButton(text='👎', callback_data='N'))
                        self.bot.send_message(call.message.chat.id,translations["data_plugin"]["click_to_file_terminal"],reply_markup=markup)
            else:
                self.bot.send_message(call.message.chat.id, translations["main"]["log_in"])
                self.send_data(translations["main"]["warning"].format(id=call.message.from_user.id), "warning")
        self.send_data(translations["main"]["command_initialized"], "status")


        @self.bot.message_handler(content_types=["text"])
        def msg(message):
            if message.from_user.id in self.authorized_ids:
                self.msg_callback(message)
                self.send_data(translations["main"]["interacting_processing"].format(id=message.from_user.id), "info", f"{message.from_user.id} | {message.text}") 
            else:
                self.bot.send_message(message.chat.id, translations["main"]["log_in"])
                self.send_data(translations["main"]["warning"].format(id=message.from_user.id), "warning", f"{message.from_user.id} | {message.text}")
                
        self.send_data(translations["main"]["bot_start"], "status")
        self.bot.infinity_polling()

    
    def send_data(self, text, status, desc=""):
        self.tot_msg += 1
        self.msg.append({'id': self.tot_msg, 'text': text, 'status': status, 'desc': desc})
    def get_data(self):
        return self.tot_msg, self.msg
    
    
    def open_mouse_keyboard(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.mouse_control_keyboard)
    def open_bot_management(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.bot_control_keyboard)
    def open_music_management(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.music_control_keyboard)
    def open_video_management(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.video_control_keyboard)
    def open_volume_management(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.volume_control_keyboard)
    def open_pc_management(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.pc_control_keyboard)
    def open_plugin_management(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.plugin_keyboard)
    def end_back_end(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.main_keyboard)
    def end_back_back(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.plugin_keyboard)
    def information(self, msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"])
    def shutdown_bot(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["sure_to_turn_off"])
    def prev_track(self,msg):
        pyautogui.press('prevtrack')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def next_track(self,msg):
        pyautogui.press('nexttrack')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def play_track(self,msg):
        pyautogui.press('playpause')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def left(self,msg):
        pyautogui.press('left')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def pause(self,msg):
        pyautogui.press('space')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def right(self,msg):
        pyautogui.press('right')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def volume_up(self,msg):
        pyautogui.press('volumeup')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def volume_down(self,msg):
        pyautogui.press('volumedown')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def mute(self,msg):
        pyautogui.press('volumemute')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def hibernation(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["sure_to_hibernate"])
    def restart(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["sure_to_reboot"])
    def shutdown(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["sure_to_shutdown"])
    def lock(self,msg):
        subprocess.call('Rundll32.exe user32.dll,LockWorkStation')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def statistic(self,msg):
        message_info_eng, message_info_rus = get_system_info()
        self.bot.send_message(msg.chat.id, message_info_rus if self.main_language == "ru" else message_info_eng)
    def explorer(self,msg):
        subprocess.call('explorer')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def altf4(self,msg):
        pyautogui.hotkey('alt', 'f4')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def screenshot(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshots')
        screenshot_path = os.path.join(SCREENSHOT_DIR, 'screenshot_temp.png')
        pyautogui.screenshot(screenshot_path)
        with open(screenshot_path, 'rb') as photo_file:
            self.bot.send_photo(msg.chat.id, photo_file)
    def collapse_all(self,msg):
        pyautogui.hotkey('win', 'd')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def enter(self, msg):
        pyautogui.press('enter')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
    def battery(self,msg):
        battery = psutil.sensors_battery()
        if battery is not None:
            self.bot.send_message(msg.chat.id, self.translations["main"]["battery_connected"])
            plugged = battery.power_plugged
            percent = battery.percent
            if plugged:
                self.bot.send_message(msg.chat.id, self.translations["main"]["power_connected"].format(data=str(percent)))
            else:
                self.bot.send_message(msg.chat.id, self.translations["main"]["power_not_connected"].format(data=str(percent)))
        else:
            self.bot.send_message(msg.chat.id, self.translations["main"]["battery_not_connected"])
    def clean_cart(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["emptying_trash"])
        os.system('rd /s /q %systemdrive%\\$Recycle.bin')
    def list_of_programs(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"])
        try:
            proc_list = []
            for proc in psutil.process_iter():
                if proc.name() not in proc_list:
                    proc_list.append(proc.name())
            processes = "\n".join(proc_list)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        self.bot.send_message(msg.chat.id, processes)
    def open_keyboard_panel(self,msg):
        lang_id = get_current_keyboard_language()
        language = get_language_name(lang_id)
        if language == "RU":
            self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.kb_control_keyboard_rus)
        elif language == "EN":
            self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.kb_control_keyboard)
        else:
            self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.kb_control_keyboard_inkog)
    def change_language(self,msg):
        pyautogui.hotkey('alt', 'shift')
        self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        self.open_keyboard_panel(msg)
    def write_text(self, msg):
        text_variable = msg.text
        keyboard.write(text_variable)
        self.bot.send_message(msg.chat.id, self.translations["main"]["write_text"].format(data=text_variable))
    def write(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["write_under"])
        self.bot.register_next_step_handler(msg, self.write_text)
    def files(self,msg):
        markup = types.InlineKeyboardMarkup()
        disks = os.popen('wmic logicaldisk get caption').read().split()[1:]
        for disk in disks:
            markup.add(types.InlineKeyboardButton(text=disk, callback_data='D' + disk))
        self.bot.send_message(msg.chat.id, self.translations["main"]["select_disk"],reply_markup=markup)
    def dwnload(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["write_path_to_file"])
        self.bot.register_next_step_handler(msg, self.download)
    def uplod(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["send_need_file"])
        self.bot.register_next_step_handler(msg, self.upload)
    def download(self,message):
        try:
            file_path = message.text
            if os.path.exists(file_path):
                self.bot.send_message(message.chat.id,self.translations["main"]["file_downloading"])
                file = open(file_path, 'rb')
                self.bot.send_document(message.chat.id, file)
            else:
                self.bot.send_message(message.chat.id,self.translations["main"]["incorrect_path_to_file"])
        except:   
            self.bot.send_message(message.chat.id,self.translations["main"]["incorrect_path_to_file"])
    def upload(self,message):
        try:
            file = self.bot.get_file(message.document.file_id)
            afile = self.bot.download_file(file.file_path)
            name = message.document.file_name
            with open(name, 'wb') as file_new:
                file_new.write(afile)
            self.bot.send_message(message.chat.id,self.translations["main"]["successful_download_file_in_pc_stat_bot"])
        except:   
            self.bot.send_message(message.chat.id,self.translations["main"]["error_send_file_as_doc"])
    def open_data_management_panel(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.data_tools_keyboard)
    def move_mouse(self,msg,move):
        if move == "⬅️":
            pyautogui.move(-50, 0, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        elif move == "↖️":
            pyautogui.move(-50, -50, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        elif move == "↗️":
            pyautogui.move(50, -50, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        elif move == "⬆️":
            pyautogui.move(0, -50, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        elif move == "↙️":
            pyautogui.move(-50, 50, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        elif move == "↘️":
            pyautogui.move(50, 50, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        elif move == "⬇️":
            pyautogui.move(0, 50, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
        elif move == "➡️":
            pyautogui.move(50, 0, duration=0)
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
            pyautogui.click()
        elif move == self.translations["keyboards"]["mouse_keyboard"]["click_right"]:
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
            pyautogui.rightClick()
        elif move == self.translations["keyboards"]["mouse_keyboard"]["click_left"]:
            self.bot.send_message(msg.chat.id, self.translations["main"]["successful"])
            pyautogui.leftClick()
    def go_to_ai_keyboard(self,msg):
        self.bot.send_message(msg.chat.id, self.translations["main"]["pc-stat-bot"], reply_markup=self.g4f_tool_keyboard)
    def ai_next(self,msg):
        self.bot.send_message(msg.chat.id,self.translations["main"]["send_your_request"])
        self.bot.register_next_step_handler(msg, self.aisteptwo)
    def aisteptwo(self,message):
        ques = message.text
        self.bot.send_message(message.chat.id,self.translations["main"]["processed_the_request"].format(data=self.ai(ques)))
    def ai(self,text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{text}"}]
        )
        mesage = response.choices[0].message.content
        return mesage

    def msg_callback(self, msg):
        self.bot.delete_message(msg.chat.id, msg.message_id)
        if msg.text == self.translations["keyboards"]["main_keyboard"]["bot_management"]: self.open_bot_management(msg) 
        elif msg.text == self.translations["keyboards"]["main_keyboard"]["music_management"]: self.open_music_management(msg) 
        elif msg.text == self.translations["keyboards"]["main_keyboard"]["video_management"]: self.open_video_management(msg) 
        elif msg.text == self.translations["keyboards"]["main_keyboard"]["sound_management"]: self.open_volume_management(msg) 
        elif msg.text == self.translations["keyboards"]["main_keyboard"]["pc_management"]: self.open_pc_management(msg) 
        elif msg.text == self.translations["keyboards"]["main_keyboard"]["plugins"]: self.open_plugin_management(msg) 
        elif msg.text == self.translations["keyboards"]["keyboard_need"]["back_to_main"]: self.end_back_end(msg) 
        elif msg.text == self.translations["keyboards"]["keyboard_need"]["back"]: self.end_back_back(msg) 
        elif msg.text == self.translations["keyboards"]["bot_control_keyboard"]["information"]: self.information(msg)
        elif msg.text == self.translations["keyboards"]["bot_control_keyboard"]["shutdown"]: self.shutdown_bot(msg)
        elif msg.text == "⏮️": self.prev_track(msg)
        elif msg.text == "⏯️": self.play_track(msg)
        elif msg.text == "⏭️": self.next_track(msg)
        elif msg.text == "⏪": self.left(msg)
        elif msg.text == "⏸▶️": self.pause(msg)
        elif msg.text == "⏩": self.right(msg)
        elif msg.text == "🔉": self.volume_down(msg)
        elif msg.text == "🔇": self.mute(msg)
        elif msg.text == "🔊": self.volume_up(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["hibernation"]: self.hibernation(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["shutdown"]: self.shutdown(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["reboot"]: self.restart(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["lock"]: self.lock(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["statistics"]: self.statistic(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["explorer"]: self.explorer(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["close_window"]: self.altf4(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["screenshot"]: self.screenshot(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["collapse_all"]: self.collapse_all(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["enter"]: self.enter(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["battery"]: self.battery(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["clear_cart"]: self.clean_cart(msg)
        elif msg.text == self.translations["keyboards"]["pc_keyboard"]["list_of_program"]: self.list_of_programs(msg)

        if self.mouse_move_for_telegram:
            if msg.text == self.translations["keyboards"]["plugin_keyboard"]["mouse"]: self.open_mouse_keyboard(msg)
            if msg.text == "⬅️": self.move_mouse(msg, "⬅️")
            elif msg.text == "↖️": self.move_mouse(msg, "↖️")
            elif msg.text == "⬆️": self.move_mouse(msg, "⬆️")
            elif msg.text == "↗️": self.move_mouse(msg, "↗️")
            elif msg.text == "➡️": self.move_mouse(msg, "➡️")
            elif msg.text == "↘️": self.move_mouse(msg, "↘️")
            elif msg.text == "⬇️": self.move_mouse(msg, "⬇️")
            elif msg.text == "↙️": self.move_mouse(msg, "↙️")
            elif msg.text == "⏺️": self.move_mouse(msg, "⏺️")
            elif msg.text == self.translations["keyboards"]["mouse_keyboard"]["click_left"]: self.move_mouse(msg, self.translations["keyboards"]["mouse_keyboard"]["click_left"])
            elif msg.text == self.translations["keyboards"]["mouse_keyboard"]["click_right"]: self.move_mouse(msg, self.translations["keyboards"]["mouse_keyboard"]["click_right"])
        if self.data_function_for_telegram:
            if msg.text == self.translations["keyboards"]["plugin_keyboard"]["data"]: self.open_data_management_panel(msg)
            if msg.text == self.translations["keyboards"]["data_keyboards"]["files"]: self.files(msg)
            elif msg.text == self.translations["keyboards"]["data_keyboards"]["download"]: self.dwnload(msg)
            elif msg.text == self.translations["keyboards"]["data_keyboards"]["upload"]: self.uplod(msg)
        if self.ai_function_for_telegram:
            if msg.text == self.translations["keyboards"]["plugin_keyboard"]["ai"]: self.go_to_ai_keyboard(msg)
            if msg.text == self.translations["keyboards"]["ai_keyboards"]["ask"]: self.ai_next(msg)
        if self.keyboard_move_for_telegram:
            if msg.text == self.translations["keyboards"]["plugin_keyboard"]["keyboard"]: self.open_keyboard_panel(msg)
            if msg.text == self.translations["keyboards"]["plugin_keyboard_keyboard"]["change_language"]: self.change_language(msg)
            if msg.text == self.translations["keyboards"]["plugin_keyboard_keyboard"]["write"]: self.write(msg)
            tmp_status = keyboard_click(msg.text)
            if tmp_status is False:
                pass
            else:
                self.bot.send_message(msg.chat.id,self.translations["main"]["successful_with_key"].format(tmp_status=tmp_status))
        self.send_data(self.translations["main"]["worked"].format(id=msg.from_user.id), "status")



