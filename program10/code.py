# program ini akan mengecek apakah angka yang diberikan genap atau ganjil

inp = int(input("Masukkan Angka:  "))

if inp%2 == 0:
    print(f"{inp} adalah bilangan Genap")
else:
    print(f"{inp} adalah bilangan Ganjil")

# program yang sangat mudah, ini hanyalah permainan if else yang dimana jika integer yang dimasukkan user menggunakan input bisa dibagi 2 itu artinya bilangan tersebut adalah genap dan jika tidak atau else maka bilangan tersebut adalah ganjil. that's it

# aku ingin membuat program sejenis namun kali ini nilai yang dimasukkan haruslah angka apabila bukan maka akan muncul teks yang menunjukkan itu salah

try:
    inp1 = int(input("Masukkan Angka:  "))

    if inp1%2 == 0:
        print(f"{inp1} adalah bilangan Genap")
    elif inp1%2 == 1:
        print(f"{inp1} adalah bilangan Ganjil")
except ValueError:
    print("(Maaf, Hanya Menerima Angka)")