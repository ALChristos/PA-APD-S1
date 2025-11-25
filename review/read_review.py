import os
import inquirer
from review.review_rute import review

def daftar():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    
    perjalanan = []
    
    if jawaban['mode'] == 'Lihat Semua Review':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("SEMUA REVIEW")
        print("=" * 60)
        for i in range(len(daftar_perjalanan["Nama"])):
            perjalanan.append(i)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print(f"REVIEW {user_login.upper()}")
        print("=" * 60)
        for i in range(len(daftar_perjalanan["Nama"])):
            if daftar_perjalanan["Nama"][i] == user_login:
                perjalanan.append(i)
    
    if len(perjalanan) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nAnda belum memberikan review.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
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

    if jawaban['mode'] == 'Review Perjalanan':
        daftar()
    elif jawaban['mode'] == 'Menu Review':
        review()