import inquirer,os
from file_data.datajson import *
from pack_admin.daftar_kota import *
from pack_member.program_rute import *
from file_data.akun import *


def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
    
def menu_member():
    menu_awal = [
        inquirer.List("menu_member",
                      message = "Pilihlah Salah Satu Menu Yang Tersedia...",
                      choices = [
                          "1. Jalan-jalan",
                          "2. Logout"
                      ]
                    )
                ]
    jawab = inquirer.prompt(menu_awal)
    return jawab


def jalan_jalan(username):
    clear()
    data_rute = baca_data_perjalanan()
    kota_akhir = ambil_kota_akhir(username)
    
    if kota_akhir is None:
        kota_1 = kota_awal()
    else:
        kota_1 = kota_akhir
        print(f"Kamu sekarang berada di: {kota_1}")

    kota_tujuan = pilih_kota_tujuan(kota_1, data_rute)

    if kota_tujuan is None:
        return

    print(f"\nPerjalanan dimulai: {kota_1} → {kota_tujuan}")
    print("Perjalanan selesai!\n")

    simpan_kota_terakhir(username, kota_tujuan)
    print(f"Kota terakhir kamu sekarang: {kota_tujuan}")
    
    
    
    