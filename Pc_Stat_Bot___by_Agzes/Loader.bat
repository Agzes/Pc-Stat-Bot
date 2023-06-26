@echo off
pip install psutil
pip install python-telegram-bot==13.7
pip install pynvml

python pc_stat_bot_tg\Set.py
echo python pc_stat_bot_tg\Set.py > Set.bat
echo python pc_stat_bot_tg\bot.py > Start.bat
start "" python pc_stat_bot_tg\bot.py
timeout /t 1 /nobreak > nul
del %0

