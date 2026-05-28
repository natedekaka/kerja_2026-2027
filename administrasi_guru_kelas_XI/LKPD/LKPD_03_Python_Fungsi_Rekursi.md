# LKPD - Python Fungsi dan Rekursi
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XI / Ganjil
**Materi Pokok:** Bab 2 - Fungsi, Rekursi (Faktorial, Fibonacci), dan Algoritma Greedy (Pecahan Uang)
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Mendefinisikan dan memanggil fungsi dalam Python
2. Menerapkan fungsi rekursif untuk faktorial dan fibonacci
3. Mengimplementasikan algoritma greedy untuk masalah pecahan uang
4. Membedakan fungsi iteratif dan rekursif

## B. Alat dan Bahan
1. Komputer/laptop dengan Python 3.x
2. Teks editor / IDE Python
3. Google Colab (alternatif)

## C. Langkah Kerja

### Langkah 1: Dasar Fungsi
Buat file `fungsi_dasar.py`:
```python
# Fungsi tanpa parameter
def sapa():
    print("Halo! Selamat belajar fungsi Python.")

def garis():
    print("=" * 40)

# Fungsi dengan parameter
def sapa_orang(nama):
    print(f"Halo, {nama}! Selamat datang.")

# Fungsi dengan return value
def luas_persegi(sisi):
    return sisi * sisi

# Main program
garis()
sapa()
garis()
sapa_orang("Alex")
sapa_orang("Budi")

luas = luas_persegi(5)
print(f"Luas persegi (sisi=5) = {luas}")
```

### Langkah 2: Fungsi dengan Multiple Parameter
Buat file `fungsi_lanjut.py`:
```python
# Fungsi dengan banyak parameter
def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_volume(p, l, t):
    return p * l * t

def info_balok(p, l, t):
    luas = hitung_luas(p, l)
    volume = hitung_volume(p, l, t)
    print(f"Panjang: {p}, Lebar: {l}, Tinggi: {t}")
    print(f"Luas Alas: {luas}")
    print(f"Volume: {volume}")

# Main
info_balok(10, 5, 3)
print()

# Fungsi dengan default parameter
def pangkat(bilangan, eksponen=2):
    return bilangan ** eksponen

print(f"3^2 = {pangkat(3)}")
print(f"3^4 = {pangkat(3, 4)}")
```

### Langkah 3: Fungsi Rekursif - Faktorial
Buat file `faktorial.py`:
```python
# Faktorial secara iteratif
def faktorial_iteratif(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

# Faktorial secara rekursif
def faktorial_rekursif(n):
    if n <= 1:          # base case
        return 1
    else:               # recursive case
        return n * faktorial_rekursif(n - 1)

# Demo
print("Faktorial dengan iterasi:")
for i in range(0, 8):
    print(f"{i}! = {faktorial_iteratif(i)}")

print("\nFaktorial dengan rekursi:")
for i in range(0, 8):
    print(f"{i}! = {faktorial_rekursif(i)}")

print(f"\n5! = {faktorial_rekursif(5)}")
# Visualisasi: faktorial_rekursif(5)
# = 5 * faktorial_rekursif(4)
# = 5 * 4 * faktorial_rekursif(3)
# = 5 * 4 * 3 * faktorial_rekursif(2)
# = 5 * 4 * 3 * 2 * faktorial_rekursif(1)
# = 5 * 4 * 3 * 2 * 1 = 120
```

### Langkah 4: Fungsi Rekursif - Fibonacci
Buat file `fibonacci.py`:
```python
# Fibonacci secara rekursif
def fibonacci(n):
    if n <= 1:          # base case: F(0)=0, F(1)=1
        return n
    else:               # recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Cetak deret Fibonacci
print("Deret Fibonacci:")
n = int(input("Masukkan jumlah suku: "))
print("Rekursif:")
for i in range(n):
    print(f"F({i}) = {fibonacci(i)}")
```

### Langkah 5: Algoritma Greedy - Pecahan Uang
Buat file `pecahan_uang.py`:
```python
# Algoritma Greedy untuk Pecahan Uang
def tukar_uang(jumlah, pecahan):
    """
    Mencari kombinasi pecahan uang dengan jumlah koin minimal (greedy).
    pecahan: list pecahan yang tersedia (urut menurun)
    """
    sisa = jumlah
    hasil = {}  # dictionary untuk menyimpan hasil

    for p in pecahan:
        if sisa >= p:
            count = sisa // p         # berapa banyak pecahan p
            sisa = sisa % p           # sisa setelah diambil
            hasil[p] = count          # simpan ke dictionary
            print(f"Rp{p}: {count} keping/lembar")

    return hasil

# Pecahan uang Rupiah (urut dari terbesar)
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

print("=== Algoritma Greedy: Penukaran Uang ===")
jumlah = int(input("Masukkan jumlah uang: Rp"))
print(f"\nMenukar Rp{jumlah:,} dengan pecahan terkecil:")
hasil = tukar_uang(jumlah, pecahan)
```

### Langkah 6: Program Lengkap - Kombinasi Fungsi
Buat file `program_lengkap.py` dan lengkapi bagian yang kosong:
```python
# === PROGRAM FUNGSI LENGKAP ===

def tampil_menu():
    print("\n=== MENU FUNGSI ===")
    print("1. Faktorial")
    print("2. Fibonacci")
    print("3. Tukar Pecahan Uang")
    print("4. Keluar")

def hitung_faktorial():
    # TODO: buat fungsi faktorial (rekursif)
    n = int(input("Masukkan angka: "))
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    print(f"{n}! = {hasil}")

def cetak_fibonacci():
    # TODO: buat fungsi cetak fibonacci
    n = int(input("Masukkan jumlah suku: "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def tukar_uang():
    # TODO: buat fungsi tukar uang greedy
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    jumlah = int(input("Masukkan jumlah uang: Rp"))
    sisa = jumlah
    for p in pecahan:
        if sisa >= p:
            count = sisa // p
            sisa = sisa % p
            print(f"Rp{p} x {count}")

# Main program
while True:
    tampil_menu()
    pilih = int(input("Pilih menu: "))
    if pilih == 1:
        hitung_faktorial()
    elif pilih == 2:
        cetak_fibonacci()
    elif pilih == 3:
        tukar_uang()
    elif pilih == 4:
        print("Program selesai.")
        break
```

## D. Tabel Hasil/Data Pengamatan

| No | Program | Input | Output | Keterangan |
|----|---------|-------|--------|------------|
| 1 | fungsi_dasar.py | - | | |
| 2 | faktorial.py | n=6 | | |
| 3 | fibonacci.py | n=8 | | |
| 4 | pecahan_uang.py | Rp175.000 | | |
| 5 | program_lengkap.py | pilih 1, n=5 | | |

## E. Diskusi dan Analisis
1. Apa perbedaan fungsi iteratif dan rekursif? Sebutkan kelebihan dan kekurangan masing-masing.
2. Pada fungsi faktorial rekursif, apa yang dimaksud *base case* dan *recursive case*? Apa yang terjadi jika tidak ada base case?
3. Mengapa algoritma greedy pada pecahan uang menggunakan pecahan yang diurutkan dari terbesar ke terkecil? Apakah selalu menghasilkan solusi optimal? Jelaskan.
4. Buatlah visualisasi/dekomposisi pemanggilan `fibonacci(5)` secara rekursif (pohon rekursi).
5. Buatlah fungsi rekursif untuk menghitung pangkat: `pangkat(bil, eks)` yang mengembalikan `bil` pangkat `eks`.

## F. Kesimpulan
Tuliskan kesimpulan dari praktikum ini minimal 3 poin.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Fungsi dasar dan parameter | 15% | | |
| Fungsi rekursif faktorial | 20% | | |
| Fungsi rekursif fibonacci | 20% | | |
| Algoritma greedy pecahan uang | 20% | | |
| Jawaban diskusi dan analisis | 15% | | |
| Kesimpulan | 10% | | |
| **Total** | **100%** | | |
