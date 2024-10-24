import os

main_Path = os.path.dirname(os.path.abspath(__file__))
if "\\" in main_Path:
    main_Path = main_Path.replace("\\", "/") + "/"

config_File = main_Path + "settings.cfg"

domain_Line = 0
token_Line = 1
interval_Line = 2

domain = str()
token = str()
interval = int()

def setUp():
    global domain, token, interval

    def prepare(file, line):
        cfg_Lines = file.readlines()
        cfg = str(cfg_Lines[line]).strip()
        cfg = cfg.split("= ")[-1]
        return cfg

    try:
        with open(config_File, "r") as domain_Cfg:
            domain = str(prepare(domain_Cfg, domain_Line))

        with open(config_File, "r") as token_Cfg:
            token = str(prepare(token_Cfg, token_Line))

        with open(config_File, "r") as interval_Cfg:
            interval = int(prepare(interval_Cfg, interval_Line))

        if "=" in domain or "=" in token:
            raise ValueError

    except:
        with open(config_File, "w") as file:
            file.write("domain = movansha" "\n"
                       "token = token" "\n"
                       "update_interval = 15" "\n")

        domain = "movansha"
        token = "token"
        interval = 15

def write_Value(line, text):
    global domain, token, interval

    try:
        with open(config_File, 'r') as file:
            cfg_Lines = file.readlines()
            option = str(cfg_Lines[line]).strip()
            option = option.split("=")[0] + ("=")

            with open(config_File, "w") as file:
                cfg_Lines[line] = f"{option} {text}\n"
                file.writelines(cfg_Lines)

    except:
        with open(config_File, "w") as file:
            file.write("domain = movansha" "\n"
                       "token = token" "\n"
                       "update_interval = 15" "\n")

        domain = "movansha"
        token = "token"
        interval = 15

def enter_Domain(text):
    global domain

    if text == "":
        text = "movansha"

    text = text.replace(" ", "")
    domain = str(text)
    write_Value(domain_Line, str(text))

def enter_Token(text):
    global token

    if text == "":
        text = "token"

    text = text.replace(" ", "")
    token = str(text)
    write_Value(token_Line, str(text))

def enter_Interval(value):
    global interval

    try:
        interval = int(value)
    except:
        interval = int(15)

    write_Value(interval_Line, str(interval))