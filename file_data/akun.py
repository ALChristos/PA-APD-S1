import json, os
# from datajson import baca_data_akun
from file_data.datajson import *
from pesan import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrasi():
    while True:
        data = baca_data_akun()
        member_akun = data["member"]
        admin_akun = data["admin"]
        try:
            regis_username = input("Masukkan username: ").strip()
            regis_password = input("Masukkan password: ").strip()
            if regis_username in [akun["username"] for akun in member_akun] or regis_username in [a["username"] for a in admin_akun]:
                raise ValueError("Username sudah terdaftar. Silakan coba username lain.")
            elif regis_password.strip() == "":
                raise ValueError("Password tidak boleh kosong.")
            elif regis_username.strip() == "":
                raise ValueError("Username tidak boleh kosong.")
            
            cek_id = sorted([int(akun["id"]) for akun in member_akun])
            id_awal = 1
            for uid in cek_id:
                if uid == id_awal:
                    id_awal += 1
                else:
                    break
                
            id_baru = id_awal
            akun_baruM = {
                "id": str(id_baru),
                "username": regis_username,
                "password": regis_password,
                "status": "Aktif"
            }
            member_akun.append(akun_baruM)
            
            with open("file_data/data_akun.json", "w") as file:
                json.dump(data, file, indent = 4)
                
            print("\nRegistrasi berhasil!")
            input("Tekan Enter untuk kembali...")
            break

        except ValueError as e:
            print(e)
            input("Tekan Enter untuk kembali...")
            break      

def login_akun():
    kesempatan = 3
    while kesempatan > 0:
        teks_mulai()
        data = baca_data_akun()
        data_laporan = baca_data_laporan()
        akun_member = data["member"]
        akun_admin = data["admin"]
        laporan = data_laporan["laporan_akun"]
        try:
            username_input = input("Masukkan username: ").strip()
            password_input = input("Masukkan password: ").strip()
            
            if password_input.strip() == "":
                raise ValueError("Password tidak boleh kosong.")
            elif username_input.strip() == "":
                raise ValueError("Username tidak boleh kosong.")
            
        # Login akun member
            for member in akun_member:
                if username_input == member["username"]:
                    if password_input == member["password"]:
                        if member["status"] == "BANNED":
                            print("Akun anda telah di banned. Silakan hubungi admin untuk mendapat bantuan/Buat akun baru")
                            while True:
                                tanya = input("Apakah anda ingin menghubungi admin sekarang? (y/n): ")
                                if tanya.lower() == 'y':
                                    clear()
                                    laporan_aktif = next((lap for lap in laporan if lap["id"] == member["id"]), None)
                                    if laporan_aktif:
                                        print("Anda Sudah Mengirim Laporan Ke Admin. Silakan Tunggu Admin Menangani Laporan Anda...")
                                        detik5()
                                        return None, None
                                    
                                    pesan = input("Masukan Keluhan Anda: ").strip()
                                    if pesan == "":
                                        print("Pesan Kosong, Gagal Membuat Laporan!!")
                                        detik5()
                                        return None, None
                                    else:
                                        laporan_member = {
                                            "id": member["id"],
                                            "username": member["username"],
                                            "status": member["status"],
                                            "pesan": pesan
                                        }
                                        laporan.append(laporan_member)
                                        with open("file_data/data_laporan.json", "w") as file:
                                            json.dump(data_laporan, file, indent = 4 )
                                            
                                        print("Menghubungi admin...")
                                        detik5()
                                        print("\nBerhasil Terhubung Dengan Admin, Silahkan Tunggu Respon Admin Tentang Akun Anda")
                                        input("Tekan Enter Untuk Kembali Ke Menu Utama...")
                                        clear()
                                        return None, None
                                
                                elif tanya.lower() == 'n':
                                    print("\nSilahkan Hubungi Admin Kembali Jika Anda Berubah Pikiran...")
                                    detik5()
                                    return None, None
                                else:
                                    print("\nInput harus 'y' atau 'n'. Silakan coba lagi.")
                                    detik3_coba_lagi()
                                    clear()
                                    continue
                                
                        elif member["status"] == "BLOKIR":
                            clear()
                            print("Akun Anda Telah Diblokir Permanen Oleh Atmin\nSilahkan Buat Akun Baru Dimenu Registrasi...")
                            input("Tekan Enter Untuk Kembali Ke Menu Utama...")
                            detik5()
                            clear()
                            return None, None
                        
                        else:
                            return "member", member["username"]
                        
                    elif password_input != member["password"] :
                        kesempatan -= 1
                        input("Password salah. Silakan tekan enter untuk coba lagi.")
                        detik3_coba_lagi()
                        clear()
                        break
                         
        # Login akun admin
            for admin in akun_admin:
                        
                if username_input == admin["username"]:
                    if password_input == admin["password"]:
                        return "admin", admin["username"]
                    else:
                        kesempatan -= 1
                        input("Password salah. Silakan tekan enter untuk coba lagi.")
                        detik3_coba_lagi()
                        break
            
            username_terdaftar = (any(username_input == akun["username"] for akun in akun_admin) or any(username_input == akun["username"] for akun in akun_member))
            if not username_terdaftar:         
                print("Username tidak ditemukan/Sudah Dihapus!!\nSilakan registrasi terlebih dahulu.")
                detik5()
                return None, None
                  
        except ValueError as e:
            print(e)
            detik3_coba_lagi()
            return None, None
            
    print("Kesempatan login habis. Silakan coba lagi nanti.")
    detik5()
    return None, None    
      
