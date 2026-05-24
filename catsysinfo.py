"""
System information display script.
"""

import ctypes
import json
import os
import platform
import shutil

import psutil
from colorama import Fore, Style, init

init()

DEFAULT_CONFIG = {
    "box_width": 35,
    "show_uptime": True,
    "show_kernel": True,
    "show_shell": True,
    "show_ram": True,
    "show_disk": True,
    "show_free": True
}


def get_config_path():
    """Возвращает путь к файлу конфигурации."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "sysinfo_config.json")


def load_config():
    """Загружает конфигурацию из JSON файла."""
    config_path = get_config_path()

    if not os.path.exists(config_path):
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(DEFAULT_CONFIG, f, indent=4, ensure_ascii=False)
            print(f"Создан конфиг: {config_path}")
        except IOError as e:
            pass
        return DEFAULT_CONFIG.copy()

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = DEFAULT_CONFIG.copy()
            config.update(json.load(f))
            return config
    except (json.JSONDecodeError, IOError) as e:
        pass
        return DEFAULT_CONFIG.copy()

def main():
    """Отображает системную информацию."""
    config = load_config()

    username = os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown'
    hostname = platform.node()
    path = os.path.dirname(os.path.abspath(__file__)) or '.'

    total, used, free = shutil.disk_usage(path)
    percent_disk = (used / total) * 100

    if platform.system() == "Windows":
        shell = os.path.basename(os.environ.get('COMSPEC', 'cmd.exe'))
        uptime_seconds = ctypes.windll.kernel32.GetTickCount64() / 1000
    else:
        shell = os.path.basename(os.environ.get('SHELL', '/bin/sh'))
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])

    uptime_days = int(uptime_seconds // 86400)
    uptime_hours = int((uptime_seconds % 86400) // 3600)

    ram = psutil.virtual_memory()
    disk_used_gb = used / (1024 ** 3)
    disk_total_gb = total / (1024 ** 3)
    free_gb = free / (1024 ** 3)

    w = config["box_width"]

    print(Fore.MAGENTA + "╭" + "─" * w + "╮")
    print(Fore.MAGENTA + f"│ {Fore.LIGHTMAGENTA_EX}{username}@{hostname}" +
          " " * (w - len(f"{username}@{hostname}") - 2) + Fore.MAGENTA + " │")
    print(Fore.MAGENTA + "├" + "─" * w + "┤")
    print(Fore.MAGENTA + f"│ {Fore.CYAN}OS: {Fore.LIGHTMAGENTA_EX}{platform.system()} {platform.version().split('.')[0]}" +
          " " * (w - len(f"OS: {platform.system()} {platform.version().split('.')[0]}") - 2) + Fore.MAGENTA + " │")

    if config["show_kernel"]:
        print(Fore.MAGENTA + f"│ {Fore.CYAN}Kernel: {Fore.LIGHTMAGENTA_EX}{platform.release()}" +
              " " * (w - len(f"Kernel: {platform.release()}") - 2) + Fore.MAGENTA + " │")

    if config["show_shell"]:
        print(Fore.MAGENTA + f"│ {Fore.CYAN}Shell: {Fore.LIGHTMAGENTA_EX}{shell}" +
              " " * (w - len(f"Shell: {shell}") - 2) + Fore.MAGENTA + " │")

    if config["show_uptime"]:
        print(Fore.MAGENTA + f"│ {Fore.CYAN}Uptime: {Fore.LIGHTMAGENTA_EX}{uptime_days}d {uptime_hours}h" +
              " " * (w - len(f"Uptime: {uptime_days}d {uptime_hours}h") - 2) + Fore.MAGENTA + " │")

    if config["show_ram"]:
        print(Fore.MAGENTA + f"│ {Fore.CYAN}RAM: {Fore.LIGHTMAGENTA_EX}{ram.used/1e9:.1f}/{ram.total/1e9:.1f}GB ({ram.percent:.0f}%)" +
              " " * (w - len(f"RAM: {ram.used/1e9:.1f}/{ram.total/1e9:.1f}GB ({ram.percent:.0f}%)") - 2) + Fore.MAGENTA + " │")

    if config["show_disk"]:
        print(Fore.MAGENTA + f"│ {Fore.CYAN}Disk: {Fore.LIGHTMAGENTA_EX}{disk_used_gb:.1f}/{disk_total_gb:.1f}GB ({percent_disk:.0f}%)" +
              " " * (w - len(f"Disk: {disk_used_gb:.1f}/{disk_total_gb:.1f}GB ({percent_disk:.0f}%)") - 2) + Fore.MAGENTA + " │")

    if config["show_free"]:
        print(Fore.MAGENTA + f"│ {Fore.CYAN}Free: {Fore.LIGHTMAGENTA_EX}{free_gb:.1f}GB" +
              " " * (w - len(f"Free: {free_gb:.1f}GB") - 2) + Fore.MAGENTA + " │")

    print(Fore.MAGENTA + "╰" + "─" * w + "╯" + Style.RESET_ALL)


if __name__ == "__main__":
    main()