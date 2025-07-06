import calendar

year = int(input("Masukkan Tahun:  "))
month = int(input("Masukkan Bulan:  "))

cal = calendar.month(year, month)
print(cal)

# sebuah program kalender yang cukup simple
# deklarasikan variabel year dan month agar user dapat memasukkan inputnya
# kemudian panggil function month yang ada di modul calendar dengan . dan masukkan 2 parameter variabel input tadi
# print ke console

# kemudian aku akan mencoba membuat program yang serupa namun dengan function berbeda
# aku mendapatkan informasi pada modul calendar terdapat function calendar pula yang dapat menampilkan seluruh tahun
# mari kita coba buat

# Input (year)
tahun = int(input("Masukkan Tahun:  "))

# Cari Function Calendar di Modul Calendar lalu masukkan parameter input Tahun
calen = calendar.calendar(tahun)

# print ke console
print(calen)

# yeay berhasil dan itu menampilkan seluruh kalender bulan pada tahun 2025 secara lengkap