from typing import Dict
from core import *


def operate():
    settings = openSettings()['wr']
    cmd_handler(settings)
    old_settings = openSettings()
    old_settings['wr'] = settings
    saveSettings(old_settings)

def cmd_handler(settings):
    cmd_help = """commands:
    ch   -> change settings
    ex   -> exit
    else -> start operating
    """
    while True:
        print_operate_settings(settings)
        print(cmd_help)
        cmd = input("input command: ").split(' ')
        if cmd[0] == "ch":
            settings = changeSettings(settings,cmd[1:])
        elif cmd[0] == "ex":
            break
        else:
            startOperate(settings)

def startOperate(settings):
    operateMethod_dict:Dict[str,Method] = {
        "en_voc":EnVocab,
        "en":English,
        "en_prep":EnPrep
    }
    operateMethod_dict[settings["method"]].operate(settings)


def changeSettings(settings,cmd_default=[]):
    finish = False
    flag_names = """flag names:
    m -> operate method name
    tg -> tags
    """
    flag_names_dict = {
        "m":"method",
    }
    if len(cmd_default) > 0:
        cmd_default.append("ex")
    def getCMD(hint=""):
        if len(cmd_default) > 0:
            cmd = cmd_default.pop(0)
            print(hint + cmd)
            return cmd
        return input(hint)
    
    while not finish:
        print(flag_names)
        flag = getCMD("input name (ex -> exit): ")
        if flag == "ex":
            finish = True
        if flag == "tg":
            settings["tags"] = "|" + getCMD("input tags: ") + "|"
        elif flag in flag_names_dict:
            settings[flag_names_dict[flag]] = getCMD("input value: ")
        else:
            print("cannot recognize name: " + flag)
    
    return settings

def print_operate_settings(settings):
    print("{:=^60s}".format("Settings"))
    print("method name: \t" + settings["method"])
    print("tags: \t\t" + str(settings["tags"]))
    print("{:*^60s}".format(""))


if __name__ =="__main__":
    operate()