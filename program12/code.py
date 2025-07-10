# sebuah program yang dibuat untuk mengetahui nilai ASCII dibalik setiap karakter dalam alphabet

# dimulai dengan input
# lalu print yang didalamnya berisikan built-in fuction sepertinya
nilai = input("Masukkan Karakter:  ")
print(f"Nilai ASCII dari '{nilai}' adalah ", ord(nilai))
# thats it?

# jadi ASCII itu adalah standar pengkodean yang dimana setiap huruf ditandai dengan nomor bahkan nilai dari huruf uppercase dan huruf lowcase saja nilai nya bisa berbeda oleh karena itu program ini dibutuhkan jika kita ingin mempelajari atau bahkan menghitung nilai pada setiap karakter dan diubah menjadi sebuah nilai ASCII
# ord() adalah sebuah built-in function yang memungkinkan fungsi sederhana dapat menghitung nilai dari ASCII namun function ini terbatas pada argument nya yang hanya bisa satu karakter saja

# namun karena aku tidak ingin sebatas menghitung satu karakter saja jadinya aku akan membuat program yang memungkinkan kita dapat mengonversi kalimat menjadi nilai ASCII

char = input("Masukkan Kalimat:  ")
print(f"Nilai ASCII dari '{char}' adalah: ")
for karakter in char:
    print(f"'{karakter}' = {ord(karakter)}")
# logikanya untuk kali ini cukup mudah
# deklarasikan variabel input
# print ke analog dengan f-string agar variabel dapat masuk kedalam string
# deklarasikan looping menggunakan keyword for
# karakter adalah variabel sementara
# in adalah kunci kesuksesan program ini karena 'in' memungkinkan python tau darimana data diambil terlebih dahulu secara satu persatu berurutan [1, 2, 3]
# kemudian setelah data diambil dengan metode pengurutan dari depan, in akan menugaskan kepada variabel sebelumnya yang dalam hal ini adalah variabel karakter
# dengan ini 'in' memindahkan tanggung jawabnya ke variabel sementara
# print ke analog dengan f-string agar variabel dapat masuk
# done