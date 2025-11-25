import os
import inquirer

def hapus():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("HAPUS REVIEW SAYA")
        print("=" * 60)

        perjalanan_saya = [
            i for i in range(len(daftar_perjalanan["Nama"]))
            if daftar_perjalanan["Nama"][i] == login_akun
        ]

        if not perjalanan_saya:
            print("\nTidak ada review yang bisa dihapus.")
            input("\nTekan Enter untuk kembali...")
            return


        choices = []
        for nomor, idx in enumerate(perjalanan_saya, start=1):
            nama = daftar_perjalanan["Nama Perjalanan"][idx]
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

        nama = daftar_perjalanan["Nama Perjalanan"][index_dict]

        konfirmasi = [
            inquirer.List(
                'pilih',
                message=f"Yakin ingin menghapus '{nama}'?",
                choices=['Iya', 'Tidak']
            )
        ]

        jawab = inquirer.prompt(konfirmasi)

        if jawab['pilih'] == 'Iya':
        
            for key in daftar_perjalanan:
                daftar_perjalanan[key].pop(index_dict)

            print("\n✓ Review berhasil dihapus!")
        else:
            print("\nPenghapusan dibatalkan.")

        input("\nTekan Enter untuk kembali...")
        return
