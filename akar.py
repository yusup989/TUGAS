# Program Akar
# Programer : Muhamad Yusup Alfajar
# Tanggal ( v1.0 ) : 8 Februari 2025 

import math
bilangan = float(input("Masukkan bilangan: "))
pangkat = float(input("Masukkan pangkat akar (misalnya 3 untuk akar pangkat tiga): "))
if bilangan >= 0 or (bilangan < 0 and pangkat % 2 != 0):
    akar = bilangan ** (1 / pangkat)
    print(f"Akar pangkat {pangkat} dari {bilangan} adalah {akar}")
else:
    print("Maaf, akar pangkat genap dari bilangan negatif tidak dapat dihitung dalam bilangan real.")