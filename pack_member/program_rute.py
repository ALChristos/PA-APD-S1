import inquirer
from file_data.datajson import *
from pack_admin.daftar_kota import *

def pilih_kota_tujuan(kota_1, data_rute):
    daftar_rute = [rute["rute"] for rute in data_rute[kota_1]]

    if not daftar_rute:
        print("Tidak ada rute lanjutan dari kota ini.")
        return None

    pertanyaan = [
        inquirer.List(
            "tujuan",
            message = f"Pilih kota tujuan dari {kota_1}",
            choices = daftar_rute
        )
    ]

    jawab = inquirer.prompt(pertanyaan)
    rute_pilihan = jawab["tujuan"]     

    
    kota_tujuan = rute_pilihan.split("-")[1]

    return kota_tujuan


def ambil_kota_akhir(username):
    data = baca_data_perjalanan_akhir()
    kota_akhir = data["perjalanan_terakhir"].get(username)
    return kota_akhir

def simpan_kota_terakhir(username, kota):
    data = baca_data_perjalanan_akhir()
    data["perjalanan_terakhir"][username] = kota
    
    with open("file_data/data_perjalanan_akhir.json", "w") as file:
        json.dump(data, file, indent = 4)
    