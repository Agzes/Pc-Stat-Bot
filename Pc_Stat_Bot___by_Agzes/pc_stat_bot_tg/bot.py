import sys
import psutil
import pynvml
import os
import subprocess
import time
import platform
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from datapcstatbot import TOKENtg,  authorized_ids, Appdata
pc_stat_bot_VER = "BETA 1.0"
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"""{bcolors.OKGREEN}
      
██████╗░░█████╗░░░░░░░░██████╗████████╗░█████╗░████████╗░░░░░░██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗░░░░░░██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝░░░░░░██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝██║░░╚═╝█████╗╚█████╗░░░░██║░░░███████║░░░██║░░░█████╗██████╦╝██║░░██║░░░██║░░░
██╔═══╝░██║░░██╗╚════╝░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░╚════╝██╔══██╗██║░░██║░░░██║░░░
██║░░░░░╚█████╔╝░░░░░░██████╔╝░░░██║░░░██║░░██║░░░██║░░░░░░░░░██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░░░░░╚════╝░░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░  
      """)
print(f"""{bcolors.OKGREEN}{bcolors.BOLD} ʙʏ ᴀɢᴢᴇs """)
print(" ")
print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запускаюсь! ")

pynvml.nvmlInit()
device_count = pynvml.nvmlDeviceGetCount()

def off_bot():
    sys.exit()
def off(update, context):
    user_id = update.effective_user.id
    if user_id in authorized_ids:
        confirm_message = "🔴Вы уверены, что хотите ВЫКЛЮЧИТЬ бота?\n" \
                        "🔴Введите '/confirm_off' для подтверждения."
        context.bot.send_message(chat_id=update.effective_chat.id, text=confirm_message)
    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} {user_id} ввёл команду /off. ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Вы не авторизованы. ДОСТУП ЗАПРЕЩЁН.")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запретил доступ: {user_id}.")
def confirm_off(update, context):
    user_id = update.effective_user.id
    if user_id in authorized_ids:
        if update.message.text.lower() == "/confirm_off":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Выключение бота...")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Бот будет выключен через 3 секунды.")
            time.sleep(2.5)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Бот выключен.")
            # Здесь выполняйте код для перезапуска бота, например, используя функцию restart_bot()
            off_bot()
    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} {user_id} ввёл команду /confirm_off. ")
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} Стоит обеспокоиться кто-то нашёл вашего бота! ")
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} Кто-то может проспамить командами бота и бот может отключиться!!! ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Вы не авторизованы. ДОСТУП ЗАПРЕЩЁН.")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запретил доступ: {user_id}.")
    

# Функция для обработки команды /start
def start(update, context):
    user_id = update.effective_user.id
    if user_id in authorized_ids:
        context.bot.send_message(chat_id=update.effective_chat.id, text="👋Добро пожаловать! \nℹ️Я бот для мониторинга системы.\n\n 🔓Нашёл тебя в базе авторизованых: доступ разрешён!")
    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} {user_id} ввёл команду /start. ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="👋Приветствую! \nℹ️Я бот для мониторинга системы.\n\n 🔒Для использования бота авторезируйтесь.")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Жду авторизации: {user_id}.")

# Функция для обработки команды /info
def info(update, context):
    user_id = update.effective_user.id
    if user_id in authorized_ids:
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} {user_id} активировал команду /info он есть в базе авторезированных начинаю сбор данных.")
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=update.effective_chat.id, text="✅Вы  авторизованы.✅ \n🆗Доступ разрешен.🆗 \n🔥Начинаю сбор данных.🔥 ")
        message = context.bot.send_message(chat_id=update.effective_chat.id, text="🔥Сбор данных: 0% ")
        msg = message.message_id
        # Получаем информацию о системе
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_text = f"🔥Сбор данных: 5%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text=new_text
        )
        os_info = platform.system()
        operating_system_version = platform.release()
        new_text = f"🔥Сбор данных: 10%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text=new_text
        )
        cpu_percent = psutil.cpu_percent()
        sred_oczagruz = psutil.cpu_freq()
        new_text = f"🔥Сбор данных: 20%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text=new_text
        )
        new_text = f"🔥Сбор данных: 30%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text=new_text
        )
        memory = psutil.virtual_memory()
        memory_usage = memory.used / (1024 ** 3)
        total_memory = memory.total / (1024 ** 3)
        for i in range(device_count):
            # Получение информации о текущем устройстве
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            gpu_info = pynvml.nvmlDeviceGetUtilizationRates(handle)

            # Загрузка GPU в процентах
            gpu_load = gpu_info.gpu

            

        # Отправляем информацию пользователю
        message = f"⏲️ Время: {current_time}\n"
        message = f"🔷 Версия бота: {pc_stat_bot_VER}\n"
        new_text = f"🔥Сбор данных: 50%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg,
            text=new_text
        )
        message += f"🖥️ ОС: {os_info}\n"
        message += f"🖥️ ОС версия: {operating_system_version}\n"
        new_text = f"🔥Сбор данных: 60%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg,
            text=new_text
        )
        message += f"🔴 ЦП: {cpu_percent}%\n"
        new_text = f"🔥Сбор данных: 70%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg,
            text=new_text
        )
        new_text = f"🔥Сбор данных: 80%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg,
            text=new_text
        )
        message += f"🟢 ГП: {gpu_load}%\n"
        new_text = f"🔥Сбор данных: 95%"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg,
            text=new_text
        )
        message += f"🔵 Память: {memory_usage:.2f} GB / {total_memory:.2f} GB\n"
        message += f"⚪ Частота ЦП: {sred_oczagruz}%\n"

        new_text = f"✅Сбор данных: 100%✅"
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg,
            text=new_text
        )
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} ( сессия {user_id} ) Сбор данных закончен высылаю результат.")
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} {user_id} ввёл команду /info. ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Вы не авторизованы. ДОСТУП ЗАПРЕЩЁН.")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запретил доступ: {user_id}.")


# Функция для обработки команды /uptime
def uptime(update, context):
    user_id = update.effective_user.id
    if user_id in authorized_ids:
        context.bot.send_message(chat_id=update.effective_chat.id, text="✅Вы  авторизованы.✅ \n🆗Доступ разрешен.🆗 \n🔥Начинаю сбор данных.🔥 ")
        # Получаем время работы бота
        uptime = datetime.now() - start_time

        # Отправляем информацию пользователю
        message = f"Бот в онлайне {uptime}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} {user_id} ввёл команду /uptime . ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Вы не авторизованы. ДОСТУП ЗАПРЕЩЁН.")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запретил доступ: {user_id}.")

# Функция для обработки неизвестных команд и сообщений
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="😔Извините, я не понимаю эту команду.")

# Функция для запуска указанного приложения
def launch_app(update, context):
    user_id = update.effective_user.id
    if user_id in authorized_ids:
            print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} {user_id} подал команду для запуска приложения.")
            context.bot.send_message(chat_id=update.effective_chat.id, text="✅Вы  авторизованы.✅ \n🆗Доступ разрешен.🆗 \n🔥Что запустить?🔥 ")
            try:
                # Запуск приложения
                subprocess.Popen(Appdata)
                print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Приложение успешно запущено.")
                context.bot.send_message(chat_id=update.effective_chat.id, text="🔥Запустил🔥 ")
            except Exception as e:
                print(f"{bcolors.WARNING}W:{bcolors.WARNING} Ошибка при запуске приложения:", str(e))
                context.bot.send_message(chat_id=update.effective_chat.id, text="❌Ошибка❌ ")
    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} {user_id} ввёл команду /launch_app . ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Вы не авторизованы. ДОСТУП ЗАПРЕЩЁН.")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запретил доступ: {user_id}.")

# Функция для проверки авторизации пользователя
def check_auth(username, password):
    with open(os.path.join(os.path.dirname(__file__), "login.txt"), "r") as file:
        for line in file:
            saved_username, saved_password = line.strip().split(":")
            if username == saved_username and password == saved_password:
                return True
    return False

def button_click(update, context):
    query = update.callback_query
    button = query.data
    
    if button == 'off':
        off(update, context)
    elif button == 'info':
        info(update, context)
    elif button == 'fp':
        launch_app(update, context)
    elif button == 'up':
        uptime(update, context)

def menu(update, context):
    user_id = update.effective_user.id
    if user_id in authorized_ids:
        context.bot.send_message(chat_id=update.effective_chat.id, text="🟦Загрузка меню🟦")
        keyboard = [
            [InlineKeyboardButton("🔴 Выключение ", callback_data='off')],
            [InlineKeyboardButton("🖥️ Информация о ПК", callback_data='info')],
            [InlineKeyboardButton("⏏️ Запуск Программы ", callback_data='fp')],
            [InlineKeyboardButton("🟢 UPtime bot ", callback_data='up')]
        ]
            

        # Отправка сообщения с кнопками
        update.message.reply_text('⏏️ меню ⏏️', reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} {user_id} ввёл команду /menu или /mm . ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Вы не авторизованы. ДОСТУП ЗАПРЕЩЁН.")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запретил доступ: {user_id}.")

# Функция для обработки команды /login
def login(update, context):
    user_id = update.effective_user.id
    print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Проверяю данные которые дал: {user_id}")
    if len(context.args) > 0:
        username = context.args[0]
    else:
        username = "u9fdyudfnu wyt78024tvtnv wte9867vn84672 bt64237nv5682 vb6fw8b wetfw6b6 6w     stdfs8tsyutft sdf dasd"
    if len(context.args) > 1:
        password = context.args[1]
    else:
        password = "utyafsd 7927eft dsioyf72fsd fg4 tdsyfg24867rf gads fg 2g7 gaf 2037rrgfd07usfg 27r2 gq0w7erg 07t27r 0w"
    if check_auth(username, password):
        authorized_ids.append(user_id)  # Добавляем идентификатор авторизованного пользователя в список
        context.bot.send_message(chat_id=update.effective_chat.id, text="Авторизация успешна!")
        print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} {user_id} успешно авторизировался! ")
        keyboard = [
        [InlineKeyboardButton("🔴 Выключение ", callback_data='off')],
        [InlineKeyboardButton("🖥️ Информация о ПК", callback_data='info')],
        [InlineKeyboardButton("⏏️ Запуск Программы ", callback_data='fp')],
        [InlineKeyboardButton("🟢 UPtime bot ", callback_data='up')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        

        # Отправка сообщения с кнопками
        update.message.reply_text('👋Добро Пожаловать👋 \n ⏏️выбери действие⏏️', reply_markup=reply_markup)

    else:
        print(f"{bcolors.WARNING}W:{bcolors.WARNING} Данные которые дал {user_id} неверны! ")
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Неправильный логин или пароль.")


# Функция для обработки всех остальных сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
# Создаем экземпляр бота и регистрируем обработчики команд
updater = Updater(token=TOKENtg, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("info", info))
dispatcher.add_handler(CommandHandler("menu", menu))
dispatcher.add_handler(CommandHandler("mm", menu))
dispatcher.add_handler(CommandHandler("uptime", uptime))
dispatcher.add_handler(CommandHandler("launch_app", launch_app))
dispatcher.add_handler(CommandHandler("login", login))
dispatcher.add_handler(CommandHandler("off", off))
dispatcher.add_handler(CommandHandler("confirm_off", confirm_off))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))
dispatcher.add_handler(CallbackQueryHandler(button_click))
print(f"{bcolors.OKGREEN}I:{bcolors.OKCYAN} Запущен и готов к работе!{bcolors.ENDC}")
# Запускаем бота
updater.start_polling()
start_time = datetime.now()
updater.idle()


