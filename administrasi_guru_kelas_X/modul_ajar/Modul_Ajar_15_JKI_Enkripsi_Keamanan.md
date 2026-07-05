# MODUL AJAR INFORMATIKA KELAS X

## JKI: ENKRIPSI & KEAMANAN JARINGAN (TP.4.3)

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | JKI — Jaringan Komputer & Internet |
| Tujuan Pembelajaran | TP.4.3: Menerapkan enkripsi & proteksi data saat online |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 15 |
| Kompetensi Awal | Peserta didik telah memahami konsep konektivitas internet, IP address, DNS, dan DHCP. Peserta didik juga telah menggunakan browser dan aplikasi sehari-hari. |
| Integrasi 8 Dimensi | Keimanan & Bertakwa (menjaga amanah data diri sebagai tanggung jawab moral), Penalaran Kritis (membedakan enkripsi kuat vs lemah), Kemandirian (mengelola keamanan digital sendiri), Kolaborasi (simulasi enkripsi berpasangan) |
| **Integrasi 7 KAIH** | Bermasyarakat, Gemar Belajar |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Prasarana | Komputer/lab, proyektor, browser, koneksi internet, kertas & pensil untuk simulasi Caesar cipher, contoh email phishing (simulasi), Windows Defender Firewall |
| Target Peserta Didik | Reguler (dengan diferensiasi 3 tingkat) |
| Model Pembelajaran | Praktik + Diskusi + Simulasi |
| Metode | Simulasi enkripsi Caesar cipher manual, demo firewall, simulasi phishing, diskusi keamanan digital |
| Sumber Belajar | Buku Informatika Kemendikbud Bab 5, artikel "HTTPS vs HTTP" (Cloudflare), video "How Encryption Works" (Computerphile), situs UU ITE dan UU PDP |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Internet dan jaringan adalah infrastruktur modern — memahami cara kerjanya membuat kita lebih bijak dan aman dalam menggunakan teknologi.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan Pembelajaran

1. Menjelaskan konsep enkripsi dan pentingnya dalam komunikasi digital.
2. Menerapkan Caesar cipher untuk mengenkripsi dan mendekripsi pesan secara manual.
3. Menjelaskan peran firewall dalam melindungi komputer dari akses tidak sah.
4. Mengidentifikasi ciri-ciri serangan phishing dan cara menghindarinya.
5. Menerapkan praktik keamanan digital dalam penggunaan internet sehari-hari.

#### B.2 Indikator Keberhasilan

| Indikator | Kriteria |
|---|---|
| Menjelaskan konsep enkripsi dengan analogi sendiri | Analogi logis dan sesuai konteks |
| Menerapkan Caesar cipher enkripsi & dekripsi dengan benar | Minimal 3 dari 4 soal benar |
| Menunjukkan fungsi firewall di sistem operasi | Menemukan pengaturan firewall dan menjelaskan 1 aturan |
| Mengidentifikasi ciri-ciri phishing dari contoh | Minimal 3 dari 5 ciri teridentifikasi |
| Menyusun 5 tips keamanan digital | 5 tips spesifik dan relevan |

#### B.3 Kata Kunci

Enkripsi, dekripsi, Caesar cipher, ciphertext, plaintext, kunci, HTTPS, SSL/TLS, firewall, phishing, malware, ransomware, 2FA (two-factor authentication), VPN

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 15 menit | 1) Salam dan doa. 2) Cek kehadiran. 3) Orientasi: tunjukkan ikon gembok di browser — "Pernah lihat simbol ini? Tahu artinya?" 4) Apersepsi: tanya apakah siswa pernah membuka situs tanpa "https". 5) Asesmen diagnostik: 3 pertanyaan tentang keamanan online. 6) Menyampaikan TP dan indikator | 1) Menjawab salam dan berdoa. 2) Mengecek ikon gembok di browser masing-masing. 3) Berbagi pengalaman situs tanpa https. 4) Menjawab diagnostik. 5) Mencatat TP | Browser, proyektor, slide |
| **MINING FULL** | **Eksplorasi** — Eksplorasi Konsep** | 15 menit | 1) Menjelaskan enkripsi: mengubah data agar tidak bisa dibaca pihak tak berwenang. Analogi: pesan rahasia masa perang. 2) Menjelaskan HTTPS vs HTTP — peran SSL/TLS. 3) Memperlihatkan sertifikat digital di browser (klik ikon gembok → detail). 4) Menjelaskan enkripsi simetris (satu kunci) vs asimetris (kunci publik & privat) | 1) Menyimak penjelasan. 2) Membuka sertifikat digital di browser. 3) Membaca detail sertifikat. 4) Mencatat perbedaan enkripsi simetris vs asimetris | Browser, proyektor, slide |
| **MINING FULL** | **Eksplorasi** — Praktik Caesar Cipher** | 20 menit | 1) Menjelaskan Caesar cipher: geser setiap huruf sesuai kunci (shift). 2) Contoh: "HELLO" shift 3 → "KHOOR". 3) Memberikan 3 soal enkripsi dan 2 soal dekripsi. 4) Meminta siswa membuat pesan rahasia untuk teman sebangku. 5) Mengecek hasil dan membahas jika ada kesalahan | 1) Menyimak penjelasan. 2) Mengerjakan soal enkripsi. 3) Membuat pesan rahasia. 4) Bertukar dengan teman. 5) Mendekripsi pesan teman | LKPD, kertas, pensil, tabel alfabet |
| **MINING FULL** | **Eksplorasi** — Demo Firewall** | 10 menit | 1) Membuka Windows Defender Firewall (atau yang setara). 2) Menunjukkan daftar aturan inbound & outbound. 3) Mendemonstrasikan memblokir aplikasi tertentu. 4) Menjelaskan kenapa firewall penting untuk keamanan | 1) Mengamati demo. 2) Membuka firewall di komputer sendiri. 3) Mencatat 2 aturan yang ada. 4) Bertanya jika ada yang kurang jelas | Komputer, Windows Firewall, proyektor |
| **MINING FULL** | **Eksplorasi** — Simulasi Phishing** | 15 menit | 1) Menampilkan contoh email phishing di proyektor. 2) Meminta siswa mengidentifikasi ciri-ciri mencurigakan. 3) Membahas setiap ciri: alamat pengirim aneh, URL tipuan, urgensi palsu, lampiran mencurigakan, grammar buruk. 4) Tips: jangan klik link, cek URL, hubungi pengirim via saluran resmi | 1) Mengamati contoh email. 2) Mengidentifikasi ciri phishing. 3) Berdiskusi. 4) Mencatat 5 tips menghindari phishing | Proyektor, screenshot email phishing, LKPD |
| **JOYFULL** | **Penutup Kreatif** | 15 menit | 1) Refleksi: "Bagaimana cara menjaga keamanan data kita saat online?" 2) Brainstorming 10 tips keamanan digital. 3) Penguatan: enkripsi adalah fondasi keamanan digital. 4) Tugas: buka pengaturan privasi 3 aplikasi di HP — catat izin yang diminta. 5) Doa | 1) Refleksi. 2) Menyumbang tips keamanan. 3) Mencatat tugas. 4) Berdoa | Papan tulis, lembar refleksi |

### D. ASESMEN

#### D.1 Asesmen Diagnostik

1. Apa perbedaan HTTP dan HTTPS?
2. Apa yang kalian lakukan jika mendapat email dari bank yang minta password?
3. Menurut kalian, apa itu enkripsi?

#### D.2 Asesmen Formatif

Observasi saat simulasi Caesar cipher dan identifikasi phishing. Guru menilai pemahaman siswa dari kecepatan dan ketepatan mengenkripsi pesan.

#### D.3 Asesmen Sumatif

1. LKPD Caesar cipher (produk individu)
2. Lembar identifikasi phishing (produk individu)
3. Tugas audit izin aplikasi (tugas rumah)

#### D.4 Rubrik Penilaian

| Aspek | SB = 4 (Sangat Baik) | B = 3 (Baik) | C = 2 (Cukup) | PB = 1 (Perlu Bimbingan) |
|---|---|---|---|---|---|
| Caesar cipher | 5 soal benar semua, membuat pesan sendiri untuk teman | 4 soal benar | 3 soal benar | < 3 soal benar |
| Identifikasi phishing | Menemukan 5 ciri, memberi alasan tiap ciri | Menemukan 4 ciri | Menemukan 3 ciri | < 3 ciri |
| Partisipasi diskusi | Aktif menyumbang ide dan bertanya | Menyumbang 2 ide | Menyumbang 1 ide | Pasif |
| Audit izin aplikasi | 3 aplikasi, lengkap dengan analisis izin wajar/tidak wajar | 3 aplikasi, tercatat | 2 aplikasi | Tidak mengumpulkan |

#### D.5 Contoh Soal/Tugas

"Soal 1: Enkripsikan kata "SEKOLAH" dengan Caesar cipher shift 5.
Soal 2: Jika ciphertext "JRRG" dengan shift 3, apa plaintext-nya?
Soal 3: Mengapa HTTPS lebih aman daripada HTTP? Jelaskan peran SSL/TLS!"

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**LKPD 15.1 — Enkripsi & Keamanan Digital**

Nama: _____________ Kelas: _____________ Tanggal: _____________

**Bagian A: Praktik Caesar Cipher**

Gunakan tabel alfabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Soal Enkripsi (geser huruf sesuai shift):
1. "KOMPUTER" shift 4 → ________
2. "INTERNET" shift 7 → ________
3. "FIREWALL" shift 10 → ________

Soal Dekripsi (kembalikan ke plaintext):
4. "QEB NRFZH YOLTK CLU" (shift 3) → ________
5. "ZNK WKXO" (shift 6) → ________

Buat pesan rahasia untuk temanmu (tulis ciphertext & shift):
Pesan asli: ________ → Ciphertext: ________ shift: ________

**Bagian B: Identifikasi Phishing**

Amati contoh email di proyektor. Catat ciri-ciri phishing yang ditemukan:

| No | Ciri Phishing | Ada/Tidak | Penjelasan |
|---|---|---|---|
| 1 | Alamat pengirim aneh | ________ | ________ |
| 2 | ________ | ________ | ________ |
| 3 | ________ | ________ | ________ |
| 4 | ________ | ________ | ________ |
| 5 | ________ | ________ | ________ |

**Tantangan Bertingkat:**
- Level Dasar (C): Kerjakan soal enkripsi nomor 1 & 4, identifikasi 3 ciri phishing
- Level Menengah (B): Kerjakan semua soal enkripsi & dekripsi, identifikasi 4 ciri
- Level Mahir (A): Kerjakan semua + buat pesan rahasia + analisis: "Jika Caesar cipher mudah dipecahkan, bagaimana cara kerja enkripsi modern yang lebih aman?"

### F. DIFERENSIASI PEMBELAJARAN

1. **Level Dasar (C):** Siswa mendapat tabel alfabet lengkap dengan nomor urut. Soal enkripsi hanya 2 nomor. Simulasi phishing difokuskan pada 3 ciri utama.
2. **Level Menengah (B):** Soal enkripsi standar (5 soal). Identifikasi phishing 4 ciri. Boleh menggunakan tabel alfabet biasa.
3. **Level Mahir (A):** Soal tambahan: enkripsi dengan shift berbeda tiap kata. Identifikasi phishing 5+ ciri. Tantangan: cari tahu bagaimana cara komputer memecahkan Caesar cipher (brute force dengan frekuensi huruf).

### G. REFLEKSI GURU

1. Apakah simulasi Caesar cipher membantu memahami konsep enkripsi? Apakah siswa kesulitan dengan perhitungan manual?
2. Bagaimana respons siswa terhadap simulasi phishing? Apakah ada yang mengaku pernah hampir tertipu?
3. Apakah demo firewall cukup jelas? Perlu praktik langsung atau cukup demonstrasi?
4. Apakah siswa menyadari pentingnya ikon gembok HTTPS setelah pembelajaran?
5. Bagaimana kualitas audit izin aplikasi yang dikumpulkan siswa?

### H. BAHAN BACAAN UNTUK GURU

1. **Sejarah Enkripsi:** Caesar cipher digunakan Julius Caesar untuk komunikasi militer (58 SM). Selama ribuan tahun, enkripsi berkembang: Vigenere cipher (1500-an), Enigma (PD II), DES (1977), hingga AES (2001) dan RSA (1977). Enkripsi modern menggunakan algoritma matematika kompleks yang tidak bisa dipecahkan dengan brute force dalam waktu wajar.
2. **HTTPS dan SSL/TLS:** HTTPS = HTTP + SSL/TLS. SSL/TLS menggunakan kombinasi enkripsi asimetris (untuk pertukaran kunci) dan simetris (untuk enkripsi data). Sertifikat SSL diterbitkan oleh Certificate Authority (CA) seperti Let's Encrypt, DigiCert. Browser memeriksa keabsahan sertifikat — jika tidak valid, browser menampilkan peringatan.
3. **Jenis Serangan Siber:** Phishing (penipuan mencuri kredensial), Man-in-the-Middle (menyadap komunikasi), DDoS (membanjiri server), Ransomware (mengenkripsi data korban), SQL Injection (menyusup ke database). Di Indonesia, kasus kebocoran data (Tokopedia 2020: 91 juta data, BPJS 2021: 279 juta data) menunjukkan pentingnya keamanan.
4. **Password Security:** Password yang lemah (123456, password) bisa dipecahkan dalam hitungan detik. Praktik terbaik: password panjang minimal 12 karakter, kombinasi huruf besar-kecil-angka-simbol, unik tiap akun, gunakan password manager. 2FA menambah lapisan keamanan dengan kode OTP atau biometrik.

---

Mengetahui,
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
