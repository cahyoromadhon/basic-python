def extract_username(email):
    parts = email.split('@')

    if len(parts) == 2:
        return parts[0]
    else:
        return "Invalid email format"
    
try:
    email = input('Masukkan Email Address:  ')
    username = extract_username(email)
    print(username)
except ValueError:
    print('Invalid input, Masukkan Input Email yang sesuai')

# deklarasi fungsi dengan indentasi extract_username dengan parameter variabel email
# deklarasi variabel lokal bernama parts dan gunakan anotasi dot dan built-in function bernama split
# agar kalimat dapat tersplit maka spesifikkan parameternya menggunakan @
# check apakah email address memiliki format yang diharapkan
# jika panjang email sesuai maka masuk ke sintaks selanjutnya
# menggunakan try-except agar dapat menangkap error di akhir kodenya
# deklarasikan variabel input bernama email yang memungkinkan user dapat memasukkan sebuah input
# deklarasikan username dengan value function beserta parameternya
# print variabel yang berisikan fungsi yang telah dideklarasikan diatas
# namun jika terjadi error maka tangkap error menggunakan ValueError
# lalu print string ke console
