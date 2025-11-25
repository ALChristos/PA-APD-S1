import os
import inquirer
from file_data.akun import login_akun
from review.create_review import catat
from review.read_review import daftar
from review.update_review import update
from review.delate_review import hapus

def review() -> None:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(f"User: {login_akun}")
        print("=" * 60)
        
        pertanyaan = [
            inquirer.List('menu',
                         message="Pilih menu utama",
                         choices=[
                             'Lihat Review Kota Ini',
                             'Berikan Review',
                             'Edit Review Saya',
                             'Hapus Review Saya',
                             'Selesai'
                         ],
                         ),
        ]
        
        jawaban = inquirer.prompt(pertanyaan)

        if jawaban['menu'] == 'Lihat Review Kota Ini':
            daftar()
        elif jawaban['menu'] == 'Berikan Review':
            catat()
        elif jawaban['menu'] == 'Edit Review Saya':
            update()
        elif jawaban['menu'] == 'Hapus Review Saya':
            hapus()
        elif jawaban['menu'] == 'Selesai':
            if Menu_utama():
                break