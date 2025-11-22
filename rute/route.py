from rute.traffic import MasalahLaluLintas

class Rute:
    def __init__(self, nama, waktu_dasar):
        self.nama = nama
        self.waktu_dasar = waktu_dasar
        self.daftar_masalah = []

    def tambah_masalah(self, masalah: MasalahLaluLintas):
        self.daftar_masalah.append(masalah)

    def hapus_masalah(self, index):
        if 0 <= index < len(self.daftar_masalah):
            del self.daftar_masalah[index]
            return True
        return False

    def hitung_waktu(self):
        total = self.waktu_dasar
        perlu_rute_alternatif = False

        for masalah in self.daftar_masalah:

            if masalah.penyebab == "macet":
                if masalah.tingkat == "ringan":
                    total += 5
                elif masalah.tingkat == "sedang":
                    total += 10
                elif masalah.tingkat == "parah":
                    total += 20

            elif masalah.penyebab == "penutupan":
                perlu_rute_alternatif = True

            elif masalah.penyebab == "kecelakaan":
                if masalah.tingkat == "ringan":
                    total += 15
                elif masalah.tingkat == "parah":
                    return "KECELAKAAN_PARAH"

        return "ALTERNATIF" if perlu_rute_alternatif else total

    def __str__(self):
        return f"{self.nama} (Waktu dasar: {self.waktu_dasar} menit)"
