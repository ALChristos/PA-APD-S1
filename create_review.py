from file_data.datajson import *

def catat() -> None:
    import os
    import inquirer
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("MASUKAN REVIEW")
        print("=" * 60)

        try:
            nama_perjalanan = input("Nama Perjalanan : ").strip()
            if not nama_perjalanan:
                raise ValueError("\nNama perjalanan tidak boleh kosong!")

            destinasi = input("Destinasi : ").strip()
            if not destinasi:
                raise ValueError("\nDestinasi tidak boleh kosong!")

            tanggal = input("Tanggal Pergi : ").strip()
            durasi = input("Berapa Lama : ").strip()

            budget = input("Budget (angka saja) : ").strip()
            if not budget.isdigit():
                raise ValueError("\nBudget harus berupa angka!")

            cerita = input("Cerita/Experience : ").strip()
            star = input("Rating (1-5) : ").strip()
            if star not in ['1', '2', '3', '4', '5']:
                raise ValueError("\nRating harus antara 1 sampai 5 dan tidak boleh kosong!")

            daftar_perjalanan["Nama"].append(user_login)
            daftar_perjalanan["Nama Perjalanan"].append(nama_perjalanan)
            daftar_perjalanan["Destinasi"].append(destinasi)
            daftar_perjalanan["Tanggal"].append(tanggal)
            daftar_perjalanan["Durasi"].append(durasi)
            daftar_perjalanan["Budget"].append(budget)
            daftar_perjalanan["Cerita"].append(cerita)
            daftar_perjalanan["Rating"].append(star)

            print("\nPerjalanan berhasil dicatat!")
            input("\nTekan Enter untuk kembali ke menu...")
            return

        except ValueError as e:
            print(e)
            pertanyaan = [
            inquirer.List('menu',
                        message="apa ingin mengisi ulang?",
                        choices=[
                            'ya',
                            'tidak'
                        ],
                        ),
        ]
            jawaban = inquirer.prompt(pertanyaan)
            
            if jawaban['menu'] == 'ya':
                continue
            elif jawaban['menu'] == 'tidak':
                return