total = 0
for i in range(10):
    angka = float(input(f"Masukkan angka ke-{i+1}: "))
    total += angka 
rata_rata = total / 10
print(f"Rata-rata dari 10 angka adalah: {rata_rata}")
