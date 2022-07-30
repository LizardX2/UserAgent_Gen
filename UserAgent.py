# Made by LizardX2
#
#   For issues or improvements you can contact me on Telegram;
# 
#   Telegram: @LizardX2 // t.me/LizardX2
#
from colorama import *
from time import sleep
import random
import string
import os

static = "Mozilla/5.0"
staticM = "Safari/537.36"
valid = ["w", "m", "l", "a"]
os.system("cls")
settings = input(f"{Fore.YELLOW}Windows [{Fore.GREEN}W{Fore.RESET}{Fore.YELLOW}] | MacOS [{Fore.GREEN}M{Fore.RESET}{Fore.YELLOW}] | Linux [{Fore.GREEN}L{Fore.RESET}{Fore.YELLOW}] | ALL [{Fore.CYAN}A{Fore.RESET}{Fore.YELLOW}] ? {Fore.CYAN}> {Fore.RESET}")
if settings.lower() not in valid:
    os.system("cls")
    print(f"{Fore.RED}ERROR! Choose a valid option! {Fore.RESET}")
    print("")
    sleep(5)
    exit()
else: 
    option = input(f"{Fore.LIGHTYELLOW_EX}How many ? > {Fore.RESET}")
    os.system("cls")

def Generator():
    rv = random.randint(99, 108)
    Mac2_1 = random.randint(10, 11)
    Mac2_2 = random.randint(0, 15)
    MacVer = f"{Mac2_1}_{Mac2_2}"
    WinFox = random.choice([f"10.0; Win64; rv:{rv}.0", f"10.0; WOW64; rv:{rv}.0", f"10.0; Win64; x64; rv:{rv}.0", f"10.0; Win64; x64; rv:{rv}.0esr", f"10.0; WOW64; x64; rv:{rv}.0"])
    WinVer = random.choice(["10.0; WOW64", "11.0; Win64", "10.0; Win64", "11.0; WOW64", "11.0; WOW64; x64", "10.0; WOW64; x64"])
    LinVer = random.choice(["X11; U; Linux x86_64", "X11; Linux x86_64", "X11; Linux i686", "X11; U; Linux i686"])
    FirRnd = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for P in range(random.randint(12,15)))
    FirVer = random.randint(0, 9)
    Win2_1 = random.randint(101, 104)
    Win2_2 = random.randint(4262, 5704)
    Win2_3 = random.randint(101, 194)
    Win4_1 = random.randint(99, 102)
    Win4_2 = random.randint(1190, 1205)
    Win4_3 = random.randint(5, 72) 
    Win6_1 = random.randint(78, 83)
    Win6_2 = random.randint(1964, 3999)
    Win6_3 = random.randint(35, 147)
    LinFirGe = random.randint(2001, 2017)
    LinFirGe2 = random.randint(100, 246)
    LinFirGe3 = random.randint(1004, 2661)
    
    LinExt = random.choice([f"Ubuntu Chromium/{Win2_1}.0.{Win2_2}.{Win2_3} {staticM}", f"Chrome/{Win2_1}.0.{Win2_2}.{Win2_3} {staticM}", f"Ubuntu Chromium/{Win2_1}.0.{Win2_2}.{Win2_3} Chrome/{Win2_1}.0.{Win2_2}.{Win2_3} {staticM}"])
    WinFir = random.choice([f"Firefox/10{FirVer}.0esr/{FirRnd}", f"Firefox/10{FirVer}.0", f"Firefox/10{FirVer}.0esr", f"Firefox/10{FirVer}.0/{FirRnd}"])
    op_win_2 = random.choice(["Gecko/20110101", "Gecko/20000101", "AppleWebKit/537.36 (KHTML, like Gecko)"])
    op_lin_3 = random.choice([f"Gecko/{LinFirGe}0{LinFirGe2}", f"Gecko/{LinFirGe}{LinFirGe3}"])
    LinFir = random.choice([f"en-GB", f"en-US; rv:{rv}.0esr", f"en-GB; rv:{rv}.0esr", "en-US", f"en-US; rv:{rv}.0", f"en-GB; rv:{rv}.0"])
    op_win_3 = f"Chrome/{Win2_1}.0.{Win2_2}.{Win2_3} {staticM}"
    MacEnd = f"Macintosh; Intel Mac OS X {MacVer}"
    Edg = f" Edg/{Win4_1}.0.{Win4_2}.{Win4_3}"
    Opr = f" OPR/{Win6_1}.0.{Win6_2}.{Win6_3}"
    op_win_1 = f"Windows NT {WinVer}"
    WinEnd = f"Windows NT {WinFox}"

    Win_Firefox = f"{static} ({WinEnd}) {op_win_2} {WinFir}"
    Mac_Firefox = f"{static} ({MacEnd}) {op_win_2} {WinFir}"
    Lin_Firefox = f"{static} ({LinVer}; {LinFir}) {op_lin_3} {WinFir}"
    Win_Random_UserAgent = random.choice([f"{static} ({op_win_1}) {op_win_2} {op_win_3}{Edg}", f"{static} ({op_win_1}) {op_win_2} {op_win_3}{Opr}", f"{static} ({op_win_1}) {op_win_2} {op_win_3}", f"{static} ({WinEnd}) {op_win_2} {WinFir}"])
    Mac_Random_UserAgent = random.choice([f"{static} ({MacEnd}) {op_win_2} {op_win_3}{Edg}", f"{static} ({MacEnd}) {op_win_2} {op_win_3}{Opr}", f"{static} ({MacEnd}) {op_win_2} {op_win_3}", f"{static} ({MacEnd}) {op_win_2} {WinFir}"])
    Lin_Random_UserAgent = random.choice([f"{static} ({LinVer}) {LinExt}", f"{static} ({LinVer}; {LinFir}) {op_lin_3} {WinFir}"])
    All_Random_UserAgent = random.choice([f"{static} ({op_win_1}) {op_win_2} {op_win_3}{Edg}", f"{static} ({op_win_1}) {op_win_2} {op_win_3}{Opr}", f"{static} ({op_win_1}) {op_win_2} {op_win_3}", f"{static} ({WinEnd}) {op_win_2} {WinFir}", f"{static} ({MacEnd}) {op_win_2} {op_win_3}{Edg}", f"{static} ({MacEnd}) {op_win_2} {op_win_3}{Opr}", f"{static} ({MacEnd}) {op_win_2} {op_win_3}", f"{static} ({MacEnd}) {op_win_2} {WinFir}", f"{static} ({LinVer}) {LinExt}", f"{static} ({LinVer}; {LinFir}) {op_lin_3} {WinFir}"])

    if settings.lower() == "w":
        if op_win_2 == "Gecko/20110101" or op_win_2 == "Gecko/20000101":
            print(f"{Fore.GREEN}{Win_Firefox}{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}{Win_Random_UserAgent}{Fore.RESET}")
    elif settings.lower() == "m":
        if op_win_2 == "Gecko/20110101" or op_win_2 == "Gecko/20000101":
            print(f"{Fore.GREEN}{Mac_Firefox}{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}{Mac_Random_UserAgent}{Fore.RESET}")
    elif settings.lower() == "l":
        if op_win_2 == op_lin_3:
            print(f"{Fore.GREEN}{Lin_Firefox}{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}{Lin_Random_UserAgent}{Fore.RESET}")
    elif settings.lower() == "a":
        print(f"{Fore.GREEN}{All_Random_UserAgent}{Fore.RESET}")

for _ in range(int(option)):
    Generator()
close = input(f"\n{Fore.RED}PRESS ENTER TO EXIT{Fore.RESET}")
    