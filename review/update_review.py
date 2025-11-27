from datetime import datetime
import os, json, inquirer
from file_data.datajson import *

def update(username):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("\t\tEDIT REVIEW SAYA")
        print("=" * 60)

        data = baca_data_laporan()
        review_rute = data["review_rute"]

        try:
            perjalanan_saya = [i for i, r in enumerate(review_rute) if r["Nama"] == username]

            if not perjalanan_saya:
                raise ValueError("Belum ada perjalanan yang bisa diedit.")

            choices = []
            for nomor, idx in enumerate(perjalanan_saya, start=1):
                nama_perjalanan = review_rute[idx]["Destinasi"]
                choices.append((f"{nomor}. {nama_perjalanan}", idx))

            choices.append(("Batal", None))

            pertanyaan = [
                inquirer.List(
                    'pilihan', 
                    message="Pilih review yang ingin diedit :",
                    choices=choices
                )
            ]

            jawaban = inquirer.prompt(pertanyaan)
            index_dict = jawaban["pilihan"]

            if index_dict is None:
                return
            
            r = review_rute[index_dict]

            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 60)
            print("EDIT REVIEW")
            print("=" * 60)

            destinasi_sekarang = r["Destinasi"]
            tanggal_sekarang = r["Tanggal"]
            durasi_sekarang = r["Durasi"]
            budget_sekarang = r["Budget"]
            cerita_sekarang = r["Cerita"]
            rating_sekarang = r["Rating"]

            print("\nMasukkan data baru (tekan Enter untuk tidak mengubah):\n")

            destinasi_baru = input(f"Destinasi [{destinasi_sekarang}]: ").strip()
            if destinasi_baru:
                r["Destinasi"] = destinasi_baru

            tanggal_baru = input(f"Tanggal Pergi [{tanggal_sekarang}] (DD/MM/YYYY): ").strip()
            if tanggal_baru:
                try:
                    datetime.strptime(tanggal_baru, "%d/%m/%Y")
                except ValueError:
                    raise ValueError("Format tanggal salah! Gunakan format DD/MM/YYYY.")
                r["Tanggal"] = tanggal_baru
                
            durasi_baru = input(f"Durasi [{durasi_sekarang}]: ").strip()
            if durasi_baru:
                r["Durasi"] = durasi_baru

            budget_baru = input(f"Budget [{budget_sekarang}]: ").strip()
            if budget_baru:
                if not budget_baru.isdigit():
                    raise ValueError("Budget harus berupa angka!")
                r["Budget"] = budget_baru

            cerita_baru = input(f"Cerita [{cerita_sekarang}]: ").strip()
            if cerita_baru:
                r["Cerita"] = cerita_baru

            rating_baru = input(f"Rating (1-5) [{rating_sekarang}]: ").strip()
            if rating_baru:
                if rating_baru not in ['1','2','3','4','5']:
                    raise ValueError("Rating harus antara 1-5!")
                r["Rating"] = rating_baru

            with open("file_data/data_laporan.json", "w") as file:
                json.dump(data, file, indent=4)

            print("\n✓ Review berhasil diedit!")
            input("\nTekan Enter untuk kembali...")
            return

        except ValueError as e:
            print(e)
            input("\nTekan Enter Untuk Kembali...")
            continue
