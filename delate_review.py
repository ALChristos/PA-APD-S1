def hapus() -> None:
    import os

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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