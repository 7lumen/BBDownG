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
    with open(config_path, 'r') as f:
        config = json.loads(f.read())
        return config


# 保存配置文件
def save_config(obj):
    old_config = {}
    # 判断是否有配置文件
    if os.path.isfile(config_path):
        with open(config_path, 'r') as f:
            old_config = json.loads(f.read())

    config = {}
    for name in dir(obj):
        if name.startswith("checkBox_"):
            widget = getattr(obj, name)
            config[name] = widget.isChecked()
        elif name.startswith("radioButton_"):
            widget = getattr(obj, name)
            config[name] = widget.isChecked()
        elif name.startswith("lineEdit_"):
            widget = getattr(obj, name)
            config[name] = widget.text()
        elif name.startswith("comboBox_"):
            widget = getattr(obj, name)
            config[name] = widget.currentIndex()

    old_config.update(config)
    with open(config_path, 'w') as f:
        f.write(json.dumps(old_config, indent=4))


# 加载配置文件
def load_config(obj):
    # 判断是否有配置文件

    with open(config_path, 'r') as f:
        config = json.loads(f.read())
    # 按照配置文件设置
    for i in config:
        try:
            if type(config[i]) is type(True):
                exec(f'obj.{i}.setChecked({config[i]})')
                getattr(obj, i)
            elif type(config[i]) is type(''):
                exec(f'obj.{i}.setText(r"{config[i]}")')
            elif type(config[i]) is type(0):
                exec(f'obj.{i}.setCurrentIndex({config[i]})')
        except:
            continue
