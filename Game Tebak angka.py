import random

rahasia = random.randint(1,100)
print("=" * 40)
print("Game Tebak Angka")
print("=" * 40)

print("1. Level Mudah")
print("2. Level Menengah")
print("3. Level Sulit")
level = int(input("Pilih Level: "))

batas = 0
if level == 1:
    batas = 15
elif level == 2:
    batas = 10
elif level == 3:
    batas = 5
    
for percobaan in range(batas):
    jawaban = int(input(f"Percobaan ke- {percobaan + 1}, masukan angka tebakanmu: "))
    if jawaban == rahasia:
        print("Jawabanmu benar!!!")
        break
    else:
        print(
            "Tebakan mu terlalu",
            "kecil" if jawaban < rahasia else "besar"
            )
        
else:
    print("Kesempatan mu sudah habis")