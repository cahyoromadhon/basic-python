import random
print(f"Your Random Number: {random.randint(1, 100)}")

# keyword import memungkinkan python dapat memanggil atau memasukkan modul kedalam program
# print menampilkan output kedalam console
# f merupakan built-in function yang memungkinkan kita dapat memasukkan variabel kedalam string
# random.randint adalah cara python mengakses fungsi randint didalam modul random melalui .
# cara kerjanya adalah "Di dalam modul random tolong cari fungsi bernama randint dengan parameter yang bebas ditentukan developer dan dalam hal ini developer menentukan parameter 1 sampai 100"

# apabila penasaran dengan apasaja function yang ada di dalam modul yang kita panggil kita bisa menggunakan built-in function dari python yang bernama dir()
# print(dir(random))
# Output: ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# help(random)
# Ini juga akan bisa membantu dalam memahaminya karena akan muncul dokumentasi dari modul yang dipanggil namun tetap dengan syarat bahwa modul telah dilakukan import sebelum menggunakan fungsi ini agar python dapat mengembalikan modul yang dipanggil
# Jangan Lupa Tekan q untuk bisa keluar dari console documentasinya hehe


## Untuk apasaja modul yang tersedia silahkan bisa dibaca di dokumentasi python langsung ##