# Membuat program untuk menyapa pengunjung hotel
# Memasukkan nama dan jenis kelamin pengunjung hotel
Nama_pengunjung_hotel = input("Masukkan nama pengunjung hotel :")
Jenis_kelamin_pengunjung = input("Masukkan jenis kelamin pengunjung (L/P) :")

# Output
if Jenis_kelamin_pengunjung == "L" :
    print("Selamat datang, Tuan",Nama_pengunjung_hotel,"!")
else:
    print("Selamat datang, Nyonya",Nama_pengunjung_hotel,"!")