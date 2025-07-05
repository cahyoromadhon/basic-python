kilometers = float(input("Masukkan Angka:  "))

# Konversi 1 Kilometers = 0,621371 Miles
konversi = 0.621371

miles = kilometers * konversi

print(f"{kilometers} KM sama dengan {miles} Miles")

# Ini adalah sebuah program yang dapat mengonversikan kilometer menjadi miles
# logikanya cukup sederhana yang dimulai dengan user melakukan input nilai
# diikuti dengan deklarasi konversi terlebih dahulu
# kemudian tinggal dikalikan saja kilometer dengan konversi nya yang akan menghasilkan miles
# print menggunakan f-string agar variabel dapat dimasukkan kedalam string
