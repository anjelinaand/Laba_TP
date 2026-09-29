import json
import platform
import os
import socket
import sys
import getpass
import shutil
import locale

if platform.system() == "Darwin":
        usage = shutil.disk_usage('/')
elif platform.system() == "Windows":
        usage = shutil.disk_usage('C:\\')
full_info = { "Операционная система": platform.system(),
        "Версия ОС": platform.version(),
        "Выпуск ОС": platform.release(),
        "Архитектура": platform.machine(),
        "Процессор": platform.processor(),
        "Версия Python": sys.version.split()[0],
        "Разрядность Python": platform.architecture()[0],
        "Количество ядер": os.cpu_count(),

        "Занятый объем диска(ГБ)": round(usage.used/(1024**3), 2),
        "Свободный объем диска(ГБ)": round(usage.free/(1024**3),2),
        "Весь объем диска(ГБ)": round(usage.total/(1024**3), 2),
        
        "Пользователь": getpass.getuser(),
        "Исполняемый файл": sys.executable,
        "Имя компьютера": socket.gethostname(),
        "Язык системы": locale.getlocale()[0],
        "Рабочая директория": os.getcwd(),
        "Максимальное целое": sys.maxsize,

        } 

with open("system_info.json", "w", encoding="utf-8") as f:
    json.dump(full_info, f, indent=4, ensure_ascii=False)
print("Данные сохранены в system_info.json")
