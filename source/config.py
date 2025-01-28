import os

main_path = os.path.dirname(os.path.abspath(__file__))
if "\\" in main_path:
    main_path = main_path.replace("\\", "/") + "/"


config_file = main_path + "settings.cfg"

domains_line = 0
token_line = 1
interval_line = 2

domains = str()
token = str()
interval = int()


def enter_domain(string):
    global domains

    if string == "":
        string = "movansha"

    domains = string.replace(" ", "")
    write_value(domains_line, domains)

def enter_token(string):
    global token

    if string == "":
        string = "token"

    token = string.replace(" ", "")
    write_value(token_line, token)

def enter_interval(value):
    global interval

    try:
        interval = int(value)
    except:
        interval = int(15)

    write_value(interval_line, str(interval))


def load_cfg():
    global domains, token, interval

    def prepare(file, line):
        cfg_lines = file.readlines()

        cfg = str(cfg_lines[line]).strip()
        cfg = cfg.split("= ")[-1]

        return cfg

    try:
        with open(config_file, "r") as cfg_domains:
            domains = str(prepare(cfg_domains, domains_line))

        with open(config_file, "r") as cfg_token:
            token = str(prepare(cfg_token, token_line))

        with open(config_file, "r") as cfg_interval:
            interval = int(prepare(cfg_interval, interval_line))

        if "=" in domains or "=" in token:
            raise ValueError

    except:
        with open(config_file, "w") as file:
            file.write("domains = movansha" "\n"
                       "token = token" "\n"
                       "update_interval = 15" "\n")

        domains = "movansha"
        token = "token"
        interval = 15


def write_value(line, text):
    global domains, token, interval

    try:
        with open(config_file, 'r') as file:
            cfg_lines = file.readlines()

            option = str(cfg_lines[line]).strip()
            option = option.split("=")[0] + ("=")

            with open(config_file, "w") as file:
                cfg_lines[line] = f"{option} {text}\n"
                file.writelines(cfg_lines)

    except:
        with open(config_file, "w") as file:
            file.write("domains = movansha" "\n"
                       "token = token" "\n"
                       "update_interval = 15" "\n")

        domains = "movansha"
        token = "token"
        interval = 15