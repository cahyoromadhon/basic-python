# Ini adalah sebuah program yang dapat mengubah Celcius menjadi Farenheit

celcius = float(input("Masukkan Angka (°C):  "))
# Conversion Formula: Farenheit: (Celcius * 9/5) + 32
farenheit = (celcius * 9/5) + 32
print(f"Result: {celcius} °C sama dengan {farenheit} °F")

# proramnya cukup simple asalkan mengikuti formula basic aritmatika sederhana dengan membagi lalu menambah
# di awal user cukup memasukkan input angka suhu
# masuk kedalam formula yang mengalikan celcius dengan 9 lalu dibagi 5 dan ditambah 32
# tampilkan ke konsol dan tambahkan f-string agar variabel dapat masuk kedalam string


# sekarang aku akan membuat program yang serupa yaitu Celcius menjadi Kelvin
inputC = float(input("Masukkan Angka (°C):  "))
# Formula
kelvin = inputC + 273.15
# output
print(f"Output: {inputC}°C sama dengan {kelvin}°K")

# setelah melakukan penambahan program pada mini-program konversi ini aku jadi belajar sesuatu karena telah melakukan kesalahan
# jika ingin menggunakan koma pada suatu nomor jangan menggunakan koma secara langsung karena akan menyebakan python akan mengira ada 2 nomor sehingga harus menggunakan titik sebagai penanda bahwa itu koma
# dan seperti yang dilihat ini cukup simple programnya
# user melakukan input dan tulis formulanya dengan melakukan deklarasi variabel kemudian tampilkan di console
# selesai