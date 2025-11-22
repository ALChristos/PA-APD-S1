from .route import Rute
from .traffic import MasalahLaluLintas

class SistemLaluLintas:
    def __init__(self):
        self.rute_terdaftar = {}

    def tambah_rute(self, nama, waktu_dasar):
        if nama in self.rute_terdaftar:
            return False  # rute sudah ada
        self.rute_terdaftar[nama] = Rute(nama, waktu_dasar)
        return True

    def tambah_masalah_ke_rute(self, nama_rute, penyebab, tingkat=None, deskripsi=""):
        rute = self.rute_terdaftar.get(nama_rute)
        if not rute:
            return False

        masalah = MasalahLaluLintas(penyebab, tingkat, deskripsi)
        rute.tambah_masalah(masalah)
        return True

    def daftar_masalah(self, nama_rute):
        rute = self.rute_terdaftar.get(nama_rute)
        return rute.daftar_masalah if rute else None

    def hapus_masalah(self, nama_rute, index):
        rute = self.rute_terdaftar.get(nama_rute)
        if not rute:
            return False
        return rute.hapus_masalah(index)

    def hitung_waktu_rute(self, nama_rute):
        rute = self.rute_terdaftar.get(nama_rute)
        if not rute:
            return None
        return rute.hitung_waktu()
