# Input nama
nama = input("Masukkan nama anda (nama pendek anda): ")

# Validasi sederhana (tidak boleh kosong)
if nama.strip() != "":
    print(f"Selamat datang {nama}")
else:
    print("Program selesai")

# Input umur
umur = int(input("\nMasukkan umur anda: "))

# Percabangan kondisi umur
if umur >= 18:
    print("anda cukup umur")

if umur < 18:
    print("anda belum cukup umur")

if umur <= 0:
    print("anda belum lahir")

if umur > 60:
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")