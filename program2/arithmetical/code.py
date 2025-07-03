# Addition
num1 = float(input("Enter the first number of addition:  "))
num2 = float(input("Enter the second number of addition:  "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result} ")


# num1 adalah nama variabel yang telah di deklarasikan
# float berguna sebagai mengubah tipe data string menjadi number dan float juga masuk dalam kategori built-in function
# input juga sama built-in dan fungsinya adalah memungkinkan user untuk memasukkan nilai pada console
# print seperti namanya adalah menampilkan hasil kedalam console

# Division
num3 = float(input("Masukkan Nomor Pembagian:  "))
num4 = float(input("Masukkan Nomor Pembagian:  "))
if num4 == 0:
    print("Error: Pembagian 0 tidak diperbolehkan")
else:
    divre = num3 / num4
    print(f"Hasil Pembagian: {num3} / {num4} = {divre}")