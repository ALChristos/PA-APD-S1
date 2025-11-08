import inquirer
import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

def menu_login() -> None:
    while True:
        clear()
        print("=" * 60)
        print(f"User: {data.user_login}")
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
                Menu_utama()
                break
                    
        except KeyboardInterrupt:
            if Menu_utama():
                break

def review() -> None:
    while True:
        clear()
        print("=" * 60)
        print(f"User: {data.user_login}")
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
    clear()
    print("=" * 60)
    print("DAFTAR PERJALANAN")
    print("=" * 60)
    
    questions = [
        inquirer.List('mode',
                     message="Pilih mode tampilan",
                     choices=['Lihat Review Saya', 'Lihat Semua Review'],
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    
    if answers is None:
        return
    
    perjalanan = []
    
    if answers['mode'] == 'Lihat Semua Review':

        print("\n" + "=" * 60)
        print("SEMUA REVIEW")
        print("=" * 60)
        for i in range(len(daftar_perjalanan["Nama"])):
            perjalanan.append(i)
    else:
        
        print("\n" + "=" * 60)
        print(f"PERJALANAN {data.user_login.upper()}")
        print("=" * 60)
        for i in range(len(daftar_perjalanan["Nama"])):
            if daftar_perjalanan["Nama"][i] == data.user_login:
                perjalanan.append(i)
    
    if len(perjalanan) == 0:
        print("\nBelum ada Review yang tercatat.")
    else:
        print()
        nomor = 1
        for idx in perjalanan:
            print(f"\n{'─' * 60}")
            print(f"[{nomor}] PERJALANAN")
            print(f"{'─' * 60}")

            if answers['mode'] == 'Lihat Semua Perjalanan (Multiuser)':
                print(f"User              : {daftar_perjalanan['Nama'][idx]}")
            
            print(f"Nama Perjalanan   : {daftar_perjalanan['Nama Perjalanan'][idx]}")
            print(f"Destinasi         : {daftar_perjalanan['Destinasi'][idx]}")
            print(f"Tanggal           : {daftar_perjalanan['Tanggal'][idx]}")
            print(f"Durasi            : {daftar_perjalanan['Durasi'][idx]}")
            print(f"Budget            : Rp {daftar_perjalanan['Budget'][idx]:,}")
            print(f"Cerita            : {daftar_perjalanan['Cerita'][idx]}")
            star = int(daftar_perjalanan["Rating"][idx])
            print("Rating             : " + "★" * star + "☆" * (5 - star))
            
            nomor += 1
        
        print(f"\n{'─' * 60}")
        print(f"Total: {len(perjalanan)} perjalanan")
        print(f"{'─' * 60}")
    
    input("\nTekan Enter untuk kembali...")

def catat() -> None:
    while True:
        clear()
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
                raise ValueError("\nRating harus antara 1 sampai 5!")

            daftar_perjalanan["Nama"].append(data.user_login)
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
            ulang = input("\nCoba isi lagi? (ya/tidak): ").strip().lower()
            if ulang in ("ya", "y"):
                continue
            else:
                return