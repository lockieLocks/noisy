import json
from pathlib import Path
from colorama import Fore, Style, init
from cogs.webhook_spammer import runner
init(autoreset=True)

def loader(webhooks: bool):
    stored_data = Path("stored_data.json")
    if stored_data.exists():
        if webhooks:
            with open(stored_data):
                data = json.load(stored_data)
                webhooks_loaded = len(data["webhook"])
            return webhooks_loaded
    else:
        input(f"[{Fore.RED}-{Style.RESET_ALL}] - Data File not Found | Error.\nPress Enter to Return...")

def dumper(webhook_opt: bool):
    webhook = input(f"[{Fore.GREEN}+{Style.RESET_ALL}] Enter Webhook: ")
    stored_data = Path("stored_data.json")
    with open(stored_data) as r:
        data = json.load(r)
    with open(stored_data, "w", encoding="utf-8") as fr:
        if webhook_opt:
            data["webhooks"].append(webhook)
            json.dump(data, fr, indent=4)
        

def asc():
    ascii_ = f""" {Fore.LIGHTRED_EX}
                    ██████   █████           ███                    
                    ░░██████ ░░███           ░░░                     
                    ░███░███ ░███   ██████  ████   █████  █████ ████
                    ░███░░███░███  ███░░███░░███  ███░░  ░░███ ░███ 
                    ░███ ░░██████ ░███ ░███ ░███ ░░█████  ░███ ░███ 
                    ░███  ░░█████ ░███ ░███ ░███  ░░░░███ ░███ ░███ 
                    █████  ░░█████░░██████  █████ ██████  ░░███████ 
                    ░░░░░    ░░░░░  ░░░░░░  ░░░░░ ░░░░░░    ░░░░░███ 
                                                            ███ ░███ 
                                                        ░░██████  
                                                            ░░░░░░ 
    {Style.RESET_ALL}
        [1] - Store Webhook
        [2] - Webhook Spammer
    """
    print(ascii_)


commands = {
    "1": dumper,
    "2": runner
}

def main():
    asc()
    option = input(">> ")
    if option == '1':
        dumper(webhook_opt=True)
    elif option in commands:
        commands[option]()
    else:
        input("Invalid Input...")
    
    
if __name__ == '__main__':
    while True:
        main()