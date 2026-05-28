# LKPD - Sorting dan Searching dalam Bahasa C
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XII / Ganjil
**Materi Pokok:** Bab 3 – Algoritma Sorting & Searching
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Peserta didik mampu mengimplementasikan Bubble Sort dan Selection Sort dalam C.
2. Peserta didik mampu mengimplementasikan Linear Search dan Binary Search dalam C.
3. Peserta didik mampu menganalisis kompleksitas waktu algoritma sorting dan searching.
4. Peserta didik mampu membandingkan efisiensi berbagai algoritma.

## B. Alat dan Bahan
- PC/Laptop dengan compiler C (GCC/MinGW/Dev-C++/CodeBlocks)
- Teks editor (VS Code / CodeBlocks / vim)
- Terminal/Command Prompt

## C. Langkah Kerja

### Bagian 1: Bubble Sort (45 menit)

**Teori:** Bubble Sort membandingkan elemen bersebelahan dan menukar jika tidak urut. Proses diulang sampai semua terurut.

1. Buat file `bubble_sort.c`:

```c
#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Tukar elemen
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void cetakArray(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Array sebelum sorting: ");
    cetakArray(arr, n);

    bubbleSort(arr, n);

    printf("Array setelah sorting: ");
    cetakArray(arr, n);

    return 0;
}
```

2. Kompilasi dan jalankan:
```bash
gcc bubble_sort.c -o bubble_sort
./bubble_sort
```

3. **Modifikasi:** Tambahkan variabel `counter` untuk menghitung berapa kali perbandingan terjadi.

### Bagian 2: Selection Sort (45 menit)

**Teori:** Selection Sort mencari elemen terkecil lalu menukar dengan elemen pertama, kemudian mencari elemen terkecil kedua, dan seterusnya.

1. Buat file `selection_sort.c`:

```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    int i, j, minIdx, temp;
    
    for (i = 0; i < n - 1; i++) {
        minIdx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Tukar elemen terkecil dengan elemen ke-i
        if (minIdx != i) {
            temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
    }
}

void cetakArray(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {29, 10, 14, 37, 13, 33, 48};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Array sebelum sorting: ");
    cetakArray(arr, n);

    selectionSort(arr, n);

    printf("Array setelah sorting: ");
    cetakArray(arr, n);

    return 0;
}
```

### Bagian 3: Linear Search (45 menit)

1. Buat file `linear_search.c`:

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int cari) {
    int i;
    for (i = 0; i < n; i++) {
        if (arr[i] == cari) {
            return i;  // Ditemukan di indeks i
        }
    }
    return -1;  // Tidak ditemukan
}

int main() {
    int arr[] = {12, 34, 54, 2, 3, 78, 45, 23, 67, 89};
    int n = sizeof(arr) / sizeof(arr[0]);
    int cari, hasil;

    printf("Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("Masukkan angka yang dicari: ");
    scanf("%d", &cari);

    hasil = linearSearch(arr, n, cari);

    if (hasil != -1) {
        printf("Angka %d ditemukan di indeks ke-%d\n", cari, hasil);
    } else {
        printf("Angka %d tidak ditemukan\n", cari);
    }

    return 0;
}
```

### Bagian 4: Binary Search (60 menit)

**Syarat:** Array HARUS sudah terurut.

1. Buat file `binary_search.c`:

```c
#include <stdio.h>

int binarySearch(int arr[], int kiri, int kanan, int cari) {
    while (kiri <= kanan) {
        int tengah = kiri + (kanan - kiri) / 2;
        
        // Jika elemen tengah adalah yang dicari
        if (arr[tengah] == cari) {
            return tengah;
        }
        
        // Jika cari lebih besar, abaikan kiri
        if (arr[tengah] < cari) {
            kiri = tengah + 1;
        }
        // Jika cari lebih kecil, abaikan kanan
        else {
            kanan = tengah - 1;
        }
    }
    
    return -1;  // Tidak ditemukan
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 45, 56, 72};
    int n = sizeof(arr) / sizeof(arr[0]);
    int cari, hasil;

    printf("Array terurut: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("Masukkan angka yang dicari: ");
    scanf("%d", &cari);

    hasil = binarySearch(arr, 0, n - 1, cari);

    if (hasil != -1) {
        printf("Angka %d ditemukan di indeks ke-%d\n", cari, hasil);
    } else {
        printf("Angka %d tidak ditemukan\n", cari);
    }

    return 0;
}
```

2. **Modifikasi:** Buat versi rekursif dari Binary Search:

```c
int binarySearchRekursif(int arr[], int kiri, int kanan, int cari) {
    if (kanan >= kiri) {
        int tengah = kiri + (kanan - kiri) / 2;
        
        if (arr[tengah] == cari)
            return tengah;
        
        if (arr[tengah] > cari)
            return binarySearchRekursif(arr, kiri, tengah - 1, cari);
        
        return binarySearchRekursif(arr, tengah + 1, kanan, cari);
    }
    
    return -1;
}
```

### Bagian 5: Perbandingan Kinerja (45 menit)

Buat program yang membandingkan waktu eksekusi:

```c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void bubbleSort(int arr[], int n);
void selectionSort(int arr[], int n);
void cetakArray(int arr[], int n);

int main() {
    int arr[1000];
    int arrCopy[1000];
    int n = 1000;
    clock_t start, end;
    double waktu;

    srand(time(NULL));
    
    // Generate 1000 angka acak
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000;
    }

    // Uji Bubble Sort
    for (int i = 0; i < n; i++) arrCopy[i] = arr[i];
    start = clock();
    bubbleSort(arrCopy, n);
    end = clock();
    waktu = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Bubble Sort: %.4f detik\n", waktu);

    // Uji Selection Sort
    for (int i = 0; i < n; i++) arrCopy[i] = arr[i];
    start = clock();
    selectionSort(arrCopy, n);
    end = clock();
    waktu = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Selection Sort: %.4f detik\n", waktu);

    return 0;
}
```

## D. Tabel Hasil/Data Pengamatan

### Perbandingan Algoritma Sorting
| Algoritma | n=10 | n=100 | n=1000 | n=10000 | Kompleksitas |
|-----------|------|-------|--------|---------|-------------|
| Bubble Sort | | | | | O(n²) |
| Selection Sort | | | | | O(n²) |

### Perbandingan Algoritma Searching
| Algoritma | Data Ditemukan (indeks) | Data Tidak Ditemukan | Kompleksitas |
|-----------|----------------------|---------------------|-------------|
| Linear Search (n=10) | | | O(n) |
| Binary Search (n=10) | | | O(log n) |

## E. Diskusi dan Analisis

1. Jelaskan perbedaan cara kerja Bubble Sort dan Selection Sort! Mana yang lebih efisien? Mengapa?
2. Mengapa Binary Search membutuhkan array yang sudah terurut? Apa yang terjadi jika array belum terurut?
3. Hitung secara manual berapa kali perbandingan terjadi pada Bubble Sort untuk array berisi 5 elemen!
4. Pada data yang sudah hampir terurut, algoritma sorting mana yang paling efisien? Jelaskan!
5. Jika kita memiliki 1 juta data, algoritma searching mana yang sebaiknya digunakan? Berapa perkiraan waktu yang dibutuhkan masing-masing?

## F. Kesimpulan

Buat kesimpulan tentang prinsip kerja algoritma sorting (Bubble Sort, Selection Sort) dan searching (Linear Search, Binary Search), serta pentingnya memilih algoritma yang tepat berdasarkan karakteristik data.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Program Bubble Sort | 15% | | |
| Program Selection Sort | 15% | | |
| Program Linear Search | 15% | | |
| Program Binary Search | 20% | | |
| Program perbandingan kinerja | 20% | | |
| Analisis dan kesimpulan | 15% | | |
| **Total** | **100%** | | |
