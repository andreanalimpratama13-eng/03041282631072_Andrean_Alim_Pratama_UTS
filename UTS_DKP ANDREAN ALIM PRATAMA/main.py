# Data Inti
data_arus = [1.6, 2.2, 3.5, 4.1, 5.4, 2.8, 6.0, 3.9, 1.9, 4.8, 5.1, 2.6, 3.2, 4.4, 5.8]

# Data Tambahan
data_tambahan = [2.5, 6.1, 7, 7.4, 5.9]

# V Listrik
V = 220

# Data Gabungan
data_gabungan = data_arus + data_tambahan

# Fungsi 1 Daya
def hitung_daya(v, i):
    P = v * i
    return P

# Fungsi 2 Menentukan status Beban Listrik
def status_beban(p):
    if p <= 700:
        return "NORMAL"
    elif 700 < p <= 1000:
        return "WARNING"
    else:
        return "BEBAN TINGGI"

# Fungsi 3 Menghitung Rata-rata Data
def rata_rata(data):
    total = sum(data)
    jumlah_data = len(data)
    rata = total / jumlah_data
    return rata

# Proses Monitoring Beban/Daya Listrik

data_daya = []

jumlah_normal = 0
jumlah_warning = 0
jumlah_beban_tinggi = 0

print("=" * 55)
print("Monitoring Beban/Daya Listrik")
print("=" * 55)
print(f"Tegangan Listrik: {V} V")
print(f"Total data {len(data_gabungan)}")
print("=" * 55)

# Memproses 20 Data
for i, arus in enumerate(data_gabungan, start=1):

    # Menghitung Daya
    daya = hitung_daya(V, arus)

    # Menentukan Status Beban
    status = status_beban(daya)

    # Menyimpan Hasil Daya
    data_daya.append(daya)

    # Menghitung Jumlah Setiap kategori
    if status == "NORMAL":
        jumlah_normal += 1
    elif status == "WARNING":
        jumlah_warning += 1
    else:
        jumlah_beban_tinggi += 1

    # Menampilkan Hasil Setiap Data
    print(f"{i:02d}. Arus = {arus:.2f} A | "
          f"Daya = {daya:.2f} W | "
          f"Status = {status}")

# Ringkasan Hasil Monitoring
print("=" * 55)
print("RINGKASAN HASIL MONITORING")
print("=" * 55)

print(f"Total Data: {len(data_gabungan)}")
print(f"Jumlah NORMAL: {jumlah_normal}")
print(f"Jumlah WARNING: {jumlah_warning}")
print(f"Jumlah BEBAN TINGGI: {jumlah_beban_tinggi}")

print(f"Rata-rata Daya: {rata_rata(data_daya):.2f} W")
print(f"Daya Maksimum: {max(data_daya):.2f} W")
print(f"Daya Minimum: {min(data_daya):.2f} W")

print("=" * 55)
print("TESTING PROGRAM MONITORING BEBAN/DAYA LISTRIK")
print("=" * 55)

test_cases = [
    (699.99, "NORMAL"),
    (700.00, "NORMAL"),
    (700.01, "WARNING"),
    (999.99, "WARNING"),
    (1000.00, "WARNING"),
    (1000.01, "BEBAN TINGGI"),
    (220.00, "NORMAL"),
    (1320.00, "BEBAN TINGGI"),
]

for nomor, (daya, expected) in enumerate(test_cases, start=1):

    actual = status_beban(daya)

    if actual == expected:
        hasil = "PASS"
    else:
        hasil = "FAIL"

    print(f"Test {nomor}")
    print(f"Input Daya     : {daya:.2f} W")
    print(f"Expected       : {expected}")
    print(f"Actual         : {actual}")
    print(f"Hasil          : {hasil}")

    # UJI GABUNGAN PERHITUNGAN DAYA DAN STATUS

arus = 3.5

daya = hitung_daya(V, arus)
status = status_beban(daya)

print("=" * 50)
print("UJI GABUNGAN")
print("=" * 50)
print(f"Input Arus : {arus:.2f} A")
print(f"Hasil Daya : {daya:.2f} W")
print(f"Status     : {status}")
print("=" * 50)

print("=" * 55)
print("TESTING SELESAI")
print("=" * 55)