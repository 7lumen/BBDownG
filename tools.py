import os
import json
import sys
import platform
import time

# 判断系统类型
system = 'Windows' if platform.system() == 'Windows' else 'Linux'


# 获取当前工作路径
def get_workdir():
    workdir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return workdir


# 获取BBDownT的路径
def get_bbdown_path():
    h = '_win-x64.exe' if system == 'Windows' else '_linux-x64'
    bbdown = os.path.join(get_workdir(), "BBDownT" + h)
    return bbdown


workdir = get_workdir()
# 配置文件路径
config_path = os.path.join(get_workdir(), 'config.json')


def log():
    t = time.time()
    return f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}.{int(t * 1000) % 1000}]'


# 读取配置文件
def read_config():
    """读取配置文件。配置不存在或损坏时返回空配置。"""
    if not os.path.isfile(config_path):
        return {}

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}

    return config if isinstance(config, dict) else {}


# 保存配置文件
def save_config(obj):
    """保存 Qt 控件配置，并保留其他窗口已经保存的配置。"""
    old_config = read_config()
    config = {}

    for name in dir(obj):
        if name.startswith(("checkBox_", "radioButton_")):
            widget = getattr(obj, name, None)
            if widget is not None and hasattr(widget, "isChecked"):
                config[name] = widget.isChecked()

        elif name.startswith("lineEdit_"):
            widget = getattr(obj, name, None)
            if widget is not None and hasattr(widget, "text"):
                config[name] = widget.text()

        elif name.startswith("comboBox_"):
            widget = getattr(obj, name, None)
            if widget is not None and hasattr(widget, "currentIndex"):
                config[name] = widget.currentIndex()

    old_config.update(config)

    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(old_config, f, ensure_ascii=False, indent=4)
    except OSError:
        return False

    return True


# 加载配置文件
def load_config(obj):
    """将配置加载到 Qt 控件中。"""
    config = read_config()

    for name, value in config.items():
        widget = getattr(obj, name, None)
        if widget is None:
            continue

        try:
            if hasattr(widget, "setChecked") and isinstance(value, bool):
                widget.setChecked(value)
            elif hasattr(widget, "setText") and isinstance(value, str):
                widget.setText(value)
            elif hasattr(widget, "setCurrentIndex") and isinstance(value, int):
                widget.setCurrentIndex(value)
        except:
            # 配置文件中的单项异常不应影响程序启动
            continue
