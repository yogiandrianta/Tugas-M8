nilai_kuis = [80, 75, 90, 65]

for nilai in nilai_kuis:
    hasil = nilai + 5
    print(hasil)

#2
for i in range(3, 31, 3):
    print(i, end=" ")

#3
teks = "STATISTIKA BISNIS"

for huruf in teks:
    print(huruf.lower())

#4
peserta = ["Ijul", "Chlea", "Reza", "Citra", "Budi"]

for nama in peserta:
    if nama == "Reza":
        continue
    print(nama)

#5
departemen = ["Statbis", "Statistika", "Matematika"]
angkatan = [2025, 2026]

for dept in departemen:
    for angk in angkatan:
        print(f"{dept} angkatan {angk}")

#6
pelamar = [("Budi", 3.2, 5), ("Siti", 3.6, 3), ("Dodi", 3.8, 1)]

for nama, ipk, semester in pelamar:
    if ipk >= 3.5 and semester > 2:
        print(f"{nama}: Diterima")
    else:
        print(f"{nama}: Ditolak")

#7
karyawan = [("Joko", "IT", 7000), ("Rina", "HR", 5000), ("Toni", "Data", 8000), ("Lia", "IT", 6500)]
total_gaji = 0

for nama, departemen, gaji in karyawan:
    if departemen == "IT" or departemen == "Data":
        total_gaji += gaji

print(total_gaji)

#8
penjualan = [("Kopi", 60, False), ("Teh", 30, False), ("Boba", 80, True)]

for nama, jumlah, promo in penjualan:
    if jumlah > 50 and not promo:
        print(nama)