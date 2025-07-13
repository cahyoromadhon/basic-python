# ini adalah program yang akan mengecek apakah bilangan tersebut termasuk kedalam bilangan prima atau bukan
# bilangan prima adalah bilangan yang hanya bisa dibagi 1 dan bilangan itu sendiri selebihnya tidak bisa dibagi lagi

# deklarasikan variabel input
num = int(input("Masukkan Angka:  "))

# deklarasikan variabel flag dengan bool default yaitu false
flag = False

# periksa jika input adalah 1 maka print ke konsol bukan bilangan prima
if num == 1:
    print(f'{num} bukanlah bilangan prima')
# periksa jika input lebih besar dari 1 dan masukkan ke looping
elif num > 1:
    for i in range(2, num): # jalankan looping dan masukkan built-in function yang dapat mengurutkan angka (start, finish)
        if (num % i) == 0: # jika input dibagi dengan urutan terus menerus menghasilkan angka 0 
            flag = True # maka ubah flag menjadi True
            break # dan hentikan looping dengan break

# logikanya cukup kompleks sedikit yang dimana looping akan berjalan terus menerus sambil mengecek kondisi if dibawahnya yaitu jika input dibagikan dengan loopingan urutan bilangan sebelum bilangan input itu sendiri maka akan terus mengecek apakah bernilai 0 atau 1
# dan jika bernilai 0 maka loopingan berakhir dan masuk ke kondisi berikutnya dibawah
# dan apabila loopingan terus berlanjut hingga input-1 ternyata tidak ditemukan hasil 0 maka tetap akan di hentikan agar tidak infinity looping dan dilanjutkan kondisi else dibawahnya
# sebagai contoh yang dimaksud input-1 adalah: jika user memasukkan input 5 maka looping akan berjalan dengan memeriksa
# 5 dibagi 2 = 1  maka artinya akan dilanjutkan ke angka berikutnya sesuai dengan loopingan hingga berakhir di angka 4 karena tidak mungkin jika loopingan terus berjalan hingga 5 maka 5 dibagi 5 akan menghasilkan 0 dan itu akan membuat program akan selamanya menghasilkan nilai true
# ini adalah nilai default dari loopingan for yang secara sengaja mengurangi 1 angka yang aku mention diatas input-1 (ntahlah sudah default nya begitu)
# jika pernah belajar javascript bagian looping juga variabel i dalam looping for diberikan increment atau i++ yang berarti nilai finisih pada range() akan menambahkan angka 1 yang berarti jika kita gunakan input 5 tadi maka dengan adanya increment akan menghasilkan output 5 dibagi 5
# semoga paham dengan penjelasannya ^^

if flag: # cek apakah flag bernilai True
    print(f'{num} adalah bilangan prima')
else: # jika tidak maka print bukan
    print(f'{num} bukanlah bilangan prima')

