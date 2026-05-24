import ctypes
import shutil
import os
import platform
import psutil

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

print("╭" + "─" * 35 + "╮")
print(f"│ {username}@{hostname}" + " " * 21 + "│")
print("├" + "─" * 35 + "┤")
print(f"│ OS: {platform.system()} {platform.version().split('.')[0]}" + " " * 20 + "│")
print(f"│ Kernel: {platform.release()}" + " " * 24 + "│")
print(f"│ Shell: {shell}" + " " * 20 + "│")
print(f"│ Uptime: {uptime_days}d {uptime_hours}h" + " " * 20 + "│")
print(f"│ RAM: {ram.used/1e9:.1f}/{ram.total/1e9:.1f}GB ({ram.percent:.0f}%)" + " " * 12 + "│")
print(f"│ Disk: {disk_used_gb:.1f}/{disk_total_gb:.1f}GB ({percent_disk:.0f}%)" + " " * 9 + "│")
print(f"│ Free: {free_gb:.1f}GB" + " " * 22 + "│")
print("╰" + "─" * 35 + "╯")