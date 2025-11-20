import json, inquirer, time, os

from pesan import *
from file_data.akun import *
from file_data.datajson import *
from list_inquirer import *
from pack_admin.menu_admin import *
from pack_admin.daftar_kota import *
from pack_admin.program_menuA import *
from pack_member.menu_member import *

def bersih():
    os.system("cls" if os.name == "nt" else "clear")
    
data = baca_data_akun()

while True:
    bersih()
    jawab = inquirer_login()
    print("="*60)
    if jawab["list_login"] == "Login":
        bersih()
        role, username = login_akun() 
        bersih()
        if role == "admin":
            tampilan_menu_admin(username)
            bersih()
            while True:
                header_menu_admin()
                jawab = menu_admin()  

                if jawab["admin_menu"][0] == "1":
                    detik3()
                    bersih()
                    while True:
                        header_menu_admin()
                        jawab_pil1 = mengelola_rute_perjalanan()
                        if jawab_pil1["menu_pil1"][0] == "1":
                            bersih()
                            membuat_rute_perjalanan()
                        elif jawab_pil1["menu_pil1"][0] == "2":
                            bersih()
                            melihat_rute_perjalanan()
                            break
                        elif jawab_pil1["menu_pil1"][0] == "3":
                            # NANTI AKAN DI LANJUT LAGI 
                            pass
                        elif jawab_pil1["menu_pil1"][0] == "4":
                            bersih()
                            break
                        
                elif jawab["admin_menu"][0] == "2":
                    detik3()
                    bersih()
                    while True:
                        header_menu_admin()
                        break
                 
                elif jawab["admin_menu"][0] == "3":
                    detik3()
                    bersih()
                    while True:
                        header_menu_admin()
                        jawab_pil3 = mengelola_akun_pengguna()
                        if jawab_pil3["menu_pil3"][0] == "1":
                            bersih()
                            melihat_akun_pengguna()
                        elif jawab_pil3["menu_pil3"][0] == "2":
                            bersih()
                            ban_akun_pengguna()
                        elif jawab_pil3["menu_pil3"][0] == "3":
                            bersih()
                            menangani_laporan_akun()
                        elif jawab_pil3["menu_pil3"][0] == "4":
                            bersih()
                            break
                
                elif jawab["admin_menu"][0] == "4":
                    bersih()
                    break
                    
        elif role == "member":
            tampilan_menu_member(username)
            bersih()
            while True:
                header_menu_member()
                jawab = menu_member()
                if jawab["menu_member"][0] == "1":
                    bersih()
                    jalan_jalan(username)
                elif jawab["menu_member"][0] == "2":
                    bersih()
                    break
                
    elif jawab["list_login"] == "Registrasi":
        registrasi()  
        bersih()
    elif jawab["list_login"] == "Keluar":
        bersih()
        print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
        break
