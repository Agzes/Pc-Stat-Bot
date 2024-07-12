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
        except:  # noqa: E722
            pass
        self.send_data("[Telegram BOT][Статус]: Инициализация" if self.main_language == "ru" else "[Telegram BOT][Status]: Initialization", "status")
        self.send_data("[Telegram BOT][Информация]: Проверяю ваши настройки" if self.main_language == "ru" else "[Telegram BOT][Information]: Checking your settings", "info") 
        self.client = Client()
        try:
            self.main_name = data_for_bot_init["main"]["main_name"]
        except:  # noqa: E722
            pass
        try:
            self.main_token = data_for_bot_init["main"]["main_token"]
        except:  # noqa: E722
            pass
        try:
            self.main_id = data_for_bot_init["main"]["main_id"]
        except:  # noqa: E722
            pass
        try:
            self.main_login = data_for_bot_init["main"]["main_login"]
        except:  # noqa: E722
            pass
        try:
            self.main_password = data_for_bot_init["main"]["main_password"]
        except:  # noqa: E722
            pass
        try:
            self.main_language = data_for_bot_init["main"]["main_language"]
        except:  # noqa: E722
            pass
        try:
            self.ai_function_for_telegram = data_for_bot_init["plugins"]["telegram"]["ai_function_for_telegram"]
        except:  # noqa: E722
            pass
        try:
            self.mouse_move_for_telegram = data_for_bot_init["plugins"]["telegram"]["mouse_move_for_telegram"]
        except:  # noqa: E722
            pass
        try:
            self.keyboard_move_for_telegram = data_for_bot_init["plugins"]["telegram"]["keyboard_move_for_telegram"]
        except:  # noqa: E722
            pass
        try:
            self.data_function_for_telegram = data_for_bot_init["plugins"]["telegram"]["data_function_for_telegram"]
        except:  # noqa: E722
            pass
        
        self.send_data("[Telegram BOT][Информация]: Вношу данные для бота" if self.main_language == "ru" else "[Telegram BOT][Information]: Entering data for the bot", "info") 
        self.autorizated_ids = [int(self.main_id)]
        self.bot = telebot.TeleBot(self.main_token)
        lang = self.main_language

        

        self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру [0/]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard [0/]", "info") 
        self.main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        main_bot = types.KeyboardButton('| 🕹️ Управление Ботом 🤖 |'if lang == "ru" else "| 🕹️ Bot Management 🤖 |")
        main_music = types.KeyboardButton('| 🕹️ Управление Музыкой 🎵 |'if lang == "ru" else "| 🕹️ Music Management 🎵 |")
        main_video = types.KeyboardButton('| 🕹️ Управление Видео 📼 |'if lang == "ru" else "| 🕹️ Video Management 📼 |")
        main_volume = types.KeyboardButton('| 🕹️ Управление Звуком 🔈 |'if lang == "ru" else "| 🕹️ Sound Management 🔈|")
        main_pc = types.KeyboardButton('| 🕹️ Управление ПК 🖥️ |'if lang == "ru" else "| 🕹️ PC Management 🖥️ |")
        main_plugin = types.KeyboardButton('| ➕ Плагины ➕ |'if lang == "ru" else "| ➕ Plugins ➕ |")
        self.main_keyboard.row(main_bot)
        self.main_keyboard.row(main_music)
        self.main_keyboard.row(main_video)
        self.main_keyboard.row(main_volume)
        self.main_keyboard.row(main_pc)
        self.main_keyboard.row(main_plugin)
        self.bot.send_message(self.main_id, f"| Pc-Stat-Bot | бета 4.0 |\nЗдравствуйте, {self.main_name}." if lang == "ru" else f"| Pc-Stat-Bot | beta 4.0 |\nHello, {self.main_name}.", reply_markup=self.main_keyboard)
        self.bot_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        bot_control_info = types.KeyboardButton('| ℹ️ Информация ℹ️ |'if lang == "ru" else "| ℹ️ Information ℹ️ |")
        bot_control_off = types.KeyboardButton('| 🔴 Выключение 🔴 |'if lang == "ru" else "| 🔴 Shutdown 🔴 |")
        bot_control_back = types.KeyboardButton('| 🔚 Назад 🔚 |'if lang == "ru" else "| 🔚 Back 🔚 |")
        self.bot_control_keyboard.row(bot_control_info)
        self.bot_control_keyboard.row(bot_control_off)
        self.bot_control_keyboard.row(bot_control_back)
        self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: управление музыкой [1/4]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: music management [1/4]", "info") 
        self.music_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        music_control_back = types.KeyboardButton('⏮️')
        music_control_pause_play = types.KeyboardButton('⏯️')
        music_control_next = types.KeyboardButton('⏭️')
        music_control_back_kb = types.KeyboardButton('| 🔚 Назад 🔚 |'if lang == "ru" else "| 🔚 Back 🔚 |")
        self.music_control_keyboard.row(music_control_back, music_control_pause_play, music_control_next)
        self.music_control_keyboard.row(music_control_back_kb)
        self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: управление видео [2/4]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: video management [2/4]", "info") 
        self.video_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        video_control_back = types.KeyboardButton('⏪')
        video_control_pause_play = types.KeyboardButton('⏸▶️')
        video_control_next = types.KeyboardButton('⏩')
        video_control_back_kb = types.KeyboardButton('| 🔚 Назад 🔚 |'if lang == "ru" else "| 🔚 Back 🔚 |")
        self.video_control_keyboard.row(video_control_back, video_control_pause_play, video_control_next)
        self.video_control_keyboard.row(video_control_back_kb)
        self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: управление звуком [3/4]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: volume management [3/4]", "info") 
        self.volume_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        volume_control_minus = types.KeyboardButton('🔉')
        volume_control_off_on = types.KeyboardButton('🔇')
        volume_control_plus = types.KeyboardButton('🔊')
        volume_control_back_kb = types.KeyboardButton('| 🔚 Назад 🔚 |'if lang == "ru" else "| 🔚 Back 🔚 |")
        self.volume_control_keyboard.row(volume_control_minus, volume_control_off_on, volume_control_plus)
        self.volume_control_keyboard.row(volume_control_back_kb)
        self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: управление ПК [4/4]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: PC management [4/4]", "info") 
        self.pc_control_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        
        pc_control_sleep = types.KeyboardButton('⚪Гибернация⚪' if lang == "ru" else "⚪Hibernation⚪")
        pc_control_shutdown = types.KeyboardButton('🔴Выключение🔴' if lang == "ru" else "🔴Shutdown🔴")
        pc_control_restart = types.KeyboardButton('⭕Перезагрузка⭕' if lang == "ru" else "⭕Reboot⭕")

        pc_control_block = types.KeyboardButton('🔒Блокировка🔒' if lang == "ru" else "🔒Lock🔒")
        pc_control_info = types.KeyboardButton('📊Статистика📊' if lang == "ru" else "📊Statistics📊")
        pc_control_explorer = types.KeyboardButton('📁Проводник📁' if lang == "ru" else "📁Explorer📁")

        pc_control_close_wd = types.KeyboardButton('❌Закрыть окно❌' if lang == "ru" else "❌Close window❌")
        pc_control_screenshot = types.KeyboardButton('🎦Скриншот🎦' if lang == "ru" else "🎦Screenshot🎦")
        pc_control_collapse_all = types.KeyboardButton('⬛Свернуть всё⬛' if lang == "ru" else "⬛Collapse all⬛")

        pc_control_enter = types.KeyboardButton('⏭Enter⏭' if lang == "ru" else "⏭Enter⏭")
        pc_control_battery = types.KeyboardButton('🔋Батарея🔋' if lang == "ru" else "🔋Battery🔋")
        pc_control_basket_clean = types.KeyboardButton('🗑️Очистить корзину🗑️' if lang == "ru" else "🗑️Clear cart🗑️")

        pc_control_test = types.KeyboardButton('📃Список программ📃' if lang == "ru" else "📃List of programs📃")

        pc_control_back = types.KeyboardButton('| 🔚 Назад 🔚 |'if lang == "ru" else "| 🔚 Back 🔚 |")
        self.pc_control_keyboard.row(pc_control_sleep, pc_control_shutdown, pc_control_restart)
        self.pc_control_keyboard.row(pc_control_block, pc_control_info, pc_control_screenshot)
        self.pc_control_keyboard.row(pc_control_enter, pc_control_close_wd, pc_control_collapse_all)
        self.pc_control_keyboard.row(pc_control_explorer, pc_control_battery, pc_control_basket_clean)
        self.pc_control_keyboard.row(pc_control_test, pc_control_back)

        self.plugin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        if self.keyboard_move_for_telegram is True:
            self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: [Плагин] Управление клавиатурой [5/8]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] KeyBoard management [5/8]", "info") 
            plugin_keyboard_1 = types.KeyboardButton('| ⌨️ Управление клавиатурой ⌨️ |'if lang == "ru" else "| ⌨️ KeyBoard management ⌨️ |")
            self.plugin_keyboard.row(plugin_keyboard_1)
        if self.mouse_move_for_telegram is True:
            self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: [Плагин] Управление мышкой [6/8]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] Mouse management [6/8]", "info") 
            plugin_keyboard_2 = types.KeyboardButton('| 🖱️ Управление мышкой 🖱️ |'if lang == "ru" else "| 🖱️ Mouse management 🖱️ |")
            self.plugin_keyboard.row(plugin_keyboard_2)
        if self.data_function_for_telegram is True:
            self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: [Плагин] Управление данными [7/8]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] Data management [7/8]", "info") 
            plugin_keyboard_3 = types.KeyboardButton('| 💻️ Управление данными 💻️ |'if lang == "ru" else "| 💻️ Data management 💻️ |")
            self.plugin_keyboard.row(plugin_keyboard_3)
        if self.ai_function_for_telegram is True:
            self.send_data("[Telegram BOT][Информация]: Инициализирую клавиатуру: [Плагин] ИИ [8/8]" if self.main_language == "ru" else "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] AI [8/8]", "info") 
            plugin_keyboard_4 = types.KeyboardButton('| 🧑‍💻 ИИ 🧑‍💻 |' if lang == "ru" else "| 🧑‍💻 AI 🧑‍💻 |")
            self.plugin_keyboard.row(plugin_keyboard_4)

        plugin_keyboard_back = types.KeyboardButton('| 🔚 Назад 🔚 |'if lang == "ru" else "| 🔚 Back 🔚 |")
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
            mouse_control_keyboard_left_botton = types.KeyboardButton('↙️')
            mouse_control_keyboard_click = types.KeyboardButton('⏺️')
            mouse_control_keyboard_screenshot = types.KeyboardButton('🎦Скриншот🎦' if lang == "ru" else "🎦Screenshot🎦")
            mouse_control_keyboard_click_left = types.KeyboardButton('⏺ ПКМ ⏺'if lang == "ru" else "⏺ RB ⏺")
            mouse_control_keyboard_click_right = types.KeyboardButton('⏺ ЛКМ ⏺'if lang == "ru" else "⏺ RB ⏺") 
            mouse_control_keyboard_back = types.KeyboardButton('| 🔙 |'if lang == "ru" else "| 🔙 |")
            self.mouse_control_keyboard.row(mouse_control_keyboard_left_top, mouse_control_keyboard_top,mouse_control_keyboard_right_top)
            self.mouse_control_keyboard.row(mouse_control_keyboard_left, mouse_control_keyboard_click,mouse_control_keyboard_right)
            self.mouse_control_keyboard.row(mouse_control_keyboard_left_botton, mouse_control_keyboard_bottom,mouse_control_keyboard_right_bottom)
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
                '⌨️ Написать ⌨️' if lang == "ru" else "⌨️ Write ⌨️", 'backspace', '🎦Скриншот🎦' if lang == "ru" else "🎦Screenshot🎦",
                'Смена Языка' if lang == "ru" else "Change Language",
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

            kb_control_keyboard_BACK = types.KeyboardButton('| 🔙 Назад 🔙 |'if lang == "ru" else "| 🔙 Back 🔙 |")
            self.kb_control_keyboard.row(kb_control_keyboard_BACK)

            self.kb_control_keyboard_rus = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            keys = [
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',
                'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',
                'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'ю',
                'space',
                '⌨️ Написать ⌨️' if lang == "ru" else "⌨️ Write ⌨️", 'backspace', '🎦Скриншот🎦' if lang == "ru" else "🎦Screenshot🎦",
                'Смена Языка' if lang == "ru" else "Change Language",
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

            kb_control_keyboard_rus_BACK = types.KeyboardButton('| 🔙 Назад 🔙 |'if lang == "ru" else "| 🔙 Back 🔙 |")
            self.kb_control_keyboard_rus.row(kb_control_keyboard_BACK)

            self.kb_control_keyboard_inkog = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            kb_control_keyboard_inkog_change = types.KeyboardButton('Смена Языка' if lang == "ru" else "Change Language")
            kb_control_keyboard_inkog_back = types.KeyboardButton('| 🔙 Назад 🔙 |'if lang == "ru" else "| 🔙 Back 🔙 |")
            self.kb_control_keyboard_inkog.row(kb_control_keyboard_inkog_change)
            self.kb_control_keyboard_inkog.row(kb_control_keyboard_inkog_back)
        if self.data_function_for_telegram is True:
            self.data_tools_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            data_tools_keyboard_disk = types.KeyboardButton('📂 Файлы 📂' if lang == "ru" else "📂 Files 📂")
            data_tools_keyboard_upload = types.KeyboardButton('⬆️Скачать с ПК⬆️' if lang == "ru" else "⬆️Download from PC⬆️")
            data_tools_keyboard_download = types.KeyboardButton('⬇️Загрузить на ПК⬇️' if lang == "ru" else "⬇️Upload on PC⬇️")
            data_tools_keyboard_back = types.KeyboardButton('| 🔙 Назад 🔙 |'if lang == "ru" else "| 🔙 Back 🔙 |")
            self.data_tools_keyboard.row(data_tools_keyboard_disk)
            self.data_tools_keyboard.row(data_tools_keyboard_upload)
            self.data_tools_keyboard.row(data_tools_keyboard_download)
            self.data_tools_keyboard.row(data_tools_keyboard_back)
        if self.ai_function_for_telegram is True:
            self.g4f_tool_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            g4f_tool_keyboard_respon = types.KeyboardButton('❓ Спросить ❓'if lang == "ru" else "❓ Ask ❓")
            g4f_tool_keyboard_back = types.KeyboardButton('| 🔙 Назад 🔙 |'if lang == "ru" else "| 🔙 Back 🔙 |")
            self.g4f_tool_keyboard.row(g4f_tool_keyboard_respon)
            self.g4f_tool_keyboard.row(g4f_tool_keyboard_back)
        self.send_data("[Telegram BOT][Статус]: Клавиатура инициализирована" if self.main_language == "ru" else "[Telegram BOT][Status]: KeyBoard initialized", "status")
        self.send_data("[Telegram BOT][Статус]: Инициализирую команды" if self.main_language == "ru" else "[Telegram BOT][Status]: Initializing the commands", "info")
        @self.bot.message_handler(commands=['start'])
        def start(message):
            if message.from_user.id in self.autorizated_ids:
                self.bot.send_message(self.main_id, f"| Pc-Stat-Bot | бета 4.0 |\nЗдравствуйте, {self.main_name}." if lang == "ru" else f"| Pc-Stat-Bot | beta 4.0 |\nHello, {self.main_name}.", reply_markup=self.main_keyboard)
            else:
                self.bot.send_message(message.chat.id, "| Pc-Stat-Bot | бета 4.0 |\n🔐 Войдите в систему используя /login {login} {password}" if lang == "ru" else "| Pc-Stat-Bot | beta 4.0 |\n🔐 Log in using /login {login} {password}")
                self.send_data(f"[Telegram BOT][Предупреждение]: {message.from_user.id} нажал на кнопку в меню или что-то ввёл" if lang == "ru" else f"[Telegram BOT][Warning]: {message.from_user.id} pressed a button in the menu or entered something", "warning")
        @self.bot.message_handler(commands=['login'])
        def login(message):
            if message.from_user.id in self.autorizated_ids:
                self.bot.send_message(message.chat.id, "| Pc-Stat-Bot | бета 4.0 |\nВы уже авторизированны!" if lang == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nYou already autorizated!")
            else:
                self.send_data(f"[Telegram BOT][Статус]: {message.from_user.id} хочет авторизироваться, проверяю его данные" if self.main_language == "ru" else f"[Telegram BOT][Status]: {message.from_user.id} wants to log in, checking his data", "info")
                words = message.text.split()
                if len(words) >= 3:
                    login_check = words[1]
                    password_check = words[2]
                    if login_check == self.main_login and password_check == self.main_password:
                        self.autorizated_ids.append(message.from_user.id)
                        self.send_data(f"[Telegram BOT][Статус]: {message.from_user.id} успешно авторизировался" if self.main_language == "ru" else f"[Telegram BOT][Status]: {message.from_user.id} successfully logged in", "info")
                        self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nАвторизация успешна!\nДобро пожаловать в ПУ\n⚠️ При перезапуске бота вы не будете авторизированы ⚠️" if lang == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nAuthorization is successful!\n Welcome to Panel!\n⚠️ When restarting the bot , you will not be logged in ⚠️",reply_markup=self.main_keyboard)
                        return
                    else:
                        self.send_data(f"[Telegram BOT][Предупреждение]: {message.from_user.id} дал неверные данные" if self.main_language == "ru" else f"[Telegram BOT][Warning]: {message.from_user.id} gave incorrect data", "warning")
                        self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nВы дали неверный логин или пароль!" if lang == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nYou have given an incorrect username or password!")
                        return
                else:
                    self.send_data(f"[Telegram BOT][Предупреждение]: {message.from_user.id} дал неверные данные" if self.main_language == "ru" else f"[Telegram BOT][Warning]: {message.from_user.id} gave incorrect data", "warning")
                    self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nНе хватает данных!\nИспользуйте /login {login} {password}" if lang == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nThere is not enough data!\nUse /login {login} {password}")
                    return
        @self.bot.message_handler(commands=['off_bot'])
        def off(message):
            if message.from_user.id in self.autorizated_ids:
                self.send_data("off_bot_and_programm", "code")
        @self.bot.message_handler(commands=['shutdown'])
        def shutdown(message):
            if message.from_user.id in self.autorizated_ids:
                self.send_data("off_bot_and_programm_and_shutdown", "code")
        @self.bot.message_handler(commands=['hibernation'])
        def hibernate(message):
            if message.from_user.id in self.autorizated_ids:
                self.send_data("off_bot_and_programm_and_hibernate", "code")
        @self.bot.message_handler(commands=['reboot'])
        def reboot(message):
            if message.from_user.id in self.autorizated_ids:
                self.send_data("off_bot_and_programm_and_reboot", "code")

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            if call.message.chat.id in self.autorizated_ids:
                if call.data[0] == 'Y':
                    self.send_data(f"[Telegram BOT][Информация]: {call.message.from_user.id} решил скачать файл, выгружаю" if self.main_language == "ru" else f"[Telegram BOT][Information]: {call.message.from_user.id} decided to download the file, uploading it", "info") 
                    file_path = call.data[1:]
                    if os.path.isfile(file_path):
                        with open(file_path, 'rb') as file:
                            self.bot.send_document(call.message.chat.id, file)
                elif call.data[0] == 'N':
                    self.send_data(f"[Telegram BOT][Информация]: {call.message.from_user.id} решил не скачивать файл" if self.main_language == "ru" else f"[Telegram BOT][Information]: {call.message.from_user.id} decided not to download the file", "info") 
                    self.bot.send_message(call.message.chat.id, "| Pc-Stat-Bot | бета 4.0 | 🆗"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | 🆗")
                if call.data[0] == 'D':
                    self.send_data(f"[Telegram BOT][Информация]: {call.message.from_user.id} гуляет по директориям" if self.main_language == "ru" else f"[Telegram BOT][Information]: {call.message.from_user.id} walks through the directories", "info") 
                    dir_path = call.data[1:]
                    if os.path.isdir(dir_path):
                        markup = types.InlineKeyboardMarkup()
                        for item in os.listdir(dir_path):
                            item_path = os.path.join(dir_path, item)
                            if os.path.isdir(item_path):
                                markup.add(types.InlineKeyboardButton(text=item, callback_data='D' + item_path))
                            else:
                                markup.add(types.InlineKeyboardButton(text=item, callback_data='F' + item_path))
                        self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="| Pc-Stat-Bot | бета 4.0 |"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |",reply_markup=markup)
                elif call.data[0] == 'F':
                    self.send_data(f"[Telegram BOT][Информация]: {call.message.from_user.id} нажал на файл, спрашиваю дальнейшие действия" if self.main_language == "ru" else f"[Telegram BOT][Information]: {call.message.from_user.id} clicked on the file, ask for further actions", "info") 
                    file_path = call.data[1:]
                    if os.path.isfile(file_path):
                        markup = types.InlineKeyboardMarkup()
                        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Y' + file_path))
                        markup.add(types.InlineKeyboardButton(text='Нет', callback_data='N'))
                        self.bot.send_message(call.message.chat.id,"| Pc-Stat-Bot | бета 4.0 | Вы хотите загрузить этот файл?"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | Do you want to download this file?",reply_markup=markup)
            else:
                self.bot.send_message(call.message.chat.id, "| Pc-Stat-Bot | бета 4.0 |\n🔐 Войдите в систему используя /login {login} {password}" if lang == "ru" else "| Pc-Stat-Bot | beta 4.0 |\n🔐 Log in using /login {login} {password}")
                self.send_data(f"[Telegram BOT][Предупреждение]: {call.message.from_user.id} нажал на кнопку в меню или что-то ввёл" if lang == "ru" else f"[Telegram BOT][Warning]: {call.message.from_user.id} pressed a button in the menu or entered something", "warning")
        self.send_data("[Telegram BOT][Статус]: Команды инициализированы" if self.main_language == "ru" else "[Telegram BOT][Status]: The commands are initialized", "status")


        @self.bot.message_handler(content_types=["text"])
        def msg(message):
            if message.from_user.id in self.autorizated_ids:
                self.msg_callback(message)
                self.send_data(f"[Telegram BOT][Информация]: {message.from_user.id} с чем то взаимодействовал обрабатываю информацию" if self.main_language == "ru" else f"[Telegram BOT][Information]: {message.from_user.id} was interacting with something, processing information", "info", f"{message.from_user.id} | {message.text}") 
            else:
                self.bot.send_message(message.chat.id, "| Pc-Stat-Bot | бета 4.0 |\n🔐 Войдите в систему используя /login {login} {password}" if lang == "ru" else "| Pc-Stat-Bot | beta 4.0 |\n🔐 Log in using /login {login} {password}")
                self.send_data(f"[Telegram BOT][Предупреждение]: {message.from_user.id} нажал на кнопку в меню или что-то ввёл" if lang == "ru" else f"[Telegram BOT][Warning]: {message.from_user.id} pressed a button in the menu or entered something", "warning", f"{message.from_user.id} | {message.text}")
                
        self.send_data("[Telegram BOT][Статус]: Бот запущен!" if self.main_language == "ru" else "[Telegram BOT][Status]: The bot is running!", "status")
        self.bot.infinity_polling()

    
    def send_data(self, text, status, desc=""):
        self.tot_msg += 1
        self.msg.append({'id': self.tot_msg, 'text': text, 'status': status, 'desc': desc})
    def get_data(self):
        return self.tot_msg, self.msg
    
    
    def open_bot_management(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.bot_control_keyboard)
    def open_music_management(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.music_control_keyboard)
    def open_video_management(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.video_control_keyboard)
    def open_volume_management(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.volume_control_keyboard)
    def open_pc_management(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.pc_control_keyboard)
    def open_plugin_management(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.plugin_keyboard)
    def end_back_end(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.main_keyboard)
    def end_back_back(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.plugin_keyboard)
    def information(self, msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nhttps://agzes.netlify.app/pc-stat-bot")
    def shutdown_bot(self,msg):
        self.bot.send_message(msg.chat.id,  "| Pc-Stat-Bot | бета 4.0 |\nВы уверены что хотите Выключить бота?\nИспользуйте команду /off_bot для выключения" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to turn off the bot?\nUse the /off_bot command to turn off")
    def prev_track(self,msg):
        pyautogui.press('prevtrack')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def next_track(self,msg):
        pyautogui.press('nexttrack')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def play_track(self,msg):
        pyautogui.press('playpause')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def left(self,msg):
        pyautogui.press('left')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def pause(self,msg):
        pyautogui.press('space')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def right(self,msg):
        pyautogui.press('right')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def volume_up(self,msg):
        pyautogui.press('volumeup')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def volume_down(self,msg):
        pyautogui.press('volumedown')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def mute(self,msg):
        pyautogui.press('volumemute')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def hibernation(self,msg):
        self.bot.send_message(msg.chat.id,  "| Pc-Stat-Bot | бета 4.0 |\nВы уверены что хотите перевести ПК в режим гибернации?\nИспользуйте команду /hibernation для перевода в режим гибернации" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to put your PC into hibernation mode?\nUse the /hibernation command to switch to hibernation mode")
    def restart(self,msg):
        self.bot.send_message(msg.chat.id,  "| Pc-Stat-Bot | бета 4.0 |\nВы уверены что хотите Перезапустить ПК?\nИспользуйте команду /reboot для перезагрузки" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to restart your PC?\n Use the /reboot command to reboot")
    def shutdown(self,msg):
        self.bot.send_message(msg.chat.id,  "| Pc-Stat-Bot | бета 4.0 |\nВы уверены что хотите Выключить ПК?\nИспользуйте команду /shutdown для выключения" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to turn off your PC?\n Use the /shutdown command to turn off")
    def lock(self,msg):
        subprocess.call('Rundll32.exe user32.dll,LockWorkStation')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def statistic(self,msg):
        message_info_eng, message_info_rus = get_system_info()
        self.bot.send_message(msg.chat.id, message_info_rus if self.main_language == "ru" else message_info_eng)
    def explorer(self,msg):
        subprocess.call('explorer')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def altf4(self,msg):
        pyautogui.hotkey('alt', 'f4')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def screenshot(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshots')
        screenshot_path = os.path.join(SCREENSHOT_DIR, 'screenshot_temp.png')
        pyautogui.screenshot(screenshot_path)
        with open(screenshot_path, 'rb') as photo_file:
            self.bot.send_photo(msg.chat.id, photo_file)
    def collapse_all(self,msg):
        pyautogui.hotkey('win', 'd')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def enter(self, msg):
        pyautogui.press('enter')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
    def battery(self,msg):
        battery = psutil.sensors_battery()
        if battery is not None:
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |\nБатарея подключена!\nПроверяю подключено ли зарядное устройство"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nBattery is connected!\ncheck if the charger is connected")
            plugged = battery.power_plugged
            percent = battery.percent
            if plugged:
                self.bot.send_message(msg.chat.id,'| Pc-Stat-Bot | бета 4.0 |\nЗарядное устройство подключено! \nЗаряд: ' + str(percent) + '%'if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nThe charger is connected! \Charge: " + str(percent) + '%')
            else:
                self.bot.send_message(msg.chat.id,'| Pc-Stat-Bot | бета 4.0 |\nЗарядное устройство не подключено!\nЗаряд: ' + str(percent) + '%'if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nThe charger is not connected!\Charge: " + str(percent) + '%')
        else:
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |\nБатарея не подключена!"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nBattery is not connected!")
    def clean_cart(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |\nОчищаю корзину..."if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nI'm emptying the trash...")
        os.system('rd /s /q %systemdrive%\\$Recycle.bin')
    def list_of_programs(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |")
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
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.kb_control_keyboard_rus)
        elif language == "EN":
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.kb_control_keyboard)
        else:
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.kb_control_keyboard_inkog)
    def change_language(self,msg):
        pyautogui.hotkey('alt', 'shift')
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        self.open_keyboard_panel(msg)
    def write_text(self, msg):
        text_variable = msg.text
        keyboard.write(text_variable)
        self.bot.send_message(msg.chat.id, f"| Pc-Stat-Bot | бета 4.0 | Написал: {text_variable}"if self.main_language == "ru" else f"| Pc-Stat-Bot | beta 4.0 | Writed: {text_variable}")
    def write(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | Напишите⤵️"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | Write⤵️")
        self.bot.register_next_step_handler(msg, self.write_text)
    def files(self,msg):
        markup = types.InlineKeyboardMarkup()
        disks = os.popen('wmic logicaldisk get caption').read().split()[1:]
        for disk in disks:
            markup.add(types.InlineKeyboardButton(text=disk, callback_data='D' + disk))
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |\n| Выберите диск:" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\n| Select disk:",reply_markup=markup)
    def dwnload(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |\nНапишите путь для файла" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nWrite path to file")
        self.bot.register_next_step_handler(msg, self.download)
    def uplod(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |\nОтправьте нужный файл" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nSend file")
        self.bot.register_next_step_handler(msg, self.upload)
    def download(self,message):
        try:
            file_path = message.text
            if os.path.exists(file_path):
                self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nВаш файл загружается ожидайте."if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nYour file is being uploaded, wait.")
                file = open(file_path, 'rb')
                self.bot.send_document(message.chat.id, file)
            else:
                self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nОшибка: указан неверный путь или же файла не существует."if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nMistake: the path is incorrect or the file does not exist")
        except:  # noqa: E722
            self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nОшибка: указан неверный путь или же файла не существует."if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nMistake: the path is incorrect or the file does not exist")
    def upload(self,message):
        try:
            file = self.bot.get_file(message.document.file_id)
            afile = self.bot.download_file(file.file_path)
            name = message.document.file_name
            with open(name, 'wb') as file_new:
                file_new.write(afile)
            self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nУспешно. Файл будет в папке с ботом" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nSuccessfully. The file will be in the folder with the bot")
        except:  # noqa: E722
            self.bot.send_message(message.chat.id,"| Pc-Stat-Bot | бета 4.0 |\nОшибка: отправьте файл в виде документа. " if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nError: Send the file as a document")
    def open_data_managment_panel(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.data_tools_keyboard)
    def move_mouse(self,msg,move):
        if move == "⬅️":
            pyautogui.move(-50, 0, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        elif move == "↖️":
            pyautogui.move(-50, -50, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        elif move == "↗️":
            pyautogui.move(50, -50, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        elif move == "⬆️":
            pyautogui.move(0, -50, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        elif move == "↙️":
            pyautogui.move(-50, 50, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        elif move == "↘️":
            pyautogui.move(50, 50, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        elif move == "⬇️":
            pyautogui.move(0, 50, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
        elif move == "➡️":
            pyautogui.move(50, 0, duration=0)
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
            pyautogui.click()
        elif move == "⏺ ПКМ ⏺" or move == "⏺ RB ⏺":
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
            pyautogui.rightClick()
        elif move == "⏺ ЛКМ ⏺" or move == "⏺ LB ⏺":
            self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 | ✅"if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 | ✅")
            pyautogui.leftClick()
    def go_to_ai_keyboard(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |", reply_markup=self.g4f_tool_keyboard)
    def ai_next(self,msg):
        self.bot.send_message(msg.chat.id, "| Pc-Stat-Bot | бета 4.0 |\nОтправьте ваш запрос" if self.main_language == "ru" else "| Pc-Stat-Bot | beta 4.0 |\nSend your request")
        self.bot.register_next_step_handler(msg, self.aisteptwo)
    def aisteptwo(self,message):
        ques = message.text
        self.bot.send_message(message.chat.id, f"| Pc-Stat-Bot | бета 4.0 |\n{self.ai(ques)}" if self.main_language == "ru" else f"| Pc-Stat-Bot | beta 4.0 |\n{self.ai(ques)}")
    def ai(self,text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{text}"}]
        )
        mesage = response.choices[0].message.content
        return mesage

    def msg_callback(self, msg):
        self.bot.delete_message(msg.chat.id, msg.message_id)
        if msg.text == "| 🕹️ Управление Ботом 🤖 |" or msg.text == "| 🕹️ Bot Management 🤖 |": self.open_bot_management(msg) 
        elif msg.text == "| 🕹️ Управление Музыкой 🎵 |" or msg.text == "| 🕹️ Music Management 🎵 |": self.open_music_management(msg) 
        elif msg.text == "| 🕹️ Управление Видео 📼 |" or msg.text == "| 🕹️ Video Management 📼 |": self.open_video_management(msg) 
        elif msg.text == "| 🕹️ Управление Звуком 🔈 |" or msg.text == "| 🕹️ Sound Management 🔈|": self.open_volume_management(msg) 
        elif msg.text == "| 🕹️ Управление ПК 🖥️ |" or msg.text == "| 🕹️ PC Management 🖥️ |": self.open_pc_management(msg) 
        elif msg.text == "| ➕ Плагины ➕ |" or msg.text == "| ➕ Plugins ➕ |": self.open_plugin_management(msg) 
        elif msg.text == "| 🔚 Назад 🔚 |" or msg.text == "| 🔚 Back 🔚 |": self.end_back_end(msg) 
        elif msg.text == "| 🔙 Назад 🔙 |" or msg.text == "| 🔙 Back 🔙 |": self.end_back_back(msg) 
        elif msg.text == "| ℹ️ Информация ℹ️ |" or msg.text == "| ℹ️ Information ℹ️ |": self.information(msg)
        elif msg.text == "| 🔴 Выключение 🔴 |" or msg.text == "| 🔴 Shutdown 🔴 |": self.shutdown_bot(msg)
        elif msg.text == "⏮️": self.prev_track(msg)
        elif msg.text == "⏯️": self.play_track(msg)
        elif msg.text == "⏭️": self.next_track(msg)
        elif msg.text == "⏪": self.left(msg)
        elif msg.text == "⏸▶️": self.pause(msg)
        elif msg.text == "⏩": self.right(msg)
        elif msg.text == "🔉": self.volume_down(msg)
        elif msg.text == "🔇": self.mute(msg)
        elif msg.text == "🔊": self.volume_up(msg)
        elif msg.text == "⚪Гибернация⚪" or msg.text == "⚪Hibernation⚪": self.hibernation(msg)
        elif msg.text == "🔴Выключение🔴" or msg.text == "🔴Shutdown🔴": self.shutdown(msg)
        elif msg.text == "⭕Перезагрузка⭕" or msg.text == "⭕Reboot⭕": self.restart(msg)
        elif msg.text == "🔒Блокировка🔒" or msg.text == "🔒Lock🔒": self.lock(msg)
        elif msg.text == "📊Статистика📊" or msg.text == "📊Statistics📊": self.statistic(msg)
        elif msg.text == "📁Проводник📁" or msg.text == "📁Explorer📁": self.explorer(msg)
        elif msg.text == "❌Закрыть окно❌" or msg.text == "❌Close window❌": self.altf4(msg)
        elif msg.text == "🎦Скриншот🎦" or msg.text == "🎦Screenshot🎦": self.screenshot(msg)
        elif msg.text == "⬛Свернуть всё⬛" or msg.text == "⬛Collapse all⬛": self.collapse_all(msg)
        elif msg.text == "⏭Enter⏭" or msg.text == "⏭Enter⏭": self.enter(msg)
        elif msg.text == "🔋Батарея🔋" or msg.text == "🔋Battery🔋": self.battery(msg)
        elif msg.text == "🗑️Очистить корзину🗑️" or msg.text == "🗑️Clear cart🗑️": self.clean_cart(msg)
        elif msg.text == "📃Список программ📃" or msg.text == "📃List of programs📃": self.list_of_programs(msg)

        if self.mouse_move_for_telegram:
            if msg.text == "⬅️": self.move_mouse(msg, "⬅️")
            elif msg.text == "↖️": self.move_mouse(msg, "↖️")
            elif msg.text == "⬆️": self.move_mouse(msg, "⬆️")
            elif msg.text == "↗️": self.move_mouse(msg, "↗️")
            elif msg.text == "➡️": self.move_mouse(msg, "➡️")
            elif msg.text == "↘️": self.move_mouse(msg, "↘️")
            elif msg.text == "⬇️": self.move_mouse(msg, "⬇️")
            elif msg.text == "↙️": self.move_mouse(msg, "↙️")
            elif msg.text == "⏺️": self.move_mouse(msg, "⏺️")
            elif msg.text == "⏺ ПКМ ⏺" or msg.text == "⏺ RB ⏺": self.move_mouse(msg, "⏺ ПКМ ⏺" if self.main_language == "ru" else "⏺ RB ⏺")
            elif msg.text == "⏺ ЛКМ ⏺" or msg.text == "⏺ LB ⏺": self.move_mouse(msg, "⏺ ЛКМ ⏺" if self.main_language == "ru" else "⏺ LB ⏺")
        if self.data_function_for_telegram:
            if msg.text == "| 💻️ Управление данными 💻️ |" or msg.text == "| 💻️ Data management 💻️ |": self.open_data_managment_panel(msg)
            if msg.text == "📂 Файлы 📂" or msg.text == "📂 Files 📂": self.files(msg)
            elif msg.text == "⬆️Скачать с ПК⬆️" or msg.text == "⬆️Download from PC⬆️": self.dwnload(msg)
            elif msg.text == "⬇️Загрузить на ПК⬇️" or msg.text == "⬇️Upload on PC⬇️": self.uplod(msg)
        if self.ai_function_for_telegram:
            if msg.text == "| 🧑‍💻 ИИ 🧑‍💻 |" or msg.text == "| 🧑‍💻 AI 🧑‍💻 |": self.go_to_ai_keyboard(msg)
            if msg.text == "❓ Спросить ❓" or msg.text == "❓ Ask ❓": self.ai_next(msg)
        if self.keyboard_move_for_telegram:
            if msg.text == "| ⌨️ Управление клавиатурой ⌨️ |" or msg.text == "| ⌨️ KeyBoard management ⌨️ |": self.open_keyboard_panel(msg)
            if msg.text == "Смена Языка" or msg.text == "Change Language": self.change_language(msg)
            if msg.text == "⌨️ Написать ⌨️" or msg.text == "⌨️ Write ⌨️": self.write(msg)
            tmp_status = keyboard_click(msg.text)
            if tmp_status is False:
                pass
            else:
                self.bot.send_message(msg.chat.id, f"| Pc-Stat-Bot | бета 4.0 | {tmp_status} ✅" if self.main_language == "ru" else f"| Pc-Stat-Bot | beta 4.0 | {tmp_status} ✅")
        self.send_data(f"[Telegram BOT][Информация]: Обработал запрос от {msg.from_user.id}" if self.main_language == "ru" else f"[Telegram BOT][Information]: Processed the request from {msg.from_user.id}", "info") 



