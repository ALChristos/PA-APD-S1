import os, inquirer, prettytable
from file_data.datajson import *
from review.create_review import bintang

def daftar(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("REVIEW PERJALANAN")
    print("=" * 60)

    data = baca_data_laporan()
    laporan_review = data["review_rute"]

    pertanyaan = [
        inquirer.List(
            'mode',
            message="Review mana yang ingin dilihat?",
            choices=['Lihat Review Saya', 'Lihat Semua Review']
        )
    ]
    
    jawaban = inquirer.prompt(pertanyaan)
    
    perjalanan = []

    for item in laporan_review:  
        if jawaban['mode'] == 'Lihat Semua Review':
            perjalanan.append(item)
        elif jawaban['mode'] == 'Lihat Review Saya':
            if item["Nama"] == username:
                perjalanan.append(item)


    if len(perjalanan) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            "\nAnda belum memberikan review."
            if jawaban['mode'] == "Lihat Review Saya"
            else "\nBelum ada pengguna yang memberikan review."
        )
        input("Tekan Enter Untuk Kembali...")
        return

    os.system('cls' if os.name == 'nt' else 'clear')

    if jawaban["mode"] == "Lihat Semua Review":
        print("=" * 60)
        print("SEMUA REVIEW")
    else:
        print("=" * 60)
        print(f"REVIEW {username.upper()}")
    print("=" * 60)
    print()
    tabel = prettytable.PrettyTable()
    tabel.field_names = [
        "Nama", "Nama Perjalanan", "Destinasi",
        "Tanggal", "Durasi", "Budget", "Cerita", "Rating"
    ]

    for r in perjalanan:
        tabel.add_row([
            r["Nama"],
            r["Nama Perjalanan"],
            r["Destinasi"],
            r["Tanggal"],
            r["Durasi"],
            r["Budget"],
            r["Cerita"],
            bintang(r["Rating"])
        ])

    print(tabel)
    input("\nTekan Enter untuk kembali...")
    os.system("cls" if os.name == "nt" else "clear")
    return
