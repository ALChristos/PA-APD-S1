import inquirer,os
from file_data.datajson import *
from pack_admin.daftar_kota import *
from pack_member.program_rute import *
from file_data.akun import *
from review.review_rute import review

kecepatan_kendaraan = {
    "Motor": 60,
    "Mobil": 50,
    "Bus": 40,
    "Kapal": 40,
    "Pesawat": 800
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
  
def menu_kendaraan():
    jenis_kendaraan = [
        inquirer.List("kendaraan",
                      message = "Pilih Salah Satu Kendaraan Yand Akan Anda Gunakan...",
                      choices = [
                          "Motor",
                          "Mobil",
                          "Bus",
                          "Kapal",
                          "Pesawat"
                      ])
    ]
    jawab_kendaraan = inquirer.prompt(jenis_kendaraan)
    return jawab_kendaraan["kendaraan"]
    
    
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
        
    kendaraan = menu_kendaraan()
    clear()
    kota_tujuan = pilih_kota_tujuan(kota_1, data_rute)

    if kota_tujuan is None:
        return

    rute = data_rute[kota_1]
    jarak = None
    for item in rute:
        if item["rute"] == f"{kota_1}-{kota_tujuan}":
            jarak = item["jarak_tempuh"]
            break

    if jarak is None:
        print("Jarak tidak ditemukan!")
        input("Tekan Enter Untuk Kembali...")
        return

    clear()
    print(f"\nPerjalanan dimulai: {kota_1} → {kota_tujuan}")
    print(f"Jarak: {jarak} km")
    print(f"Kendaraan: {kendaraan}")

    waktu_menit = hitung_waktu_tempuh(jarak, kendaraan)

    print(f"Waktu tempuh: {waktu_menit} Menit")
    print("Perjalanan sedang berlangsung...\n")
    loading_waktu(waktu_menit)

    pertanyaan = [
            inquirer.List('menu',
                         message="Apakah anda ingin memberikan review/laporan untuk kota ini?",
                         choices=[
                            'Ya',
                            'Tidak'
                         ],
                         ),
        ]
    jawaban = inquirer.prompt(pertanyaan)
    
    if jawaban['menu'] == 'Ya':
        pertanyaan = [
                inquirer.List('menu',
                            message="Pilih salah satu:",
                            choices=[
                                '1. Saya ingin memberikan review untuk kota ini',
                                '2. Saya ingin memberikan laporan untuk kota ini',
                                '3. Keluar'
                            ],
                            ),
            ]
        jawaban_pertanyaan = inquirer.prompt(pertanyaan)
        if jawaban_pertanyaan['menu'][0] == '1':
            review(username)
        elif jawaban_pertanyaan['menu'][0] == '2':
            pass
        elif jawaban_pertanyaan['menu'][0] == '3':
            pass

    clear()
    
    simpan_kota_terakhir(username, kota_tujuan)
    print(f"Kota terakhir kamu sekarang: {kota_tujuan}")
    
    
    
    