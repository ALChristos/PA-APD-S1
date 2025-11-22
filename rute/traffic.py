class MasalahLaluLintas:
    def __init__(self, penyebab, tingkat=None, deskripsi=""):
        self.penyebab = penyebab        
        self.tingkat = tingkat          
        self.deskripsi = deskripsi

    def __str__(self):
        if self.tingkat:
            return f"{self.penyebab.capitalize()} ({self.tingkat}) - {self.deskripsi}"
        return f"{self.penyebab.capitalize()} - {self.deskripsi}"
