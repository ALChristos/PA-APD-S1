import os
import inquirer
from file_data.datajson import *

def catat(username): 
    os.system('cls' if os.name == 'nt' else 'clear')
    data = baca_data_laporan()
    data_review = data["review_rute"]
    while True:
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

            tambah_review ={
                "Nama": username,
                "Nama Perjalanan": nama_perjalanan,
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
                os.system('cls' if os.name == 'nt' else 'clear')

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
            
            if jawaban['menu'] == 'ya':
                continue
            elif jawaban['menu'] == 'tidak':
                return