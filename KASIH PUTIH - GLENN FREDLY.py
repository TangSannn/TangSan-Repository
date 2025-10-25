import sys
import time

def jalanin_lirik():
    lirik = [
        ("BIARKANLAH KURASAKAN", 0.16),
        ("HANGATNYA SENTUHAN", 0.16),
        ("KASIHMU", 0.16),
        ("BAWA DAKU, PENUHIKU", 0.16),
        ("BERILAH DIRIKU", 0.16),
        ("KASIH PUTIH", 0.16),
        ("DI HATIKU", 0.16),
    ]
    
    delay = [1.1, 1.1, 1.5, 1.7, 1.7, 1.7, 1.2]
    print("\n== KASIH PUTIH - YOVIE WIDIANTO & GLENN FREDLY ==")
    time.sleep(0.1)
    
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end="")
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print("")
    
    print("//code by TangSan")

jalanin_lirik()