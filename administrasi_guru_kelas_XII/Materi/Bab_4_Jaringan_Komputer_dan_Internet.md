# 🌐 Bab 4: Jaringan Komputer dan Internet

> **Semester Genap** | **Fase F** | **Kelas XII** | **25 JP**

---

---
## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Jaringan Komputer dan Internet | Peserta didik mampu memahami konsep jaringan komputer, topologi, perangkat jaringan, dan protokol TCP/IP, serta menerapkan prinsip keamanan siber. |

## 🎯 Tujuan Pembelajaran

- **A.** Apa Itu Jaringan Komputer?
- **B.** Topologi Jaringan
- **C.** Komponen & Perangkat Jaringan
- **D.** Bagaimana Data Bepergian? (TCP/IP)
- **E.** Cyber Security: Jaga Diri di Dunia Maya

## 🗺️ Peta Konsep

```
               🌐 JARINGAN KOMPUTER DAN INTERNET
                     |
                     ├── A. Apa Itu Jaringan Komputer?
                     ├── B. Topologi Jaringan
                     ├── C. Komponen & Perangkat Jaringan
                     ├── D. Bagaimana Data Bepergian? (TCP/IP)
                     └── E. Cyber Security: Jaga Diri di Dunia Maya
```

## A. Apa Itu Jaringan Komputer?

### 🌐 Apa Itu Jaringan Komputer?
Jaringan komputer adalah **dua atau lebih komputer yang saling terhubung** untuk berbagi data, file, printer, dan koneksi internet.

> 🧩 **Analogi:** Jaringan komputer itu seperti sistem jalan raya. Setiap komputer adalah sebuah rumah. Jalan raya menghubungkan rumah-rumah itu sehingga bisa saling mengirim barang (data). **Internet adalah jalan tol antar kota!**

### Manfaat Jaringan
1. 📂 **Berbagi file** — Kirim dokumen tanpa flashdisk
2. 🖨️ **Berbagi printer** — Satu printer dipakai banyak komputer
3. 🌍 **Internet** — Akses informasi global
4. 💬 **Komunikasi** — Email, chat, video call
5. ☁️ **Cloud storage** — Simpan data di server, akses dari mana saja

### Klasifikasi Jaringan
| Jenis | Luas Area | Contoh | Analogi |
|-------|-----------|--------|---------|
| **PAN** | 1-10 m | Bluetooth hape ke speaker | Kamar pribadi |
| **LAN** | 10-1000 m | Lab komputer sekolah | Perumahan |
| **MAN** | 10-50 km | Antar kecamatan dalam kota | Satu kota |
| **WAN** | 100+ km | Internet global | Seluruh Indonesia |

### 🔍 Cek Pemahaman
1. Apa perbedaan LAN dan WAN?
2. Sebutkan 3 manfaat jaringan komputer!
3. Berikan contoh jaringan PAN dalam kehidupan sehari-hari!

### 📋 Studi Kasus
**Jaringan Lab Komputer Sekolah**

SMA Negeri 1 memiliki 3 lab komputer. Lab A (30 PC), Lab B (20 PC), dan Lab C (15 PC). Setiap lab punya switch sendiri, dan ketiganya terhubung ke router utama. Guru bisa mencetak dari lab mana pun ke printer yang ada di Lab A. Kepala sekolah juga bisa memonitor aktivitas semua lab dari ruangannya.

*Pertanyaan:*
1. Tipe jaringan apa yang digunakan di setiap lab? (LAN/MAN/WAN)
2. Perangkat apa yang menghubungkan ketiga lab dan menghubungkan ke internet?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Topologi Jaringan

### 📐 Topologi Jaringan
Topologi adalah bentuk/susunan koneksi antar komputer dalam jaringan.

### Jenis-Jenis Topologi

#### 1. Bus 🚌
```
     ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
     │ PC 1 │  │ PC 2 │  │ PC 3 │  │ PC 4 │
     └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘
        └─────────┴─────────┴─────────┘
     ═══════════════KABEL═══════════════════
```
✅ Hemat kabel | ❌ Kalau kabel putus, semua mati

#### 2. Star ⭐
```
                ┌──────┐
                │ PC 1 │
                └──┬───┘
                   │
        ┌──────┐  ┌─┴──────┐  ┌──────┐
        │ PC 2 ├──┤ SWITCH ├──┤ PC 3 │
        └──────┘  └──┬─────┘  └──────┘
                   │
                ┌──┴───┐
                │ PC 4 │
                └──────┘
```
✅ Paling populer, jika 1 kabel putus yang lain aman | ❌ Butuh switch

#### 3. Ring ⭕ — Data mengalir satu arah. Jika satu mati, semua terpengaruh.

#### 4. Mesh 🔀 — Setiap komputer terhubung ke semua. Paling andal, paling boros kabel.

### 🔍 Cek Pemahaman
1. Sebutkan 4 jenis topologi jaringan!
2. Mengapa topologi Star paling banyak digunakan?
3. Apa kelemahan topologi Bus?

### 📋 Studi Kasus
**Memilih Topologi untuk Kantor Desa**

Kantor Desa Sukamaju akan memasang jaringan untuk 8 komputer. Anggaran terbatas, tapi jaringan harus tetap berfungsi meskipun salah satu kabel putus. Pak Lurah minta saran topologi yang tepat.

*Pertanyaan:*
1. Topologi apa yang paling tepat untuk kondisi ini? Mengapa?
2. Gambarkan skema topologi yang kamu usulkan!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Komponen & Perangkat Jaringan

### 🖧 Komponen & Perangkat Jaringan

| Perangkat | Fungsi | Analogi |
|-----------|--------|---------|
| **Router** | Menghubungkan jaringan berbeda (LAN ke Internet) | Pintu gerbang antar perumahan |
| **Switch** | Menghubungkan banyak komputer dalam satu LAN | Pos satpam yang mengatur lalu lintas |
| **Modem** | Mengubah sinyal ISP jadi sinyal digital | Penerjemah bahasa |
| **Access Point** | Memancarkan WiFi | Menara sinyal di perumahan |
| **NIC/Kartu LAN** | Setiap komputer punya ini agar bisa jaringan | Pintu rumah agar bisa keluar/masuk |

### Kabel UTP
```
   ╔══╗  ╔══╗  ╔══╗  ╔══╗
   ║  ║  ║  ║  ║  ║  ║  ║  ← 8 pin (RJ45)
   ╚══╝  ╚══╝  ╚══╝  ╚══╝
```

**Urutan Kabel Straight:**
Pin 1: Putih-Oranye | Pin 2: Oranye | Pin 3: Putih-Hijau | Pin 4: Biru
Pin 5: Putih-Biru | Pin 6: Hijau | Pin 7: Putih-Coklat | Pin 8: Coklat

### 🔍 Cek Pemahaman
1. Apa fungsi router dan switch? Jelaskan perbedaannya!
2. Kapan menggunakan kabel Straight dan kapan Crossover?
3. Apa kepanjangan dari NIC?

### 📋 Studi Kasus
**Jaringan Internet di Rumah**

Keluarga Pak Budi berlangganan IndiHome. Modem dari ISP terhubung ke router WiFi. Router terhubung ke switch yang melayani 3 komputer (PC kakak, PC adik, PC Pak Budi) dan 1 printer. Semua anggota keluarga juga bisa WiFi-an dari smartphone masing-masing.

*Pertanyaan:*
1. Identifikasi perangkat: mana modem, router, switch dalam kasus ini?
2. Apa fungsi masing-masing perangkat tersebut?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Bagaimana Data Bepergian? (TCP/IP)

### 📦 Bagaimana Data Bepergian? (TCP/IP)
TCP/IP adalah protokol (aturan) yang mengatur bagaimana data dikirim melalui internet.

> 🧩 **Analogi:** Bayangkan kamu mau kirim kue ke teman di luar kota.
> 1. Kue dipotong jadi potongan kecil → Data dipecah jadi paket (TCP)
> 2. Setiap potong dibungkus dan dialamati → Paket data + alamat IP
> 3. Kurir antar ke alamat tujuan → Routing lewat router
> 4. Teman konfirmasi semua potong sampai → ACK (TCP)
> 5. Kue dirakit lagi → Data di-rakit ulang

### TCP vs UDP
| TCP | UDP |
|-----|-----|
| ✅ Data sampai utuh | ✅ Cepat, tanpa konfirmasi |
| ❌ Lebih lambat | ❌ Ada kemungkinan data hilang |
| Untuk: Download file, browsing web | Untuk: Streaming video, VoIP, game |

### IP Address & DNS
- **IP Address** = alamat unik setiap perangkat (contoh: 192.168.1.1)
- **DNS** = Buku telepon internet (`google.com` → 142.250.64.78)

```
  Kamu ketik: www.google.com
       ↓
  DNS menerjemahkan → 142.250.64.78
       ↓
  🎉 Halaman Google muncul!
```

### 🔍 Cek Pemahaman
1. Apa perbedaan TCP dan UDP?
2. Kapan sebaiknya menggunakan UDP daripada TCP?
3. Apa fungsi DNS dalam komunikasi internet?

### 📋 Studi Kasus
**Streaming Film vs Download File**

Dodi sedang streaming film di Netflix (menggunakan UDP) sambil mendownload file tugas dari Google Drive (menggunakan TCP). Saat streaming, kadang kualitas video turun tapi tidak buffering lama. Saat download, file harus utuh — kalau terputus, download diulang dari awal.

*Pertanyaan:*
1. Mengapa Netflix menggunakan UDP dan Google Drive menggunakan TCP?
2. Apa yang terjadi jika Netflix menggunakan TCP?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## E. Cyber Security: Jaga Diri di Dunia Maya

### 🔒 Cyber Security: Jaga Diri di Dunia Maya
Cyber Security adalah praktik melindungi sistem, jaringan, dan data dari serangan digital. Ibarat mengunci pintu rumah.

### Ancaman Umum
| Ancaman | Apa Itu? | Analogi |
|---------|----------|---------|
| **Malware** | Virus, trojan, ransomware | Pencuri masuk rumah |
| **Phishing** | Pemancing data pribadi | Orang mengaku satpam, padahal maling |
| **DDoS** | Serangan banjir traffic | 1000 orang antre palsu di kasir |
| **Hacking** | Membobol sistem | Maling tebak kunci rumah |
| **Social Engineering** | Manipulasi psikologis | Tipu-tipu dengan modus |

### Tips Aman di Internet 🛡️
```
  🔑  Gunakan password KUAT dan BERBEDA untuk tiap akun
  🔐  Aktifkan 2FA (otentikasi 2 faktor)
  🔗  Jangan klik link sembarangan
  📧  Cek alamat email pengirim
  🔄  Update software & antivirus
  📁  Backup data penting
```

### Password Kuat itu...
❌ `password123` — Terlalu mudah
❌ `namahewan` — Bisa ditebak dari medsos
✅ `S4y4!ncL4s$XII_2026` — Kombinasi huruf besar, kecil, angka, simbol

### 🔍 Cek Pemahaman
1. Sebutkan 3 jenis ancaman cyber security!
2. Apa perbedaan phishing dan social engineering?
3. Sebutkan 3 tips aman di internet!

### 📋 Studi Kasus
**Teman Kena Phishing**

Aldo mendapat DM Instagram dari akun yang mengaku sebagai panitia lomba desain. Akun itu meminta Aldo mengklik link "bit.ly/lombadesain" dan memasukkan username serta password Instagram-nya. Aldo curiga karena link terlihat mencurigakan. Ia bertanya pada gurunya, dan ternyata itu adalah phishing! Akun itu palsu.

*Pertanyaan:*
1. Tanda-tanda apa yang membuat Aldo curiga?
2. Apa yang sebaiknya dilakukan jika menerima DM mencurigakan seperti itu?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: 🌐 Konfigurasi Jaringan Dasar

Konfigurasi jaringan sederhana menggunakan Cisco Packet Tracer. Hubungkan 2 PC, 1 switch, dan 1 router, lalu atur IP address agar semua perangkat bisa saling ping. Proyek ini mengajarkan konsep IP addressing, subnet, dan routing dasar.

**Alat dan Bahan:**
- Cisco Packet Tracer (gratis dari NetAcad)
- Laptop/PC
- Modul panduan Cisco Packet Tracer

**Langkah-langkah:**
1. Buka Cisco Packet Tracer dan buat proyek baru
2. Tempatkan 1 router (Router-PT), 1 switch (Switch-PT), dan 2 PC (PC-PT) di workspace
3. Hubungkan PC1 dan PC2 ke switch dengan kabel Copper Straight-Through
4. Hubungkan switch ke router dengan kabel Copper Straight-Through
5. Konfigurasi IP address: PC1 = 192.168.1.2/24, PC2 = 192.168.1.3/24, Router interface = 192.168.1.1/24
6. Konfigurasi gateway default PC1 dan PC2 ke 192.168.1.1
7. Uji koneksi: dari PC1 ping ke PC2 (192.168.1.3) dan ke router (192.168.1.1)

> **Output:** File .pkt Cisco Packet Tracer dengan 2 PC + 1 switch + 1 router, semua saling ping berhasil

## 📝 Rangkuman

1. Jaringan komputer memungkinkan berbagi data, printer, dan akses internet — diklasifikasikan menjadi PAN, LAN, MAN, dan WAN berdasarkan luas area.
2. Topologi jaringan meliputi Bus (hemat kabel), Star (paling populer), Ring, dan Mesh (paling andal) — masing-masing memiliki kelebihan dan kekurangan.
3. Komponen jaringan utama meliputi Router (penghubung jaringan), Switch (penghubung dalam LAN), Modem, Access Point, dan NIC.
4. TCP/IP adalah protokol yang mengatur pengiriman data di internet — TCP memastikan data utuh, UDP mengutamakan kecepatan.
5. Cyber security melindungi sistem dari ancaman seperti malware, phishing, DDoS, dan hacking — tips aman: password kuat, 2FA, dan tidak klik link sembarangan.

---

## ✍️ Latihan Soal

### A. Pilihan Ganda

1. Jaringan yang mencakup area satu kota disebut…
   a. PAN
   b. LAN
   c. MAN
   d. WAN
   e. GAN
   **Jawaban: MAN**

2. Topologi jaringan yang paling umum digunakan di laboratorium komputer sekolah adalah…
   a. Bus
   b. Ring
   c. Mesh
   d. Star
   e. Tree
   **Jawaban: Star**

3. Perangkat yang berfungsi menghubungkan jaringan LAN ke internet adalah…
   a. Switch
   b. Hub
   c. Router
   d. Modem
   e. Access Point
   **Jawaban: Router**

4. Protokol yang memastikan data sampai dengan utuh tetapi lebih lambat adalah…
   a. UDP
   b. HTTP
   c. DNS
   d. TCP
   e. FTP
   **Jawaban: TCP**

5. Serangan yang memancing korban untuk memberikan data pribadi melalui link palsu disebut…
   a. Malware
   b. DDoS
   c. Phishing
   d. Hacking
   e. Social Engineering
   **Jawaban: Phishing**

### B. Uraian

1. Jelaskan 4 jenis topologi jaringan beserta kelebihan dan kekurangan masing-masing!

2. Bagaimana cara kerja TCP/IP dalam mengirim data dari satu komputer ke komputer lain? Gunakan analogi!

3. Jelaskan 3 ancaman cyber security yang sering terjadi dan bagaimana cara melindungi diri!

4. Apa itu DNS dan mengapa DNS penting dalam penggunaan internet sehari-hari? Jelaskan dengan contoh!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Konfigurasi Jaringan | Topologi tidak sesuai, kabel salah | Topologi benar tapi ada kesalahan konfigurasi | Topologi benar, semua perangkat terkonfigurasi tepat |
| Pemahaman IP Address | Tidak paham konsep IP address | IP address terisi tapi ada kesalahan subnet | IP address dan subnet benar semua |
| Fungsionalitas (Ping) | Tidak ada satupun ping berhasil | Ping berhasil sebagian (PC ke router saja) | Semua ping berhasil: PC1↔PC2, PC↔Router |
| Dokumentasi | Tidak ada dokumentasi | Dokumentasi ada tapi kurang detail | Dokumentasi lengkap dengan screenshot tiap langkah |

---
## 🚀 Tugas Pengayaan

### 🌐 Simulasi Jaringan dengan DHCP Server
Kembangkan proyek Cisco Packet Tracer dengan menambahkan DHCP Server sehingga PC1 dan PC2 mendapatkan IP address secara otomatis. Konfigurasi router sebagai DHCP server dengan range IP 192.168.1.10 - 192.168.1.50. Buktikan bahwa PC mendapatkan IP otomatis dan tetap bisa saling ping. Screenshot setiap langkah konfigurasi.

---
## 📖 Glosarium

- **Jaringan Komputer**: Dua atau lebih komputer yang saling terhubung untuk berbagi data dan sumber daya.
- **LAN**: Local Area Network — jaringan yang mencakup area terbatas seperti lab komputer.
- **Topologi Jaringan**: Bentuk/susunan koneksi antar komputer dalam jaringan.
- **TCP/IP**: Protokol yang mengatur bagaimana data dikirim melalui internet.
- **IP Address**: Alamat unik setiap perangkat dalam jaringan komputer.
- **DNS**: Domain Name System — menerjemahkan nama domain menjadi IP address.
- **Phishing**: Serangan yang memancing korban memberikan data pribadi melalui tautan palsu.
- **Firewall**: Sistem keamanan yang memantau dan mengontrol lalu lintas jaringan.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Apa itu Jaringan Komputer? | `youtu.be/search?q=jaringan+komputer+dasar+indonesia` | Pengantar jaringan komputer lengkap |
| YouTube | Topologi Jaringan | `youtu.be/search?q=topologi+jaringan+komputer+indonesia` | Jenis dan perbandingan topologi jaringan |
| YouTube | Cyber Security untuk Pemula | `youtu.be/search?q=cyber+security+dasar+indonesia` | Ancaman dan cara melindungi diri di internet |
| Simulasi | Cisco Packet Tracer | `https://www.netacad.com/` | Simulator jaringan dari Cisco Academy gratis |
| Website | BNPT — Belajar Keamanan Digital | `https://www.bnpt.go.id/` | Edukasi keamanan siber dari pemerintah |
