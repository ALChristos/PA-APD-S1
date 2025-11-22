import os
karakter_genshin = []

def clear ():
    os.system('cls' if os.name == 'nt' else 'clear') 
def pilih_validasi(pesan, opsi):
    print(pesan)
    for i, o in enumerate(opsi):
        print(f"{i+1}. {o}")

    try:
        pilihan = int(input("Pilih: ")) - 1
        if pilihan < 0 or pilihan >= len(opsi):
            print(" Pilihan tidak valid!")
            return None
        return opsi[pilihan]
    except ValueError:
        print(" Input harus angka!")
        return None

def create():
    clear()
    nama = input("Masukkan nama karakter: ").strip()
    if nama == "":
        print(" Nama tidak boleh kosong!")
        return

    elemen = pilih_validasi("Pilih elemen:", 
            ["Pyro", "Hydro", "Electro", "Cryo", "Geo", "Anemo", "Dendro"])
    if not elemen: 
        return

    rarity = pilih_validasi("Pilih rarity:", ["4★", "5★"])
    if not rarity:
        return

    weapon = pilih_validasi("Pilih weapon:", 
            ["Sword", "Claymore", "Polearm", "Bow", "Catalyst"])
    if not weapon:
        return

    karakter = {
        "nama": nama,
        "elemen": elemen,
        "rarity": rarity,
        "weapon": weapon
    }

    karakter_genshin.append(karakter)
    print(f" Karakter {nama} berhasil ditambahkan!")

def read():
    clear()
    if len(karakter_genshin) == 0:
        print("Belum ada karakter tersimpan.")
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    print("\n=== Daftar Karakter Genshin Impact ===")
    for i, k in enumerate(karakter_genshin):
        print(f"{i+1}. {k['nama']} | {k['elemen']} | {k['rarity']} | {k['weapon']}")
    input("\nTekan Enter untuk kembali ke menu...")

def update():
    clear()
    read()
    if len(karakter_genshin) == 0:
        return

    try:
        index = int(input("Pilih nomor karakter yang ingin diubah: ")) - 1
        if index < 0 or index >= len(karakter_genshin):
            print(" Nomor tidak valid!")
            return
    except ValueError:
        print(" Input harus angka!")
        return

    karakter = karakter_genshin[index]

    print("\n--- Ubah Data Karakter ---")
    nama_baru = input(f"Nama baru ({karakter['nama']}): ").strip()
    if nama_baru != "":
        karakter['nama'] = nama_baru

    pilihan_elemen = pilih_validasi("Pilih elemen baru:", 
            ["Pyro", "Hydro", "Electro", "Cryo", "Geo", "Anemo", "Dendro"])
    if pilihan_elemen:
        karakter['elemen'] = pilihan_elemen

    pilihan_rarity = pilih_validasi("Pilih rarity baru:", ["4★", "5★"])
    if pilihan_rarity:
        karakter['rarity'] = pilihan_rarity

    pilihan_weapon = pilih_validasi("Pilih weapon baru:",
            ["Sword", "Claymore", "Polearm, Bow", "Catalyst"])
    if pilihan_weapon:
        karakter['weapon'] = pilihan_weapon

    print(" Data karakter berhasil diperbarui.")

def delete():
    read()
    if len(karakter_genshin) == 0:
        return

    try:
        index = int(input("Pilih nomor karakter yang ingin dihapus: ")) - 1
        if index < 0 or index >= len(karakter_genshin):
            print(" Nomor tidak valid!")
            return
    except ValueError:
        print(" Input harus angka!")
        return

    terhapus = karakter_genshin.pop(index)
    print(f" Karakter {terhapus['nama']} berhasil dihapus.")

while True:
    clear()
    print("\n=== MENU Genshin Impact: Manajemen Karakter ===")
    print("1. Tambah Karakter")
    print("2. Lihat Karakter")
    print("3. Ubah Karakter")
    print("4. Hapus Karakter")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        create()
    elif pilihan == "2":
        read()
    elif pilihan == "3":
        update()
    elif pilihan == "4":
        delete()
    elif pilihan == "5":
        print("Sampai jumpa, Traveler! ✨")
        break
    else:
        print(" Pilihan tidak valid!")
