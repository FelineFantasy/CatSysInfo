# CatSysInfo 🐱📊

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)]()

A tiny system information utility written in Python. Shows who, where, what OS, uptime, RAM, disk — all in a cute box.

## 📝 Description

**CatSysInfo** collects and displays key system parameters without external APIs. Just pure ctypes, psutil, shutil, os, and platform.

### Features:
- Username & Hostname
- ️OS & Kernel version
- Current shell (cmd.exe, bash, etc.)
- ️System uptime (days + hours)
- RAM usage (used / total + percentage)
- Disk usage of script's directory
- Free space on disk
- Cross‑platform (Windows / Linux)

## ⚙️ Installation

### Requirements
- Python 3.x
- psutil

### Install dependencies

    pip install -r requirements.txt

### Or clone and run

    git clone https://github.com/FelineFantasy/CatSysInfo.git
    cd CatSysInfo
    pip install -r requirements.txt
    python catsysinfo.py

## 🧪 Example Output

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

## 📁 Project Structure

    CatSysInfo/
    ├── catsysinfo.py      # Main script
    ├── requirements.txt   # Dependencies (psutil)
    └── README.md          # Documentation

## 📋 Requirements

- Python 3.x
- psutil (see requirements.txt)
- Platform: Windows / Linux

## 👤 Author

**FelineFantasy**

License: MIT