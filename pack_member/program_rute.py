import inquirer
from file_data.datajson import *
from pack_admin.daftar_kota import *

kecepatan_kendaraan = {
    "Motor": 60,
    "Mobil": 50,
    "Bus": 40,
    "Kapal": 40,
    "Pesawat": 800
}

def pilih_kota_tujuan(kota_1, data_rute):
    daftar_rute = [rute["rute"] for rute in data_rute[kota_1]]

    if not daftar_rute:
        print("\nTidak ada rute lanjutan dari kota ini.")
        input("Tekan Enter Untuk Kembali Ke Menu Awal...")
        os.system("cls" if os.name == "nt" else "clear")
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


def simpan_kota_terakhir(username, kota):
    data = baca_data_perjalanan_akhir()
    data["perjalanan_terakhir"][username] = kota
    
    with open("file_data/data_perjalanan_akhir.json", "w") as file:
        json.dump(data, file, indent = 4)
        

def ambil_kota_akhir(username):
    data = baca_data_perjalanan_akhir()
    kota_akhir = data["perjalanan_terakhir"].get(username)
    return kota_akhir

    
def hitung_waktu_tempuh(jarak, kendaraan):
    kecepatan = kecepatan_kendaraan[kendaraan]  
    waktu_tempuh = jarak / kecepatan
    waktu_menit = int(waktu_tempuh * 30)
    return waktu_menit


