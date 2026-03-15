import aiohttp
import asyncio
from colorama import Fore, init, Style
import requests

init(autoreset=True)

def grab_and_validate():
    webhook = input(f"[{Fore.GREEN}+{Style.RESET_ALL}] - Enter Webhook: ")
    print(f"[?] Sending Validation Message...")
    r = requests.post(webhook, json={"content": "Webhook Valid"})
    if r.status_code == 204:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] - Webhook Valid...\n")
        return webhook
    else:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] - Failed to Send Message | Status Code: {r.status_code} | Validation Failed..."
        )
        return False


async def send_all(webhook: str):
    text = input(f"[{Fore.GREEN}+{Style.RESET_ALL}] - Enter Text to Spam: ")
    amount = int(input(f"[{Fore.GREEN}+{Style.RESET_ALL}] - Enter Amount of times to spam: "))
    payload = {"content": text,}
    async with aiohttp.ClientSession() as sack:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] - Spamming Loop Is now Running...")
        for i in range(amount):
            async with sack.post(webhook, json=payload) as r:
                if r.status == 204:
                    print(f"\r[{Fore.GREEN}+{Style.RESET_ALL}] - Sent: {i+1}/{amount} | Status Code: {r.status}", flush=True, end="")
                else:
                    print(f"[{Fore.RED}-{Style.RESET_ALL}] - Ratelimited | Waiting 10 Seconds...")
                    asyncio.sleep(10)
        print()
        
def runner():
    webhook = grab_and_validate()
    if webhook:
        asyncio.run(send_all(webhook))