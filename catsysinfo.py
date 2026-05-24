import ctypes
import shutil
import os
import platform
import psutil
from colorama import init, Fore, Style

init()

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

print(Fore.MAGENTA + "╭" + "─" * 35 + "╮")
print(Fore.MAGENTA + f"│ {Fore.LIGHTMAGENTA_EX}{username}@{hostname}" + " " * (35 - len(f"{username}@{hostname}") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + "├" + "─" * 35 + "┤")
print(Fore.MAGENTA + f"│ {Fore.CYAN}OS: {Fore.LIGHTMAGENTA_EX}{platform.system()} {platform.version().split('.')[0]}" + " " * (35 - len(f"OS: {platform.system()} {platform.version().split('.')[0]}") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + f"│ {Fore.CYAN}Kernel: {Fore.LIGHTMAGENTA_EX}{platform.release()}" + " " * (35 - len(f"Kernel: {platform.release()}") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + f"│ {Fore.CYAN}Shell: {Fore.LIGHTMAGENTA_EX}{shell}" + " " * (35 - len(f"Shell: {shell}") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + f"│ {Fore.CYAN}Uptime: {Fore.LIGHTMAGENTA_EX}{uptime_days}d {uptime_hours}h" + " " * (35 - len(f"Uptime: {uptime_days}d {uptime_hours}h") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + f"│ {Fore.CYAN}RAM: {Fore.LIGHTMAGENTA_EX}{ram.used/1e9:.1f}/{ram.total/1e9:.1f}GB ({ram.percent:.0f}%)" + " " * (35 - len(f"RAM: {ram.used/1e9:.1f}/{ram.total/1e9:.1f}GB ({ram.percent:.0f}%)") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + f"│ {Fore.CYAN}Disk: {Fore.LIGHTMAGENTA_EX}{disk_used_gb:.1f}/{disk_total_gb:.1f}GB ({percent_disk:.0f}%)" + " " * (35 - len(f"Disk: {disk_used_gb:.1f}/{disk_total_gb:.1f}GB ({percent_disk:.0f}%)") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + f"│ {Fore.CYAN}Free: {Fore.LIGHTMAGENTA_EX}{free_gb:.1f}GB" + " " * (35 - len(f"Free: {free_gb:.1f}GB") - 2) + Fore.MAGENTA + " │")
print(Fore.MAGENTA + "╰" + "─" * 35 + "╯" + Style.RESET_ALL)