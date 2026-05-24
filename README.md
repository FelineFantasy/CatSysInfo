# CatSysInfo 🐱📊 v1.1.0

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)]()

A tiny system information utility written in Python. Shows who, where, what OS, uptime, RAM, disk — all in a cute box. Now with JSON config and colored output!

## Description

CatSysInfo collects and displays key system parameters without external APIs. Just pure ctypes, psutil, shutil, os, platform, and colorama.

### Features
- Username & Hostname
- OS & Kernel version
- Current shell (cmd.exe, bash, etc.)
- System uptime (days + hours)
- RAM usage (used / total + percentage)
- Disk usage of script's directory
- Free space on disk
- Colored output (pink & cyan)
- JSON config (customizable fields, box width)
- Cross-platform (Windows / Linux)

## Installation

### Requirements
- Python 3.x
- psutil
- colorama

### Install dependencies
pip install -r requirements.txt

### Or clone and run
git clone https://github.com/FelineFantasy/CatSysInfo.git
cd CatSysInfo
pip install -r requirements.txt
python catsysinfo.py

## Configuration

On first run, sysinfo_config.json is created automatically. You can customize:

{
    "box_width": 35,
    "show_uptime": true,
    "show_kernel": true,
    "show_shell": true,
    "show_ram": true,
    "show_disk": true,
    "show_free": true
}

Set any field to false to hide it from the output.

## Example Output

╭───────────────────────────────────╮
│ kitty@catpc                       │
├───────────────────────────────────┤
│ OS: Windows 10                    │
│ Kernel: 10.0.19045                │
│ Shell: cmd.exe                    │
│ Uptime: 3d 5h                     │
│ RAM: 4.2/15.9GB (26%)             │
│ Disk: 128.5/512.0GB (25%)         │
│ Free: 383.5GB                     │
╰───────────────────────────────────╯

## Project Structure

CatSysInfo/
├── catsysinfo.py          # Main script
├── sysinfo_config.json    # Configuration (auto-created)
├── requirements.txt       # Dependencies
└── README.md              # Documentation

## Requirements

- Python 3.x
- psutil (RAM)
- colorama (colored output)
- Platform: Windows / Linux

## Changelog

### v1.2.0 (24.05.2026)
- Added JSON configuration file
- Added colored output (pink & cyan)
- Refactored code to PEP8 style
- Added docstrings and comments

### v1.1.0 (24.05.2026)
- Purple borders added
- Blue headers have been added

### v1.0.0 (24.05.2026)
- Initial release
- Basic system info output
- Windows and Linux support

## Author

FelineFantasy

License: MIT