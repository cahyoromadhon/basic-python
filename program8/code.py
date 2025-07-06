import calendar

year = int(input("Masukkan Tahun:  "))
month = int(input("Masukkan Bulan:  "))

cal = calendar.month(year, month)
print(cal)

# sebuah program kalender yang cukup simple
# deklarasikan variabel year dan month agar user dapat memasukkan inputnya
# kemudian panggil function month yang ada di modul calendar dengan . dan masukkan 2 parameter variabel input tadi
# print ke console