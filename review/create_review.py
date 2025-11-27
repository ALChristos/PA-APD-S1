import os, inquirer, json
from datetime import datetime
from file_data.datajson import *
from pack_member.menu_member import *

def bintang(rating):
    rating = int(rating)
    return "★" * rating + "☆" * (5 - rating)

def catat(username, kota_1, kota_tujuan): 
    os.system('cls' if os.name == 'nt' else 'clear')
    data = baca_data_laporan()
    data_review = data["review_rute"]

    while True:
        print("=" * 60)
        print("MASUKAN REVIEW")
        print("=" * 60)

        try:

            destinasi = input("Destinasi : ").strip()
            if not destinasi:
                raise ValueError("\nDestinasi tidak boleh kosong!")

            tanggal = input("Tanggal Pergi (DD/MM/YYYY): ").strip()
            try:
                datetime.strptime(tanggal, "%d/%m/%Y")
            except ValueError:
                raise ValueError("\nFormat tanggal salah! Gunakan format DD/MM/YYYY")
            
            durasi = input("Berapa Lama : ").strip()
            if not durasi:
                raise ValueError("\nDurasi tidak boleh kosong!")

            budget = input("Budget (angka saja) : ").strip()
            if not budget.isdigit():
                raise ValueError("\nBudget harus berupa angka!")

            cerita = input("Cerita/Experience : ").strip()

            star = input("Rating (1-5) : ").strip()
            if star not in ['1','2','3','4','5']:
                raise ValueError("\nRating harus 1-5!")

            tambah_review ={
                "Nama": username,
                "Nama Perjalanan": f"{kota_1}-{kota_tujuan}",
                "Destinasi": destinasi,
                "Tanggal": tanggal,
                "Durasi": durasi,
                "Budget": budget,
                "Cerita": cerita,
                "Rating": star
            }

            data_review.append(tambah_review)

            with open('file_data/data_laporan.json', 'w') as file:
                json.dump(data, file, indent=4)

            print("\nReview berhasil ditambahkan!")
            input("\nTekan Enter untuk kembali...")
            return

        except ValueError as e:
            print(e)

            pertanyaan = [
                inquirer.List('menu',
                    message="Apa ingin mengisi ulang?",
                    choices=['ya', 'tidak']
                )
            ]
            jawaban = inquirer.prompt(pertanyaan)

            if jawaban['menu'] == 'ya':
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                return