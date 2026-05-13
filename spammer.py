import time
import os


try:
    import requests
except ImportError:
    print("\n[!] 'requests' kütüphanesi bulunamadı!")
    print("[!] Lütfen terminale 'pip install requests' yazarak yükleyin.")
    input("\nKapatmak için Enter'a basın...")
    exit()


C = "\033[36m"
B = "\033[34m"
Y = "\033[33m"
G = "\033[32m"
R = "\033[31m"
W = "\033[37m"

def UI():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{C}="*50)
    print(f"{B}         SYNTHETIX - WEBHOOK SPAMMER")
    print(f"{Y}          GitHub Edition | Open Source")
    print(f"{C}="*50 + W)

def run():
    UI()
    url = input(f"{B}[>]{W} Webhook Linki: ").strip()
    msg = input(f"{B}[>]{W} Mesajın: ")
    
    if not url.startswith("http"):
        print(f"{R}[!] Geçersiz URL girdiniz!{W}")
        input("\nDevam etmek için Enter'a basın...")
        return

    try:
        sleep_time = float(input(f"{B}[>]{W} Hız (sn): "))
    except:
        sleep_time = 0.5

    print(f"\n{G}[!] SpamBaşladı Yarram Ne bakıyonlan Kardeşş... Durdurmak için CTRL+C{W}\n")
    
    sent = 0
    try:
        while True:
            payload = {"content": msg}
            res = requests.post(url, json=payload)
            
            if res.status_code == 204:
                sent += 1
                print(f"{G}[+]{W} Gönderildi: {sent}", end="\r")
            elif res.status_code == 429:
                wait = res.json().get('retry_after', 1)
                print(f"\n{R}[!] Limit! {wait}ms bekleniyor...")
                time.sleep(wait / 1000)
            else:
                print(f"\n{R}[-]{W} Hata: {res.status_code}")
                break
            
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        print(f"\n\n{Y}[-]{W} İşlem durduruldu.")
    except Exception as e:
        print(f"\n{R}[-]{W} Beklenmedik Hata: {e}")
    

    print(f"\n{C}--------------------------------------------------")
    print(f"{B}         Enes tarafından yapılmıştır.")
    print(f"{C}--------------------------------------------------{W}")
    input("\nProgramı kapatmak için Enter'a basın...")

if __name__ == '__main__':
    run()