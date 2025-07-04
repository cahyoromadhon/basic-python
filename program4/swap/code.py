# Input Two Variables
a = input("Masukkan Variabel Pertama:  ")
b = input("Masukkan Variabel Kedua:  ")
# Display The Original Variabel
print(f"Original Values: a = {a} and b = {b}")
temp = a
a = b
b = temp
print(f"Swapped Values: a = {a} and b = {b}")

# Logikanya cukup sederhana yang dimana pada tahap awal kita disuruh untuk memasukkan variabel yang kemudian kita akan display variabel yang telah dinput tadi agar kita percaya dengan nilai variabel original lalu variabel selanjutnya mendeklarasikan ulang variabel yang telah dideklarasikan dengan mengubah nilai variabelnya dengan variabel yang lainnya sehingga itu terasa seperti tertukar padahal kita hanya mengubah nilai variabel tersebut
# seperti biasa kita built-in function diikutkan sehingga kita dapat memasukkan variabel kedalam string
# ini hanyalah permainan deklarasi variabel biasa saja
# print juga seperti biasa menampilkan output ke console