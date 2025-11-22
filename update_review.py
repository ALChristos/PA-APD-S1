import os

def update() -> None:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("EDIT REVIEW SAYA")
        print("=" * 60)
        try:
            perjalanan_saya = [
                i
                for i in range(len(daftar_perjalanan["Nama"]))
                if daftar_perjalanan["Nama"][i] == user_login
            ]
            if not perjalanan_saya:
                raise ValueError("Belum ada perjalanan yang bisa diedit.")
            
            print("\nDaftar Perjalanan:")
            print("-" * 100)
            print(f"{'No':<4} {'Nama Perjalanan':<25} {'Destinasi':<20} {'Tanggal':<12} {'Durasi':<10} {'Budget':<15}")
            print("-" * 100)
            
            for nomor, idx in enumerate(perjalanan_saya, start=1):
                print(f"{nomor:<4} {daftar_perjalanan['Nama Perjalanan'][idx]:<25} "
                      f"{daftar_perjalanan['Destinasi'][idx]:<20} "
                      f"{daftar_perjalanan['Tanggal'][idx]:<12} "
                      f"{daftar_perjalanan['Durasi'][idx]:<10} "
                      f"Rp {daftar_perjalanan['Budget'][idx]:<12}")
            print("-" * 100)
            
            pilih_edit = input("\nPilih nomor perjalanan yang mau diedit (atau ketik 'batal'): ").strip()
            if pilih_edit.lower() == "batal":
                break
            if not pilih_edit.isdigit():
                raise ValueError("Input harus berupa angka!")
            pilihan_edit = int(pilih_edit) - 1
            if pilihan_edit < 0 or pilihan_edit >= len(perjalanan_saya):
                raise ValueError("Nomor perjalanan tidak valid!")
            
            index_dict = perjalanan_saya[pilihan_edit]
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 60)
            print("EDIT REVIEW")
            print("=" * 60)
            
            nama_sekarang = daftar_perjalanan["Nama Perjalanan"][index_dict]
            destinasi_sekarang = daftar_perjalanan["Destinasi"][index_dict]
            tanggal_sekarang = daftar_perjalanan["Tanggal"][index_dict]
            durasi_sekarang = daftar_perjalanan["Durasi"][index_dict]
            budget_sekarang = daftar_perjalanan["Budget"][index_dict]
            cerita_sekarang = daftar_perjalanan["Cerita"][index_dict]
            
            print("\nReview Perjalanan ini:")
            print("-" * 60)
            print(f"{'Nama Perjalanan':<20} : {nama_sekarang:<35}")
            print(f"{'Destinasi':<20} : {destinasi_sekarang:<35}")
            print(f"{'Tanggal':<20} : {tanggal_sekarang:<35}")
            print(f"{'Durasi':<20} : {durasi_sekarang:<35}")
            print(f"{'Budget':<20} : Rp {budget_sekarang:<32}")
            cerita_tampil = cerita_sekarang[:50] + "..." if len(cerita_sekarang) > 50 else cerita_sekarang
            print(f"{'Cerita':<20} : {cerita_tampil:<35}")
            print(f"{'Rating':<20} : {daftar_perjalanan['Rating'][index_dict]:<35}")
            print("-" * 60)
            
            print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")
            
            nama_baru = input(f"Nama Perjalanan [{nama_sekarang}]: ").strip()
            if nama_baru:
                daftar_perjalanan["Nama Perjalanan"][index_dict] = nama_baru
            
            destinasi_baru = input(f"Destinasi [{destinasi_sekarang}]: ").strip()
            if destinasi_baru:
                daftar_perjalanan["Destinasi"][index_dict] = destinasi_baru
            
            tanggal_baru = input(f"Tanggal Pergi [{tanggal_sekarang}]: ").strip()
            if tanggal_baru:
                daftar_perjalanan["Tanggal"][index_dict] = tanggal_baru
            
            durasi_baru = input(f"Durasi [{durasi_sekarang}]: ").strip()
            if durasi_baru:
                daftar_perjalanan["Durasi"][index_dict] = durasi_baru
            
            budget_baru = input(f"Budget [{budget_sekarang}]: ").strip()
            if budget_baru:
                if not budget_baru.isdigit():
                    raise ValueError("Budget harus berupa angka!")
                daftar_perjalanan["Budget"][index_dict] = budget_baru
            
            cerita_baru = input(f"Cerita [{cerita_sekarang}]: ").strip()
            if cerita_baru:
                daftar_perjalanan["Cerita"][index_dict] = cerita_baru

            rating_baru = input(f"Rating (1-5) [{daftar_perjalanan['Rating'][index_dict]}]: ").strip()
            if rating_baru:
                if rating_baru not in ['1', '2', '3', '4', '5']:
                    raise ValueError("Rating harus antara 1 sampai 5!")
                daftar_perjalanan["Rating"][index_dict] = rating_baru
            
            print("\n✓ Perjalanan berhasil diedit!")
            input("\nTekan Enter untuk kembali ke menu...")
            break 
        except ValueError as e:
            print(e)
            input("\nTekan Enter untuk mencoba lagi...")
            continue