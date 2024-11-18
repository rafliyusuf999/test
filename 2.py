f = open("myfile.txt", 'r')
lines = f.readlines()
baris1 = [float(x)/100 for x in lines[0].split()]
nilai = [float(x) for x in lines[1].split()]

nilai_akhir = 0
for b, n in zip(baris1, nilai):
    nilai_akhir += b * n
    
print(f"Detail perhitungan:")
print(f"{baris1[0]}{nilai[0]} + {baris1[1]}{nilai[1]} + {baris1[2]}*{nilai[2]} = {nilai_akhir}")
print(f"Nilai akhir = {nilai_akhir}")