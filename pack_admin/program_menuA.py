from pack_admin.daftar_kota import kota_awal, kota_tujuan
from prettytable import PrettyTable
from file_data.datajson import *
from pesan import *

import os, prettytable
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def membuat_rute_perjalanan():
    data = baca_data_perjalanan()
    kota_1 = kota_awal()
    
    rute_sudah_ada = [kota["rute"].split("-")[1] for kota in data[kota_1]]
    semua_kota = [kota for kota in data.keys() if kota != kota_1]
    kota_tersisa = [kota for kota in semua_kota if kota not in rute_sudah_ada]
    if not kota_tersisa:
        print(f"\nSemua kota tujuan untuk kota {kota_1} sudah dibuat.")
        print("Tidak ada rute baru yang bisa dibuat dari kota ini.\n")
        input("Tekan Enter Untuk Kembali Ke Menu Mengelola Rute Perjalnan...")
        clear()
        return

    kota_2 = kota_tujuan(kota_1, list_kota = rute_sudah_ada)
    tambah_rute = data[kota_1]
    rute = f"{kota_1}-{kota_2}"
    rute_kebalikan = f"{kota_2}-{kota_1}"
    jarak_otomatis = None

    for daftar_kota in data.values():
        for i in daftar_kota :
            if i["rute"] == rute_kebalikan:
                jarak_otomatis = i["jarak_tempuh"]
                break
        if jarak_otomatis is not None:
            break

    while True:
        if jarak_otomatis is not None:
            jarak_tempuh = jarak_otomatis
            rute_baru = {
                    "rute": rute,
                    "jarak_tempuh": jarak_tempuh,
                    "status" : "Aman"
                    }
            
            tambah_rute.append(rute_baru)
            with open("file_data/data_perjalanan.json", "w") as file:
                json.dump(data, file, indent = 4)
                
            print(f"\nRute Yang Sama Ditemukan ({rute_kebalikan}).")
            print(f"Jarak Otomatis Digunakan: {jarak_tempuh} km\n")
            input("Tekan Enter Untuk Kembali Ke Menu Mengelola Rute Perjalanan...")
            clear()
            break
        
        else:
            jarak_tempuh = input("Masukkan Jarak Tempuh (dalam km): ").strip()
            try:
                jarak_tempuh = float(jarak_tempuh)
                
                if jarak_tempuh <100:
                    print("Jarak Tidak Boleh Kurang Dari 100km")
                    input("Tekan Enter Untuk Menginput Ulang...")
                    clear()
                    continue
                    
                rute_baru = {
                    "rute": rute,
                    "jarak_tempuh": jarak_tempuh,
                    "status" : "aman"
                    }
                tambah_rute.append(rute_baru)
                with open("file_data/data_perjalanan.json", "w") as file:
                    json.dump(data, file, indent = 4)
                
                while True:
                    print(f"Rute Perjalanan Baru Telah Ditambahkan: {rute}\n")
                    ulang = input("Apakah Anda Ingin Membuat Rute Baru Lagi? (Y/N)").strip()
                    if ulang.lower() == "y":
                        detik5() 
                        clear()
                        return membuat_rute_perjalanan()
                    elif ulang.lower() == "n":
                        print("\nKembali Ke Menu Mengelola Rute Perjalanan")
                        detik5() 
                        clear()
                        return
                    else:
                        print("\nMasukan Input Sesuai Intruksi Yang Diberikan!!")
                        detik5()
                        clear()
                        continue
                        
                        
            except ValueError:
                print("Input jarak tempuh tidak valid. Harap masukkan angka saja.")
                input("Tekan Enter Untuk Menginput Ulang")
                clear()
                continue
    
                
def melihat_rute_perjalanan():
    data_perjalanan = baca_data_perjalanan()
    clear()
    print("=" * 70)
    print("📍 DAFTAR RUTE PERJALANAN".center(70))
    print("=" * 70)
    if len(data_perjalanan.keys()) < 1:
        print("\nBelum Ada Data Rute Perjalanan!")
        input("\nTekan Enter untuk kembali...")
        clear()
        return

    for kota, daftar in data_perjalanan.items():
        print(f"\nKota: {kota}")
        table = PrettyTable()
        table.field_names = ["No", "Rute", "Jarak (km)", "Status"]
        if len(daftar) == 0:
            table.add_row(["-", "(Tidak ada rute)", "-", "-"])
        else:
            for idx, r in enumerate(daftar, start=1):
                table.add_row([
                    idx,
                    r["rute"],
                    r["jarak_tempuh"],
                    r["status"]
                ])

        print(table)

    input("\nTekan Enter untuk kembali...")
    clear()


def menghapus_rute_perjalanan():
    data_perjalanan = baca_data_perjalanan()
    data_laporan = baca_data_laporan()

    review_list = data_laporan["review_rute"]

    if len(data_perjalanan.keys()) < 1:
        print("Belum Ada Data Rute Perjalanan!")
        input("Tekan Enter untuk kembali...")
        clear()
        return

    while True:
        clear()
        print("=" * 60)
        print("\t\tMENGHAPUS RUTE PERJALANAN")
        print("=" * 60)

        for kota, daftar in data_perjalanan.items():
            print(f"\nKota: {kota}")
            table = PrettyTable()
            table.field_names = ["No", "Rute", "Jarak (km)", "Status"]
            if len(daftar) == 0:
                table.add_row(["-", "(Tidak ada rute)", "-", "-"])
            else:
                for idx, r in enumerate(daftar, start=1):
                    table.add_row([
                        idx,
                        r["rute"],
                        r["jarak_tempuh"],
                        r["status"]
                    ])
            print(table)

        print("\nFormat input:")
        print("     NamaKota-IndexRute    ")
        print("Contoh: Balikpapan-1")

        pilihan = input("\nMasukkan Rute Yang Ingin Dihapus: ").strip()

        if "-" not in pilihan:
            print("\nFormat salah! Contoh: Balikpapan-1")
            input("Tekan Enter untuk ulangi...")
            continue

        kota, idx = pilihan.split("-")
        kota = kota.strip()

        if kota not in data_perjalanan:
            print("\nKota tidak ditemukan!")
            input("Tekan Enter untuk ulangi...")
            continue

        try:
            idx = int(idx) - 1
        except:
            print("\nIndex rute harus angka!")
            input("Tekan Enter untuk ulangi...")
            continue

        daftar_rute = data_perjalanan[kota]

        if idx < 0 or idx >= len(daftar_rute):
            print("\nIndex rute tidak valid!")
            input("Tekan Enter untuk ulangi...")
            continue

        rute_dihapus = daftar_rute[idx]
        nama_rute = rute_dihapus["rute"]
        kota_1, kota_2 = nama_rute.split("-")
        rute_kebalikan = f"{kota_2}-{kota_1}"

        konfirmasi = input(
            f"Yakin ingin menghapus rute '{nama_rute}' beserta rute kebalikannya '{rute_kebalikan}'? (Y/N): "
        ).strip().lower()

        if konfirmasi == "n":
            print("Penghapusan dibatalkan...")
            detik3()
            clear()
            return

        elif konfirmasi != "y":
            print("Input tidak valid, masukkan Y/N!")
            input("Tekan Enter...")
            continue

        daftar_rute.pop(idx)
        if kota_2 in data_perjalanan:
            for i, item in enumerate(data_perjalanan[kota_2]):
                if item["rute"] == rute_kebalikan:
                    data_perjalanan[kota_2].pop(i)
                    break

        review_list[:] = [
            r for r in review_list
            if r["Nama Perjalanan"] not in [nama_rute, rute_kebalikan]
        ]

        for r in [nama_rute, rute_kebalikan]:
            if r in data_laporan.get("laporan_status", {}):
                del data_laporan["laporan_status"][r]

        with open("file_data/data_perjalanan.json", "w") as f:
            json.dump(data_perjalanan, f, indent=4)

        with open("file_data/data_laporan.json", "w") as f:
            json.dump(data_laporan, f, indent=4)

        print(f"\nRute '{nama_rute}' dan rute kebalikannya '{rute_kebalikan}' BERHASIL dihapus!")
        print("Semua review dan laporan masalah terkait juga telah dihapus.")
        input("Tekan Enter untuk kembali...")
        clear()
        return

 
   
def melihat_dan_menghapus_review_pengguna(konfirmasi_awal=False):
    data = baca_data_laporan()
    review = data["review_rute"]

    clear()
    print("=" * 60)
    print("\t\tMELIHAT REVIEW PENGGUNA")
    print("=" * 60)

    if len(review) < 1:
        print("Tidak Ada Review Pengguna Yang Terdeteksi!!")
        input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Review Pengguna...")
        detik3()
        clear()
        return

    for idx, r in enumerate(review):
        print(f"ID Review           : {idx+1}")
        print(f"Nama                : {r['Nama']}")
        print(f"Nama Perjalanan     : {r['Nama Perjalanan']}")
        print(f"Destinasi           : {r['Destinasi']}")
        print(f"Tanggal             : {r['Tanggal']}")
        print(f"Durasi              : {r['Durasi']}")
        print(f"Budget              : {r['Budget']}")
        print(f"Cerita              : {r['Cerita']}")
        print(f"Rating              : {r['Rating']}")
        print("-" * 60)

    if not konfirmasi_awal:
        pilihan = input("Apakah Anda Ingin Menghapus Review Dari Daftar Ini? (Y/N): ").strip().lower()
        if pilihan == "n":
            print("\nKembali Ke Menu Mengelola Review Pengguna...")
            detik3()
            clear()
            return

        elif pilihan == "y":
            if len(review) < 1:
                print("Semua Review Sudah Dihapus!!")
                input("\nTekan Enter Untuk Kembali...")
                detik3()
                clear()
                return
        else:
            print("\nInput Tidak Valid! Masukkan Y atau N.")
            input("Tekan Enter Untuk Menginput Ulang...")
            clear()
            return melihat_dan_menghapus_review_pengguna(konfirmasi_awal=False)

    while True:
        clear()
        print("=" * 60)
        print("\t\tMENGHAPUS REVIEW PENGGUNA")
        print("=" * 60)

        for idx, r in enumerate(review):
            print(f"{idx+1}. Nama: {r['Nama']} | Perjalanan: {r['Nama Perjalanan']} | Rating: {r['Rating']}")

        hapus_id = input("\nMasukkan ID Review Yang Ingin Anda Hapus: ").strip()

        try:
            hapus_id = int(hapus_id)
            index = hapus_id - 1

            if index < 0 or index >= len(review):
                print("\nID tidak ditemukan!")
                input("Tekan Enter untuk ulangi...")
                clear()
                continue

            review_dihapus = review[index]

            while True:
                konfirmasi = input(
                    f"Apakah Anda Yakin Ingin Menghapus Review Dari Pengguna {review_dihapus['Nama']}? (Y/N): "
                ).strip().lower()

                if konfirmasi == "y":
                    review.pop(index)

                    with open("file_data/data_laporan.json", "w") as file:
                        json.dump(data, file, indent=4)

                    print(f"\nReview Dari Pengguna {review_dihapus['Nama']} Berhasil Dihapus!!")

                    while True:
                        ulang = input("Apakah Anda Ingin Menghapus Review Lagi? (Y/N): ").strip().lower()
                        if ulang == "y":
                            return melihat_dan_menghapus_review_pengguna(konfirmasi_awal=True)

                        elif ulang == "n":
                            print("Kembali Ke Menu Mengelola Review Pengguna...")
                            detik3()
                            clear()
                            return

                        else:
                            print("Masukkan pilihan Y atau N!")
                            input("Tekan Enter Untuk Menginput Ulang...")
                            clear()

                elif konfirmasi == "n":
                    print("\nPenghapusan Dibatalkan.")
                    input("Tekan Enter Untuk Kembali...")
                    clear()
                    return

                else:
                    print("Masukkan pilihan Y atau N!")
                    input("Tekan Enter Untuk Menginput Ulang...")
                    clear()
                    continue

        except ValueError:
            print("\nInput Tidak Valid!! ID Harus Berupa Angka!!")
            input("Tekan Enter Untuk Menginput Ulang...")
            detik3()
            clear()
            continue
   

def tangani_rute():
    data_rute = baca_data_perjalanan()
    laporan = baca_data_laporan()
    laporan_status = laporan.get("laporan_status", {})

    rute_masalah = {k: v for k, v in laporan_status.items() if v != "Aman"}

    if not rute_masalah:
        print("\nSemua rute dalam kondisi AMAN.\n")
        input("Tekan Enter Untuk Kembali Ke Menu...")
        os.system("cls" if os.name == "nt" else "clear")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Rute", "Status"]
    for idx, (rute, status) in enumerate(rute_masalah.items(), start=1):
        tabel.add_row([idx, rute, status])

    while True:
        print("\n⚠ Rute Bermasalah Saat Ini:")
        print(tabel)
        try:
            pilihan = int(input("\nMasukkan nomor rute yang ingin ditangani (0 untuk batal): "))
            if pilihan == 0:
                print("Tidak ada rute yang ditangani.")
                input("Tekan Enter Untuk Kembali Ke Menu...")
                os.system("cls" if os.name == "nt" else "clear")
                return
            if not (1 <= pilihan <= len(rute_masalah)):
                print("Nomor tidak valid!")
                input("Tekan Enter Untuk Kembali Ke Menu...")
                os.system("cls" if os.name == "nt" else "clear")
                continue
        except ValueError:
            print("Input harus angka!")
            input("Tekan Enter Untuk Kembali Ke Menu...")
            os.system("cls" if os.name == "nt" else "clear")
            continue

        rute_terpilih = list(rute_masalah.keys())[pilihan-1]
        kota_1, kota_2 = rute_terpilih.split("-")
        print(f"\n✔ Menangani rute: {rute_terpilih}")

        laporan_status[rute_terpilih] = "Aman"
        rute_kebalikan = f"{kota_2}-{kota_1}"
        if rute_kebalikan in laporan_status:
            laporan_status[rute_kebalikan] = "Aman"

        for item in data_rute[kota_1]:
            if item["rute"] == rute_terpilih:
                item["status"] = "Aman"
        if kota_2 in data_rute:
            for item in data_rute[kota_2]:
                if item["rute"] == rute_kebalikan:
                    item["status"] = "Aman"

        laporan["laporan_status"] = laporan_status
        with open("file_data/data_laporan.json", "w") as f:
            json.dump(laporan, f, indent=4)
        with open("file_data/data_perjalanan.json", "w") as f:
            json.dump(data_rute, f, indent=4)

        print(f"\n✔ Rute {rute_terpilih} dan {rute_kebalikan} berhasil dikembalikan ke status AMAN.")

        while True:
            konfirmasi = input("Apakah Anda Ingin Menangani Masalah Rute Lain? (Y/N) ").lower().strip()
            if konfirmasi == "y":
                os.system("cls" if os.name == "nt" else "clear")
                return tangani_rute()
            elif konfirmasi == "n":
                os.system("cls" if os.name == "nt" else "clear")
                return
            else:
                print("Input Tidak Valid Pilih Y/N Saja")
                input("Tekan Enter Untuk Menginput Ulang...")
                os.system("cls" if os.name == "nt" else "clear")
                continue
                        
          
def melihat_akun_pengguna(konfirmasi_awal = False):
    data = baca_data_akun()
    akun = data["member"]
    
    if len(akun) < 1:
        print("Tidak Ada Akun Pengguna Yang Terdeteksi!!")  
        input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
        detik3()
        clear()  
                
    table = PrettyTable()
    table.field_names = ["ID Akun", "Username Akun", "Passowrd Akun", "Status Akun"]
    for data_akun in akun:
        table.add_row([data_akun["id"], data_akun["username"], data_akun["password"], data_akun["status"]])
    print(table)
    
    if not konfirmasi_awal:
        pilihan = input("Apakah Anda Ingin Menghapus Akun Dari Daftar Ini? (Y/N)").strip().lower()
        if pilihan == "n":
            print("\nKembali Ke Menu Mengelola Akun Pengguna...")
            detik3()
            clear() 
            
        elif pilihan == "y":
            if len(akun) < 1:
                print("Semua Akun Pengguna Sudah Dihapus!!")  
                input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                detik3()
                clear()  
                
            while True:
                clear()  
                print(table)
                akun_hapus = input("Masukan ID Akun Yang Ingin Anda BAN: ").strip()
                try:
                    akun_hapus = int(akun_hapus)
                    akun_dihapus = next((i for i in akun if int(i["id"]) == akun_hapus), None)

                    if akun_dihapus is None:
                        print("\nID tidak ditemukan!")
                        input("Tekan Enter untuk ulangi...")
                        clear()
                        continue
                    
                    else:
                        while True:
                            konfirmasi = input(f"Apakah Anda Yakin Ingin Menghapus Akun {akun_dihapus["username"]}? (Y/N)").strip().lower()
                            if konfirmasi == "y":
                                index = akun.index(akun_dihapus)
                                akun.pop(index)
                                
                                with open("file_data/data_akun.json", "w") as file:
                                    json.dump(data, file, indent = 4)
                                    
                                print(f"\nAkun Dengan Username {akun_dihapus["username"]} Berhasil Dihapus!!")
                                while True:
                                    pilihan = input("Apakah Anda Ingin Menghapus Akun Lagi? (Y/N)").strip().lower()
                                    if pilihan == "y":
                                        return melihat_akun_pengguna(konfirmasi_awal = False)
                                    
                                    elif pilihan == "n":
                                        print("Kembali Ke Menu Mengelola Akun Pengguna...")
                                        detik3()
                                        clear()
                                        return
                                    else:
                                        print("\nMasukkan pilihan Y atau N!")
                                        input("Tekan Enter Untuk Menginput Ulang...")
                                        clear()
                                        continue  

                            elif konfirmasi == "n":
                                print("\nPenghapusan dibatalkan.")
                                input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                                clear()
                                return

                            else:
                                print("\nMasukkan pilihan Y atau N!")
                                input("Tekan Enter Untuk Menginput Ulang...")
                                clear()
                                continue
                
                except ValueError:
                    print("\nInput Tidak Valid!! ID Harus Berupa Angka!!")
                    input("Tekan Enter Untuk Menginput Ulang...")
                    detik3()
                    clear()
                    continue
                     

def ban_akun_pengguna():
    data = baca_data_akun()
    akun = data["member"]
    table = PrettyTable()
    
    if len(akun) < 1:
        print("Belum Ada Akun Pengguna Yang Dibuat")  
        input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
        clear()  
    else:
        table.field_names = ["ID Akun", "Username Akun", "Passowrd Akun", "Status Akun"]
        for data_akun in akun:
            table.add_row([data_akun["id"], data_akun["username"], data_akun["password"], data_akun["status"]])
            
        while True:
            print(table)
            akun_ban = input("Masukan ID Akun Yang Ingin Anda BAN: ").strip()
            try:
                akun_ban = int(akun_ban)
                akun_diban = next((i for i in akun if int(i["id"]) == akun_ban), None)
                if akun_diban is None:
                    print("\nID tidak ditemukan!")
                    input("Tekan Enter untuk ulangi...")
                    clear()
                    continue
                
                else:
                    while True:
                        konfirmasi = input(f"Apakah Anda Yakin Ingin Menge-BAN Akun {akun_diban["username"]}? (Y/N)").strip().lower()
                        if konfirmasi == "y":
                            akun_diban["status"] = "BANNED"
                            
                            with open("file_data/data_akun.json", "w") as file:
                                json.dump(data, file, indent = 4)
                                
                            print(f"\nAkun Dengan Username {akun_diban["username"]} Berhasil Di BAN!!")
                            input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                            clear()  
                            return 

                        elif konfirmasi == "n":
                            print("\nBAN dibatalkan.")
                            input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                            clear()
                            return

                        else:
                            print("\nMasukkan pilihan Y atau N!")
                            input("Tekan Enter Untuk Menginput Ulang...")
                            clear()
                            continue
                
            except ValueError:
                print("\nInput Tidak Valid!! ID Harus Berupa Angka!!")
                input("Tekan Enter Untuk Menginput Ulang...")
                detik3()
                clear()
                continue
        
        
def menangani_laporan_akun(): 
    data = baca_data_akun()
    data_laporan_akun = baca_data_laporan()
    data_akun = data["member"]
    laporan_akun = data_laporan_akun["laporan_akun"]
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Username Akun", "Status Akun", "Masalah Akun"] 
    for laporan in laporan_akun:
        tabel.add_row([laporan["id"], laporan["username"], laporan["status"], laporan["pesan"]])
    
    if len(laporan_akun) < 1:
        print("Belum Ada Laporan Tentang Akun Pengguna Yang Diterima!!")
        input("Silahkan Tekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
        clear()
        
    else:
        while True:
            print(tabel)
            pilihan = input("Masukan ID Akun: ").strip()
            try:
                pilihan = int(pilihan)
                pilih_laporan = next((i for i in laporan_akun if int(i["id"]) == pilihan), None)
                pilih_akun = next((i for i in data_akun if int(i["id"]) == pilihan), None)
                
                if pilih_laporan is None:
                    print("\nID tidak ditemukan!")
                    input("Tekan Enter untuk ulangi...")
                    clear()
                    continue
                
                else:
                    while True:
                        konfirmasi = input(f"Apakah Anda Ingin Menangani Akun dengan Username:{pilih_laporan["username"]} ? (Y/N)").strip().lower()
                        if konfirmasi == "y":
                            pilih_akun["status"] = "Aktif"
                            index = laporan_akun.index(pilih_laporan)
                            laporan_akun.pop(index)
                            
                            with open("file_data/data_akun.json", "w") as file:
                                json.dump(data, file, indent = 4)
                            with open("file_data/data_laporan.json", "w") as file:
                                json.dump(data_laporan_akun, file, indent = 4)
                                
                            print("Akun Berhasil Ditangani!!")
                            input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                            detik3()
                            clear()
                            return
                         
                        elif konfirmasi == "n":
                            clear()
                            print("Jika Tidak Menangani Akun Ini, Maka Akun Akan Otomatis Terblokir!!")
                            konfirmasi_akhir = input(f"\nApakah Anda Yakin Tidak Ingin Menangani Akun dengan Username:{pilih_laporan["username"]} ? (Y/N)").strip().lower() 
                            if konfirmasi_akhir == "y":
                                pilih_akun["status"] = "BLOKIR"
                                index = laporan_akun.index(pilih_laporan)
                                laporan_akun.pop(index)
                                
                                with open("file_data/data_akun.json", "w") as file:
                                    json.dump(data, file, indent = 4)
                                with open("file_data/data_laporan.json", "w") as file:
                                    json.dump(data_laporan_akun, file, indent = 4)
                                    
                                print("Akun Resmi Terblokir!!")
                                input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                                detik3()
                                clear()
                                return 
                            
                            elif konfirmasi_akhir == "n":
                                print("Akun Belum Ditangani, Pikirkan Lagi Baik-baik...")
                                input("\nTekan Enter Untuk Kembali Ke Menu Mengelola Akun Pengguna...")
                                detik3()
                                clear()
                                return 
                            
                            else:
                                print("\nMasukkan pilihan Y atau N!")
                                input("Tekan Enter Untuk Menginput Ulang...")
                                clear()
                                continue 
                            
                        else:
                            print("\nMasukkan pilihan Y atau N!")
                            input("Tekan Enter Untuk Menginput Ulang...")
                            clear()
                            continue 
                        
            except ValueError:
                print("\nInput Tidak Valid!! ID Harus Berupa Angka!!")
                input("Tekan Enter Untuk Menginput Ulang...")
                detik3()
                clear()
                continue          

        
    