# Program Body Mass Index adalah Alat Pengukur Badan Ideal

def bodymassindex(weight, height_c):
    height_m = height_c / 100
    return round((weight/height_m **2),2)

h = float(input("Masukkan Tinggi Badan(Cm):  "))
w = float(input("Masukkan Berat Badan(Kg):  "))

bmi = bodymassindex(w, h)
print("BMI Kamu Adalah: ", bmi)

if bmi <= 18.5:
    print("Berat Badanmu dibawah rata-rata")
elif 18.5 < bmi <= 24.9:
    print("Berat Badanmu Normal")
elif 25 < bmi <= 29.29:
    print("Berat Badanmu diatas rata-rata")
else:
    print("Berat Badanmu Obesitas")