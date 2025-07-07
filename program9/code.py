# Sebuah mini-program yang dapat mengecek apakah bilangan tersebut positif,negatif atau zero

cek = int(input("Masukkan Angka:  "))

# if {variabel}:
#   [kondisi]

if cek > 0:
    print(f"{cek} adalah bilangan Positif")
elif cek == 0:
    print(f"{cek} adalah bilangan Zero")
else:
    print(f"{cek} adalah bilangan Negatif")
# else tidak perlu ada kondisi lagi karena jika masih ada kondisi masukkan ke elif dan fungsi if hanyalah untuk pembuka saja sisanya serahkan ke elif