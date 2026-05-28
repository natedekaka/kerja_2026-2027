# LKPD - Cisco Packet Tracer
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XI / Genap
**Materi Pokok:** Bab 4 - Jaringan Komputer dan Internet (Topologi Jaringan, Konfigurasi IP/CIDR, Konektivitas)
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Merancang topologi jaringan kantor sederhana di Cisco Packet Tracer
2. Mengkonfigurasi IP address dan subnet mask (CIDR) pada perangkat jaringan
3. Melakukan pengujian konektivitas antar perangkat dengan ping
4. Menganalisis hasil pengujian dan mengidentifikasi masalah koneksi

## B. Alat dan Bahan
1. Komputer/laptop dengan sistem operasi Windows/Linux
2. Cisco Packet Tracer (minimal versi 7.x atau 8.x)
3. *Download*: https://www.netacad.com/courses/packet-tracer (gratis setelah login Cisco NetAcad)

## C. Langkah Kerja

### Langkah 1: Persiapan Cisco Packet Tracer
1. Buka aplikasi Cisco Packet Tracer
2. Pilih menu **File > New** untuk membuat project baru
3. Simpan project dengan nama `topologi_kantor.pkt`

### Langkah 2: Membuat Topologi Jaringan Kantor
Buat topologi seperti gambar berikut (deskripsi logis):

**Topologi:**
- 1 buah Router (Router-PT)
- 2 buah Switch (Switch-PT)
- 4 buah PC (PC-PT) → 2 di Switch1, 2 di Switch2
- Koneksi menggunakan kabel **Copper Straight-Through**

**Langkah detail:**
1. Dari panel *End Devices*, seret 4 PC (PC0, PC1, PC2, PC3) ke workspace
2. Dari panel *Switches*, seret 2 Switch (Switch0, Switch1) ke workspace
3. Dari panel *Routers*, seret 1 Router (Router0) ke workspace
4. Hubungkan PC0 dan PC1 ke Switch0 dengan kabel **Copper Straight-Through**
5. Hubungkan PC2 dan PC3 ke Switch1 dengan kabel **Copper Straight-Through**
6. Hubungkan Switch0 ke Router0 (port FastEthernet0/0)
7. Hubungkan Switch1 ke Router0 (port FastEthernet1/0)

### Langkah 3: Konfigurasi IP Address pada PC

**Skema IP (CIDR):**

| Perangkat | Interface | IP Address | Subnet Mask | Gateway |
|-----------|-----------|------------|-------------|---------|
| PC0 | - | 192.168.1.2 | 255.255.255.0 | 192.168.1.1 |
| PC1 | - | 192.168.1.3 | 255.255.255.0 | 192.168.1.1 |
| PC2 | - | 192.168.2.2 | 255.255.255.0 | 192.168.2.1 |
| PC3 | - | 192.168.2.3 | 255.255.255.0 | 192.168.2.1 |

**Konfigurasi PC0 (lakukan hal serupa untuk PC lainnya):**
1. Klik PC0 → tab **Desktop** → pilih **IP Configuration**
2. Pilih **Static**
3. Isi:
   - IP Address: 192.168.1.2
   - Subnet Mask: 255.255.255.0
   - Default Gateway: 192.168.1.1
   - DNS Server: (kosongkan)
4. Ulangi untuk PC1, PC2, PC3 dengan IP yang sesuai tabel

### Langkah 4: Konfigurasi Router
Klik Router0 → tab **CLI** (atau **Config**).

**Via CLI - Konfigurasi interface:**

Masuk ke mode privileged:
```
Router> enable
Router# configure terminal
```

**Konfigurasi FastEthernet0/0** (terhubung ke jaringan 192.168.1.0/24):
```
Router(config)# interface fastEthernet 0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

**Konfigurasi FastEthernet1/0** (terhubung ke jaringan 192.168.2.0/24):
```
Router(config)# interface fastEthernet 1/0
Router(config-if)# ip address 192.168.2.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# exit
Router# show ip interface brief
```

### Langkah 5: Pengujian Konektivitas (Ping Test)

**Test 1: PC0 ke Gateway**
1. Klik PC0 → tab **Desktop** → pilih **Command Prompt**
2. Ketik:
```
ping 192.168.1.1
```
3. Catat hasilnya (reply atau timeout)

**Test 2: PC0 ke PC1 (satu jaringan)**
```
ping 192.168.1.3
```

**Test 3: PC0 ke PC2 (beda jaringan)**
```
ping 192.168.2.2
```

**Test 4: PC2 ke PC3 (satu jaringan)**
1. Klik PC2 → tab **Desktop** → **Command Prompt**
```
ping 192.168.2.3
```

**Test 5: PC0 ke PC3 (beda jaringan)**
```
ping 192.168.2.3
```

### Langkah 6: Simulasi Paket Data (Opsional)
1. Beralih ke mode **Simulation** (tombol Shift+S atau icon di kanan bawah)
2. Klik **Edit Filters** → centang hanya **ICMP**
3. Klik PC0 → pilih **Ping** → target 192.168.2.3 → **Go**
4. Klik **Auto Capture / Play** untuk melihat perjalanan paket
5. Amati bagaimana paket bergerak dari PC0 → Switch0 → Router0 → Switch1 → PC3

### Langkah 7: Tugas Mandiri - Eksplorasi
Coba lakukan skenario berikut:
1. Ganti IP PC0 menjadi 192.168.1.100, apakah masih bisa ping ke gateway?
2. Ganti IP PC0 menjadi 192.168.3.2 (jaringan berbeda), ping ke 192.168.1.1. Apakah berhasil? Jelaskan.
3. Matikan interface router FastEthernet0/0 dengan perintah `shutdown`, lalu ping dari PC0 ke 192.168.1.1. Apa yang terjadi?

## D. Tabel Hasil/Data Pengamatan

| No | Pengujian | Dari | Ke | IP Tujuan | Hasil (Reply/Timeout) | Keterangan |
|----|-----------|------|----|-----------|----------------------|------------|
| 1 | Test 1 | PC0 | Gateway | 192.168.1.1 | | |
| 2 | Test 2 | PC0 | PC1 | 192.168.1.3 | | |
| 3 | Test 3 | PC0 | PC2 | 192.168.2.2 | | |
| 4 | Test 4 | PC2 | PC3 | 192.168.2.3 | | |
| 5 | Test 5 | PC0 | PC3 | 192.168.2.3 | | |
| 6 | Tugas 1 | PC0 | Gateway | 192.168.1.1 | | |
| 7 | Tugas 2 | PC0 | Gateway | 192.168.1.1 | | |
| 8 | Tugas 3 | PC0 | Gateway | 192.168.1.1 | | |

## E. Diskusi dan Analisis
1. Mengapa PC0 dan PC1 (satu jaringan 192.168.1.0/24) bisa saling ping tanpa melalui router? Jelaskan peran switch dalam hal ini.
2. Mengapa PC0 perlu gateway 192.168.1.1 agar bisa berkomunikasi dengan PC2 (jaringan 192.168.2.0/24)? Apa fungsi router?
3. Tuliskan perintah untuk melihat konfigurasi interface di router dan interpretasikan outputnya.
4. Apa yang dimaksud dengan CIDR? Hitunglah jumlah host maksimal pada jaringan 192.168.1.0/24 dan 192.168.1.0/28.
5. Jika ada 30 perangkat dalam satu jaringan, subnet mask apa yang paling efisien digunakan?

## F. Kesimpulan
Tuliskan kesimpulan dari praktikum ini minimal 3 poin.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Topologi jaringan sesuai | 20% | | |
| Konfigurasi IP dan gateway benar | 20% | | |
| Konfigurasi router benar | 20% | | |
| Pengujian ping dan analisis | 20% | | |
| Jawaban diskusi | 20% | | |
| **Total** | **100%** | | |
