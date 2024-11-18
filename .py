Data_Nilai = [30, 30, 40]
Komponen = [75, 80, 68]
Nilai_Akhir = sum(b * n for b, n in zip(Data_Nilai, Komponen))
rumus = " + ".join(f"{b:.1f}*{n}" for b, n in zip(Data_Nilai, Komponen))
print(f"{rumus} = {Nilai_Akhir:.2f}")