import inquirer
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

daftar_users = {"Username": ["Mutia"], "Password": ["040"]}

daftar_perjalanan = {
    "Nama": ["Mutia"], 
    "Nama Perjalanan": ["Liburan ke Balikpapan"], 
    "Destinasi": ["Balikpapan"], 
    "Tanggal": ["1 Januari 2025"], 
    "Durasi": ["5 hari"], 
    "Budget": ["5000000"], 
    "Cerita": ["Seru banget"],
    "Rating": ["5"] 
}

user_login = "mouriu"

def Menu_utama() -> bool:
    clear_screen()
    print("=" * 60)
    print("MENU UTAMA")
    print("=" * 60)
    
    pertanyaan = [
        inquirer.List('menu',
                     message="Pilih menu",
                     choices=[
                         'Review Perjalanan',
                         'Kembali ke Menu Awal'
                     ],
                     ),
    ]
    
    try:
        jawaban = inquirer.prompt(pertanyaan)
        
        if jawaban is None:
            return True
        
        if jawaban['menu'] == 'Review Perjalanan':
            menu_login()
            return False
        elif jawaban['menu'] == 'Kembali ke Menu Awal':
            menu_awal()
            
    except KeyboardInterrupt:
        return True


def menu_login() -> None:
    while True:
        clear_screen()
        print("=" * 60)
        print(f"User: {user_login}")
        print("=" * 60)
        
        pertanyaan = [
            inquirer.List('pertanyaan',
                         message="apakah anda ingin memberikan review?",
                         choices=[
                             'iya, saya ingin memberikan review',
                             'tidak'
                         ],
                         ),
        ]
        
        try:
            jawaban = inquirer.prompt(pertanyaan)
            
            if jawaban is None:
                if Menu_utama():
                    break
            
            if jawaban['pertanyaan'] == 'iya, saya ingin memberikan review':
                review()
            elif jawaban['pertanyaan'] == 'tidak':
                if Menu_utama():
                    break
                    
        except KeyboardInterrupt:
            if Menu_utama():
                break



def review() -> None:
    while True:
        clear_screen()
        print("=" * 60)
        print(f"User: {user_login}")
        print("=" * 60)
        
        pertanyaan = [
            inquirer.List('menu',
                         message="Pilih menu utama",
                         choices=[
                             'Lihat Review Kota Ini',
                             'Berikan Review',
                             'Edit Review Saya',
                             'Hapus Review Saya',
                             'Selesai'
                         ],
                         ),
        ]
        
        try:
            jawaban = inquirer.prompt(pertanyaan)
            
            if jawaban is None:
                if Menu_utama():
                    break

            if jawaban['menu'] == 'Lihat Review Kota Ini':
                daftar()
            elif jawaban['menu'] == 'Berikan Review':
                catat()
            elif jawaban['menu'] == 'Edit Review Saya':
                update()
            elif jawaban['menu'] == 'Hapus Review Saya':
                hapus()
            elif jawaban['menu'] == 'Selesai':
                if Menu_utama():
                    break
                    
        except KeyboardInterrupt:
            if Menu_utama():
                break


def daftar() -> None:
    clear_screen()
    print("=" * 60)
    print("REVIEW PERJALANAN")
    print("=" * 60)
    
    pertanyaan = [
        inquirer.List('mode',
                     message="Review mana yang ingin dilihat?",
                     choices=['Lihat Review Saya', 'Lihat Semua Review'],
                     ),
    ]
    
    jawaban = inquirer.prompt(pertanyaan)
    
    if jawaban is None:
        return
    
    perjalanan = []
    
    if jawaban['mode'] == 'Lihat Semua Review':
        clear_screen()
        print("\n" + "=" * 60)
        print("SEMUA REVIEW")
        print("=" * 60)
        for i in range(len(daftar_perjalanan["Nama"])):
            perjalanan.append(i)
    else:
        clear_screen()
        print("\n" + "=" * 60)
        print(f"REVIEW {user_login.upper()}")
        print("=" * 60)
        for i in range(len(daftar_perjalanan["Nama"])):
            if daftar_perjalanan["Nama"][i] == user_login:
                perjalanan.append(i)
    
    if len(perjalanan) == 0:
        clear_screen()
        print("\nAnda belum memberikan review.")
    else:
        clear_screen()
        print()
        nomor = 1
        for idx in perjalanan:
            print(f"\n{'─' * 60}")
            print(f"[{nomor}] REVIEW DARI @{daftar_perjalanan['Nama'][idx]}")
            print(f"{'─' * 60}")
            
            print(f"Nama Perjalanan   : {daftar_perjalanan['Nama Perjalanan'][idx]}")
            print(f"Destinasi         : {daftar_perjalanan['Destinasi'][idx]}")
            print(f"Tanggal           : {daftar_perjalanan['Tanggal'][idx]}")
            print(f"Durasi            : {daftar_perjalanan['Durasi'][idx]}")
            print(f"Budget            : Rp {int(daftar_perjalanan['Budget'][idx]):,}")
            print(f"Cerita            : {daftar_perjalanan['Cerita'][idx]}")
            star = int(daftar_perjalanan["Rating"][idx])
            print(f"Rating            : " + "★" * star + "☆" * (5 - star))
            
            nomor += 1
    
    input("\nTekan Enter untuk kembali...")
    pertanyaan = [
        inquirer.List('mode',
                     message="ingin kembali ke?",
                     choices=['Review Perjalanan', 'Menu Review'],
                     ),
    ]
    
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return
    if jawaban['mode'] == 'Review Perjalanan':
        daftar()
    elif jawaban['mode'] == 'Menu Review':
        review()

def catat() -> None:
    while True:
        clear_screen()
        print("=" * 60)
        print("MASUKAN REVIEW")
        print("=" * 60)

        try:
            nama_perjalanan = input("Nama Perjalanan : ").strip()
            if not nama_perjalanan:
                raise ValueError("\nNama perjalanan tidak boleh kosong!")

            destinasi = input("Destinasi : ").strip()
            if not destinasi:
                raise ValueError("\nDestinasi tidak boleh kosong!")

            tanggal = input("Tanggal Pergi : ").strip()
            durasi = input("Berapa Lama : ").strip()

            budget = input("Budget (angka saja) : ").strip()
            if not budget.isdigit():
                raise ValueError("\nBudget harus berupa angka!")

            cerita = input("Cerita/Experience : ").strip()
            star = input("Rating (1-5) : ").strip()
            if star not in ['1', '2', '3', '4', '5']:
                raise ValueError("\nRating harus antara 1 sampai 5 dan tidak boleh kosong!")

            daftar_perjalanan["Nama"].append(user_login)
            daftar_perjalanan["Nama Perjalanan"].append(nama_perjalanan)
            daftar_perjalanan["Destinasi"].append(destinasi)
            daftar_perjalanan["Tanggal"].append(tanggal)
            daftar_perjalanan["Durasi"].append(durasi)
            daftar_perjalanan["Budget"].append(budget)
            daftar_perjalanan["Cerita"].append(cerita)
            daftar_perjalanan["Rating"].append(star)

            print("\nPerjalanan berhasil dicatat!")
            input("\nTekan Enter untuk kembali ke menu...")
            return

        except ValueError as e:
            print(e)
            pertanyaan = [
            inquirer.List('menu',
                        message="apa ingin mengisi ulang?",
                        choices=[
                            'ya',
                            'tidak'
                        ],
                        ),
        ]
            jawaban = inquirer.prompt(pertanyaan)
            if jawaban is None:
                return
            if jawaban['menu'] == 'ya':
                continue
            elif jawaban['menu'] == 'tidak':
                return


def update() -> None:
    while True:
        clear_screen()
        print("=" * 60)
        print("EDIT REVIEW SAYA")
        print("=" * 60)
        try:
            perjalanan_saya = [
                i
                for i in range(len(daftar_perjalanan["Nama"]))
                if daftar_perjalanan["Nama"][i] == user_login
            ]
            if not perjalanan_saya:
                raise ValueError("Belum ada perjalanan yang bisa diedit.")
            
            print("\nDaftar Perjalanan:")
            print("-" * 100)
            print(f"{'No':<4} {'Nama Perjalanan':<25} {'Destinasi':<20} {'Tanggal':<12} {'Durasi':<10} {'Budget':<15}")
            print("-" * 100)
            
            for nomor, idx in enumerate(perjalanan_saya, start=1):
                print(f"{nomor:<4} {daftar_perjalanan['Nama Perjalanan'][idx]:<25} "
                      f"{daftar_perjalanan['Destinasi'][idx]:<20} "
                      f"{daftar_perjalanan['Tanggal'][idx]:<12} "
                      f"{daftar_perjalanan['Durasi'][idx]:<10} "
                      f"Rp {daftar_perjalanan['Budget'][idx]:<12}")
            print("-" * 100)
            
            pilih_edit = input("\nPilih nomor perjalanan yang mau diedit (atau ketik 'batal'): ").strip()
            if pilih_edit.lower() == "batal":
                break
            if not pilih_edit.isdigit():
                raise ValueError("Input harus berupa angka!")
            pilihan_edit = int(pilih_edit) - 1
            if pilihan_edit < 0 or pilihan_edit >= len(perjalanan_saya):
                raise ValueError("Nomor perjalanan tidak valid!")
            
            index_dict = perjalanan_saya[pilihan_edit]
            clear_screen()
            print("=" * 60)
            print("EDIT REVIEW")
            print("=" * 60)
            
            nama_sekarang = daftar_perjalanan["Nama Perjalanan"][index_dict]
            destinasi_sekarang = daftar_perjalanan["Destinasi"][index_dict]
            tanggal_sekarang = daftar_perjalanan["Tanggal"][index_dict]
            durasi_sekarang = daftar_perjalanan["Durasi"][index_dict]
            budget_sekarang = daftar_perjalanan["Budget"][index_dict]
            cerita_sekarang = daftar_perjalanan["Cerita"][index_dict]
            
            print("\nReview Perjalanan ini:")
            print("-" * 60)
            print(f"{'Nama Perjalanan':<20} : {nama_sekarang:<35}")
            print(f"{'Destinasi':<20} : {destinasi_sekarang:<35}")
            print(f"{'Tanggal':<20} : {tanggal_sekarang:<35}")
            print(f"{'Durasi':<20} : {durasi_sekarang:<35}")
            print(f"{'Budget':<20} : Rp {budget_sekarang:<32}")
            cerita_tampil = cerita_sekarang[:50] + "..." if len(cerita_sekarang) > 50 else cerita_sekarang
            print(f"{'Cerita':<20} : {cerita_tampil:<35}")
            print(f"{'Rating':<20} : {daftar_perjalanan['Rating'][index_dict]:<35}")
            print("-" * 60)
            
            print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")
            
            nama_baru = input(f"Nama Perjalanan [{nama_sekarang}]: ").strip()
            if nama_baru:
                daftar_perjalanan["Nama Perjalanan"][index_dict] = nama_baru
            
            destinasi_baru = input(f"Destinasi [{destinasi_sekarang}]: ").strip()
            if destinasi_baru:
                daftar_perjalanan["Destinasi"][index_dict] = destinasi_baru
            
            tanggal_baru = input(f"Tanggal Pergi [{tanggal_sekarang}]: ").strip()
            if tanggal_baru:
                daftar_perjalanan["Tanggal"][index_dict] = tanggal_baru
            
            durasi_baru = input(f"Durasi [{durasi_sekarang}]: ").strip()
            if durasi_baru:
                daftar_perjalanan["Durasi"][index_dict] = durasi_baru
            
            budget_baru = input(f"Budget [{budget_sekarang}]: ").strip()
            if budget_baru:
                if not budget_baru.isdigit():
                    raise ValueError("Budget harus berupa angka!")
                daftar_perjalanan["Budget"][index_dict] = budget_baru
            
            cerita_baru = input(f"Cerita [{cerita_sekarang}]: ").strip()
            if cerita_baru:
                daftar_perjalanan["Cerita"][index_dict] = cerita_baru

            rating_baru = input(f"Rating (1-5) [{daftar_perjalanan['Rating'][index_dict]}]: ").strip()
            if rating_baru:
                if rating_baru not in ['1', '2', '3', '4', '5']:
                    raise ValueError("Rating harus antara 1 sampai 5!")
                daftar_perjalanan["Rating"][index_dict] = rating_baru
            
            print("\n✓ Perjalanan berhasil diedit!")
            input("\nTekan Enter untuk kembali ke menu...")
            break 
        except ValueError as e:
            print(e)
            input("\nTekan Enter untuk mencoba lagi...")
            continue


def hapus() -> None:
    while True:
        clear_screen()
        print("=" * 60)
        print("HAPUS REVIEW")
        print("=" * 60)
        try:
            perjalanan_saya = [
                i
                for i in range(len(daftar_perjalanan["Nama"]))
                if daftar_perjalanan["Nama"][i] == user_login
            ]
            if not perjalanan_saya:
                raise ValueError("Belum ada perjalanan yang bisa dihapus.")
            
            print("\nDaftar Perjalanan:")
            print("-" * 100)
            print(f"{'No':<4} {'Nama Perjalanan':<25} {'Destinasi':<20} {'Tanggal':<12} {'Durasi':<10} {'Budget':<15} {'Rating':<10}")
            print("-" * 100)
            
            for nomor, idx in enumerate(perjalanan_saya, start=1):
                print(f"{nomor:<4} {daftar_perjalanan['Nama Perjalanan'][idx]:<25} "
                      f"{daftar_perjalanan['Destinasi'][idx]:<20} "
                      f"{daftar_perjalanan['Tanggal'][idx]:<12} "
                      f"{daftar_perjalanan['Durasi'][idx]:<10} "
                      f"Rp {daftar_perjalanan['Budget'][idx]:<12} "
                      f"{daftar_perjalanan['Rating'][idx]:<10}")
            print("-" * 100)
            
            pilih_hapus = input("\nPilih nomor perjalanan yang mau dihapus (atau ketik 'batal'): ").strip()
            if pilih_hapus.lower() == "batal":
                break
            if not pilih_hapus.isdigit():
                raise ValueError("Input harus berupa angka!")
            pilihan_hapus = int(pilih_hapus) - 1
            if pilihan_hapus < 0 or pilihan_hapus >= len(perjalanan_saya):
                raise ValueError("Nomor perjalanan tidak valid!")
            
            index_dict = perjalanan_saya[pilihan_hapus]
            konfirmasi = input(f"Yakin ingin menghapus perjalanan '{daftar_perjalanan['Nama Perjalanan'][index_dict]}'? (ya/tidak): ").strip().lower()
            if konfirmasi in ("ya", "y"):
                for key in daftar_perjalanan.keys():
                    del daftar_perjalanan[key][index_dict]
                print("\n✓ Perjalanan berhasil dihapus!")
            else:
                print("\nHapus perjalanan dibatalkan.")
            input("\nTekan Enter untuk kembali ke menu...")
            break
        except ValueError as e:
            print(e)
            input("\nTekan Enter untuk mencoba lagi...")
            continue


def out() -> bool:
    clear_screen()
    print("=" * 60)
    print("LOGOUT")
    print("=" * 60)

    pertanyaan = [
            inquirer.List('menu',
                        message="Yakin mau logout?",
                        choices=[
                            'ya, saya ingin logout',
                            'tidak jadi'
                        ],
                        ),
        ]
        
    try:
        jawaban = inquirer.prompt(pertanyaan)
        
        if jawaban is None:
            return True
        
        if jawaban['menu'] == 'ya, saya ingin logout':
            clear_screen()
            print("=" * 60)
            print("Logout berhasil!")
            print("=" * 60 + "\n")
            print("Terima kasih sudah menggunakan Jurnal Perjalanan")
            print("Kembali ke Menu Awal...")
            input("\nTekan Enter untuk melanjutkan...")
            return Menu_utama()
        
        elif jawaban['menu'] == 'tidak jadi':
            print("\nLogout dibatalkan.")
            input("\nTekan Enter untuk kembali...")
            menu_login()
            return False
                
    except KeyboardInterrupt:
        return True

   


if __name__ == "__main__":
    Menu_utama()