# MODUL AJAR INFORMATIKA KELAS X

## JKI: KONEKTIVITAS INTERNET (TP.4.2)

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | JKI — Jaringan Komputer & Internet |
| Tujuan Pembelajaran | TP.4.2: Menerapkan konfigurasi konektivitas internet |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 14 |
| Kompetensi Awal | Peserta didik telah memahami jenis jaringan dan topologi (LAN/MAN/WAN) serta perangkat jaringan pada pertemuan sebelumnya. |
| Integrasi 8 Dimensi | Kemandirian (praktik konfigurasi IP mandiri), Kolaborasi (kerja sama dalam praktik kelompok), Penalaran Kritis (menganalisis penyebab internet lemot), Keimanan & Bertakwa (memanfaatkan teknologi untuk kebaikan) |
| Sarana & Prasarana | Komputer/lab dengan koneksi internet, akses command prompt/terminal, proyektor, koneksi WiFi, aplikasi speedtest.net, Google DNS (8.8.8.8) |
| Target Peserta Didik | Reguler (dengan diferensiasi 3 tingkat) |
| Model Pembelajaran | Praktik Langsung |
| Metode | Demonstrasi, praktik konfigurasi berpasangan, eksperimen DNS, diskusi hasil speedtest |
| Sumber Belajar | Buku Informatika Kemendikbud Bab 5, dokumentasi ipconfig/ifconfig, artikel "How DNS Works" (Cloudflare), situs speedtest.net |

### B. TUJUAN PEMBELAJARAN

#### B.1 Tujuan Pembelajaran

1. Menjelaskan konsep IP address, DNS, dan DHCP serta analoginya dalam kehidupan sehari-hari.
2. Mengidentifikasi konfigurasi IP komputer sendiri melalui perintah ipconfig/ifconfig.
3. Menguji koneksi internet menggunakan perintah ping dan tracert/traceroute.
4. Membedakan pengaturan IP statis dan dinamis (DHCP) serta dampaknya.
5. Mengevaluasi kualitas koneksi internet melalui speedtest dan analisis faktor penyebab lambat.

#### B.2 Indikator Keberhasilan

| Indikator | Kriteria |
|---|---|
| Menjelaskan IP, DNS, DHCP dengan analogi yang tepat | Minimal 2 dari 3 konsep dijelaskan dengan analogi benar |
| Menjalankan ipconfig/ifconfig dan membaca output | Menemukan IP, subnet mask, gateway, DNS dengan benar |
| Melakukan ping ke google.com dan tracert | Ping berhasil, tracert menampilkan minimal 5 hop |
| Mengganti DNS ke Google DNS dan membandingkan | Perubahan tercatat, perbedaan dijelaskan |
| Mengukur speedtest & menganalisis hasil | Data kecepatan tercatat, faktor penyebab dianalisis |

#### B.3 Kata Kunci

IP address, subnet mask, gateway, DNS (Domain Name System), DHCP (Dynamic Host Configuration Protocol), ipconfig/ifconfig, ping, tracert/traceroute, statis, dinamis, latency, bandwidth, throughput

### C. KEGIATAN PEMBELAJARAN

| Tahap | Waktu | Aktivitas Guru | Aktivitas Siswa | Media/Sumber |
|---|---|---|---|---|
| **Pendahuluan** | 15 menit | 1) Salam dan doa. 2) Cek kehadiran. 3) Orientasi: "Kalian connect WiFi setiap hari — tapi apa yang sebenarnya terjadi di balik layar?" 4) Apersepsi: tanya siswa apakah tahu IP address HP mereka. 5) Asesmen diagnostik: 3 pertanyaan tentang koneksi internet. 6) Menyampaikan TP | 1) Menjawab salam dan berdoa. 2) Menyimak orientasi. 3) Mengecek IP HP (jika bisa). 4) Menjawab diagnostik. 5) Mencatat TP | Proyektor, HP siswa, slide orientasi |
| **Inti — Eksplorasi Konsep** | 15 menit | 1) Menjelaskan analogi: IP address = alamat rumah, DNS = buku telepon (menerjemahkan nama domain ke IP), DHCP = resepsionis yang memberi alamat otomatis. 2) Menjelaskan subnet mask (pembatas lingkungan), gateway (pintu keluar ke internet). 3) Mendemonstrasikan perintah ipconfig di CMD | 1) Menyimak dan mencatat analogi. 2) Menggambar analogi di buku catatan. 3) Mengamati demonstrasi | Proyektor, slide analogi, command prompt |
| **Inti — Praktik 1: Cek Konfigurasi IP** | 15 menit | 1) Membimbing siswa membuka CMD/Terminal. 2) Memandu mengetik perintah ipconfig (Windows) atau ifconfig (Linux/macOS). 3) Meminta siswa mencari: IP address, subnet mask, default gateway, DNS server. 4) Meminta siswa mencatat di LKPD | 1) Membuka CMD/Terminal. 2) Mengetik ipconfig/ifconfig. 3) Membaca output dan mencatat 4 parameter. 4) Membandingkan dengan teman sebangku | Komputer, command prompt, LKPD |
| **Inti — Praktik 2: Ping & Tracert** | 15 menit | 1) Menjelaskan perintah ping (uji koneksi ke host, ukur waktu respon). 2) Memandu: ping google.com — lihat reply time & packet loss. 3) Menjelaskan perintah tracert/traceroute (lihat jalur data). 4) Memandu: tracert google.com — catat jumlah hop. 5) Mendiskusikan: mengapa hop berpengaruh pada kecepatan | 1) Mengetik ping google.com. 2) Mencatat reply time dan packet loss. 3) Mengetik tracert google.com. 4) Menghitung jumlah hop. 5) Mendiskusikan hubungan hop dengan kecepatan | Komputer, command prompt, LKPD |
| **Inti — Praktik 3: Setting IP & DNS** | 20 menit | 1) Menjelaskan perbedaan IP statis (tetap) vs dinamis (DHCP — otomatis berubah). 2) Memandu mengganti DNS ke Google DNS (8.8.8.8 dan 8.8.4.4) di Network Settings. 3) Meminta siswa membuka situs sebelum dan sesudah ganti DNS — bandingkan kecepatan loading. 4) Memandu mengembalikan ke DNS otomatis | 1) Menyimak penjelasan. 2) Mengganti DNS ke 8.8.8.8. 3) Membuka situs dan membandingkan loading. 4) Mengembalikan ke DNS otomatis | Komputer, Network Settings, stopwatch HP |
| **Penutup** | 10 menit | 1) Diskusi: "Kenapa kadang internet lemot?" — brainstrom faktor: bandwidth terbatas, banyak pengguna, jarak ke server, gangguan sinyal. 2) Refleksi: "Apa hal baru yang kalian pelajari hari ini?" 3) Tugas: cek speedtest di rumah, screenshot hasil, laporkan. 4) Doa | 1) Berdiskusi faktor internet lemot. 2) Refleksi pembelajaran. 3) Mencatat tugas speedtest. 4) Berdoa | Papan tulis, lembar refleksi |

### D. ASESMEN

#### D.1 Asesmen Diagnostik

1. Apa yang dimaksud dengan IP address?
2. Kenapa kita mengetik google.com bukan 142.250.24.68?
3. Apa yang terjadi saat HP kalian connect ke WiFi?

#### D.2 Asesmen Formatif

Ceklist praktik: guru berkeliling dan menandai siswa yang berhasil menjalankan setiap perintah (ipconfig, ping, tracert, ganti DNS).

#### D.3 Asesmen Sumatif

1. LKPD praktik konfigurasi IP (produk individu)
2. Laporan speedtest dan analisis (tugas rumah)

#### D.4 Rubrik Penilaian

| Aspek | SB = 4 (Sangat Baik) | B = 3 (Baik) | C = 2 (Cukup) | PB = 1 (Perlu Bimbingan) |
|---|---|---|---|---|
| Praktik ipconfig | Menemukan 4 parameter benar, mencatat lengkap | Menemukan 3 parameter | Menemukan 2 parameter | < 2 atau tidak bisa menjalankan |
| Praktik ping & tracert | Ping berhasil + tracert ≥ 8 hop + analisis latency | Ping berhasil + tracret 5-7 hop | Ping berhasil + tracert < 5 hop | Ping gagal |
| Praktik ganti DNS | Berhasil ganti, membandingkan, menjelaskan perbedaan | Berhasil ganti, ada perbandingan | Berhasil ganti, tanpa perbandingan | Tidak berhasil |
| Laporan speedtest | Data lengkap + analisis 3 faktor penyebab | Data lengkap + analisis 1 faktor | Data ada tanpa analisis | Tidak mengumpulkan |

#### D.5 Contoh Soal/Tugas

"Jika seseorang di Jakarta mengakses server yang berlokasi di Amerika, data melewati banyak router (hop). Jika rata-rata latency per hop adalah 20 ms dan ada 15 hop, berapa perkiraan total waktu yang dibutuhkan?"

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**LKPD 14.1 — Eksplorasi Konektivitas Internet**

Nama: _____________ Kelas: _____________ Tanggal: _____________

**Bagian A: Cek Konfigurasi IP**

| Parameter | Hasil |
|---|---|
| IP Address | ________ |
| Subnet Mask | ________ |
| Default Gateway | ________ |
| DNS Server | ________ |

Analogi: Jika IP address adalah alamat rumah, maka gateway adalah ________.

**Bagian B: Uji Koneksi**

Perintah ping google.com — hasil:
- Reply time rata-rata: ________ ms
- Packet loss: ________ %
- Status: Terhubung / Tidak Terhubung

Perintah tracert google.com — hasil:
- Jumlah hop: ________
- Hop tercepat: ________ ms (hop ke-____)
- Hop terlambat: ________ ms (hop ke-____)

**Bagian C: Eksperimen DNS**

| Kondisi | Situs dibuka | Waktu loading (detik) |
|---|---|---|
| DNS default | ________ | ________ |
| Google DNS (8.8.8.8) | ________ | ________ |

Kesimpulan perbedaan: ________________________________________________

**Tantangan Bertingkat:**
- Level Dasar (C): Selesaikan Bagian A dan Bagian B
- Level Menengah (B): Selesaikan A, B, dan C
- Level Mahir (A): Selesaikan A, B, C + analisis: "Jika tracert menunjukkan hop terakhir di Jepang, tapi server yang dituju di Amerika, bagaimana ini bisa terjadi?"

### F. DIFERENSIASI PEMBELAJARAN

1. **Level Dasar (C):** Siswa mendapat LKPD dengan langkah terperinci (screenshot letak perintah). Didampingi intensif oleh guru. Hanya mengerjakan ping dan ipconfig.
2. **Level Menengah (B):** LKPD standar, mengerjakan semua praktik dengan panduan minimal. Mandiri berpasangan.
3. **Level Mahir (A):** LKPD diperkaya dengan tantangan: cari IP publik melalui whatismyip.com, bandingkan dengan IP lokal. Eksperimen tracert ke 3 server berbeda (google, youtube, server lokal). Analisis perbedaan hop.

### G. REFLEKSI GURU

1. Apakah analogi (alamat rumah, buku telepon, resepsionis) cukup membantu? Apakah ada analogi yang lebih baik?
2. Apakah semua komputer di lab bisa menjalankan perintah dengan lancar? Jika tidak, bagaimana solusinya?
3. Bagian praktik mana yang paling sulit bagi siswa — ganti DNS atau memahami output perintah?
4. Apakah laporan speedtest dari rumah bisa dijadikan bahan diskusi pertemuan berikutnya?
5. Bagaimana mengatasi siswa yang tidak memiliki akses internet di rumah untuk tugas speedtest?

### H. BAHAN BACAAN UNTUK GURU

1. **Cara Kerja DNS:** Saat user mengetik google.com, komputer mengirim query ke DNS server. Jika DNS server tidak tahu, ia akan bertanya ke DNS server lain secara hierarkis: Root DNS → TLD DNS (.com) → Authoritative DNS (google.com). Proses ini terjadi dalam hitungan milidetik. Cache DNS di komputer dan browser mempercepat proses ini.
2. **DHCP DORA Process:** DHCP bekerja dalam 4 langkah: Discover (client mencari server DHCP), Offer (server menawarkan IP), Request (client meminta IP yang ditawarkan), Acknowledge (server mengonfirmasi). Lease time adalah durasi IP diberikan — setelah habis, client harus memperbarui.
3. **IPv4 vs IPv6:** IPv4 memiliki 32 bit (4,3 miliar alamat — habis sejak 2019). IPv6 memiliki 128 bit (340 undecillion alamat — tak terbatas). Indonesia masih dominan IPv4 dengan NAT. IPv6 penting untuk IoT (Internet of Things).
4. **Bandwidth vs Throughput vs Latency:** Bandwidth = kapasitas maksimal (seperti lebar pipa). Throughput = data aktual yang berhasil dikirim. Latency = waktu tempuh data. Internet lemot bisa disebabkan oleh tiga faktor ini secara berbeda. Speedtest mengukur ketiganya.

---

Mengetahui,
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
