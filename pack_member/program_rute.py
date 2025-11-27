import inquirer, os
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
    daftar_rute = [rute["rute"] for rute in data_rute[kota_1]] #kota_1 = Balikpapan #data_rute = myimpan history perjalanan yang sudah di lakukan

    if not daftar_rute:
        print("\n===Tidak ada rute lanjutan dari kota ini===")
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

def cek_kondisi_rute(kota_1, kota_tujuan, data_rute):
    laporan = baca_data_laporan()  
    laporan_status = laporan.get("laporan_status", {})  
    kunci_rute = f"{kota_1}-{kota_tujuan}"
    kondisi = laporan_status.get(kunci_rute, "Aman")

    tambahan_waktu = 0
    jarak = None

    for item in data_rute[kota_1]:
        if item["rute"] == kunci_rute:
            jarak = item["jarak_tempuh"]
            break

    if jarak is None:
        print("Jarak rute tidak ditemukan!")
        return kota_tujuan, None, 0

    if kondisi == "ditutup":
        print("\n⚠ Rute ini DITUTUP! Harus memilih rute alternatif.")
        alternatif = None
        min_jarak = 999999

        for item in data_rute[kota_1]:
            if item["rute"] != kunci_rute and item["jarak_tempuh"] < min_jarak:
                min_jarak = item["jarak_tempuh"]
                alternatif = item
        while True:
            print(f"\n✔ Rute alternatif: {alternatif['rute']} ({alternatif['jarak_tempuh']} km)")
            konfirmasi = input("Apakah Anda Setuju Melewati Rute Ini? (Y/N)").lower().strip()
            if konfirmasi == "y":
                kota_tujuan = alternatif["rute"].split("-")[1]
                jarak = alternatif["jarak_tempuh"]
                os.system("cls" if os.name == "nt" else "clear")
                break
            elif konfirmasi == "n":
                os.system("cls" if os.name == "nt" else "clear")
                return
            else:
                print("Input Tidak Valid Pilih Y/N Saja")
                input("Tekan Enter Untuk Menginput Ulang...")
                os.system("cls" if os.name == "nt" else "clear")
                continue
                    
                

    elif kondisi.startswith("macet"):
        kategori = kondisi.split("_")[1]  

        if kategori == "tidak":
            tambahan_waktu = 5
        elif kategori == "sedang":
            tambahan_waktu = 10
        elif kategori == "parah":
            tambahan_waktu = 15

        print(f"\n⚠ Rute MACET {kategori.upper()} → +{tambahan_waktu} menit")

    elif kondisi.startswith("kecelakaan"):
        kategori = kondisi.split("_")[1]  

        if kategori == "tidak":
            tambahan_waktu = 15
            print("\n⚠ Ada KECELAKAAN TIDAK PARAH → +15 menit")

        else:
            pilihan = [
                inquirer.List(
                    "opsi",
                    message="⚠ Kecelakaan PARAH! Pilih tindakan:",
                    choices=[
                        "Lewat saja (+30 menit)",
                        "Gunakan rute alternatif"
                    ]
                )
            ]

            jawab = inquirer.prompt(pilihan)["opsi"]

            if jawab.startswith("Lewat"):
                tambahan_waktu = 30
                print("✔ Tetap lewat → +30 menit")

            else:
                alternatif = None
                min_jarak = 999999

                for item in data_rute[kota_1]:
                    if item["rute"] != kunci_rute and item["jarak_tempuh"] < min_jarak:
                        min_jarak = item["jarak_tempuh"]
                        alternatif = item

                print(f"✔ Alternatif dipilih: {alternatif['rute']} ({alternatif['jarak_tempuh']} km)")
                kota_tujuan = alternatif["rute"].split("-")[1]
                jarak = alternatif["jarak_tempuh"]

    else:
        print("✔ Rute AMAN, tidak ada hambatan.")

    return kota_tujuan, jarak, tambahan_waktu



def laporkan_rute(kota_1, kota_tujuan):
    data_rute = baca_data_perjalanan()
    laporan = baca_data_laporan()           
    laporan_status = laporan.get("laporan_status", {})

    rute_key = f"{kota_1}-{kota_tujuan}"
    rute_key_reverse = f"{kota_tujuan}-{kota_1}"

    rute_list = data_rute.get(kota_1, [])
    target = next((i for i in rute_list if i["rute"] == rute_key), None)

    if target is None:
        print("\nRute tidak ditemukan!")
        input("Enter untuk kembali...")
        return

    print(f"\nMelaporkan kondisi untuk rute: {rute_key}")

    pilihan = [
        inquirer.List(
            "jenis",
            message="Pilih jenis masalah:",
            choices=[
                "Macet",
                "Kecelakaan",
                "Perbaikan jalan / Ditutup",
                "Batalkan"
            ]
        )
    ]

    jenis = inquirer.prompt(pilihan)["jenis"]
    if jenis == "Batalkan":
        return

    if jenis == "Macet":
        kategori = inquirer.prompt([
            inquirer.List(
                "kat",
                message="Kategori kemacetan:",
                choices=["Tidak parah", "Sedang", "Parah"]
            )
        ])["kat"]

        status = f"macet_{kategori.lower().replace(' ', '_')}"

    elif jenis == "Kecelakaan":
        kategori = inquirer.prompt([
            inquirer.List(
                "kat",
                message="Kategori kecelakaan:",
                choices=["Tidak parah", "Parah"]
            )
        ])["kat"]

        status = f"kecelakaan_{kategori.lower().replace(' ', '_')}"

    elif jenis == "Perbaikan jalan / Ditutup":
        status = "ditutup"

    laporan_status[rute_key] = status
    laporan_status[rute_key_reverse] = status 

    laporan["laporan_status"] = laporan_status

    with open("file_data/data_laporan.json", "w") as file:
        json.dump(laporan, file, indent=4)

    for item in data_rute[kota_1]:
        if item["rute"] == rute_key:
            item["status"] = status

    if kota_tujuan in data_rute:
        for item in data_rute[kota_tujuan]:
            if item["rute"] == rute_key_reverse:
                item["status"] = status

    with open("file_data/data_perjalanan.json", "w") as file:
        json.dump(data_rute, file, indent=4)

    print(f"\n✔ Laporan disimpan! Status baru: {status}")
    input("Tekan Enter untuk kembali...")
    os.system("cls" if os.name == "nt" else "clear")


