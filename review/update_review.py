from prettytable import PrettyTable
import os, json
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

            table = PrettyTable()
            table.field_names = ["No", "Nama Perjalanan", "Destinasi", "Tanggal", "Durasi", "Budget", "Rating"]

            for nomor, idx in enumerate(perjalanan_saya, start=1):
                r = review_rute[idx]
                table.add_row([
                    nomor,
                    r['Nama Perjalanan'],
                    r['Destinasi'],
                    r['Tanggal'],
                    r['Durasi'],
                    f"Rp {r['Budget']}",
                    r['Rating']
                ])

            print("\nDaftar Perjalanan Saya:")
            print(table)

            pilih_edit = input("\nPilih nomor review yang mau diedit (atau ketik 'batal'): ").strip()
            if pilih_edit.lower() == "batal":
                return

            if not pilih_edit.isdigit():
                raise ValueError("Input harus berupa angka!")

            pilihan_edit = int(pilih_edit) - 1
            if pilihan_edit < 0 or pilihan_edit >= len(perjalanan_saya):
                raise ValueError("Nomor perjalanan tidak valid!")

            index_dict = perjalanan_saya[pilihan_edit]
            r = review_rute[index_dict]

            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 60)
            print("EDIT REVIEW")
            print("=" * 60)

            nama_sekarang = r["Nama Perjalanan"]
            destinasi_sekarang = r["Destinasi"]
            tanggal_sekarang = r["Tanggal"]
            durasi_sekarang = r["Durasi"]
            budget_sekarang = r["Budget"]
            cerita_sekarang = r["Cerita"]
            rating_sekarang = r["Rating"]

            print("\nMasukkan data baru (tekan Enter untuk tidak mengubah):")

            nama_baru = input(f"Nama Perjalanan [{nama_sekarang}]: ").strip()
            if nama_baru:
                r["Nama Perjalanan"] = nama_baru

            destinasi_baru = input(f"Destinasi [{destinasi_sekarang}]: ").strip()
            if destinasi_baru:
                r["Destinasi"] = destinasi_baru

            tanggal_baru = input(f"Tanggal Pergi [{tanggal_sekarang}]: ").strip()
            if tanggal_baru:
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
            return
