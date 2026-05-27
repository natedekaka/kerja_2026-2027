# 🌐 Bab 4: Jaringan Komputer dan Internet

> **Semester Genap** | **Fase F** | **Kelas XI** | **25 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Jaringan Komputer dan Internet (JKI) | Memahami arsitektur jaringan, model OSI, dan menerapkan prinsip keamanan siber dalam tata kelola akses data |

---

## 🎯 Tujuan Pembelajaran

- **A.** Pengantar Jaringan & Topologi
- **B.** OSI Layer & Mekanisme Pertukaran Data
- **C.** Cyber Security: Ancaman & Mitigasi
- **D.** Tata Kelola Akses Data
- **E.** Praktik Packet Tracer

## 🗺️ Peta Konsep

```
               🌐 JARINGAN KOMPUTER DAN INTERNET
                     |
                     ├── A. Pengantar Jaringan & Topologi
                     ├── B. OSI Layer & Mekanisme Pertukaran Data
                     ├── C. Cyber Security: Ancaman & Mitigasi
                     ├── D. Tata Kelola Akses Data
                     └── E. Praktik Packet Tracer
```

## A. Pengantar Jaringan & Topologi

### 🌐 Pengantar Jaringan & Topologi
Jaringan komputer adalah **dua atau lebih komputer yang terhubung** untuk berbagi data dan sumber daya.

> 🧩 **Analogi:** Jaringan komputer itu seperti **sistem jalan**. Ada jalan kampung (LAN), jalan provinsi (MAN), dan jalan tol antar pulau (WAN). Semakin lebar jalannya, semakin banyak data yang bisa lewat!

### Jenis Jaringan
| Jenis | Luas | Contoh | Seperti... |
|-------|------|--------|------------|
| **LAN** | 1 ruangan - 1 gedung | Lab komputer sekolah | Jalan di komplek perumahan |
| **MAN** | 1 kota | Koneksi antar cabang bank | Jalan provinsi |
| **WAN** | Antar kota/negara | Internet | Jalan tol lintas pulau |

### Topologi Jaringan
```
STAR:        RING:         BUS:          MESH:
  ⭐           ⭕           🚌             🔀
  PC─Switch   PC─PC        PC PC PC       PC═PC
  │  │  │     │   │        │  │  │       ║║║║
  PC PC PC    PC─PC        ═══KABEL═══    PC═PC
✅ Paling    ✅ Satu arah  ✅ Hemat      ✅ Paling andal
❌ Butuh hub ❌ 1 mati= ❌ Kabel putus ❌ Boros kabel
              semua mati   =semua mati
```

### Perangkat Jaringan
| Perangkat | Fungsi | 
|-----------|--------|
| **Router** | Menghubungkan jaringan berbeda (LAN → Internet) |
| **Switch** | Menghubungkan komputer dalam satu LAN |
| **Access Point** | Memancarkan sinyal WiFi |
| **Modem** | Mengubah sinyal ISP jadi data digital |

> 💡 **Topologi Star** adalah yang paling umum karena jika satu kabel putus, komputer lain tidak terganggu.

### 🔍 Cek Pemahaman
1. Jelaskan perbedaan antara LAN, MAN, dan WAN! Berikan contoh masing-masing!
2. Gambarkan topologi Star dan Ring! Apa kelebihan dan kekurangan masing-masing?
3. Apa fungsi Router, Switch, dan Access Point dalam sebuah jaringan?

### 📋 Studi Kasus
SMA Harapan Bangsa sedang membangun **laboratorium komputer baru** dengan 30 PC. Semua PC harus terhubung ke internet dan bisa saling berbagi data. Kepala sekolah meminta usulan desain jaringan yang efisien dan mudah dikelola.

**Analisis:**
1. Topologi apa yang paling tepat untuk laboratorium tersebut? Jelaskan kelebihan dan kekurangannya!
2. Perangkat jaringan apa saja yang dibutuhkan? Gambarkan skema jaringan sederhananya!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. OSI Layer & Mekanisme Pertukaran Data

### 📦 OSI Layer & Mekanisme Pertukaran Data

### OSI 7 Layer
OSI (Open Systems Interconnection) adalah **model referensi** yang menjelaskan bagaimana data berpindah dari satu komputer ke komputer lain.

> 🧩 **Analogi:** OSI Layer itu seperti **proses pengiriman paket**. Kamu beli kue online, kue dibungkus (Presentation), dikasih label alamat (Session), diantar kurir (Transport), lewat jalan tertentu (Network), dikirim bit per bit (Data Link), jadi sinyal listrik (Physical).

```
┌──────┬─────────────────────────────────────────────┐
│Layer │ Fungsi                    │ Contoh Protocol │
├──────┼───────────────────────────┼─────────────────┤
│ 7    │ APPLICATION — Antarmuka   │ HTTP, FTP, DNS  │
│      │ user dengan jaringan      │                 │
│ 6    │ PRESENTATION — Enkripsi,  │ SSL/TLS, JPEG   │
│      │ kompresi, format data     │                 │
│ 5    │ SESSION — Mengelola sesi  │ NetBIOS, RPC    │
│      │ koneksi                   │                 │
│ 4    │ TRANSPORT — Pengiriman    │ TCP, UDP        │
│      │ data andal (TCP) / cepat  │                 │
│ 3    │ NETWORK — Routing, alamat │ IP, ICMP        │
│      │ IP                        │                 │
│ 2    │ DATA LINK — Framing,      │ Ethernet, MAC   │
│      │ deteksi error             │                 │
│ 1    │ PHYSICAL — Sinyal listrik │ Kabel, WiFi     │
│      │ / radio, bit              │                 │
└──────┴───────────────────────────┴─────────────────┘
```

### Enkapsulasi Data
Setiap layer **membungkus** data dari layer di atasnya dengan header-nya sendiri.

```
[Data Asli] → Layer 7-6-5
↓
[TCP header | Data] → Layer 4 (Transport)
↓
[IP header | TCP header | Data] → Layer 3 (Network)
↓
[MAC header | IP | TCP | Data | Trailer] → Layer 2 (Data Link)
↓
[10101010010101010101010] → Layer 1 (Physical)
```

> 🔑 **Mnemonic:** **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing (Application → Physical)

### 🔍 Cek Pemahaman
1. Sebutkan 7 layer OSI dari atas ke bawah beserta fungsi masing-masing!
2. Apa yang dimaksud dengan enkapsulasi data dalam konteks OSI Layer?
3. Pada layer berapa protokol HTTP dan TCP bekerja? Jelaskan perbedaan fungsi keduanya!

### 📋 Studi Kasus
Ketika kamu mengirim foto selfie ke teman melalui **Instagram**, data foto tersebut melewati proses enkapsulasi berlapis sebelum sampai ke temanmu. Mulai dari data foto asli hingga menjadi sinyal listrik yang dikirim melalui kabel atau WiFi.

**Analisis:**
1. Jelaskan bagaimana data foto selfie tersebut dibungkus (enkapsulasi) di setiap layer OSI! Mulai dari Application hingga Physical layer!
2. Jika koneksi internet temanmu lambat, layer apa yang paling mungkin terpengaruh? Mengapa?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Cyber Security: Ancaman & Mitigasi

### 🔒 Cyber Security: Ancaman & Mitigasi
Cyber Security adalah praktik melindungi sistem, jaringan, dan data dari serangan digital.

> 🧩 **Analogi:** Cyber security itu seperti **sistem keamanan rumah**. Ada pagar (firewall), CCTV (monitoring), kunci ganda (MFA), satpam (antivirus), dan asuransi (backup). Semakin banyak lapisan, semakin aman!

### Jenis Ancaman
| Ancaman | Deskripsi | Contoh |
|---------|-----------|--------|
| **Malware** | Software berbahaya | Virus, ransomware WannaCry |
| **Phishing** | Pemancing data pribadi | Email palsu dari "bank" |
| **DDoS** | Banjir traffic ke server | Website down total |
| **Man-in-the-Middle** | Menyadap komunikasi | WiFi palsu di kafe |
| **SQL Injection** | Inject kode ke database | Bocor data pengguna |
| **Social Engineering** | Manipulasi psikologis | "Saya dari IT, minta password" |

### Mitigasi: Cara Melindungi Diri
```
🔐  Gunakan password berbeda untuk setiap akun
🔑  Aktifkan 2FA (Two Factor Authentication)
🔄  Update software & antivirus secara rutin
📁  Backup data penting ke cloud + hard drive
🔗  Jangan klik link sembarangan
📧  Verifikasi pengirim email
🛡️  Gunakan VPN di WiFi publik
```

### Password Manager
Gunakan **password manager** (Bitwarden, 1Password, Google Password Manager) untuk menyimpan semua password — kamu cukup ingat 1 password utama.

> 🔑 **Aturan Password:** Minimal 12 karakter, kombinasi huruf besar-kecil-angka-simbol. Contoh: `S4y4!ncL4s$XI_2026`

### 🔍 Cek Pemahaman
1. Sebutkan 3 jenis ancaman cyber dan jelaskan cara kerjanya!
2. Apa itu phishing? Bagaimana cara mengenali email phishing?
3. Sebutkan minimal 4 cara untuk melindungi data pribadi dari serangan cyber!

### 📋 Studi Kasus
Rudi menerima SMS yang mengaku dari "Bank Central" yang menyatakan: "Akun Anda akan diblokir! Klik link berikut untuk verifikasi: bit.ly/bank-central-verif. Abaikan = akun diblokir 24 jam!" Rudi panik karena ia memang punya rekening di bank tersebut. Ia hampir mengklik link itu sebelum bertanya pada gurunya.

**Analisis:**
1. Jenis serangan cyber apa yang dialami Rudi? Jelaskan ciri-cirinya!
2. Apa yang seharusnya dilakukan Rudi? Buat langkah-langkah yang benar!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Tata Kelola Akses Data

### 🛡️ Tata Kelola Akses Data
Tata kelola akses data mengatur **siapa boleh mengakses apa** dalam sebuah sistem.

> 🧩 **Analogi:** Akses data itu seperti **tingkatan di game**. Player biasa cuma bisa main di level 1-5. Admin bisa akses semua level. Game master bisa ubah aturan game. Setiap peran punya **wewenang berbeda**.

### Model Kontrol Akses
```
┌────────────────────────────────────────────────────┐
│  MAC (Mandatory) — Label keamanan (Top Secret,     │
│                    Confidential, Public)           │
│  DAC (Discretionary) — Pemilik data atur akses    │
│  RBAC (Role-Based) — Akses berdasar peran          │
│                    (Siswa, Guru, Admin)            │
│  ABAC (Attribute-Based) — Akses berdasar atribut   │
│                    (Jam kerja, lokasi, device)     │
└────────────────────────────────────────────────────┘
```

### Implementasi
| Peran | Akses ke Data Nilai | Akses ke Data Pribadi | Akses ke Konfigurasi |
|-------|--------------------|----------------------|---------------------|
| **Siswa** | Lihat nilai sendiri | ✗ | ✗ |
| **Guru** | Input & edit nilai | ✗ | ✗ |
| **Wali Kelas** | Lihat semua nilai kelas | Lihat data pribadi | ✗ |
| **Admin IT** | ✗ | ✗ | Kelola server & akun |
| **Kepala Sekolah** | Lihat laporan | Lihat laporan | ✗ |

### Prinsip Keamanan
- **Least Privilege:** Beri akses seminimal mungkin
- **Need to Know:** Akses hanya pada yang perlu diketahui
- **Separation of Duties:** Tugas penting dipegang > 1 orang
- **Audit Trail:** Catat semua aktivitas akses

### 🔍 Cek Pemahaman
1. Jelaskan perbedaan antara model akses RBAC dan MAC!
2. Apa yang dimaksud dengan prinsip Least Privilege? Berikan contohnya!
3. Mengapa prinsip Separation of Duties penting dalam keamanan data?

### 📋 Studi Kasus
SMA Nusantara menggunakan **sistem informasi sekolah** yang memiliki data nilai, data pribadi siswa, data keuangan, dan konfigurasi server. Pengguna sistem meliputi: siswa, guru, wali kelas, admin TU, kepala sekolah, dan admin IT. Saat ini, semua pengguna bisa mengakses hampir semua data — dan baru-baru ini terjadi kebocoran data nilai.

**Analisis:**
1. Rancang tabel akses (siapa boleh mengakses apa) menggunakan model RBAC untuk sistem tersebut!
2. Kebocoran data nilai terjadi karena seorang siswa bisa mengakses database. Prinsip apa yang dilanggar? Bagaimana seharusnya?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## E. Praktik Packet Tracer

### 🖥️ Praktik Packet Tracer
**Cisco Packet Tracer** adalah software simulasi jaringan yang memungkinkan kamu merancang, mengkonfigurasi, dan menguji jaringan tanpa alat fisik.

> 🧩 **Analogi:** Packet Tracer itu seperti **game simulasi kota (SimCity)** tapi untuk jaringan komputer. Kamu bisa bangun jaringan, sambungkan perangkat, atur konfigurasi — tanpa harus beli router beneran!

### Aktivitas: Konfigurasi Jaringan Dasar
```
┌──────────┐        ┌──────────┐        ┌──────────┐
│   PC 0   │───────►│  Switch  │◄───────│   PC 1   │
│ 192.168. │        │          │        │ 192.168. │
│  1.1     │        └────┬─────┘        │  1.2     │
└──────────┘             │              └──────────┘
                        │
                 ┌──────┴──────┐
                 │   Router    │───► Internet
                 │ 192.168.1.1 │
                 └─────────────┘
```

### Langkah-Langkah
1. **Buka Packet Tracer** → Tambahkan 2 PC, 1 Switch, 1 Router
2. **Sambungkan** dengan kabel Copper Straight-Through
3. **Konfigurasi IP:**
   - PC0: 192.168.1.2/24, Gateway: 192.168.1.1
   - PC1: 192.168.1.3/24, Gateway: 192.168.1.1
   - Router: 192.168.1.1/24
4. **Uji koneksi** → Buka Command Prompt di PC0 → `ping 192.168.1.3`

### Perintah Dasar
| Perintah | Fungsi |
|----------|--------|
| `ping [IP]` | Tes koneksi ke IP tujuan |
| `ipconfig` | Lihat konfigurasi IP sendiri |
| `tracert [IP]` | Lacak jalur yang dilewati paket |
| `show ip route` (Router) | Lihat tabel routing |

> 💡 **Tips:** Kalau ping gagal, cek: kabel terhubung?, IP sudah benar? firewall mati?

### 🔍 Cek Pemahaman
1. Apa fungsi Cisco Packet Tracer dalam pembelajaran jaringan?
2. Sebutkan langkah-langkah untuk mengkonfigurasi 2 PC agar bisa saling ping!
3. Apa artinya jika perintah `ping` berhasil? Apa yang terjadi jika gagal?

### 📋 Studi Kasus
Sekolah kamu memiliki **2 gedung** yang berjarak 200 meter. Gedung A (lab komputer) dan Gedung B (perpustakaan). Kamu diminta merancang jaringan yang menghubungkan kedua gedung agar siswa di perpustakaan bisa mengakses internet dari server di lab komputer. Tersedia 2 router, 2 switch, dan kabel secukupnya.

**Analisis:**
1. Gambarkan desain jaringan di Packet Tracer untuk menghubungkan kedua gedung!
2. Konfigurasi IP apa yang akan kamu berikan untuk PC di Gedung A dan Gedung B? Bagaimana cara memastikan koneksi berhasil?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: 🌐 Desain + Simulasi Jaringan

Rancang jaringan komputer untuk 2 laboratorium sekolah menggunakan Cisco Packet Tracer. Konfigurasi IP, routing dasar, dan uji konektivitas antar perangkat dalam jaringan.

**Alat dan Bahan:**
- Cisco Packet Tracer (install di lab atau download)
- Laptop/komputer
- Buku catatan untuk sketsa desain

**Langkah-langkah:**
1. Buat sketsa desain jaringan di kertas: 2 lab (@10 PC), 1 server, 2 switch, 1 router, koneksi internet.
2. Buka Cisco Packet Tracer dan tambahkan semua perangkat sesuai sketsa.
3. Sambungkan perangkat dengan kabel Copper Straight-Through yang sesuai.
4. Konfigurasi IP address: Lab A (192.168.1.0/24), Lab B (192.168.2.0/24), Router sebagai gateway.
5. Konfigurasi routing statis di router agar kedua lab bisa saling terhubung.
6. Uji koneksi dengan perintah `ping` antar PC di lab yang berbeda — dokumentasikan hasilnya.

> **Output:** File Packet Tracer (.pkt) + laporan konfigurasi + screenshot hasil ping

## 📝 Rangkuman

- Jaringan komputer dibagi menjadi **LAN** (lokal), **MAN** (kota), dan **WAN** (luas). Topologi yang paling umum adalah **Star** karena jika satu kabel putus yang lain tidak terganggu.
- **OSI Model** memiliki 7 layer: Physical, Data Link, Network, Transport, Session, Presentation, Application. Setiap layer membungkus data dengan header-nya (enkapsulasi).
- **Cyber Security** melindungi sistem dari ancaman seperti Malware, Phishing, DDoS, Man-in-the-Middle, SQL Injection, dan Social Engineering dengan mitigasi seperti 2FA dan password manager.
- **Tata kelola akses data** menggunakan model RBAC (Role-Based Access Control) dengan prinsip Least Privilege — beri akses seminimal mungkin sesuai peran.
- **Cisco Packet Tracer** adalah simulator jaringan yang memungkinkan praktik konfigurasi tanpa alat fisik. Perintah dasar: ping, ipconfig, tracert.

---
## ✍️ Latihan Soal

### Pilihan Ganda

1. Topologi jaringan yang paling umum digunakan pada jaringan sekolah saat ini adalah...
   a. Bus
   b. Ring
   c. Star
   d. Mesh
   e. Tree
   **Kunci Jawaban: C**

2. Layer OSI yang bertanggung jawab untuk routing dan pengalamatan IP adalah...
   a. Physical Layer
   b. Data Link Layer
   c. Network Layer
   d. Transport Layer
   e. Application Layer
   **Kunci Jawaban: C**

3. Serangan cyber berupa pemancingan data pribadi melalui email palsu disebut...
   a. Malware
   b. Phishing
   c. DDoS
   d. SQL Injection
   e. Social Engineering
   **Kunci Jawaban: B**

4. Prinsip keamanan yang menyatakan 'beri akses seminimal mungkin' disebut...
   a. Need to Know
   b. Separation of Duties
   c. Audit Trail
   d. Least Privilege
   e. Zero Trust
   **Kunci Jawaban: D**

5. Perintah Cisco untuk menguji koneksi ke IP tujuan adalah...
   a. ipconfig
   b. tracert
   c. ping
   d. show ip route
   e. netstat
   **Kunci Jawaban: C**

### Uraian

1. Jelaskan perbedaan antara LAN, MAN, dan WAN! Berikan contoh masing-masing dalam konteks kehidupan sehari-hari!

2. Gambarkan dan jelaskan fungsi dari 7 layer OSI Model! Gunakan mnemonik untuk memudahkan mengingat urutan layer!

3. Apa saja jenis ancaman cyber security yang perlu diwaspadai? Jelaskan cara mitigasi untuk melindungi data pribadi dari serangan tersebut!

4. Jelaskan prinsip Least Privilege dan Need to Know dalam tata kelola akses data! Berikan contoh penerapannya di lingkungan sekolah!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Desain Topologi | Topologi tidak sesuai, perangkat kurang | Topologi sesuai, perangkat lengkap | Topologi optimal, efisien, dan rapi |
| Konfigurasi IP | IP tidak sesuai, tidak ada pemetaan | IP benar untuk satu lab | IP benar untuk kedua lab, routing berfungsi |
| Fungsionalitas Jaringan | Tidak ada koneksi antar perangkat | Koneksi berhasil dalam satu lab | Semua perangkat terhubung, ping berhasil antar lab |
| Dokumentasi | Tidak ada dokumentasi | Dokumentasi ada tapi kurang detail | Dokumentasi lengkap dengan screenshot |

---
## 🚀 Tugas Pengayaan

### 🌐 Kursus Jaringan di Cisco NetAcad
Daftar dan mulai modul *Introduction to Networks* di [Cisco Networking Academy](https://www.netacad.com/) (gratis). Selesaikan modul 1-3 dan catat: 3 konsep baru yang kamu pelajari, 1 hal yang paling menarik, dan 1 pertanyaan yang masih mengganjal.

### 🔐 Tantangan Cyber Security
Pelajari dasar-dasar cyber security melalui [Cisco CyberOps Associate](https://www.netacad.com/) atau artikel di [NCSC Indonesia](https://www.bssn.go.id/). Buat poster infografis tip keamanan digital untuk remaja — minimal 5 tips dengan ilustrasi menarik.

---
## 📖 Glosarium

- **LAN**: Local Area Network — jaringan komputer dalam area terbatas seperti satu ruangan atau gedung.
- **MAN**: Metropolitan Area Network — jaringan komputer yang mencakup satu kota.
- **WAN**: Wide Area Network — jaringan komputer yang mencakup area luas antar kota atau negara.
- **OSI Model**: Model referensi 7 layer yang menjelaskan proses pertukaran data dalam jaringan komputer.
- **Enkapsulasi**: Proses pembungkusan data dengan header di setiap layer OSI sebelum dikirim melalui jaringan.
- **Phishing**: Serangan cyber berupa pemancingan data pribadi melalui email atau pesan palsu.
- **Malware**: Perangkat lunak berbahaya yang dirancang untuk merusak sistem atau mencuri data.
- **Least Privilege**: Prinsip keamanan yang memberikan akses seminimal mungkin kepada pengguna.
- **RBAC**: Role-Based Access Control — model kontrol akses berdasarkan peran pengguna dalam organisasi.
- **Cisco Packet Tracer**: Software simulasi jaringan untuk merancang dan mengkonfigurasi jaringan tanpa alat fisik.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Apa itu Jaringan Komputer? | `youtu.be/search?q=apa+itu+jaringan+komputer` | Penjelasan dasar jaringan komputer |
| Simulasi | Cisco Packet Tracer — Tutorial | `youtu.be/search?q=packet+tracer+tutorial+indonesia` | Panduan praktik Packet Tracer |
| YouTube | OSI Layer Dijelaskan | `youtu.be/search?q=OSI+layer+indonesia` | Penjelasan 7 layer OSI dengan analogi |
| Website | Cyber Security untuk Remaja | `youtu.be/search?q=cyber+security+dasar` | Tips keamanan digital untuk pelajar |
| Website | Cisco Networking Academy | `https://www.netacad.com/` | Kursus jaringan gratis dari Cisco |
