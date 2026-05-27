# 🌐 Bab 5: Jaringan Komputer dan Internet

> **Semester Genap** | **Fase E** | **Kelas X** | **15 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Jaringan Komputer dan Internet | Memahami jenis-jenis jaringan, cara kerja internet, dan keamanan dasar di dunia maya. |

---

## 🎯 Tujuan Pembelajaran

- **A.** Dasar-Dasar Jaringan Komputer
- **B.** Internet dan Cara Kerjanya
- **C.** Keamanan Dasar di Dunia Maya

## 🗺️ Peta Konsep

```
               🌐 JARINGAN KOMPUTER DAN INTERNET
                     |
                     ├── A. Dasar-Dasar Jaringan Komputer
                     ├── B. Internet dan Cara Kerjanya
                     └── C. Keamanan Dasar di Dunia Maya
```

## A. Dasar-Dasar Jaringan Komputer

### 🌐 Dasar-Dasar Jaringan Komputer

Jaringan komputer adalah **dua atau lebih komputer yang saling terhubung** untuk berbagi data dan sumber daya.

> 🧩 **Analogi:** Jaringan komputer itu seperti **sistem pos**. Setiap komputer adalah sebuah rumah. Alamat rumah adalah IP Address. Tukang pos yang mengantarkan surat adalah data packet. Dan jalan yang menghubungkan rumah-rumah adalah kabel atau sinyal WiFi. **Internet adalah sistem pos seluruh dunia!**

### Manfaat Jaringan

1. 📂 **Berbagi file** — Kirim data tanpa flashdisk
2. 🖨️ **Berbagi printer** — Satu printer untuk banyak komputer
3. 🌍 **Akses internet** — Terhubung ke seluruh dunia
4. 💬 **Komunikasi** — Email, chat, video call
5. ☁️ **Penyimpanan cloud** — Data bisa diakses di mana saja

### Jenis Jaringan Berdasarkan Luas

| Jenis | Luas | Contoh | Ilustrasi |
|-------|------|--------|-----------|
| **PAN** (Personal) | 1-10 m | Bluetooth HP ke speaker | Satu kamar |
| **LAN** (Local) | 10-1000 m | Lab komputer sekolah | Satu perumahan |
| **MAN** (Metropolitan) | 10-50 km | WiFi seluruh kota | Satu kecamatan |
| **WAN** (Wide) | >100 km | Internet global | Seluruh dunia |

### Topologi Jaringan

```
Topologi Bus:                Topologi Star:
    ┌──┐  ┌──┐  ┌──┐          ┌──┐
    │PC│  │PC│  │PC│          │PC│
    └┬─┘  └┬─┘  └┬─┘          └┬─┘
     └─────┴──────┘            │
══════════════════════     ┌────┴────┐
                          │ SWITCH  │
Topologi Ring:             ├─────────┤
  ┌──┐                    │ ─── ─── │
┌─│PC│                    │ PC  PC  │
│ └──┘                    └─────────┘
│  │
└──┴──┐
   ┌──┐
   │PC│
   └──┘
```

### 📌 Contoh Nyata

Di lab komputer sekolahmu, biasanya menggunakan **topologi Star**: setiap komputer terhubung ke satu **switch**, dan switch terhubung ke **router** yang menyediakan internet. Jika satu komputer mati, yang lain tidak terpengaruh.

### 🔍 Cek Pemahaman
1. Sebutkan 4 jenis jaringan berdasarkan luas area beserta cakupannya!
2. Apa perbedaan antara topologi Bus, Star, dan Ring?
3. Sebutkan 3 manfaat jaringan komputer di lingkungan sekolah!

### 📋 Studi Kasus
Di lab komputer sekolah terdapat 20 komputer yang semuanya mati saat satu komputer dimatikan. Ternyata masalahnya ada di kabel utama yang putus.

**Pertanyaan:**
1. Topologi jaringan apa yang paling mungkin digunakan berdasarkan gejala tersebut?
2. Topologi apa yang lebih baik untuk lab komputer? Mengapa?

> 🤔 **Refleksi:** Coba lihat sekeliling ruang kelas/lab komputer. Bagaimana kira-kira topologi jaringannya?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Internet dan Cara Kerjanya

### 🌍 Internet dan Cara Kerjanya

Internet adalah **jaringan global** yang menghubungkan miliaran perangkat di seluruh dunia. Internet memungkinkan kita **mengakses informasi**, **berkomunikasi**, dan **bertransaksi** tanpa batas geografis.

> 🧩 **Analogi:** Internet itu seperti **jalan tol global**. Setiap situs web adalah **kota**. Google adalah **papan petunjuk** yang memberitahu lokasi kota. Data yang bepergian adalah **mobil-mobil** yang melaju di jalan tol. Protokol TCP/IP adalah **aturan lalu lintas** yang memastikan semua mobil sampai dengan selamat.

### Bagaimana Internet Bekerja?

```
  Kamu ketik: www.google.com
       │
       ▼
  [DNS Server]  ── "Google? IP-nya 142.250.64.78"
       │
       ▼
  [Router ISP]  ── Menemukan rute tercepat
       │
       ▼
  [Router Global] ── Melompat dari router ke router
       │
       ▼
  [Server Google] ── "Halaman HTML siap dikirim!"
       │
       ▼
  Browser menampilkan Google.com ✅
```

### Komponen Internet

| Komponen | Fungsi | Analogi |
|----------|--------|---------|
| **Server** | Komputer yang menyimpan website/data | Toko penyedia barang |
| **Client** | Perangkat kita (HP/laptop) | Pembeli |
| **ISP** | Penyedia layanan internet | Jalan tol & gerbang |
| **Router** | Mengarahkan data ke tujuan | Simpang jalan & rambu |
| **DNS** | Menerjemahkan nama jadi IP | Buku telepon raksasa |
| **Domain** | Alamat website (google.com) | Nama toko |
| **IP Address** | Alamat unik perangkat | Koordinat GPS |

### TCP/IP: Aturan Lalu Lintas Internet

```
   ┌──────────┐     ┌──────────┐     ┌──────────┐
   │   DATA   │────►│ DI-PECAH │────►│ DIBERI   │
   │ (File)   │     │ (Packet) │     │ ALAMAT   │
   └──────────┘     └──────────┘     └────┬─────┘
                                           │
                                           ▼
   ┌──────────┐     ┌──────────┐     ┌──────────┐
   │ DITAMPILKAN│◄───│ DI-RAKIT │◄────│ DIKIRIM  │
   │ (Hasil)   │     │ (Packet) │     │ (Route)  │
   └──────────┘     └──────────┘     └──────────┘
```

### 📌 Contoh Nyata

Saat kamu nonton YouTube, **data video tidak dikirim utuh**. Video dipecah menjadi ribuan packet kecil, masing-masing mencari rute tercepat ke HP-mu. Kadang ada packet yang datang terlambat atau hilang — itulah yang menyebabkan video **buffering**! YouTube akan meminta ulang packet yang hilang.

### 🔍 Cek Pemahaman
1. Jelaskan peran DNS, Router, dan ISP dalam proses mengakses website!
2. Apa yang dimaksud dengan TCP/IP dan bagaimana cara kerjanya?
3. Apa yang menyebabkan video buffering saat menonton YouTube?

### 📋 Studi Kasus
Budi sedang mengerjakan ujian online di rumah menggunakan Zoom. Tiba-tiba koneksi internetnya sangat lambat. la melihat ada 5 perangkat yang terhubung ke WiFi rumah: HP ayah, HP ibu, laptop kakak, TV pintar, dan PlayStation.

**Pertanyaan:**
1. Faktor apa saja yang menyebabkan koneksi Budi lambat?
2. Apa saranmu agar koneksi Budi stabil saat ujian?

> 🤔 **Refleksi:** Pernah mengalami internet lambat saat Zoom atau main game? Kira-kira apa penyebabnya? Diskusikan dengan teman!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Keamanan Dasar di Dunia Maya

### 🔒 Keamanan Dasar di Dunia Maya

Dunia maya (cyberspace) tidak selalu aman. Sama seperti di dunia nyata ada penjahat, di internet juga ada **ancaman digital** yang perlu kamu waspadai.

> 🧩 **Analogi:** Keamanan internet itu seperti **mengunci rumah**. Kamu tidak akan meninggalkan rumah dalam keadaan pintu terbuka lebar, kan? Di internet, password adalah kuncinya, antivirus adalah satpamnya, dan dirimu sendiri adalah pemilik rumah yang harus waspada!

### Ancaman Digital yang Umum

| Ancaman | Penjelasan | Analogi |
|---------|-----------|---------|
| **Malware** | Virus, trojan, ransomware yang merusak sistem | Pencuri yang masuk rumah |
| **Phishing** | Pancingan untuk mencuri data pribadi | Orang mengaku bank, padahal penipu |
| **Cyberbullying** | Perundungan di dunia digital | Perundungan di sekolah — tapi online |
| **Hoaks** | Berita bohong | Gosip yang sengaja dibuat |
| **Doxing** | Menyebarkan data pribadi orang | Memajang KTP orang di publik |
| **Hacking** | Membobol akun orang | Mendobrak pintu rumah orang |

### Tips Aman di Internet 🛡️

```
  🔑  Password KUAT & BERBEDA untuk tiap akun!
      ❌ password123, nama, tanggal lahir
      ✅ G4nT3ng!2026_KlsX (min 8 karakter, campur huruf besar/kecil/angka/simbol)

  🔐  Aktifkan 2FA (Otentikasi 2 Faktor)
      Password + kode via SMS/Google Authenticator

  ❓  Jangan Klik Link Sembarangan!
      Cek URL sebelum klik — "g00gle.com" ≠ "google.com"

  📱  Jaga Data Pribadi
      Jangan sembarangan posting: alamat rumah, nomor HP, KTP

  🛑  STOP — THINK — CONNECT
      Berhenti, pikir dulu, baru terhubung!
```

### Cara Membuat Password Kuat

| ❌ Lemah | ⚠️ Sedang | ✅ Kuat |
|----------|-----------|---------|
| `123456` | `kelas10` | `K1@$X_2026!` |
| `password` | `sekolahku` | `B4ndung#Smkn6` |
| `admin` | `jokowi` | `L!ndungi_AkunMu` |

### 📌 Contoh Nyata

**Kasus:** Seorang siswa mendapat email yang mengatakan "Akun Google-mu akan dihapus! Klik link ini untuk menyelamatkan akun." Link-nya mirip google.com tapi sebenarnya **g00gle.com** (angka 0). Dia panik dan mengklik, lalu mengisi email dan password — **AKUN-NYA DICURI!**

Ini adalah **phishing**. Selalu cek URL dengan saksama dan jangan panik!

### 🔍 Cek Pemahaman
1. Sebutkan 3 jenis ancaman digital beserta penjelasan singkatnya!
2. Apa itu phishing? Berikan contoh cara kerjanya!
3. Sebutkan 3 karakteristik password yang kuat!

### 📋 Studi Kasus
Sinta menerima pesan di WhatsApp dari nomor tidak dikenal yang mengaku sebagai operator sekolah. Pesan itu berisi link untuk mengisi data penerima bantuan siswa miskin dan meminta nomor rekening serta password akun sekolah.

**Pertanyaan:**
1. Termasuk ancaman apakah pesan yang diterima Sinta? Jelaskan!
2. Apa yang harus dilakukan Sinta? Tuliskan langkah-langkahnya!

> 🤔 **Refleksi:** Apakah kamu pakai password yang sama untuk semua akun? Kalau iya, apa risikonya? Diskusikan dengan temanmu!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: Desain Jaringan Sekolah 🏫

Buat desain topologi jaringan yang ideal untuk lingkungan sekolah. Gambar menunjukkan bagaimana komputer di lab, laptop guru, server sekolah, dan koneksi internet terhubung.

**Alat dan Bahan:**
- Canva / draw.io / Cisco Packet Tracer / Kertas gambar
- Spidol warna / alat desain

**Langkah-langkah:**
1. Identifikasi perangkat yang perlu terhubung: lab komputer (20 PC), laptop guru (10), server sekolah, WiFi untuk siswa, printer jaringan
2. Pilih topologi yang sesuai (Star direkomendasikan untuk sekolah)
3. Gambar tata letak jaringan: router → switch → komputer/laptop/AP WiFi
4. Beri label: alamat IP sederhana (192.168.1.x) dan nama perangkat
5. Tambahkan legenda: router, switch, access point, kabel, server
6. Jelaskan kelebihan topologi yang kamu pilih untuk sekolah

> **Output:** Diagram jaringan (.pdf/.jpg) + paragraf penjelasan topologi

---

## 📝 Rangkuman

- Jaringan komputer memungkinkan berbagi data dan sumber daya. Berdasarkan luas: PAN, LAN, MAN, dan WAN.
- Internet bekerja melalui DNS, router ISP, dan server global — data dipecah menjadi packet, dikirim, lalu dirakit kembali.
- Ancaman digital meliputi malware, phishing, cyberbullying, hoaks, dan hacking. Lindungi diri dengan password kuat, 2FA, dan jangan klik link sembarangan.

---

## ✍️ Latihan Soal

### A. Pilihan Ganda

1. Jaringan komputer yang mencakup area satu kota disebut...
   a. PAN
   b. LAN
   c. MAN
   d. WAN
   e. CAN
   **Kunci Jawaban: C**

2. Perangkat yang mengarahkan data ke tujuan yang benar di internet adalah...
   a. Switch
   b. Hub
   c. Router
   d. Modem
   e. Repeater
   **Kunci Jawaban: C**

3. Kepanjangan dari DNS adalah...
   a. Domain Name System
   b. Digital Network Service
   c. Data Network Security
   d. Domain Network Server
   e. Digital Name System
   **Kunci Jawaban: A**

4. Tindakan penipuan dengan mengirim link palsu untuk mencuri data pribadi disebut...
   a. Hacking
   b. Cracking
   c. Phishing
   d. Spamming
   e. Doxing
   **Kunci Jawaban: C**

5. Password yang PALING kuat di bawah ini adalah...
   a. 123456
   b. password
   c. K1@$X_2026!
   d. admin
   e. kelas10
   **Kunci Jawaban: C**

### B. Uraian

1. Jelaskan perbedaan antara jaringan PAN, LAN, MAN, dan WAN! Berikan contoh masing-masing!

2. Jelaskan bagaimana cara kerja internet saat kamu mengetik www.google.com di browser hingga halaman muncul!

3. Apa yang dimaksud dengan phishing? Jelaskan cara kerja dan 3 cara menghindarinya!

4. Sebutkan 5 tips menjaga keamanan saat berselancar di internet yang wajib diketahui pelajar!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Topologi & Kesesuaian | Topologi tidak sesuai untuk sekolah | Topologi cukup sesuai | Topologi sangat sesuai untuk sekolah |
| Kelengkapan Perangkat | Perangkat tidak lengkap | Sebagian perangkat tercantum | Semua perangkat lengkap dengan IP |
| Visual & Label | Tidak rapi, sulit dipahami | Cukup rapi, ada label | Rapi, jelas, legenda lengkap |
| Analisis & Justifikasi | Tidak ada penjelasan | Penjelasan ada tapi kurang mendalam | Penjelasan kelebihan topologi mendalam |

---

## 🚀 Tugas Pengayaan

### Eksplorasi Keamanan
Cek keamanan password kamu di https://haveibeenpwned.com/. Cari tahu apakah email atau akunmu pernah bocor. Tulis laporan: temuan dan langkah yang kamu ambil.

### Simulasi Jaringan
Coba Cisco Packet Tracer (gratis dari https://www.netacad.com/). Buat simulasi 2 PC terhubung ke switch, lalu ke router. Screenshot hasilnya dan jelaskan alur data.

---

## 📖 Glosarium

- **Jaringan Komputer**: Dua atau lebih perangkat yang saling terhubung untuk berbagi data.
- **PAN (Personal Area Network)**: Jaringan pribadi dengan jangkauan sangat pendek (1-10 m).
- **LAN (Local Area Network)**: Jaringan lokal dengan jangkauan satu gedung atau perumahan.
- **Router**: Perangkat yang mengarahkan data ke tujuan yang benar di internet.
- **DNS (Domain Name System)**: Sistem yang menerjemahkan nama domain menjadi IP Address.
- **Phishing**: Upaya penipuan dengan memancing korban memberikan data pribadi melalui link palsu.
- **Firewall**: Sistem keamanan yang menyaring lalu lintas data dan melindungi dari akses tidak sah.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Cara Kerja Internet dalam 5 Menit | `https://youtu.be/...search?q=cara+kerja+internet+animasi` | Penjelasan internet dengan animasi |
| YouTube | Kok Bisa? — WiFi dan Jaringan | `https://youtu.be/...search?q=kok+bisa+wifi+jaringan` | Animasi edukasi tentang cara kerja jaringan nirkabel |
| Simulasi | Cisco Packet Tracer | `https://www.netacad.com/courses/packet-tracer` | Simulator jaringan untuk belajar topologi dan routing |
| Website | Daftar Phishing Terbaru | `https://www.kominfo.go.id/` | Portal Kominfo — info keamanan digital |
| YouTube | Tips Aman Internet — Kemendikbud | `https://youtu.be/...search?q=aman+di+internet+kemdikbud` | Tips keamanan digital dari Kemendikbud |
