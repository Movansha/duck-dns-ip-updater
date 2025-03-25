from platform import system
import os

os_name = system()

if os_name == "Linux" or os_name == "Darwin":
    config_folder = str(os.path.expanduser("~")) + "/.config/Movansha/duck-dns-ip-updater"
    config_file = config_folder + "/config"

else:
    config_folder = os.getenv("APPDATA") + "\\Movansha\\Duck DNS IP Updater"
    config_file = config_folder + "\\config"

line_domains = 0
line_token = 1
line_interval = 2

domains = str()
token = str()
interval = int()


def enter_domain(string):
    global domains

    if string == "":
        string = "movansha"

    for i in [" ", "\t", "\n", "\r"]:
        string = string.replace(i, "")
    
    domains = string

    write_value(line_domains, domains)

def enter_token(string):
    global token

    if string == "":
        string = "token"

    for i in [" ", "\t", "\n", "\r"]:
        string = string.replace(i, "")

    token = string

    write_value(line_token, token)

def enter_interval(value):
    global interval

    try:
        interval = int(value)
    except:
        interval = int(15)

    write_value(line_interval, str(interval))

##########

def load_defaults():
    global domains, token, interval

    with open(config_file, "w") as file:
        file.write("domains = movansha" "\n"
                   "token = token" "\n"
                   "update_interval = 15" "\n")

        domains = "movansha"
        token = "token"
        interval = 15

def load_config():
    global domains, token, interval
    os.makedirs(config_folder, exist_ok=True)

    def prepare(read_lines, line):
        cfg = read_lines[line].strip()
        cfg = cfg.split("= ")[-1]

        return cfg

    try:
        with open(config_file, "r") as file:
            read_lines = file.readlines()

            domains = str(prepare(read_lines, line_domains))
            token = str(prepare(read_lines, line_token))
            interval = int(prepare(read_lines, line_interval))

    except:
        load_defaults()

def write_value(line, string):
    os.makedirs(config_folder, exist_ok=True)

    try:
        read_lines = []
        
        with open(config_file, "r") as file:
            read_lines = file.readlines()

        with open(config_file, "w") as file:
            option = read_lines[line].strip()
            option = option.split("=")[0] + ("=")

            read_lines[line] = f"{option} {string}\n"
            file.writelines(read_lines)

    except:
        load_defaults()
