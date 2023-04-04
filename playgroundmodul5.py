# Latihan 1

nama = "Pramudhita Bagus Tri Wibowo"

for i in nama:
    print(i)

# Latihan 2

matkul = ["1. Biologi","2. Fisika Dasar","3. Kalkulus","4. Material Teknik","5. Mekanika Teknik","6. Analisis dan Estimasi Biaya","7. Psikologi Industri"]

print("\nDaftar Mata Kuliah Teknik Industri :\n")
for i in matkul:
    print(i)
    if i == "4. Material Teknik":
        print(f"Aku sangat suka Mata Kuliah Material Teknik")

print("\nDaftar Mata Kuliah Teknik Industri :\n")
for matkul in ["Biologi","Fisika Dasar","Kalkulus","Material Teknik","Mekanika Teknik","Analisis dan Estimasi Biaya","Psikologi Industri"]:
    if matkul == "Kalkulus":
        print("Aku sangat suka Mata Kuliah", matkul)
    else:
        print(matkul)
print()
