import os, json, inquirer
from file_data.datajson import *

def hapus(username):
    data = baca_data_laporan()
    review_rute = data["review_rute"]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("HAPUS REVIEW SAYA")
        print("=" * 60)

        perjalanan_saya = []
        for i in range(len(review_rute)):
            if review_rute[i]["Nama"] == username:
                perjalanan_saya.append(i)

        if not perjalanan_saya:
            print("\nTidak ada review yang bisa dihapus.")
            input("\nTekan Enter untuk kembali...")
            return

        choices = []
        for nomor, idx in enumerate(perjalanan_saya, start=1):
            nama = review_rute[idx]["Destinasi"]
            choices.append((f"{nomor}. {nama}", idx))

        choices.append(("Batal", None))

        pertanyaan = [
            inquirer.List(
                'review',
                message="Pilih review yang ingin dihapus:",
                choices=choices
            )
        ]

        pilih = inquirer.prompt(pertanyaan)
        index_dict = pilih["review"]

        if index_dict is None:
            return

        nama = review_rute[index_dict]["Destinasi"]
        konfirmasi = [
            inquirer.List(
                'pilih',
                message=f"Yakin ingin menghapus '{nama}'?",
                choices=['Iya', 'Tidak']
            )
        ]
        jawab = inquirer.prompt(konfirmasi)

        if jawab['pilih'] == 'Iya':
            review_rute.pop(index_dict)

            with open('file_data/data_laporan.json', 'w') as f:
                json.dump(data, f, indent=4)

            print("\n✓ Review berhasil dihapus!")
        else:
            print("\nPenghapusan dibatalkan.")

        input("\nTekan Enter untuk kembali...")
        return
