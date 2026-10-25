class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True
        
    def berlari(self):
        # TODO 2: Buat behavior agar karakter mulai berlari
        self.is_running = True
        print(f"{self.nama} mulai berlari kencang menghindari kejaran inspektur!")
        
    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan jumlah koin ke properties koin
        self.koin += jumlah
        self.skor += (jumlah * 10)  # Bonus skor setiap ambil koin
        print(f"{self.nama} berhasil mengumpulkan {jumlah} koin! (Total Koin: {self.koin})")
        
    def tabrak_rintangan(self):
        # TODO 4: Jika menabrak rintangan, ubah is_running menjadi False
        self.is_running = False
        print(f"Duh! {self.nama} menabrak rintangan! GAME OVER.")
        
    def info_player(self):
        # TODO 5: Cetak status terkini
        print("=== STATUS PLAYER SUBWAY SURFERS ===")
        print(f"Nama Karakter : {self.nama}")
        print(f"Skor saat ini : {self.skor}")
        print(f"Jumlah Koin   : {self.koin}")
        print(f"Status Berlari: {self.is_running}")
        print("===================================\n")


# --- PENGUJIAN OBJEK ---
# Buat objek dengan nama variabel "player1" (misal: "Jake")
player1 = KarakterSurfer("Jake")

# Uji coba jalankan method-methodnya
player1.info_player()
player1.berlari()
player1.ambil_koin(15)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()