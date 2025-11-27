import os, inquirer
from review.create_review import catat
from review.read_review import daftar
from review.update_review import update
from review.delate_review import hapus
from pack_member.menu_member import *
from file_data.datajson import *


def menu_review(username, kota_1, kota_tujuan):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(f"User: {username}")
        print("=" * 60)
        
        pertanyaan = [
            inquirer.List('menu',
                         message="Pilih menu utama",
                         choices=[
                             '1. Lihat Review Kota Ini',
                             '2. Berikan Review',
                             '3. Edit Review Saya',
                             '4. Hapus Review Saya',
                             '5. Selesai'
                         ],
                         ),
        ]
        
        jawaban = inquirer.prompt(pertanyaan)

        if jawaban['menu'][0] == '1':
            daftar(username)
        elif jawaban['menu'][0] == '2':
            catat(username, kota_1, kota_tujuan)
        elif jawaban['menu'][0] == '3':
            update(username)
        elif jawaban['menu'][0] == '4':
            hapus(username)
        elif jawaban['menu'][0] == '5':
            return