# Ini adalah sebuah program yang dapat mengubah Celcius menjadi Farenheit

celcius = float(input("Masukkan Angka (°C):  "))
# Conversion Formula: Farenheit: (Celcius * 9/5) + 32
farenheit = (celcius * 9/5) + 32
print(f"Result: {celcius} °C sama dengan {farenheit} °F")

# proramnya cukup simple asalkan mengikuti formula basic aritmatika sederhana dengan membagi lalu menambah
# di awal user cukup memasukkan input angka suhu
# masuk kedalam formula yang mengalikan celcius dengan 9 lalu dibagi 5 dan ditambah 32
# tampilkan ke konsol dan tambahkan f-string agar variabel dapat masuk kedalam string