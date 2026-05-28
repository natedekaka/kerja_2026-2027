# LKPD - Konfigurasi Jaringan dengan Cisco Packet Tracer
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XII / Ganjil
**Materi Pokok:** Bab 4 – Jaringan Komputer – Routing, IP, Gateway, DNS
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Peserta didik mampu merancang topologi jaringan dengan 2 switch, 1 router, dan 4 PC.
2. Peserta didik mampu mengkonfigurasi IP address dan subnet mask pada setiap PC.
3. Peserta didik mampu mengkonfigurasi router (gateway/default gateway) untuk routing antar jaringan.
4. Peserta didik mampu menguji koneksi antar PC menggunakan perintah ping.
5. Peserta didik mampu mengkonfigurasi DNS server dan menguji resolusi nama.

## B. Alat dan Bahan
- PC/Laptop dengan Cisco Packet Tracer terinstal
- File Packet Tracer (dibuat sendiri selama praktikum)

## C. Langkah Kerja

### Bagian 1: Merancang Topologi Jaringan (30 menit)

1. Buka Cisco Packet Tracer.
2. Buat topologi jaringan berikut:

```
                        +---------------------+
                        |                     |
                        |      Router         |
                        |    (Router-PT)      |
                        |                     |
                        +--------+-----------+
                                 |
                   +-------------+-------------+
                   |                           |
            +------+------+            +------+------+
            |             |            |             |
         [Switch0]    [Switch1]    [Switch0]    [Switch1]
         (Switch-PT)  (Switch-PT)  (Switch-PT)  (Switch-PT)
            |             |            |             |
            |             |            |             |
          [PC0]         [PC1]        [PC2]         [PC3]
          (PC-PT)       (PC-PT)      (PC-PT)       (PC-PT)
```

3. Rencana pengalamatan IP:

| Perangkat | Interface | IP Address | Subnet Mask | Gateway |
|-----------|-----------|------------|-------------|---------|
| Router    | Gig0/0    | 192.168.1.1 | 255.255.255.0 | - |
| Switch0 VLAN1 | -    | 192.168.1.254 | 255.255.255.0 | 192.168.1.1 |
| PC0       | FastEthernet0 | 192.168.1.10 | 255.255.255.0 | 192.168.1.1 |
| PC1       | FastEthernet0 | 192.168.1.11 | 255.255.255.0 | 192.168.1.1 |
| Router    | Gig0/1    | 192.168.2.1 | 255.255.255.0 | - |
| Switch1 VLAN1 | -    | 192.168.2.254 | 255.255.255.0 | 192.168.2.1 |
| PC2       | FastEthernet0 | 192.168.2.10 | 255.255.255.0 | 192.168.2.1 |
| PC3       | FastEthernet0 | 192.168.2.11 | 255.255.255.0 | 192.168.2.1 |

### Bagian 2: Menambahkan dan Menghubungkan Perangkat (30 menit)

1. Dari panel **End Devices**, seret 4 PC (PC-PT) ke workspace.
2. Dari panel **Network Devices > Switches**, seret 2 Switch (Switch-PT).
3. Dari panel **Network Devices > Routers**, seret 1 Router (Router-PT).
4. Hubungkan kabel:
   - **PC0 → Switch0:** Gunakan kabel **Copper Straight-Through**
     - Klik PC0 → pilih FastEthernet0 → klik Switch0 → pilih port FastEthernet0/1
   - **PC1 → Switch0:** FastEthernet0 → Switch0 FastEthernet0/2
   - **Switch0 → Router:** Switch0 FastEthernet0/24 → Router GigabitEthernet0/0
   - **PC2 → Switch1:** FastEthernet0 → Switch1 FastEthernet0/1
   - **PC3 → Switch1:** FastEthernet0 → Switch1 FastEthernet0/2
   - **Switch1 → Router:** Switch1 FastEthernet0/24 → Router GigabitEthernet0/1

### Bagian 3: Konfigurasi IP pada PC (30 menit)

1. Klik **PC0** → Tab **Desktop** → **IP Configuration**.
2. Isi:
   - IP Address: `192.168.1.10`
   - Subnet Mask: `255.255.255.0`
   - Default Gateway: `192.168.1.1`
   - DNS Server: (kosongkan dulu)
3. Ulangi untuk PC1:
   - IP: `192.168.1.11` / Mask: `255.255.255.0` / Gateway: `192.168.1.1`
4. Ulangi untuk PC2:
   - IP: `192.168.2.10` / Mask: `255.255.255.0` / Gateway: `192.168.2.1`
5. Ulangi untuk PC3:
   - IP: `192.168.2.11` / Mask: `255.255.255.0` / Gateway: `192.168.2.1`

### Bagian 4: Konfigurasi Router (45 menit)

1. Klik **Router** → Tab **CLI**.
2. Ketik perintah berikut (ENTER setelah setiap baris):

```
enable
configure terminal
hostname R1

interface GigabitEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit

interface GigabitEthernet0/1
ip address 192.168.2.1 255.255.255.0
no shutdown
exit

exit
write memory
```

3. Verifikasi konfigurasi:
```
show ip interface brief
```
Pastikan kedua interface berstatus `up` dan `up`.

### Bagian 5: Uji Koneksi (Ping) (30 menit)

1. Klik **PC0** → Tab **Desktop** → **Command Prompt**.
2. Uji koneksi ke gateway sendiri:
```
ping 192.168.1.1
```
Jika berhasil: `Reply from 192.168.1.1: bytes=32 time<1ms TTL=255`

3. Uji koneksi ke PC1 (satu jaringan):
```
ping 192.168.1.11
```

4. Uji koneksi ke PC2 (beda jaringan):
```
ping 192.168.2.10
```

5. Ulangi dari PC2:
```
ping 192.168.1.10
ping 192.168.1.11
ping 192.168.2.1
```

6. Catat hasil ping ke tabel pengamatan.

### Bagian 6: Konfigurasi DNS Server (45 menit)

1. Tambahkan **Server-PT** dari panel **End Devices**.
2. Hubungkan server ke **Switch0** (FastEthernet0 → Switch0 FastEthernet0/3).
3. Konfigurasi IP Server:
   - IP: `192.168.1.100` / Mask: `255.255.255.0` / Gateway: `192.168.1.1`
4. Klik **Server** → Tab **Services** → **DNS**.
5. Aktifkan DNS dengan **On**.
6. Tambahkan record:
   - Name: `www.sekolahku.local` → Address: `192.168.1.10` (PC0)
   - Name: `mail.sekolahku.local` → Address: `192.168.1.11` (PC1)
   - Name: `server.sekolahku.local` → Address: `192.168.1.100`
   - Klik **Add** setiap kali.
7. Konfigurasi DNS di PC0:
   - Klik **PC0** → **Desktop** → **IP Configuration**
   - DNS Server: `192.168.1.100`
8. Ulangi untuk PC1, PC2, PC3 dengan DNS Server yang sama.
9. Uji DNS dari **Command Prompt PC0**:
```
ping www.sekolahku.local
ping mail.sekolahku.local
```

10. Jika berhasil, akan muncul `Reply from 192.168.1.10 ...` (nama domain beresolusi ke IP).

## D. Tabel Hasil/Data Pengamatan

### Hasil Uji Ping
| Dari | Ke | IP Tujuan | Status (Success/Fail) | Waktu (ms) |
|------|----|-----------|----------------------|------------|
| PC0  | Gateway | 192.168.1.1 | | |
| PC0  | PC1 | 192.168.1.11 | | |
| PC0  | PC2 | 192.168.2.10 | | |
| PC2  | PC0 | 192.168.1.10 | | |
| PC2  | Gateway | 192.168.2.1 | | |
| PC2  | PC1 | 192.168.1.11 | | |

### Hasil Uji DNS
| Dari | Nama Domain | Hasil Resolusi IP | Status |
|------|-------------|-------------------|--------|
| PC0  | www.sekolahku.local | | |
| PC0  | mail.sekolahku.local | | |
| PC1  | server.sekolahku.local | | |

## E. Diskusi dan Analisis

1. Mengapa PC0 dapat melakukan ping ke PC1 (satu jaringan) tanpa konfigurasi router? Jelaskan alurnya!
2. Apa fungsi default gateway pada konfigurasi IP setiap PC? Apa yang terjadi jika gateway tidak diisi?
3. Pada saat PC0 melakukan ping ke PC2 (beda jaringan), data melewati perangkat apa saja? Sebutkan jalur lengkapnya!
4. Bagaimana cara router mengetahui bahwa paket untuk 192.168.2.x harus dikirim ke interface Gig0/1?
5. Apa keuntungan menggunakan DNS dibandingkan menggunakan IP address secara langsung? Dalam skenario apa penggunaan DNS menjadi sangat penting?

## F. Kesimpulan

Buat kesimpulan tentang konsep routing antar jaringan, fungsi gateway, peran DNS dalam resolusi nama, dan pentingnya konfigurasi IP yang benar dalam komunikasi jaringan.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Topologi jaringan | 15% | | |
| Konfigurasi IP setiap PC | 15% | | |
| Konfigurasi router (CLI) | 20% | | |
| Uji koneksi (ping) | 15% | | |
| Konfigurasi DNS | 20% | | |
| Analisis dan kesimpulan | 15% | | |
| **Total** | **100%** | | |
