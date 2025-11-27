import time, sys, os


def teks_mulai():
    print("=" * 60)
    print("+==========================================================+")
    print("|                  ✦ Selamat Datang ✦                      |")
    print("|                      GwehMauJalan                        |")
    print("+----------------------------------------------------------+")
    print("|                Silahkan Login Terlebih Dahulu            |")
    print("+==========================================================+")
    print("=" * 60)


def tampilan_menu_admin(username):
    print("="*50) 
    print("👑 Selamat Datang, Admin! 👑") 
    print(f"Username Akun: {username}") 
    print(f"Login Berhasil: {time.strftime("%d %B %Y %H:%M:%S")}") 
    print("="*50) 
    loading()
    
def header_menu_admin():
    print("="*46) 
    print("\t👑 Ini Menu Admin! 👑")
    print(" Silahkan Pilih Salah Satu Menu Yang Tersedia") 
    print("="*46) 
    


def tampilan_menu_member(username):
    print("="*50) 
    print(f"🧢 Selamat Datang, {username}! 🧢") 
    print(f"Username Akun: {username}") 
    print(f"Login Berhasil: {time.strftime("%d %B %Y %H:%M:%S")}") 
    print("="*50) 
    loading()
    
def header_menu_member():
    print("="*46) 
    print("\t🧢 Ini Menu Member! 🧢")
    print(" Silahkan Pilih Salah Satu Menu Yang Tersedia") 
    print("="*46) 
    
   
    
def detik3_coba_lagi():
    for i in range(3, 0, -1):
        print(f"Anda dapat mencoba lagi dalam {i} detik...", end="\r")
        sys.stdout.flush()
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  
   
   
def detik3():
    for i in range(3, 0, -1):
        print(f"Tunggu {i} detik...", end="\r")
        sys.stdout.flush()
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  
    
    
def detik5():
    for i in range(5, 0, -1):
        print(f"Tunggu {i} detik...", end="\r")
        sys.stdout.flush()
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def loading():
    panjang_loading = 50
    for i in range(panjang_loading + 1):
        persen = int((i / panjang_loading) * 100)
        bar = "█" * i + "░" * (panjang_loading - i)
        sys.stdout.write(f"\rLoading |{bar}| {persen}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    
    
def loading_waktu(waktu_menit):
    for sisa in range(waktu_menit, -1, -10):
        bar = "█" * (waktu_menit - sisa)
        bar += "_" * sisa

        print(f"\rWaktu Tersisa: {sisa} Menit |{bar}|", end = "\r")
        sys.stdout.flush()
        time.sleep(0.5)

    print("\nPerjalanan selesai!\n")
    

    
