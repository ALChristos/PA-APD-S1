import json

def baca_data_akun():
    with open("file_data/data_akun.json", "r") as file:
        return json.load(file)
    
    
def baca_data_perjalanan():
    with open("file_data/data_perjalanan.json", "r") as file:
        return json.load(file)
    
    
def baca_data_laporan():
    with open("file_data/data_laporan.json", "r") as file:
        return json.load(file)
    
    
def baca_data_perjalanan_akhir():
    with open("file_data/data_perjalanan_akhir.json", "r") as file:
        return json.load(file)
    
def simpan_data_daftarperjalanan():
    with open("file_data/data_daftarperjalanan.json", "r") as file:
        return json.load(file)