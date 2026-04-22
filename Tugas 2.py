# Nama yang dianggap benar
nama_benar = "zur"   # ganti dengan nama pendek anda

nama = input("Masukan nama anda: ")

if nama.lower() == nama_benar:
    print("Nama benar, lanjut ke program berikutnya\n")
    
    angka = int(input("Masukkan angka (1-10): "))
    
    if 1 <= angka <= 10:
        for i in range(1, 11):
            print(f"{angka} x {i} = {angka * i}")
    else:
        print("Angka harus antara 1 sampai 10")

else:
    print("silahkan coba lagi")