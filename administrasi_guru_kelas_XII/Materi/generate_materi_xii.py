#!/usr/bin/env python3
"""Generator Materi Ajar menarik & mudah dipahami — Informatika Kelas XII."""
import os, textwrap

BASE = "/home/daniarsyah/Documents/kerja_2026-2027/administrasi_guru_kelas_XII/Materi"
os.makedirs(BASE, exist_ok=True)

BAB = [
    {"id":"1","judul":"Informatika Sekarang dan Masa Depan","emoji":"🚀","smt":1,
     "sub":[("A","Apa Itu Literasi Digital?"),("B","Revolusi Industri 4.0"),("C","Internet of Things (IoT)"),("D","Big Data"),("E","Kecerdasan Buatan (AI)"),("F","Cloud Computing")]},
    {"id":"2","judul":"Sistem Komputer","emoji":"💻","smt":1,
     "sub":[("A","SBC vs Mikrokontroler"),("B","Kenalan dengan Arduino"),("C","Instalasi IDE Arduino"),("D","Komponen Penunjang Arduino"),("E","Simulator Arduino"),("F","Praktik: LED & Sensor"),("G","Proyek Mini: Monitoring Suhu")]},
    {"id":"3","judul":"Berpikir Komputasional dan Algoritma Pemrograman","emoji":"🧠","smt":1,
     "sub":[("A","Mengapa Berpikir Komputasional?"),("B","Dasar Pemrograman C untuk Arduino"),("C","Struktur Dasar Program C"),("D","Percabangan & Perulangan"),("E","Array: Kumpulan Data"),("F","Fungsi & Library Arduino"),("G","Proyek: Kontrol Otomatis")]},
    {"id":"4","judul":"Jaringan Komputer dan Internet","emoji":"🌐","smt":2,
     "sub":[("A","Apa Itu Jaringan Komputer?"),("B","Topologi Jaringan"),("C","Komponen & Perangkat Jaringan"),("D","Bagaimana Data Bepergian? (TCP/IP)"),("E","Cyber Security: Jaga Diri di Dunia Maya")]},
    {"id":"5","judul":"Dampak Sosial Informatika","emoji":"🌍","smt":2,
     "sub":[("A","Teknologi Digital & Masyarakat"),("B","Media Sosial: Pisau Bermata Dua"),("C","Digitalisasi Pendidikan"),("D","Ekonomi Digital: E-commerce & Fintech"),("E","UU ITE: Aturan Main di Dunia Digital")]},
    {"id":"6","judul":"Praktik Lintas Bidang","emoji":"🔧","smt":2,
     "sub":[("A","Apa Itu Proyek Lintas Bidang?"),("B","Tahap 1: Identifikasi Masalah"),("C","Tahap 2: Perencanaan Proyek"),("D","Tahap 3: Desain Solusi"),("E","Tahap 4: Implementasi Prototipe"),("F","Tahap 5: Pengujian & Perbaikan"),("G","Tahap 6: Dokumentasi & Laporan"),("H","Tahap 7: Presentasi & Refleksi")]},
]

# ─── SOAL PILIHAN GANDA ────────────────────────────────────────

SOAL_PG = {
    "1": [
        {
            "q":"Berikut ini yang BUKAN merupakan pilar literasi digital adalah…",
            "o":["Digital Skill","Digital Culture","Digital Economy","Digital Ethics","Digital Safety"],
            "a":"Digital Economy"
        },
        {
            "q":"Revolusi Industri 4.0 ditandai dengan…",
            "o":["Penemuan mesin uap","Produksi massal dengan listrik","Otomatisasi dengan komputer","IoT, AI, Big Data, dan Cyber Physical Systems","Penggunaan tenaga manusia"],
            "a":"IoT, AI, Big Data, dan Cyber Physical Systems"
        },
        {
            "q":"Contoh penerapan Internet of Things (IoT) dalam kehidupan sehari-hari adalah…",
            "o":["Mengetik dokumen di Word","Mengirim e-mail","Smart lamp yang bisa dikontrol lewat smartphone","Membaca buku cetak","Menghitung dengan kalkulator"],
            "a":"Smart lamp yang bisa dikontrol lewat smartphone"
        },
        {
            "q":"Karakteristik Big Data yang dikenal dengan istilah 3V adalah…",
            "o":["Volume, Variety, Velocity","Vision, Value, Volume","Vector, Virtual, Visual","Voice, Video, Variety","Validation, Verification, Version"],
            "a":"Volume, Variety, Velocity"
        },
        {
            "q":"Contoh AI yang menggunakan teknologi Computer Vision adalah…",
            "o":["ChatGPT","Google Maps","Spotify","Face ID iPhone","TikTok recommendation"],
            "a":"Face ID iPhone"
        },
    ],
    "2": [
        {
            "q":"Perbedaan utama antara SBC (Single Board Computer) dan Mikrokontroler adalah…",
            "o":["SBC lebih murah","SBC bisa menjalankan OS, mikrokontroler tidak","Mikrokontroler lebih cepat","SBC tidak punya GPIO","Mikrokontroler punya HDMI"],
            "a":"SBC bisa menjalankan OS, mikrokontroler tidak"
        },
        {
            "q":"Arduino Uno menggunakan mikrokontroler jenis…",
            "o":["ESP32","ATmega328P","ATmega2560","STM32","Raspberry Pi"],
            "a":"ATmega328P"
        },
        {
            "q":"Fungsi `pinMode(13, OUTPUT)` dalam program Arduino digunakan untuk…",
            "o":["Membaca data dari pin 13","Mengatur pin 13 sebagai output","Menyalakan LED di pin 13","Mematikan pin 13","Mengirim data serial"],
            "a":"Mengatur pin 13 sebagai output"
        },
        {
            "q":"Komponen yang berfungsi mendeteksi perubahan lingkungan seperti suhu atau cahaya disebut…",
            "o":["Aktuator","Resistor","Breadboard","Sensor","Kabel jumper"],
            "a":"Sensor"
        },
        {
            "q":"Fungsi `analogRead(A0)` pada Arduino menghasilkan nilai antara…",
            "o":["0–1","0–255","0–1023","0–5000","1–100"],
            "a":"0–1023"
        },
    ],
    "3": [
        {
            "q":"Memecah masalah besar menjadi bagian-bagian kecil adalah pilar berpikir komputasional yang disebut…",
            "o":["Pengenalan Pola","Abstraksi","Algoritma","Dekomposisi","Evaluasi"],
            "a":"Dekomposisi"
        },
        {
            "q":"Struktur program Arduino terdiri dari…",
            "o":["input() dan output()","start() dan end()","setup() dan loop()","begin() dan run()","init() dan process()"],
            "a":"setup() dan loop()"
        },
        {
            "q":"Perhatikan kode berikut:\n\nint a = 10, b = 3;\nint hasil = a % b;\n\nNilai dari variabel `hasil` adalah…",
            "o":["3","7","1","10","13"],
            "a":"1"
        },
        {
            "q":"Perulangan `for` cocok digunakan ketika…",
            "o":["Tidak tahu kapan berhenti","Sudah tahu berapa kali akan mengulang","Hanya mengulang sekali","Tidak perlu mengulang","Ingin mengulang tanpa syarat"],
            "a":"Sudah tahu berapa kali akan mengulang"
        },
        {
            "q":"Fungsi dalam pemrograman berguna untuk…",
            "o":["Memperlambat program","Memecah program jadi bagian kecil yang bisa dipanggil berulang","Menghapus variabel","Mengganti nama file","Mengulang program tanpa henti"],
            "a":"Memecah program jadi bagian kecil yang bisa dipanggil berulang"
        },
    ],
    "4": [
        {
            "q":"Jaringan yang mencakup area satu kota disebut…",
            "o":["PAN","LAN","MAN","WAN","GAN"],
            "a":"MAN"
        },
        {
            "q":"Topologi jaringan yang paling umum digunakan di laboratorium komputer sekolah adalah…",
            "o":["Bus","Ring","Mesh","Star","Tree"],
            "a":"Star"
        },
        {
            "q":"Perangkat yang berfungsi menghubungkan jaringan LAN ke internet adalah…",
            "o":["Switch","Hub","Router","Modem","Access Point"],
            "a":"Router"
        },
        {
            "q":"Protokol yang memastikan data sampai dengan utuh tetapi lebih lambat adalah…",
            "o":["UDP","HTTP","DNS","TCP","FTP"],
            "a":"TCP"
        },
        {
            "q":"Serangan yang memancing korban untuk memberikan data pribadi melalui link palsu disebut…",
            "o":["Malware","DDoS","Phishing","Hacking","Social Engineering"],
            "a":"Phishing"
        },
    ],
    "5": [
        {
            "q":"Dampak NEGATIF dari media sosial adalah…",
            "o":["Tempat belajar tutorial","Bisnis online","Cyberbullying","Networking","Kreativitas konten"],
            "a":"Cyberbullying"
        },
        {
            "q":"Contoh platform LMS (Learning Management System) adalah…",
            "o":["Shopee","TikTok","Google Classroom","Gojek","Netflix"],
            "a":"Google Classroom"
        },
        {
            "q":"Fintech adalah singkatan dari…",
            "o":["Financial Technology","Final Technology","Finance Technique","First Technology","Fiscal Network"],
            "a":"Financial Technology"
        },
        {
            "q":"Pasal dalam UU ITE yang mengatur tentang pencemaran nama baik adalah…",
            "o":["Pasal 27 ayat 1","Pasal 27 ayat 3","Pasal 28 ayat 1","Pasal 30","Pasal 45A"],
            "a":"Pasal 27 ayat 3"
        },
        {
            "q":"Salah satu ciri ekonomi digital adalah…",
            "o":["Pembayaran tunai","Transaksi melalui platform online","Barang dibeli di pasar tradisional","Menggunakan uang logam","Bertemu langsung penjual"],
            "a":"Transaksi melalui platform online"
        },
    ],
    "6": [
        {
            "q":"Proyek lintas bidang mengintegrasikan berbagai disiplin ilmu untuk…",
            "o":["Membuat karya seni","Menyelesaikan masalah nyata di lingkungan sekitar","Menulis buku","Mengikuti lomba","Menambah nilai rapor"],
            "a":"Menyelesaikan masalah nyata di lingkungan sekitar"
        },
        {
            "q":"Tahap pertama dalam metodologi proyek adalah…",
            "o":["Desain solusi","Implementasi prototipe","Identifikasi masalah","Pengujian","Presentasi"],
            "a":"Identifikasi masalah"
        },
        {
            "q":"Tujuan SMART digunakan dalam tahap…",
            "o":["Identifikasi masalah","Perencanaan proyek","Implementasi","Pengujian","Dokumentasi"],
            "a":"Perencanaan proyek"
        },
        {
            "q":"Flowchart dan diagram blok sistem dibuat pada tahap…",
            "o":["Identifikasi","Perencanaan","Desain solusi","Implementasi","Dokumentasi"],
            "a":"Desain solusi"
        },
        {
            "q":"Jenis pengujian yang menguji setiap komponen secara terpisah disebut…",
            "o":["Integration Test","Stress Test","User Test","Unit Test","Alpha Test"],
            "a":"Unit Test"
        },
    ],
}

# ─── SOAL URAIAN ──────────────────────────────────────────────

SOAL_URAIAN = {
    "1": [
        "Jelaskan 4 pilar literasi digital dan berikan masing-masing 1 contoh penerapannya!",
        "Bagaimana pengaruh Revolusi Industri 4.0 terhadap dunia pendidikan di Indonesia? Berikan 3 contoh!",
        "Jelaskan perbedaan antara AI, IoT, dan Cloud Computing. Berikan contoh masing-masing!",
        "Mengapa Big Data penting dalam perkembangan e-commerce seperti Shopee dan Tokopedia? Jelaskan!",
    ],
    "2": [
        "Bandingkan SBC (Single Board Computer) dengan mikrokontroler dari segi OS, konsumsi daya, dan kegunaan!",
        "Jelaskan langkah-langkah membuat program LED berkedip di Arduino! Mulai dari rangkaian hingga kode program.",
        "Apa fungsi sensor LM35 dan bagaimana cara membaca nilainya di program Arduino? Jelaskan dengan rumus konversinya!",
        "Jelaskan perbedaan antara sensor dan aktuator. Berikan 3 contoh masing-masing!",
    ],
    "3": [
        "Jelaskan 4 pilar berpikir komputasional dan berikan contoh penerapannya dalam kehidupan sehari-hari!",
        "Apa perbedaan antara `for` dan `while` dalam pemrograman C? Kapan sebaiknya menggunakan masing-masing?",
        "Buatlah program Arduino sederhana menggunakan array untuk menyalakan 6 LED secara bergantian!",
        "Jelaskan manfaat penggunaan fungsi dan library dalam pemrograman Arduino! Berikan contoh library yang sering digunakan!",
    ],
    "4": [
        "Jelaskan 4 jenis topologi jaringan beserta kelebihan dan kekurangan masing-masing!",
        "Bagaimana cara kerja TCP/IP dalam mengirim data dari satu komputer ke komputer lain? Gunakan analogi!",
        "Jelaskan 3 ancaman cyber security yang sering terjadi dan bagaimana cara melindungi diri!",
        "Apa itu DNS dan mengapa DNS penting dalam penggunaan internet sehari-hari? Jelaskan dengan contoh!",
    ],
    "5": [
        "Jelaskan 3 dampak positif dan 3 dampak negatif media sosial bagi remaja!",
        "Bagaimana digitalisasi pendidikan mengubah cara belajar siswa? Sebutkan keuntungan dan tantangannya!",
        "Apa yang dimaksud dengan ekonomi digital? Jelaskan peran e-commerce dan fintech dalam perekonomian Indonesia!",
        "Sebutkan 3 pasal penting dalam UU ITE dan jelaskan apa yang diatur serta ancaman hukumannya!",
    ],
    "6": [
        "Jelaskan 7 tahapan dalam proyek lintas bidang secara berurutan!",
        "Apa yang dimaksud dengan tujuan SMART? Berikan contoh tujuan SMART untuk proyek alat penyiram tanaman otomatis!",
        "Jelaskan perbedaan antara Unit Test, Integration Test, dan Stress Test dalam pengujian prototipe!",
        "Mengapa dokumentasi penting dalam sebuah proyek? Jelaskan format laporan proyek yang baik!",
    ],
}

# ─── RANGKUMAN ──────────────────────────────────────────────

RANGKUMAN = {
    "1": [
        "Literasi digital mencakup 4 pilar: Digital Skill, Digital Culture, Digital Ethics, dan Digital Safety — kemampuan ini penting agar kita menjadi warga digital yang cerdas dan bertanggung jawab.",
        "Revolusi Industri 4.0 ditandai dengan digitalisasi, otomatisasi, konektivitas real-time, dan integrasi sistem berbasis IoT, AI, Big Data, serta Cloud Computing.",
        "IoT menghubungkan benda-benda fisik ke internet sehingga bisa dikendalikan dan dimonitor dari jarak jauh — contohnya smart home, smartwatch, dan smart farming.",
        "Big Data adalah kumpulan data berukuran raksasa (Volume), dengan kecepatan tinggi (Velocity), dan beragam jenis (Variety) yang diolah untuk menghasilkan informasi berharga.",
        "AI adalah teknologi yang membuat mesin mampu meniru kecerdasan manusia — dari level ANI (sempit) hingga potensi AGI dan ASI di masa depan.",
        "Cloud Computing memungkinkan kita menggunakan sumber daya komputasi (server, penyimpanan, aplikasi) melalui internet dengan model SaaS, PaaS, dan IaaS.",
    ],
    "2": [
        "SBC (Single Board Computer) seperti Raspberry Pi bisa menjalankan OS dan cocok untuk tugas berat, sedangkan mikrokontroler seperti Arduino lebih hemat daya untuk tugas spesifik.",
        "Arduino adalah platform prototyping elektronik open-source yang mudah dipelajari, murah, dan memiliki komunitas besar.",
        "IDE Arduino adalah software untuk menulis, meng-compile, dan mengupload program — struktur dasarnya terdiri dari setup() dan loop().",
        "Komponen penunjang Arduino meliputi sensor (mendeteksi), aktuator (melakukan aksi), dan komponen pendukung seperti breadboard, kabel jumper, dan resistor.",
        "Simulator seperti Wokwi dan Tinkercad memungkinkan belajar Arduino tanpa hardware fisik — cocok untuk eksperimen awal.",
        "Praktik dasar meliputi menyalakan LED dan membaca sensor suhu LM35 dengan rumus konversi Suhu = (nilai × 5V / 1024) × 100.",
    ],
    "3": [
        "Berpikir komputasional memiliki 4 pilar: Dekomposisi (memecah masalah), Pengenalan Pola, Abstraksi (fokus pada hal penting), dan Algoritma (langkah penyelesaian).",
        "Struktur program Arduino terdiri dari setup() yang dijalankan sekali dan loop() yang berjalan terus-menerus.",
        "Variabel menyimpan data dengan berbagai tipe: int, float, boolean, char, String — dan operator aritmatika serta logika digunakan untuk mengolahnya.",
        "Percabangan (if/else) digunakan untuk pengambilan keputusan; perulangan (for/while) untuk mengulang eksekusi kode.",
        "Array adalah struktur data yang menyimpan banyak nilai dengan tipe yang sama dan diakses menggunakan indeks (mulai dari 0).",
        "Fungsi membuat program lebih terstruktur dengan memecah kode menjadi blok yang bisa dipanggil berulang; library menyediakan fungsi siap pakai seperti LiquidCrystal, Servo, dan DHT.",
    ],
    "4": [
        "Jaringan komputer memungkinkan berbagi data, printer, dan akses internet — diklasifikasikan menjadi PAN, LAN, MAN, dan WAN berdasarkan luas area.",
        "Topologi jaringan meliputi Bus (hemat kabel), Star (paling populer), Ring, dan Mesh (paling andal) — masing-masing memiliki kelebihan dan kekurangan.",
        "Komponen jaringan utama meliputi Router (penghubung jaringan), Switch (penghubung dalam LAN), Modem, Access Point, dan NIC.",
        "TCP/IP adalah protokol yang mengatur pengiriman data di internet — TCP memastikan data utuh, UDP mengutamakan kecepatan.",
        "Cyber security melindungi sistem dari ancaman seperti malware, phishing, DDoS, dan hacking — tips aman: password kuat, 2FA, dan tidak klik link sembarangan.",
    ],
    "5": [
        "Teknologi digital mengubah cara manusia berkomunikasi, belajar, berbelanja, dan bekerja — membawa dampak positif dan negatif yang perlu disikapi bijak.",
        "Media sosial memiliki sisi positif (belajar, bisnis, networking) dan negatif (FOMO, cyberbullying, dopamine loop) — gunakan dengan bijak dan batasi waktu.",
        "Digitalisasi pendidikan menghadirkan LMS, video conference, e-book, AI tutor, dan lab virtual — meningkatkan akses dan fleksibilitas belajar.",
        "Ekonomi digital terdiri dari e-commerce (Shopee, Tokopedia) dan fintech (GoPay, OVO, Ajaib) — memudahkan transaksi namun perlu waspada pinjol ilegal.",
        "UU ITE mengatur aktivitas di dunia digital — pasal penting meliputi larangan konten asusila, pencemaran nama baik, hoaks, dan akses ilegal.",
    ],
    "6": [
        "Proyek lintas bidang mengintegrasikan semua ilmu informatika untuk menyelesaikan masalah nyata — dimulai dari identifikasi masalah hingga presentasi.",
        "Tahap 1: Identifikasi masalah dengan observasi dan 5W+1H; Tahap 2: Perencanaan dengan tujuan SMART dan timeline proyek.",
        "Tahap 3: Desain solusi mencakup diagram blok sistem, flowchart program, dan skema rangkaian.",
        "Tahap 4-5: Implementasi prototipe dan pengujian (Unit Test, Integration Test, Stress Test) dengan dokumentasi hasil.",
        "Tahap 6-7: Dokumentasi laporan lengkap dan presentasi dengan demo alat — diakhiri dengan refleksi pembelajaran.",
        "Kunci keberhasilan proyek: kerja sama tim, perencanaan matang, dokumentasi setiap langkah, dan tidak takut gagal dalam proses.",
    ],
}


# ─── GLOSARIUM ──────────────────────────────────────────────

GLOSARIUM = {
    "1": [
        ("Literasi Digital", "Kemampuan menggunakan teknologi informasi dan komunikasi secara efektif, etis, dan kritis."),
        ("Revolusi Industri 4.0", "Era industri yang menggabungkan teknologi digital, IoT, AI, Big Data, dan Cloud Computing."),
        ("IoT (Internet of Things)", "Jaringan benda fisik yang terhubung ke internet untuk saling bertukar data."),
        ("Big Data", "Kumpulan data berukuran sangat besar yang tidak bisa diolah dengan cara konvensional."),
        ("AI (Artificial Intelligence)", "Kecerdasan buatan — kemampuan mesin meniru kecerdasan manusia untuk belajar dan mengambil keputusan."),
        ("Cloud Computing", "Penggunaan sumber daya komputasi (server, storage, aplikasi) melalui internet."),
        ("SaaS", "Software as a Service — model cloud di mana pengguna memakai aplikasi tanpa instalasi lokal."),
        ("Machine Learning", "Cabang AI di mana mesin belajar dari data tanpa diprogram secara eksplisit."),
    ],
    "2": [
        ("SBC (Single Board Computer)", "Komputer lengkap dalam satu papan sirkuit, seperti Raspberry Pi."),
        ("Mikrokontroler", "Chip tunggal yang berfungsi sebagai pengontrol sistem elektronik, seperti Arduino."),
        ("Arduino", "Platform prototyping elektronik open-source berbasis mikrokontroler."),
        ("IDE Arduino", "Lingkungan pengembangan terintegrasi untuk menulis dan mengupload kode ke Arduino."),
        ("GPIO", "General Purpose Input Output — pin pada SBC/mikrokontroler untuk koneksi komponen eksternal."),
        ("Sensor", "Komponen yang mendeteksi perubahan fisik (suhu, cahaya, gerak) dan mengubahnya menjadi sinyal listrik."),
        ("PWM", "Pulse Width Modulation — teknik mengatur daya dengan variasi lebar pulsa."),
    ],
    "3": [
        ("Berpikir Komputasional", "Cara berpikir untuk memecahkan masalah dengan menerapkan konsep dan logika ilmu komputer."),
        ("Dekomposisi", "Memecah masalah besar menjadi bagian-bagian kecil yang lebih mudah dikelola."),
        ("Algoritma", "Langkah-langkah sistematis untuk menyelesaikan suatu masalah."),
        ("Abstraksi", "Memfokuskan pada informasi penting dan mengabaikan yang tidak relevan."),
        ("Variabel", "Tempat menyimpan data dalam program komputer."),
        ("Array", "Struktur data yang menyimpan banyak nilai dengan tipe yang sama dalam satu variabel."),
        ("Fungsi", "Blok kode yang bisa dipanggil berulang kali untuk menjalankan tugas tertentu."),
        ("Library", "Kumpulan fungsi siap pakai yang bisa digunakan dalam program."),
    ],
    "4": [
        ("Jaringan Komputer", "Dua atau lebih komputer yang saling terhubung untuk berbagi data dan sumber daya."),
        ("LAN", "Local Area Network — jaringan yang mencakup area terbatas seperti lab komputer."),
        ("Topologi Jaringan", "Bentuk/susunan koneksi antar komputer dalam jaringan."),
        ("TCP/IP", "Protokol yang mengatur bagaimana data dikirim melalui internet."),
        ("IP Address", "Alamat unik setiap perangkat dalam jaringan komputer."),
        ("DNS", "Domain Name System — menerjemahkan nama domain menjadi IP address."),
        ("Phishing", "Serangan yang memancing korban memberikan data pribadi melalui tautan palsu."),
        ("Firewall", "Sistem keamanan yang memantau dan mengontrol lalu lintas jaringan."),
    ],
    "5": [
        ("Literasi Digital", "Kemampuan menggunakan teknologi digital secara efektif, etis, dan bertanggung jawab."),
        ("Cyberbullying", "Perundungan yang dilakukan melalui media digital."),
        ("FOMO", "Fear of Missing Out — kecemasan karena takut ketinggalan tren atau momen."),
        ("E-commerce", "Perdagangan elektronik — jual-beli barang/jasa melalui platform online."),
        ("Fintech", "Financial Technology — inovasi teknologi di bidang keuangan."),
        ("LMS", "Learning Management System — platform manajemen pembelajaran online."),
        ("UU ITE", "Undang-Undang Informasi dan Transaksi Elektronik yang mengatur aktivitas digital di Indonesia."),
    ],
    "6": [
        ("Proyek Lintas Bidang", "Proyek yang mengintegrasikan berbagai disiplin ilmu untuk menyelesaikan masalah nyata."),
        ("Prototipe", "Model awal atau versi percobaan dari suatu produk."),
        ("SMART", "Kriteria tujuan: Specific, Measurable, Achievable, Relevant, Time-bound."),
        ("Flowchart", "Diagram alur yang menggambarkan langkah-langkah suatu program."),
        ("Unit Test", "Pengujian setiap komponen secara terpisah untuk memastikan fungsinya."),
        ("Debugging", "Proses mencari dan memperbaiki kesalahan dalam program."),
        ("Dokumentasi", "Catatan lengkap tentang proyek agar orang lain bisa memahami dan mereproduksi."),
    ],
}

# ─── MEDIA PEMBELAJARAN ─────────────────────────────────────

MEDIA = {
    "1": [
        ("YouTube", "Apa itu Revolusi Industri 4.0?", "youtu.be/search?q=revolusi+industri+4.0+indonesia", "Penjelasan Revolusi 4.0 oleh KEMDIKBUD"),
        ("YouTube", "IoT untuk Pemula", "youtu.be/search?q=internet+of+things+pemula", "Pengenalan IoT dengan contoh sehari-hari"),
        ("YouTube", "Cara Kerja AI & Machine Learning", "youtu.be/search?q=AI+machine+learning+indonesia", "Penjelasan AI dengan animasi"),
        ("Simulasi", "Cisco Packet Tracer", "https://www.netacad.com/", "Simulator jaringan dari Cisco"),
        ("Website", "Dicoding — Belajar Cloud", "https://www.dicoding.com/", "Kelas cloud computing gratis"),
    ],
    "2": [
        ("YouTube", "Apa itu Arduino?", "youtu.be/search?q=pengenalan+arduino+indonesia", "Pengenalan Arduino oleh komunitas Indonesia"),
        ("Simulasi", "Tinkercad Circuits", "https://www.tinkercad.com/circuits", "Simulator Arduino online gratis"),
        ("Website", "Arduino Project Hub", "https://projecthub.arduino.cc/", "Koleksi proyek Arduino dari seluruh dunia"),
        ("YouTube", "Belajar C untuk Arduino", "youtu.be/search?q=dasar+program+C+arduino", "Tutorial dasar pemrograman Arduino"),
        ("Website", "Random Nerd Tutorials", "https://randomnerdtutorials.com/", "Tutorial Arduino dan ESP8266/ESP32"),
    ],
    "3": [
        ("YouTube", "Berpikir Komputasional", "youtu.be/search?q=berpikir+komputasional+indonesia", "Penjelasan 4 pilar BK oleh guru Indonesia"),
        ("YouTube", "Belajar Pemrograman C untuk Pemula", "youtu.be/search?q=belajar+pemrograman+C+arduino+pemula", "Tutorial bahasa C dari dasar"),
        ("Simulasi", "Wokwi Arduino Simulator", "https://wokwi.com/", "Simulator Arduino online dengan berbagai komponen"),
        ("Website", "Kelas Terbuka — Algoritma", "https://www.kelasterbuka.com/", "Video belajar algoritma dan pemrograman"),
        ("Website", "Programiz C Programming", "https://www.programiz.com/c-programming", "Tutorial interaktif bahasa C"),
    ],
    "4": [
        ("YouTube", "Apa itu Jaringan Komputer?", "youtu.be/search?q=jaringan+komputer+dasar+indonesia", "Pengantar jaringan komputer lengkap"),
        ("YouTube", "Topologi Jaringan", "youtu.be/search?q=topologi+jaringan+komputer+indonesia", "Jenis dan perbandingan topologi jaringan"),
        ("YouTube", "Cyber Security untuk Pemula", "youtu.be/search?q=cyber+security+dasar+indonesia", "Ancaman dan cara melindungi diri di internet"),
        ("Simulasi", "Cisco Packet Tracer", "https://www.netacad.com/", "Simulator jaringan dari Cisco Academy gratis"),
        ("Website", "BNPT — Belajar Keamanan Digital", "https://www.bnpt.go.id/", "Edukasi keamanan siber dari pemerintah"),
    ],
    "5": [
        ("YouTube", "Dampak Media Sosial", "youtu.be/search?q=dampak+media+sosial+positif+negatif", "Analisis dampak medsos bagi remaja"),
        ("YouTube", "Apa itu Fintech?", "youtu.be/search?q=fintech+indonesia+penjelasan", "Penjelasan fintech dan contohnya di Indonesia"),
        ("YouTube", "UU ITE Terbaru 2024", "youtu.be/search?q=uu+ite+2024+penjelasan", "Penjelasan pasal-pasal UU ITE revisi terbaru"),
        ("Website", "OJK — Edukasi Fintech", "https://www.ojk.go.id/", "Edukasi keuangan digital dan fintech legal"),
        ("Website", "KOMINFO — Literasi Digital", "https://www.literasidigital.id/", "Program literasi digital nasional KOMINFO"),
    ],
    "6": [
        ("YouTube", "Cara Membuat Proyek Arduino", "youtu.be/search?q=proyek+arduino+sederhana+indonesia", "Inspirasi proyek Arduino untuk pemula"),
        ("YouTube", "Tips Presentasi yang Baik", "youtu.be/search?q=tips+presentasi+proyek+sekolah", "Cara presentasi proyek yang efektif"),
        ("Website", "Instructables", "https://www.instructables.com/", "Koleksi proyek DIY lengkap dengan tutorial"),
        ("Website", "Hackster.io", "https://www.hackster.io/", "Platform berbagi proyek IoT dan embedded"),
        ("Simulasi", "Tinkercad Circuits", "https://www.tinkercad.com/circuits", "Simulator rangkaian elektronik online gratis"),
    ],
}

# ─── CAPAIAN PEMBELAJARAN ──────────────────────────────

CP_MAP = {
    "1": [
        ("Teknologi Informasi dan Komunikasi", "Peserta didik mampu memahami dan menjelaskan perkembangan teknologi IoT, AI, Big Data, dan Cloud Computing serta penerapannya dalam berbagai bidang kehidupan."),
        ("Analisis Data", "Peserta didik mampu memahami konsep Big Data, karakteristik 3V, serta penerapannya dalam pengambilan keputusan di berbagai bidang."),
    ],
    "2": [
        ("Sistem Komputer", "Peserta didik mampu memahami arsitektur sistem komputer, perbedaan SBC dan mikrokontroler, serta mampu menggunakan platform Arduino untuk membuat sistem elektronik sederhana."),
    ],
    "3": [
        ("Berpikir Komputasional", "Peserta didik mampu menerapkan berpikir komputasional (dekomposisi, pengenalan pola, abstraksi, algoritma) untuk memecahkan masalah sehari-hari."),
        ("Algoritma dan Pemrograman", "Peserta didik mampu menulis program dalam bahasa C untuk Arduino yang mencakup variabel, percabangan, perulangan, array, dan fungsi."),
    ],
    "4": [
        ("Jaringan Komputer dan Internet", "Peserta didik mampu memahami konsep jaringan komputer, topologi, perangkat jaringan, dan protokol TCP/IP, serta menerapkan prinsip keamanan siber."),
    ],
    "5": [
        ("Dampak Sosial Informatika", "Peserta didik mampu menganalisis dampak sosial perkembangan teknologi digital, termasuk media sosial, digitalisasi pendidikan, ekonomi digital, dan regulasi UU ITE."),
    ],
    "6": [
        ("Praktik Lintas Bidang", "Peserta didik mampu merencanakan, mengimplementasikan, menguji, dan mempresentasikan proyek lintas bidang yang mengintegrasikan konsep informatika untuk menyelesaikan masalah nyata."),
    ],
}

# ─── PROYEK MINI ─────────────────────────────────────

PROYEK = {
    "1": {
        "judul": "📊 Presentasi Singkat Tech Masa Depan",
        "deskripsi": "Pilih 1 teknologi (IoT/AI/Cloud/Big Data) yang paling menarik menurutmu. Buat presentasi 5 slide yang menjelaskan cara kerja, contoh penerapan, dan dampak positif-negatifnya. Presentasikan di depan kelas selama 5-7 menit.",
        "alat": ["Laptop/Chromebook", "Google Slides/Canva/Microsoft PowerPoint", "Proyektor/LCD", "Koneksi internet untuk riset"],
        "langkah": [
            "Pilih 1 topik dari: IoT, AI, Cloud Computing, atau Big Data",
            "Riset minimal dari 3 sumber berbeda (buku, artikel, YouTube)",
            "Buat 5 slide: (1) Judul, (2) Cara Kerja, (3) Contoh Penerapan, (4) Dampak, (5) Kesimpulan",
            "Tambahkan gambar/diagram untuk memperjelas penjelasan",
            "Latihan presentasi — pastikan durasi 5-7 menit",
            "Presentasikan di depan kelas dan jawab pertanyaan teman",
        ],
        "output": "File presentasi (.pdf/.pptx) + dokumentasi presentasi (foto)",
    },
    "2": {
        "judul": "💡 Rangkaian Arduino: Lampu Otomatis",
        "deskripsi": "Buat rangkaian LED yang menyala otomatis saat gelap menggunakan sensor cahaya (LDR) dan Arduino. Proyek ini mengajarkan konsep input sensor, logika percabangan, dan output aktuator. Rangkaian bisa disimulasikan di Tinkercad jika tidak punya Arduino fisik.",
        "alat": ["Arduino Uno", "Sensor LDR", "LED 5mm", "Resistor 220 Ohm dan 10k Ohm", "Kabel Jumper", "Breadboard", "Tinkercad Circuits (alternatif simulator)"],
        "langkah": [
            "Rangkai sensor LDR dengan resistor 10k Ohm membentuk voltage divider, hubungkan ke pin A0",
            "Rangkai LED dengan resistor 220 Ohm, hubungkan anoda ke pin 9 dan katoda ke GND",
            "Tulis program: baca nilai analog dari LDR pakai `analogRead(A0)`, jika nilai < 500 (gelap) LED nyala, jika >= 500 (terang) LED mati",
            "Upload program ke Arduino atau jalankan di simulator",
            "Uji coba: tutup sensor LDR dengan tangan — LED harus menyala; buka — LED harus mati",
            "Dokumentasikan rangkaian dan hasil pengujian dalam bentuk foto/video",
        ],
        "output": "Rangkaian LED otomatis fungsional + dokumentasi (foto/video + kode program)",
    },
    "3": {
        "judul": "🚦 Program Arduino: Traffic Light",
        "deskripsi": "Buat program traffic light (lampu lalu lintas) sederhana menggunakan 3 LED (merah, kuning, hijau) di Arduino/Tinkercad. Proyek ini melatih pemahaman tentang perulangan, fungsi, dan timing dalam pemrograman Arduino.",
        "alat": ["Arduino Uno", "LED Merah, Kuning, Hijau", "Resistor 220 Ohm (x3)", "Kabel Jumper", "Breadboard", "Tinkercad Circuits (alternatif simulator)"],
        "langkah": [
            "Rangkai 3 LED ke pin digital 10 (merah), 9 (kuning), 8 (hijau) masing-masing dengan resistor 220 Ohm",
            "Buat fungsi `nyalakanLED(int merah, int kuning, int hijau)` untuk mengatur nyala/mati LED dengan parameter ON/OFF",
            "Buat fungsi `trafficLightCycle()` dengan urutan: Hijau 5 detik → Kuning 2 detik → Merah 5 detik → Kuning 2 detik",
            "Panggil `trafficLightCycle()` di dalam `loop()`",
            "Upload program ke Arduino atau jalankan di simulator",
            "Uji coba: pastikan urutan dan durasi LED sesuai yang diharapkan",
        ],
        "output": "Simulasi traffic light 3 LED berjalan dengan urutan dan timing yang benar",
    },
    "4": {
        "judul": "🌐 Konfigurasi Jaringan Dasar",
        "deskripsi": "Konfigurasi jaringan sederhana menggunakan Cisco Packet Tracer. Hubungkan 2 PC, 1 switch, dan 1 router, lalu atur IP address agar semua perangkat bisa saling ping. Proyek ini mengajarkan konsep IP addressing, subnet, dan routing dasar.",
        "alat": ["Cisco Packet Tracer (gratis dari NetAcad)", "Laptop/PC", "Modul panduan Cisco Packet Tracer"],
        "langkah": [
            "Buka Cisco Packet Tracer dan buat proyek baru",
            "Tempatkan 1 router (Router-PT), 1 switch (Switch-PT), dan 2 PC (PC-PT) di workspace",
            "Hubungkan PC1 dan PC2 ke switch dengan kabel Copper Straight-Through",
            "Hubungkan switch ke router dengan kabel Copper Straight-Through",
            "Konfigurasi IP address: PC1 = 192.168.1.2/24, PC2 = 192.168.1.3/24, Router interface = 192.168.1.1/24",
            "Konfigurasi gateway default PC1 dan PC2 ke 192.168.1.1",
            "Uji koneksi: dari PC1 ping ke PC2 (192.168.1.3) dan ke router (192.168.1.1)",
        ],
        "output": "File .pkt Cisco Packet Tracer dengan 2 PC + 1 switch + 1 router, semua saling ping berhasil",
    },
    "5": {
        "judul": "🖼️ Infografis UU ITE",
        "deskripsi": "Buat infografis informatif yang menjelaskan 5 pasal penting dalam UU ITE yang relevan untuk remaja. Infografis harus mudah dipahami, menarik secara visual, dan mencantumkan sumber hukum yang benar. Hasil bisa ditempel di mading sekolah atau diunggah ke media sosial.",
        "alat": ["Canva/Adobe Express/Figma", "Laptop/Chromebook", "Akses ke UU ITE No. 1 Tahun 2024", "Referensi dari KOMINFO"],
        "langkah": [
            "Pelajari 5 pasal penting UU ITE: Pasal 27 ayat 1 (asusila), Pasal 27 ayat 3 (pencemaran nama baik), Pasal 28 ayat 1 (hoaks), Pasal 28 ayat 2 (ujaran kebencian SARA), Pasal 30 (akses ilegal)",
            "Catat poin penting setiap pasal: apa yang diatur dan ancaman hukumannya",
            "Buka Canva atau aplikasi desain grafis pilihanmu, buat ukuran A4 portrait",
            "Buat infografis dengan: judul menarik, ikon/ilustrasi tiap pasal, warna yang sesuai, dan sumber hukum di bagian bawah",
            "Minta teman atau guru membaca infografis dan memberi masukan",
            "Export dalam format PNG/PDF dan siap untuk dipajang atau diunggah",
        ],
        "output": "Infografis UU ITE 5 pasal dalam format PNG/PDF siap pajang",
    },
    "6": {
        "judul": "📋 Proposal Proyek Lintas Bidang",
        "deskripsi": "Buat proposal proyek yang menggabungkan Informatika dengan 1 bidang lain pilihanmu (Biologi, Fisika, Kimia, Seni, Ekonomi, atau Bahasa). Proposal harus mencakup identifikasi masalah, tujuan SMART, desain solusi, dan timeline pengerjaan. Proyek ini melatih kemampuan menulis ilmiah dan perencanaan sistematis.",
        "alat": ["Laptop/Chromebook", "Google Docs/Microsoft Word", "Canva/Google Slides (untuk presentasi)", "Referensi dari buku/internet"],
        "langkah": [
            "Tentukan bidang lain yang akan diintegrasikan dengan Informatika (contoh: Biologi = alat monitoring tanaman, Seni = instalasi lampu interaktif)",
            "Identifikasi masalah nyata di lingkungan sekitar yang bisa diselesaikan dengan kombinasi kedua bidang",
            "Rumuskan tujuan SMART: Specific, Measurable, Achievable, Relevant, Time-bound",
            "Buat desain solusi: diagram blok sistem, flowchart program, dan sketsa alat (jika ada hardware)",
            "Susun timeline proyek 4-6 minggu dalam bentuk tabel",
            "Tulis proposal lengkap: Pendahuluan → Kajian Teori → Metode → Timeline → Daftar Pustaka",
        ],
        "output": "Dokumen proposal proyek lintas bidang (.pdf/.docx) + slide presentasi singkat",
    },
}

# ─── RUBRIK PENILAIAN ─────────────────────────────────────

RUBRIK = {
    "1": {
        "aspek": ["Pemahaman Materi", "Kualitas Presentasi", "Visualisasi", "Kemampuan Menjawab"],
        "level1": ["Kurang memahami cara kerja teknologi yang dipilih", "Presentasi tidak terstruktur, durasi kurang/lebih", "Slide hanya teks, tidak ada gambar/diagram", "Tidak bisa menjawab pertanyaan"],
        "level2": ["Cukup memahami dengan beberapa kesalahan", "Presentasi cukup terstruktur, durasi sesuai", "Slide memiliki gambar tapi kurang relevan", "Menjawab dengan bantuan guru"],
        "level3": ["Memahami dengan baik dan bisa menjelaskan ulang", "Presentasi terstruktur, percaya diri, durasi tepat", "Slide menarik, gambar/diagram relevan", "Menjawab dengan tepat dan percaya diri"],
    },
    "2": {
        "aspek": ["Perangkaian Hardware", "Kebenaran Program", "Fungsionalitas Alat", "Dokumentasi"],
        "level1": ["Rangkaian salah, komponen tidak terpasang benar", "Program tidak sesuai spesifikasi, error", "Alat tidak berfungsi sama sekali", "Tidak ada dokumentasi"],
        "level2": ["Rangkaian benar tapi kurang rapi", "Program berjalan dengan beberapa bug", "Alat berfungsi sebagian atau kadang error", "Dokumentasi ada tapi kurang lengkap"],
        "level3": ["Rangkaian rapi dan benar sesuai skema", "Program benar, efisien, dan bebas error", "Alat berfungsi sempurna sesuai spesifikasi", "Dokumentasi lengkap (foto, video, kode program)"],
    },
    "3": {
        "aspek": ["Perangkaian Hardware", "Kebenaran Program", "Fungsionalitas Alat", "Dokumentasi"],
        "level1": ["Rangkaian traffic light salah", "Program tidak sesuai logika traffic light", "Traffic light tidak berfungsi", "Tidak ada dokumentasi"],
        "level2": ["Rangkaian benar tapi kurang rapi", "Program berjalan dengan kesalahan timing", "Traffic light berfungsi tapi ada jeda tidak sesuai", "Dokumentasi ada tapi kurang lengkap"],
        "level3": ["Rangkaian rapi, LED terpasang dengan benar", "Program benar, timing tepat, menggunakan fungsi", "Traffic light berfungsi sempurna: hijau5→kuning2→merah5→kuning2", "Dokumentasi lengkap (foto, video, kode program)"],
    },
    "4": {
        "aspek": ["Konfigurasi Jaringan", "Pemahaman IP Address", "Fungsionalitas (Ping)", "Dokumentasi"],
        "level1": ["Topologi tidak sesuai, kabel salah", "Tidak paham konsep IP address", "Tidak ada satupun ping berhasil", "Tidak ada dokumentasi"],
        "level2": ["Topologi benar tapi ada kesalahan konfigurasi", "IP address terisi tapi ada kesalahan subnet", "Ping berhasil sebagian (PC ke router saja)", "Dokumentasi ada tapi kurang detail"],
        "level3": ["Topologi benar, semua perangkat terkonfigurasi tepat", "IP address dan subnet benar semua", "Semua ping berhasil: PC1↔PC2, PC↔Router", "Dokumentasi lengkap dengan screenshot tiap langkah"],
    },
    "5": {
        "aspek": ["Kelengkapan Konten", "Desain Visual", "Akurasi Hukum", "Kreativitas"],
        "level1": ["Kurang dari 3 pasal tercantum", "Desain monoton, tidak menarik", "Terdapat kesalahan informasi pasal/hukuman", "Tidak ada sentuhan kreatif, hanya teks polos"],
        "level2": ["5 pasal tercantum tapi penjelasan kurang", "Desain cukup menarik, warna sesuai", "Informasi benar tapi kurang detail", "Ada elemen kreatif (ikon/warna) tapi minimal"],
        "level3": ["5 pasal lengkap dengan penjelasan dan hukuman", "Desain sangat menarik, ikon relevan, layout rapi", "Informasi akurat sesuai UU No. 1 Tahun 2024", "Kreatif dan original, layak dipajang"],
    },
    "6": {
        "aspek": ["Identifikasi Masalah", "Perencanaan (SMART)", "Desain Solusi", "Format Proposal"],
        "level1": ["Masalah tidak jelas atau tidak relevan", "Tujuan tidak SMART", "Tidak ada desain teknis", "Proposal tidak sesuai format, banyak typo"],
        "level2": ["Masalah teridentifikasi tapi kurang spesifik", "Tujuan cukup SMART dengan beberapa kelemahan", "Desain ada tapi kurang detail", "Proposal cukup rapi dengan beberapa kekurangan"],
        "level3": ["Masalah spesifik, relevan, teridentifikasi dengan 5W+1H", "Tujuan memenuhi semua kriteria SMART", "Desain lengkap: diagram blok, flowchart, sketsa", "Proposal rapi, format benar, bahasa ilmiah, daftar pustaka"],
    },
}

# ─── PENGAYAAN ─────────────────────────────────────

PENGAYAAN = {
    "1": [
        ("🔍 Riset Deep Dive: Dampak AI di Indonesia", "Lakukan riset lebih mendalam tentang bagaimana AI sudah digunakan di Indonesia. Cari 3 perusahaan/organisasi Indonesia yang menggunakan AI (contoh: Gojek, Shopee, Kominfo). Buat laporan 1 halaman yang menjelaskan: (1) bidang apa, (2) bagaimana AI digunakan, (3) dampak positif dan negatifnya. Kumpulkan dalam bentuk dokumen MS Word/Google Docs."),
        ("📝 Esai: Masa Depan Pekerjaanku di Era AI", "Menurutmu, pekerjaan apa yang paling mungkin digantikan AI dalam 10 tahun ke depan? Pilih 1 profesi yang kamu minati dan jelaskan: (1) apakah profesi itu akan tergantikan atau justru berubah, (2) skill apa yang perlu kamu kuasai agar tetap relevan, (3) bagaimana rencanamu untuk mempersiapkan diri. Tulis esai minimal 500 kata."),
    ],
    "2": [
        ("🔧 Proyek Tambahan: Alarm Suhu dengan Buzzer", "Kembangkan rangkaian lampu otomatis dengan menambahkan buzzer yang berbunyi jika suhu melebihi 35°C. Gunakan sensor suhu LM35/DHT11 dan buzzer piezo. Buat 3 level: suhu normal (LED hijau), waspada (LED kuning), bahaya (LED merah + buzzer). Dokumentasikan dalam bentuk video singkat."),
    ],
    "3": [
        ("🚦 Traffic Light dengan Pedestrian Crossing", "Kembangkan program traffic light sederhana menjadi sistem lalu lintas lengkap dengan pedestrian crossing. Tambahkan 2 LED tambahan (merah & hijau) untuk pejalan kaki, dan sebuah push button sebagai tombol penyeberangan. Gunakan interrupt atau polling untuk mendeteksi tombol. Buat laporan singkat berisi kode program dan penjelasan logika kerjanya."),
    ],
    "4": [
        ("🌐 Simulasi Jaringan dengan DHCP Server", "Kembangkan proyek Cisco Packet Tracer dengan menambahkan DHCP Server sehingga PC1 dan PC2 mendapatkan IP address secara otomatis. Konfigurasi router sebagai DHCP server dengan range IP 192.168.1.10 - 192.168.1.50. Buktikan bahwa PC mendapatkan IP otomatis dan tetap bisa saling ping. Screenshot setiap langkah konfigurasi."),
    ],
    "5": [
        ("📢 Kampanye Digital: Bijak Bermedsos", "Buat kampanye digital bertema 'Bijak Bermedsos' yang terdiri dari: (1) 3 poster edukatif untuk Instagram/TikTok, (2) 1 video pendek (30-60 detik) tentang tips aman bermedia sosial, (3) caption informatif yang menyertakan referensi UU ITE. Upload ke media sosial dengan hashtag #BijakBermedsos #PelajarDigital."),
    ],
    "6": [
        ("🔬 Proyek Mini: Buat Prototipe Sederhana", "Dari proposal yang sudah dibuat pada Proyek Mini Bab 6, buatlah prototipe sederhana menggunakan bahan yang tersedia di sekitar. Jika proposal menggunakan Arduino, buat rangkaian di Tinkercad. Jika proposal berupa aplikasi, buat wireframe/mockup di Figma. Dokumentasikan proses dan hasilnya dalam laporan singkat 2-3 halaman."),
    ],
}

def dedent(s):
    """Remove common leading whitespace from a multi-line string."""
    return textwrap.dedent(s).strip()


# ─── CONTENT GENERATORS ───────────────────────────────────────

def content_literasi_digital():
    return dedent("""
    ### 📱 Apa Itu Literasi Digital?

    Literasi digital adalah kemampuan menggunakan teknologi informasi dan komunikasi secara efektif, etis, dan kritis.

    > 🧩 **Analogi:** Literasi digital itu seperti SIM (Surat Izin Mengemudi).
    > Kalau kamu punya SIM, kamu tahu aturan, rambu, dan cara aman berkendara.
    > Begitu juga dengan literasi digital — kamu tahu cara aman, etis, dan cerdas berselancar di dunia maya.

    ### 4 Pilar Literasi Digital

    | Pilar | Penjelasan | Contoh |
    |-------|-----------|--------|
    | **Digital Skill** | Kemampuan teknis menggunakan perangkat | Mengoperasikan laptop, instal software |
    | **Digital Culture** | Berperilaku sesuai nilai-nilai bangsa | Tidak menyebar hoaks, sopan di medsos |
    | **Digital Ethics** | Etika berinteraksi di dunia digital | Mencantumkan sumber tulisan orang lain |
    | **Digital Safety** | Keamanan data dan privasi | Tidak sembarangan klik link, pakai password kuat |

    ### 🔍 Cek Pemahamanmu
    1. Seberapa sering kamu mengecek kebenaran berita sebelum menyebarkannya?
    2. Apa yang kamu lakukan jika menerima link mencurigakan di WhatsApp?
    3. Sebutkan 3 hal yang boleh dan 3 hal yang TIDAK boleh dilakukan di media sosial!

    ### 📋 Studi Kasus
    **Bencana Hoaks di Grup Keluarga**

    Rina, siswi SMA kelas XII, mendapat pesan berantai di WhatsApp yang mengatakan bahwa vaksin COVID-19 menyebabkan kematian. Pesan itu diteruskan oleh tantenya di grup keluarga. Rina ingat pelajaran literasi digital — ia mengecek kebenaran berita di situs resmi Kemenkes dan menemukan bahwa berita itu hoaks. Rina menjelaskan ke grup keluarganya dengan sopan dan membagikan link sumber resmi.

    *Pertanyaan:*
    1. Pilar literasi digital apa yang diterapkan Rina? Jelaskan!
    2. Apa yang akan terjadi jika Rina tidak memiliki literasi digital yang baik?

    ### 📌 Contoh Nyata
    Di Indonesia, tingkat literasi digital masih perlu ditingkatkan. Banyak kasus penipuan online, penyebaran hoaks, dan cyberbullying terjadi karena rendahnya literasi digital. Dengan menguasai 4 pilar ini, kamu bisa menjadi **warga digital yang cerdas dan bertanggung jawab**!
    """)


def content_revolusi_industri():
    return dedent("""
    ### 🏭 Revolusi Industri 4.0
    Revolusi Industri adalah perubahan besar dalam cara manusia memproduksi barang dan menjalankan kehidupan.

    ```
        Revolusi Industri 1.0  2.0        3.0          4.0
         (akhir 1700-an)  (1900)    (1970)      (2011-sekarang)
             |              |          |              |
             v              v          v              v
        Mesin Uap     Listrik &    Komputer &   IoT, AI, Big Data,
                       Produksi     Automatisasi  Cloud, Cyber
                       Massal                    Physical Systems
    ```

    ### 💡 Ciri-Ciri Revolusi 4.0
    1. **Digital** — Semua serba digital dan terhubung internet
    2. **Otomatis** — Mesin bisa bekerja tanpa campur tangan manusia
    3. **Real-time** — Data bisa diakses kapan saja, di mana saja
    4. **Terintegrasi** — Sistem saling terhubung satu sama lain

    ### 🎯 Dampak dalam Kehidupan

    | Bidang | Contoh |
    |--------|--------|
    | Pendidikan | Belajar online, kelas virtual, e-book |
    | Kesehatan | Telemedicine, rekam medis digital |
    | Transportasi | Gojek, Grab, peta digital (Google Maps) |
    | Ekonomi | E-commerce (Shopee, Tokopedia), fintech |
    | Manufaktur | Robot pabrik, 3D printing |

    > 🔑 **Pesan Penting:** Revolusi 4.0 bukan tentang mesin menggantikan manusia,
    > tapi tentang **manusia yang melek teknologi** akan lebih unggul dibanding yang tidak.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 ciri utama Revolusi Industri 4.0!
    2. Apa perbedaan utama Revolusi 3.0 dan 4.0?
    3. Bagaimana Revolusi 4.0 mempengaruhi dunia pendidikan?

    ### 📋 Studi Kasus
    **Gojek: Super App Buatan Anak Bangsa**

    Gojek adalah contoh nyata bagaimana teknologi 4.0 mengubah industri transportasi di Indonesia. Dulu, kita harus menunggu angkutan umum di pinggir jalan. Sekarang, dengan Gojek, kita bisa memesan kendaraan lewat smartphone, melihat lokasi driver secara real-time, dan membayar tanpa uang tunai. Gojek juga mengintegrasikan GoFood, GoSend, dan GoPay dalam satu aplikasi.

    *Pertanyaan:*
    1. Aspek Revolusi 4.0 apa saja yang diterapkan Gojek? (digital, real-time, otomatis, terintegrasi)
    2. Bagaimana kehidupan masyarakat sebelum dan sesudah adanya Gojek?
    """)


def content_iot():
    return dedent("""
    ### 📡 Internet of Things (IoT)
    IoT = **Internet of Things** = **Internet untuk Segala Benda**.

    > 🧩 **Analogi:** Bayangkan kamu punya asisten pribadi yang bisa mengontrol semua barang di rumahmu lewat smartphone. Mau lampu mati? Tinggal sentuh layar. Mau AC nyala sebelum pulang? Bisa diatur dari kantor. Mau pintu terkunci otomatis saat kamu lupa? Semua bisa! **Itulah IoT.**

    ### Cara Kerja IoT
    ```
      [SENSOR]  →  [PROSESOR]  →  [INTERNET]  →  [APLIKASI]
      (mendeteksi    (mengolah       (mengirim       (menampilkan
       suhu, gerak,   data)           data ke           data &
       cahaya...)                     cloud/           memberi
                                       server)         perintah)
    ```

    ### Contoh IoT dalam Kehidupan
    1. **🏠 Smart Home** — Lampu pintar (Philips Hue), kulkas yang kasih tahu stok makanan
    2. **⌚ Wearable** — Smartwatch yang menghitung langkah, detak jantung
    3. **🚗 Smart Car** — Mobil yang bisa parkir sendiri, GPS real-time
    4. **🌾 Smart Farming** — Sensor tanah yang otomatis menyiram tanaman
    5. **🏭 Smart Factory** — Mesin pabrik yang saling terhubung dan otomatis

    ### 🔍 Cek Pemahaman
    1. Apa yang dimaksud dengan Internet of Things (IoT)?
    2. Sebutkan 3 benda IoT yang ada di rumah atau sekolahmu!
    3. Jelaskan alur kerja IoT mulai dari sensor hingga aplikasi!

    ### 📋 Studi Kasus
    **Rumah Pintar ala Siswa SMA**

    Andi membuat proyek IoT sederhana: lampu kamarnya bisa menyala otomatis saat ia pulang sekolah. Ia menggunakan sensor PIR (gerakan), Arduino Uno, dan modul WiFi ESP01. Saat sensor mendeteksi gerakan di pintu kamar, Arduino mengirim sinyal ke relay untuk menyalakan lampu. Andi juga bisa mengontrol lampu dari smartphone-nya.

    *Pertanyaan:*
    1. Identifikasi sensor, prosesor, dan aktuator dalam sistem IoT Andi!
    2. Apa keuntungan sistem seperti ini dibanding saklar lampu biasa?
    """)


def content_big_data():
    return dedent("""
    ### 📊 Big Data: Data Raksasa
    Big Data adalah **kumpulan data berukuran sangat besar** yang tidak bisa diolah dengan cara biasa. Bukan cuma soal ukuran, tapi juga **kecepatan** dan **variasi** data.

    > 🧩 **Analogi:** Big Data itu seperti samudra luas. Kalau kamu punya ember kecil (komputer biasa), kamu tidak bisa mengangkut seluruh air samudra. Kamu butuh kapal raksasa (teknologi Big Data) untuk mengelolanya.

    ### 3V Big Data
    ```
             ╔══════════════════════════════╗
             ║         BIG DATA            ║
             ╠══════════════════════════════╣
             ║ 1. VOLUME  — Ukuran raksasa  ║
             ║    (terabyte - petabyte)      ║
             ║                              ║
             ║ 2. VELOCITY — Kecepatan tinggi║
             ║    (data real-time)           ║
             ║                              ║
             ║ 3. VARIETY  — Ragam jenis     ║
             ║    (teks, gambar, video...)   ║
             ╚══════════════════════════════╝
    ```

    ### Contoh Big Data
    - **Google** memproses 3,5 miliar pencarian per hari
    - **YouTube** upload 500 jam video setiap menit
    - **Gojek** memproses jutaan transaksi per hari
    - **BPJS Kesehatan** mengelola data 200+ juta peserta

    ### 🔍 Cek Pemahaman
    1. Apa yang dimaksud dengan 3V dalam Big Data? Jelaskan masing-masing!
    2. Berapa jam video yang di-upload ke YouTube setiap menit?
    3. Mengapa Big Data penting untuk perusahaan seperti Gojek atau Shopee?

    ### 📋 Studi Kasus
    **Rekomendasi Video TikTok**

    Setiap hari, TikTok memproses miliaran data interaksi pengguna: video apa yang kamu tonton sampai habis, berapa lama kamu berhenti di suatu video, komentar apa yang kamu ketik, bahkan berapa kali kamu menonton ulang. Data raksasa ini diolah menggunakan Big Data analytics untuk memberikan rekomendasi video yang sesuai dengan seleramu.

    *Pertanyaan:*
    1. Termasuk V yang mana data "berapa lama kamu berhenti di suatu video"? Jelaskan!
    2. Apa dampak positif dan negatif dari sistem rekomendasi berbasis Big Data?
    """)


def content_ai():
    return dedent("""
    ### 🤖 Artificial Intelligence (AI) / Kecerdasan Buatan
    AI adalah **kemampuan mesin untuk meniru kecerdasan manusia** — belajar, berpikir, mengambil keputusan.

    > 🧩 **Analogi:** AI itu seperti anak kecil yang belajar. Makin sering belajar, makin pintar. Bedanya, AI bisa belajar dari **jutaan data dalam hitungan detik**!

    ### Level AI
    ```
      Level 1: AI Sempit (ANI)  →  Satu tugas spesifik (Siri, ChatGPT, Google Maps)
      Level 2: AI Umum (AGI)    →  Sepintar manusia (masih dalam riset)
      Level 3: Super AI (ASI)   →  Melebihi manusia (masih fiksi ilmiah)
    ```

    ### Contoh AI yang Kamu Pakai Setiap Hari
    | Layanan | AI-nya | Fungsinya |
    |---------|--------|-----------|
    | ChatGPT/Gemini | NLP | Menjawab pertanyaan, menulis teks |
    | Google Maps | Machine Learning | Memprediksi kemacetan, rute tercepat |
    | YouTube/TikTok | Recommendation Engine | Rekomendasi video yang kamu suka |
    | Face ID iPhone | Computer Vision | Mengenali wajahmu |
    | Spotify | Recommendation System | Playlist lagu favoritmu |

    ### ⚠️ Tantangan AI
    1. **Pekerjaan** — Beberapa pekerjaan bisa digantikan AI
    2. **Privasi** — AI butuh data pribadi yang bisa disalahgunakan
    3. **Keputusan** — Kalau AI salah, siapa yang bertanggungjawab?
    4. **Kesenjangan** — Negara maju vs berkembang: siapa yang lebih diuntungkan?

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 level AI dan jelaskan perbedaannya!
    2. Berikan 3 contoh AI yang kamu gunakan dalam kehidupan sehari-hari!
    3. Apa tantangan terbesar pengembangan AI menurutmu?

    ### 📋 Studi Kasus
    **ChatGPT Ngerjain PR Matematika**

    Dini, siswi SMA, menggunakan ChatGPT untuk mengerjakan PR matematikanya. Ia tinggal memotret soal dan meminta ChatGPT menjawab. Hasilnya benar semua. Gurunya curiga karena jawaban Dini sempurna tapi saat ditanya cara mengerjakannya, Dini tidak bisa menjelaskan.

    *Pertanyaan:*
    1. Apakah yang dilakukan Dini termasuk pelanggaran etika? Mengapa?
    2. Bagaimana seharusnya AI seperti ChatGPT digunakan dalam pendidikan?
    """)


def content_cloud():
    return dedent("""
    ### ☁️ Cloud Computing
    Cloud Computing = komputasi awan = menggunakan sumber daya komputasi (server, penyimpanan, aplikasi) melalui **internet**, bukan dari komputer kita langsung.

    > 🧩 **Analogi:** Cloud Computing itu seperti listrik PLN. Kamu tidak perlu punya generator listrik sendiri di rumah. Tinggal colok, bayar, dan pakai. Kalau perlu lebih, tinggal upgrade. Sama seperti cloud — kamu **sewa**, bukan **beli**.

    ### Model Layanan Cloud
    ```
       ┌─────────────────────────────────────┐
       │         Software as a Service       │ ← Pakai langsung (Google Drive, Canva)
       │              (SaaS)                 │
       ├─────────────────────────────────────┤
       │         Platform as a Service       │ ← Buat aplikasi tanpa ribet server
       │              (PaaS)                 │
       ├─────────────────────────────────────┤
       │         Infrastructure as a Service │ ← Sewa server, storage, jaringan
       │              (IaaS)                 │
       └─────────────────────────────────────┘
    ```

    ### Contoh Cloud yang Kamu Pakai
    | Layanan | Jenis | Fungsi |
    |---------|-------|--------|
    | Google Drive, Dropbox | SaaS | Simpan file online |
    | Google Docs, Canva | SaaS | Buat dokumen, desain online |
    | Netflix, Spotify | SaaS | Streaming film, musik |
    | Google Cloud, AWS | IaaS/PaaS | Hosting aplikasi, website |

    ### 🔍 Cek Pemahaman
    1. Apa bedanya menyimpan file di **flashdisk** vs di **cloud**?
    2. Sebutkan **2 kelebihan** dan **2 kekurangan** cloud computing!
    3. Pernahkah kamu kehilangan data karena hape rusak? Apa yang akan berbeda kalau datamu tersimpan di cloud?

    ### 📋 Studi Kasus
    **Google Drive untuk Tugas Kelompok**

    Kelas XII IPA 1 mendapat tugas proyek lintas bidang. Budi, ketua kelompok, membuat folder Google Drive bersama dan membagikan link ke anggota tim. Masing-masing anggota bisa meng-upload file, mengedit dokumen secara bersamaan, dan memberikan komentar. Ketika laptop Sinta rusak, ia tetap bisa mengerjakan bagiannya dari komputer sekolah karena semua file tersimpan di cloud.

    *Pertanyaan:*
    1. Model layanan cloud apa yang digunakan dalam kasus ini? (SaaS/PaaS/IaaS)
    2. Sebutkan 3 keuntungan menggunakan cloud untuk tugas kelompok dibanding menyimpan file di flashdisk!
    """)


def content_sbc():
    return dedent("""
    ### 🖥️ SBC vs Mikrokontroler
    **SBC (Single Board Computer)** dan **Mikrokontroler** adalah dua jenis perangkat yang sering tertukar. Mari bedakan!

    ```
       ┌───────────────────────┬──────────────────────────┐
       │   SBC (Computer)      │   Mikrokontroler         │
       │                       │                          │
       │  • Seperti komputer    │  • Seperti otak alat     │
       │    mini                │    elektronik            │
       │  • Bisa pakai OS      │  • Tidak pakai OS        │
       │  • Contoh: Raspberry  │  • Contoh: Arduino       │
       │    Pi, Orange Pi      │    ESP32, STM32          │
       │  • Untuk tugas berat  │  • Untuk tugas spesifik  │
       └───────────────────────┴──────────────────────────┘
    ```

    | Aspek | SBC (Raspberry Pi) | Mikrokontroler (Arduino) |
    |-------|-------------------|------------------------|
    | **OS** | Bisa Linux/Windows IoT | Tidak ada OS, program langsung jalan |
    | **Konektivitas** | WiFi, Bluetooth, USB, HDMI | GPIO, I2C, SPI, Serial |
    | **Konsumsi Daya** | 5-15 watt | 0.1-0.5 watt |
    | **Kecepatan** | 1-2 GHz | 16-240 MHz |
    | **Cocok untuk** | Server mini, media center, IoT hub | Sensor, robot, kontrol otomatis |

    > 💡 **Intinya:** SBC itu seperti laptop mini, mikrokontroler itu seperti otak yang khusus untuk satu tugas spesifik (misal: nyalakan LED kalau suhu panas).

    ### 🔍 Cek Pemahaman
    1. Apa perbedaan utama SBC dan mikrokontroler dalam hal sistem operasi?
    2. Mana yang lebih cocok untuk membuat server mini? Mengapa?
    3. Mana yang lebih hemat daya? SBC atau mikrokontroler?

    ### 📋 Studi Kasus
    **Raspberry Pi untuk Absensi Sekolah**

    SMA Nusantara ingin membuat sistem absensi digital. Tim IT sekolah mempertimbangkan dua opsi: menggunakan Raspberry Pi (SBC) atau Arduino (mikrokontroler). Sistem absensi perlu: kamera untuk foto siswa, database untuk menyimpan data, dan layar monitor untuk menampilkan informasi.

    *Pertanyaan:*
    1. Manakah yang lebih tepat untuk proyek ini, SBC atau mikrokontroler? Mengapa?
    2. Sebutkan komponen SBC yang dibutuhkan untuk menjalankan sistem ini!
    """)


def content_arduino():
    return dedent("""
    ### 🔌 Kenalan dengan Arduino
    Arduino adalah **platform prototyping elektronik open-source** yang berbasis mikrokontroler. Dibuat di Italia, namanya diambil dari Bar di Ivrea.

    > 🧩 **Analogi:** Arduino itu seperti papan sirkuit ajaib. Kamu tinggal colokkan sensor, lampu LED, motor, lalu beri perintah lewat kode program, dan Arduino akan menjalankannya. Ini cara termudah belajar elektronika & coding!

    ### Kenapa Arduino?
    1. ✅ **Murah** — Mulai Rp70.000-an
    2. ✅ **Mudah** — Bahasa C yang disederhanakan
    3. ✅ **Komunitas besar** — Tutorial melimpah di internet
    4. ✅ **Open-source** — Skema dan software bebas dimodifikasi
    5. ✅ **Banyak sensor** — Ribuan sensor kompatibel

    ### Jenis Arduino
    | Model | Prosesor | GPIO | Cocok untuk |
    |-------|----------|------|-------------|
    | **Uno** | ATmega328P | 14 pin | Pemula, proyek dasar |
    | **Nano** | ATmega328P | 14 pin | Proyek kecil, portable |
    | **Mega** | ATmega2560 | 54 pin | Proyek besar, banyak sensor |
    | **ESP32** | Dual-core | 25 pin | IoT + WiFi + Bluetooth |

    ### 🔍 Cek Pemahaman
    1. Mengapa Arduino cocok untuk pemula yang belajar elektronika?
    2. Sebutkan 3 jenis Arduino dan kegunaannya!
    3. Apa kepanjangan dari ESP32 dan apa kelebihannya dibanding Arduino Uno?

    ### 📋 Studi Kasus
    **Proyek Lampu Otomatis untuk Kamar Kos**

    Dimas, mahasiswa rantau, ingin membuat lampu kamar kosnya menyala otomatis saat gelap. Ia memilih Arduino Uno karena murah (Rp75.000) dan mudah diprogram. Ia membeli sensor LDR (cahaya) dan modul relay. Dalam semalam, Dimas berhasil membuat prototipe lampu otomatis pertamanya berkat tutorial dari komunitas Arduino di YouTube.

    *Pertanyaan:*
    1. Mengapa Dimas memilih Arduino Uno dan bukan Raspberry Pi?
    2. Komponen apa saja yang digunakan Dimas dan apa fungsi masing-masing?
    """)


def content_ide():
    return dedent("""
    ### ⚙️ Instalasi IDE Arduino
    IDE (Integrated Development Environment) Arduino adalah software untuk menulis, meng-compile, dan mengupload program ke papan Arduino.

    ### Langkah Instalasi (Linux)
    ```bash
    # 1. Download dari https://www.arduino.cc/en/software
    # 2. Ekstrak file tar.gz
    tar -xvf arduino-*.tar.xz
    # 3. Jalankan installer
    cd arduino-*
    ./install.sh
    # 4. Beri akses port serial
    sudo usermod -a -G dialout $USER
    # 5. Instal selesai! Jalankan Arduino IDE
    arduino
    ```

    ### Tampilan Arduino IDE
    ```
      ┌─────────────────────────────────────────┐
      │  sketch_oct01a | Arduino IDE 2.x       │
      ├─────────────────────────────────────────┤
      │ [File] [Edit] [Sketch] [Tools] [Help]  │
      ├─────────────────────────────────────────┤
      │ 1  void setup() {                       │
      │ 2    pinMode(13, OUTPUT);               │ ← Area menulis kode
      │ 3  }                                     │   (Editor)
      │ 4                                        │
      │ 5  void loop() {                         │
      │ 6    digitalWrite(13, HIGH);             │
      │ 7    delay(1000);                        │
      │ 8    digitalWrite(13, LOW);              │
      │ 9    delay(1000);                        │
      │ 10 }                                     │
      ├─────────────────────────────────────────┤
      │ ✅ Compilation complete.                │
      └─────────────────────────────────────────┘
    ```

    ### ✍️ Program Pertamamu: BLINK!
    ```cpp
    void setup() {
      pinMode(13, OUTPUT);  // Set pin 13 sebagai OUTPUT
    }
    void loop() {
      digitalWrite(13, HIGH);  // Nyalakan LED
      delay(1000);              // Tunggu 1 detik
      digitalWrite(13, LOW);   // Matikan LED
      delay(1000);              // Tunggu 1 detik
    }
    ```

    > 🔑 **Struktur Dasar:** setiap program Arduino punya **setup()** (dijalankan sekali) dan **loop()** (dijalankan terus-menerus).

    ### 🔍 Cek Pemahaman
    1. Apa kepanjangan dari IDE?
    2. Sebutkan fungsi dari `setup()` dan `loop()` dalam program Arduino!
    3. Apa fungsi `pinMode(13, OUTPUT)` dan `digitalWrite(13, HIGH)`?

    ### 📋 Studi Kasus
    **Gagal Upload Program Pertama**

    Rani baru pertama kali menggunakan Arduino IDE. Ia sudah menulis kode LED blink, tapi saat mencoba upload, muncul error "port not found". Ternyata ia lupa memberi akses port serial dengan perintah `sudo usermod -a -G dialout $USER`. Setelah restart komputer dan menjalankan perintah tersebut, program berhasil di-upload.

    *Pertanyaan:*
    1. Apa penyebab error yang dialami Rani?
    2. Langkah apa yang harus dilakukan setelah memberi akses port serial?
    """)


def content_komponen():
    return dedent("""
    ### 🧩 Komponen Penunjang Arduino
    Arduino tidak bekerja sendiri. Dia butuh teman-teman berikut:

    ### 1. Sensor — Alat yang mendeteksi perubahan lingkungan
    | Sensor | Mendeteksi | Contoh Penggunaan |
    |--------|------------|-------------------|
    | **LM35/DHT11** | Suhu & kelembaban | Termometer digital |
    | **LDR** | Cahaya | Lampu otomatis |
    | **HC-SR04** | Jarak (ultrasonik) | Parking sensor mobil |
    | **PIR** | Gerakan manusia | Lampu otomatis saat ada orang |
    | **MQ-series** | Gas (asap, LPG) | Detektor kebocoran gas |

    ### 2. Aktuator — Alat yang melakukan aksi fisik
    - **LED** — Lampu indikator
    - **Motor DC** — Memutar roda/mekanik
    - **Servo** — Menggerakkan lengan robot
    - **Buzzer** — Menghasilkan bunyi
    - **LCD 16x2** — Menampilkan teks

    ### 3. Komponen Pendukung
    - **Breadboard** — Papan tempat merangkai tanpa solder
    - **Kabel Jumper** — Kabel penghubung (male-male, male-female, female-female)
    - **Resistor** — Menahan arus (biasanya 220 Ohm untuk LED)
    - **Power Supply** — Sumber listrik (USB 5V atau baterai 9V)

    > 🧩 **Analogi:** Sensor itu seperti **indera** (mata, telinga, hidung manusia), aktuator itu seperti **otot** (tangan, kaki), dan Arduino adalah **otak**-nya.

    ### 🔍 Cek Pemahaman
    1. Apa perbedaan fungsi sensor dan aktuator?
    2. Sebutkan 3 contoh sensor dan apa yang dideteksinya!
    3. Apa fungsi breadboard dalam merangkai komponen Arduino?

    ### 📋 Studi Kasus
    **Membuat Alarm Kebakaran Sederhana**

    Siswa kelas XII ingin membuat alarm kebakaran untuk laboratorium komputer. Mereka menggunakan sensor MQ-2 (pendeteksi asap), buzzer sebagai aktuator, dan Arduino Uno. Saat sensor mendeteksi konsentrasi gas di atas ambang batas, buzzer akan berbunyi nyaring dan LED merah menyala.

    *Pertanyaan:*
    1. Identifikasi mana sensor dan mana aktuator dalam sistem ini!
    2. Komponen pendukung apa saja yang dibutuhkan untuk merangkai sistem ini?
    """)


def content_simulator():
    return dedent("""
    ### 🎮 Simulator Arduino
    Tidak punya Arduino fisik? **Tidak masalah!** Kamu bisa pakai simulator online GRATIS untuk belajar merangkai dan memprogram Arduino.

    ### 🏆 Rekomendasi Simulator
    | Simulator | Kelebihan | Link |
    |-----------|-----------|------|
    | **Wokwi** | Cepat, banyak komponen, integrasi GitHub | wokwi.com |
    | **Tinkercad** | Visual 3D, cocok pemula | tinkercad.com |
    | **SimulIDE** | Offline, ringan | simufor.com |

    ### Contoh di Wokwi
    ```
      ┌──────────────────────────────────────────────┐
      │  Wokwi Online Simulator  [Run] [Save]       │
      ├──────────────┬───────────────────────────────┤
      │              │                               │
      │  [ARDUINO]   │  void setup() {               │
      │   UNO        │    pinMode(2, OUTPUT);        │
      │              │  }                            │
      │  ┌─┐ ┌─┐    │  void loop() {                │
      │  │█│ │█│    │    digitalWrite(2, HIGH);     │
      │  └─┘ └─┘    │    delay(500);                │
      │  LED LED    │    digitalWrite(2, LOW);      │
      │              │    delay(500);                │
      │  [GND] [5V] │  }                             │
      ├──────────────┴───────────────────────────────┤
      │  ✅ LED menyala berkedip setiap 500ms        │
      └──────────────────────────────────────────────┘
    ```

    > 💡 **Tips:** Gunakan simulator untuk eksperimen! Kalau salah rangkai, tinggal undo — tidak ada komponen yang meledak 😄

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 simulator Arduino yang bisa digunakan!
    2. Apa kelebihan menggunakan simulator dibanding Arduino fisik?
    3. Mana yang lebih cocok untuk pemula, Wokwi atau Tinkercad? Mengapa?

    ### 📋 Studi Kasus
    **Belajar Arduino Tanpa Modal**

    Dika ingin belajar Arduino tapi tidak punya uang untuk membeli perangkat. Temannya menyarankan untuk menggunakan Wokwi (simulator online gratis). Dika bisa merangkai LED, menulis kode, dan melihat hasilnya langsung — semua dari browser laptop sekolah. Dalam seminggu, Dika sudah bisa membuat 5 proyek berbeda tanpa merogoh kocek sepeser pun.

    *Pertanyaan:*
    1. Apa keuntungan belajar Arduino dengan simulator menurut kasus Dika?
    2. Apakah ada kekurangan belajar hanya dengan simulator? Jelaskan!
    """)


def content_praktik_dasar():
    return dedent("""
    ### 🔦 Praktik: LED & Sensor Sederhana

    ### Praktik 1: LED Berkedip
    **Alat:** Arduino, LED, Resistor 220 Ohm, Kabel Jumper, Breadboard

    **Rangkaian:**
    ```
            Arduino UNO
        ┌──────────────────┐
        │                  │
        │  Pin 13 ──► LED(+)│
        │                  │        ┌──────┐
        │          LED(-)──┼────────┤220Ω  ├──► GND
        │                  │        └──────┘
        │  GND  ──────────┤
        └──────────────────┘
    ```

    **Program:**
    ```cpp
    void setup() {
      pinMode(13, OUTPUT);
    }
    void loop() {
      digitalWrite(13, HIGH);
      delay(1000);
      digitalWrite(13, LOW);
      delay(1000);
    }
    ```

    ### Praktik 2: Baca Sensor Suhu LM35
    **Alat:** Arduino, LM35, Breadboard, Kabel Jumper

    **Program:**
    ```cpp
    void setup() {
      Serial.begin(9600);  // Mulai komunikasi serial
    }
    void loop() {
      int nilai = analogRead(A0);
      float suhu = (nilai * 5.0 / 1024.0) * 100;
      Serial.print("Suhu: ");
      Serial.print(suhu);
      Serial.println(" °C");
      delay(1000);
    }
    ```

    > 🔑 **Catatan:** `analogRead()` membaca nilai 0-1023 dari pin analog. Kita konversi ke suhu dengan rumus: Suhu = (nilai x 5V / 1024) x 100

    ### 🔍 Cek Pemahaman
    1. Apa fungsi resistor 220 Ohm pada rangkaian LED?
    2. Rumus apa yang digunakan untuk mengkonversi nilai analog ke suhu?
    3. Apa perbedaan `digitalWrite()` dan `analogRead()`?

    ### 📋 Studi Kasus
    **Suhu Lab Komputer Terlalu Panas**

    Laboratorium komputer SMA Merdeka sering terasa panas karena 30 komputer menyala bersamaan. Tim informatika ingin memonitor suhu ruangan secara real-time. Mereka menggunakan Arduino + sensor LM35 untuk membaca suhu dan menampilkannya di Serial Monitor. Data suhu dicatat setiap 5 menit selama seminggu untuk mengetahui pola kenaikan suhu.

    *Pertanyaan:*
    1. Komponen apa saja yang dibutuhkan untuk proyek monitoring suhu ini?
    2. Bagaimana cara menghubungkan LM35 ke Arduino?
    """)


def content_proyek_mini():
    return dedent("""
    ### 🌡️ Proyek Mini: Sistem Monitoring Suhu

    **Tujuan:** Membuat alat yang bisa mengukur suhu ruangan dan menyalakan LED berbeda sesuai rentang suhu.

    **Alat & Bahan:** Arduino Uno, Sensor LM35/DHT11, LED (Hijau, Kuning, Merah), Resistor 220 Ohm (x3), Breadboard & Kabel Jumper

    **Cara Kerja:**
    ```
      Suhu < 28°C  →  LED HIJAU nyala (sejuk)
      28°C - 33°C  →  LED KUNING nyala (normal)
      Suhu > 33°C  →  LED MERAH nyala (panas!)
    ```

    **Program:**
    ```cpp
    int ledHijau = 9, ledKuning = 10, ledMerah = 11;
    void setup() {
      Serial.begin(9600);
      pinMode(ledHijau, OUTPUT);
      pinMode(ledKuning, OUTPUT);
      pinMode(ledMerah, OUTPUT);
    }
    void loop() {
      int nilai = analogRead(A0);
      float suhu = (nilai * 5.0 / 1024.0) * 100;
      Serial.print("Suhu: "); Serial.println(suhu);
      if (suhu < 28) {
        digitalWrite(ledHijau, HIGH);
        digitalWrite(ledKuning, LOW);
        digitalWrite(ledMerah, LOW);
      } else if (suhu <= 33) {
        digitalWrite(ledHijau, LOW);
        digitalWrite(ledKuning, HIGH);
        digitalWrite(ledMerah, LOW);
      } else {
        digitalWrite(ledHijau, LOW);
        digitalWrite(ledKuning, LOW);
        digitalWrite(ledMerah, HIGH);
      }
      delay(1000);
    }
    ```

    > 💡 **Kembangkan!** Tambahkan buzzer yang berbunyi kalau suhu > 35°C!

    ### 🔍 Cek Pemahaman
    1. Berapa rentang suhu untuk LED hijau, kuning, dan merah pada proyek ini?
    2. Apa yang terjadi jika suhu melebihi 33°C?
    3. Bagaimana cara menambahkan buzzer ke proyek ini?

    ### 📋 Studi Kasus
    **Greenhouse Anggrek Sekolah**

    SMA Tani Mandiri memiliki greenhouse anggrek yang membutuhkan suhu stabil 25-30°C. Siswa kelas XII membuat sistem monitoring suhu menggunakan Arduino dan sensor DHT11. Jika suhu di bawah 25°C, kipas pemanas menyala. Jika suhu di atas 30°C, kipas pendingin menyala. Semua data terekam di komputer selama 24 jam.

    *Pertanyaan:*
    1. Modifikasi apa yang perlu dilakukan dari proyek mini monitoring suhu biasa untuk kasus greenhouse ini?
    2. Mengapa penting menjaga suhu stabil untuk tanaman anggrek?
    """)


def content_mengapa_bk():
    return dedent("""
    ### 🧠 Mengapa Berpikir Komputasional?
    Berpikir Komputasional (BK) adalah **cara berpikir untuk memecahkan masalah** dengan menerapkan **konsep dan logika ilmu komputer**.

    > 🧩 **Analogi:** BK itu seperti resep masakan. Kalau kamu punya resep yang jelas, langkah demi langkah, siapa pun bisa memasak hidangan yang sama. BK memberi kita resep untuk memecahkan masalah!

    ### 4 Pilar Berpikir Komputasional
    ```
      ┌──────────────────────────────────────────────┐
      │        BERPIKIR KOMPUTASIONAL                │
      ├──────────────────┬───────────────────────────┤
      │  1. DEKOMPOSISI  │ Memecah masalah besar     │
      │                  │ menjadi bagian kecil      │
      ├──────────────────┼───────────────────────────┤
      │  2. PENGENALAN   │ Mencari pola/kesamaan     │
      │     POLA         │ dari masalah              │
      ├──────────────────┼───────────────────────────┤
      │  3. ABSTRAKSI    │ Fokus pada yang penting,  │
      │                  │ abaikan yang tidak perlu  │
      ├──────────────────┼───────────────────────────┤
      │  4. ALGORITMA    │ Membuat langkah-langkah   │
      │                  │ penyelesaian              │
      └──────────────────┴───────────────────────────┘
    ```

    ### Contoh Sehari-hari
    **Masalah:** Mau masak nasi goreng untuk 5 orang.
    1. **Dekomposisi:** Beli bahan -> siapkan bumbu -> masak -> sajikan
    2. **Pola:** Sama seperti masak mie goreng, cuma beda bahan
    3. **Abstraksi:** Ukuran wajan, warna panci tidak penting; yang penting api, bumbu, nasi
    4. **Algoritma:** Langkah 1: Panaskan minyak. 2: Tumis bumbu. 3: Masukkan nasi...

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 pilar berpikir komputasional!
    2. Terapkan 4 pilar BK untuk masalah "Bangun pagi dan berangkat sekolah"!
    3. Mengapa abstraksi penting dalam pemecahan masalah?

    ### 📋 Studi Kasus
    **Memecahkan Masalah Parkir Sekolah**

    Setiap pagi, terjadi kemacetan di pintu gerbang SMA Harapan karena banyak mobil dan motor parkir sembarangan. OSIS diminta membantu mencari solusi. Mereka menggunakan berpikir komputasional:
    - **Dekomposisi:** masalah parkir → jumlah kendaraan, luas lahan, jadwal kedatangan
    - **Pola:** kendaraan datang paling banyak pukul 06.30-07.00
    - **Abstraksi:** fokus pada pengaturan alur masuk, bukan pada warna kendaraan
    - **Algoritma:** buat sistem parkir bergilir per kelas

    *Pertanyaan:*
    1. Jelaskan bagaimana setiap pilar BK diterapkan dalam kasus ini!
    2. Usulkan solusi algoritma yang lebih detail untuk masalah parkir sekolah!
    """)


def content_dasar_c():
    return dedent("""
    ### 💻 Dasar Pemrograman C untuk Arduino
    Bahasa C adalah **bahasa pemrograman level menengah** yang cepat, efisien, dan sangat cocok untuk Arduino.

    > 🧩 **Analogi:** Bahasa C itu seperti bahasa isyarat untuk Arduino. Kamu memberi instruksi dengan kode-kode tertentu, dan Arduino menjalankannya tanpa bertanya lagi.

    ### Struktur Program Arduino
    ```cpp
    void setup() {
      // Kode di sini jalan SEKALI saat Arduino dinyalakan
      pinMode(13, OUTPUT);  // Set pin 13 sebagai output
    }
    void loop() {
      // Kode di sini jalan TERUS-MENERUS
      digitalWrite(13, HIGH);
      delay(1000);
      digitalWrite(13, LOW);
      delay(1000);
    }
    ```

    ### Penjelasan
    | Bagian | Fungsi | Analogi |
    |--------|--------|---------|
    | `void setup()` | Persiapan awal (1x) | Seperti menyiapkan meja sebelum masak |
    | `void loop()` | Program utama (berulang) | Seperti kegiatan rutin harian |
    | `pinMode(pin, mode)` | Set fungsi pin | Menentukan mana saklar, mana lampu |
    | `digitalWrite(pin, value)` | Output ON/OFF | Menyalakan/mematikan saklar |
    | `delay(ms)` | Jeda waktu | Berhenti sejenak (1000 = 1 detik) |

    ### 🔍 Cek Pemahaman
    1. Sebutkan 2 fungsi utama dalam setiap program Arduino!
    2. Apa perbedaan `setup()` dan `loop()`?
    3. Fungsi apa yang digunakan untuk memberikan jeda 2 detik?

    ### 📋 Studi Kasus
    **Lampu Kedip Morse**

    Daffa ingin membuat lampu LED mengirim pesan SOS dalam kode Morse menggunakan Arduino (S = tiga kedip pendek, O = tiga kedip panjang). Ia menggunakan kombinasi `digitalWrite` dan `delay` dengan durasi berbeda. Kode SOS sudah ditentukan: pendek 200ms, panjang 600ms.

    *Pertanyaan:*
    1. Tulis kode Arduino untuk menghasilkan 1 kali kedip pendek (200ms)!
    2. Bagaimana cara membuat urutan SOS (3 pendek, 3 panjang, 3 pendek)?
    """)


def content_struktur_c():
    return dedent("""
    ### 📋 Struktur Dasar Program C

    ### 1. Variabel — Tempat Menyimpan Data
    ```cpp
    int umur = 17;           // Bilangan bulat
    float suhu = 28.5;       // Bilangan desimal
    char inisial = 'D';      // Satu karakter
    boolean menyala = true;  // true/false
    String nama = "Dani";    // Teks
    ```

    ### 2. Tipe Data
    | Tipe | Ukuran | Simpan | Contoh |
    |------|--------|--------|--------|
    | `byte` | 1 byte | 0 - 255 | `byte nilai = 100;` |
    | `int` | 2 byte | -32.768 - 32.767 | `int jumlah = 500;` |
    | `long` | 4 byte | -2M - 2M | `long waktu = 60000;` |
    | `float` | 4 byte | Desimal | `float pi = 3.14;` |
    | `boolean` | 1 bit | true/false | `boolean ok = true;` |

    ### 3. Operator Dasar
    ```cpp
    int a = 10, b = 3;
    int hasil = a + b;    // 13  (penjumlahan)
    hasil = a - b;         // 7   (pengurangan)
    hasil = a * b;         // 30  (perkalian)
    hasil = a / b;         // 3   (pembagian BULAT)
    hasil = a % b;         // 1   (sisa bagi / modulo)
    boolean cek = (a > b);  // true
    ```

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 tipe data dalam C dan contohnya!
    2. Apa yang dimaksud dengan operator modulo (`%`)? Berikan contoh!
    3. Berapa nilai dari `10 / 3` dalam pembagian bilangan bulat (int)?

    ### 📋 Studi Kasus
    **Kalkulator Nilai Rata-rata**

    Anita ingin membuat program Arduino yang menghitung rata-rata dari 3 nilai ulangannya: 85, 92, dan 78. Ia menggunakan variabel `int` untuk menyimpan nilai, lalu menjumlahkannya dan membagi dengan 3. Namun hasilnya selalu bilangan bulat, padahal nilai aslinya mengandung koma.

    *Pertanyaan:*
    1. Tipe data apa yang seharusnya digunakan Anita agar hasil rata-rata akurat?
    2. Tulis kode C yang benar untuk menghitung rata-rata 85, 92, dan 78!
    """)


def content_kontrol():
    return dedent("""
    ### 🔀 Percabangan & Perulangan

    ### A. Percabangan: if / else if / else
    Digunakan kalau ada kondisi (pilihan).
    ```cpp
    int nilai = 85;
    if (nilai >= 90) {
      Serial.println("A — Istimewa!");
    } else if (nilai >= 78) {
      Serial.println("B — Baik!");
    } else if (nilai >= 65) {
      Serial.println("C — Cukup");
    } else {
      Serial.println("D — Remedial");
    }
    ```

    ### B. Perulangan: for & while
    **for** — dipakai kalau sudah tahu berapa kali ulang:
    ```cpp
    for (int i = 0; i < 5; i++) {
      Serial.print("Halo ke-");
      Serial.println(i);
      delay(500);
    }
    ```

    **while** — dipakai kalau tidak tahu kapan berhenti:
    ```cpp
    while (digitalRead(2) == HIGH) {
      digitalWrite(13, HIGH);
    }
    ```

    > 🧩 **Analogi:** `for` itu seperti daftar belanja — kamu tahu ada 5 barang yang harus dibeli. `while` itu seperti mengaduk mie sampai matang — kamu tidak tahu berapa kali harus aduk, yang penting sampai matang!

    ### 🔍 Cek Pemahaman
    1. Kapan sebaiknya menggunakan `if` dibanding `else if`?
    2. Kapan menggunakan `for` dan kapan menggunakan `while`?
    3. Buat kode `for` untuk mencetak angka 1 sampai 10!

    ### 📋 Studi Kasus
    **Sistem Penyiraman Tanaman Otomatis**

    Sinta membuat penyiram tanaman otomatis dengan Arduino. Sensor kelembaban tanah membaca nilai: jika < 300 (kering), pompa air menyala. Jika >= 300 (basah), pompa mati. Setelah menyiram, program menunggu 5 detik sebelum membaca sensor lagi (menggunakan `while` untuk menunggu).

    *Pertanyaan:*
    1. Struktur percabangan apa yang tepat untuk logika di atas? Tulis kodenya!
    2. Mengapa perlu jeda 5 detik setelah menyiram?
    """)


def content_array():
    return dedent("""
    ### 📦 Array: Kumpulan Data
    Array adalah **variabel yang bisa menyimpan banyak data sekaligus**, dengan tipe yang sama.

    > 🧩 **Analogi:** Array itu seperti rak sepatu. Satu rak bisa menyimpan banyak sepatu, dan setiap sepatu punya nomor rak (indeks). **Indeks array mulai dari 0!**

    ### Deklarasi Array
    ```cpp
    int angka[] = {10, 20, 30, 40, 50};
    int suhu[7];  // Bisa simpan 7 suhu
    suhu[0] = 28;
    suhu[1] = 29;
    String namaHari[] = {"Senin", "Selasa", "Rabu"};
    ```

    ### Cara Kerja Array
    ```
            indeks:   0     1     2     3     4
                   ┌─────┬─────┬─────┬─────┬─────┐
            angka: │ 10  │ 20  │ 30  │ 40  │ 50  │
                   └─────┴─────┴─────┴─────┴─────┘
      int x = angka[0];    // x = 10
      angka[2] = 100;      // Ubah indeks 2 jadi 100
    ```

    ### Contoh: LED Berjalan (Cylon)
    ```cpp
    int ledPins[] = {2, 3, 4, 5, 6, 7};
    void setup() {
      for (int i = 0; i < 6; i++) pinMode(ledPins[i], OUTPUT);
    }
    void loop() {
      for (int i = 0; i < 6; i++) { digitalWrite(ledPins[i], HIGH); delay(200); digitalWrite(ledPins[i], LOW); }
      for (int i = 5; i >= 0; i--) { digitalWrite(ledPins[i], HIGH); delay(200); digitalWrite(ledPins[i], LOW); }
    }
    ```

    ### 🔍 Cek Pemahaman
    1. Apa itu array dan mengapa kita membutuhkannya?
    2. Dari indeks berapa array dimulai?
    3. Buat array untuk menyimpan 7 hari dalam seminggu!

    ### 📋 Studi Kasus
    **Lampu Hias 8 LED untuk Class Meeting**

    Class meeting akan datang! Dimas ingin membuat lampu hias dengan 8 LED yang menyala bergantian. Ia menggunakan array `int ledPins[] = {2,3,4,5,6,7,8,9}` dan perulangan `for` untuk menyalakan LED satu per satu. Pola yang diinginkan: LED menyala dari kiri ke kanan, lalu kanan ke kiri, berulang terus.

    *Pertanyaan:*
    1. Tulis kode perulangan `for` untuk menyalakan 8 LED dari kiri ke kanan!
    2. Bagaimana cara membuat efek "pantul" (kiri→kanan→kiri)?
    """)


def content_fungsi_library():
    return dedent("""
    ### 📚 Fungsi & Library Arduino

    ### A. Fungsi — Memecah Program Jadi Bagian Kecil
    Fungsi adalah blok kode yang bisa dipanggil berulang kali. Ini membuat program lebih rapi.

    > 🧩 **Analogi:** Fungsi itu seperti tombol di remote TV. Kamu tidak perlu tahu rangkaian elektronik di dalamnya. Tinggal tekan, dan TV ganti channel.

    ### Cara Membuat Fungsi
    ```cpp
    void nyalakanLED(int pin, int durasi) {
      digitalWrite(pin, HIGH);
      delay(durasi);
      digitalWrite(pin, LOW);
    }
    float konversiKeCelcius(int nilaiAnalog) {
      float volt = nilaiAnalog * 5.0 / 1024.0;
      return volt * 100;
    }
    void loop() {
      nyalakanLED(13, 1000);
      int baca = analogRead(A0);
      float suhu = konversiKeCelcius(baca);
      Serial.println(suhu);
    }
    ```

    ### B. Library Arduino
    Library adalah kumpulan fungsi siap pakai. Kamu tinggal pakai, tidak perlu buat dari nol.

    | Library | Fungsi | Contoh |
    |---------|--------|--------|
    | `LiquidCrystal` | Mengontrol LCD | Tampilkan teks di LCD |
    | `Servo` | Mengontrol motor servo | Gerakkan lengan robot |
    | `DHT` | Baca sensor suhu & kelembaban | DHT11/DHT22 |
    | `WiFi` (ESP32) | Koneksi WiFi | IoT, kirim data ke internet |

    ```cpp
    #include <Servo.h>
    Servo myservo;
    void setup() { myservo.attach(9); }
    void loop() {
      myservo.write(0); delay(1000);
      myservo.write(90); delay(1000);
      myservo.write(180); delay(1000);
    }
    ```

    > 💡 **Tips:** Cari library di **Library Manager** Arduino IDE: Sketch > Include Library > Manage Libraries

    ### 🔍 Cek Pemahaman
    1. Apa itu fungsi dalam pemrograman?
    2. Sebutkan 3 library Arduino dan fungsinya!
    3. Apa keuntungan menggunakan library dibanding menulis kode dari nol?

    ### 📋 Studi Kasus
    **Robot Arm Sederhana**

    Tim robotik SMA menggunakan servo motor untuk membuat lengan robot sederhana. Mereka menggunakan library `Servo.h` agar lebih mudah mengontrol servo. Tanpa library, mereka harus mengatur pulsa PWM secara manual — sangat rumit! Dengan `myservo.write(90)`, servo langsung bergerak ke posisi 90 derajat.

    *Pertanyaan:*
    1. Apa library yang digunakan dan mengapa?
    2. Tulis kode untuk menggerakkan servo dari 0° → 90° → 180° dengan jeda 1 detik!
    """)


def content_proyek_akhir():
    return dedent("""
    ### 🏗️ Proyek: Kontrol Otomatis

    **Tugas Akhir Bab 3:** Buatlah program Arduino yang menggabungkan semua konsep: variabel, percabangan, perulangan, array, fungsi, dan library!

    ### 💡 Ide Proyek (Pilih satu)
    1. **🌡️ Smart Fan** — Kipas otomatis menyala kalau suhu > 30°C
    2. **🚦 Lampu Lalu Lintas** — 3 LED hijau/kuning/merah dengan timer
    3. **💧 Penyiram Tanaman** — Siram otomatis kalau tanah kering
    4. **🚪 Sistem Keamanan** — Buzzer bunyi kalau ada gerakan (PIR sensor)

    ### Format Laporan
    | Bagian | Isi |
    |--------|----|
    | Judul | Nama proyek |
    | Tujuan | Masalah apa yang diselesaikan? |
    | Alat & Bahan | Komponen yang digunakan |
    | Rangkaian | Diagram/skema |
    | Kode Program | Dengan komentar |
    | Hasil | Video/foto/gambar |
    | Refleksi | Kesulitan & pembelajaran |

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 ide proyek yang bisa dipilih untuk tugas akhir Bab 3!
    2. Apa saja yang harus ada dalam laporan proyek?
    3. Mengapa refleksi penting dalam sebuah proyek?

    ### 📋 Studi Kasus
    **Smart Fan untuk Kamar Adik**

    Kakak beradik kelas XII membuat kipas otomatis yang menyala saat suhu > 30°C. Mereka menggunakan sensor DHT11, relay, dan kipas DC bekas komputer. Mereka menerapkan fungsi `bacaSuhu()` untuk membaca sensor, dan percabangan `if (suhu > 30)` untuk menyalakan kipas. Hasilnya: adik mereka tidak perlu bangun untuk menyalakan kipas saat malam panas.

    *Pertanyaan:*
    1. Identifikasi semua konsep Bab 3 yang digunakan dalam proyek ini!
    2. Perbaikan apa yang bisa ditambahkan untuk membuat proyek ini lebih baik?
    """)


def content_apa_jaringan():
    return dedent("""
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
    """)


def content_topologi():
    return dedent("""
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
    """)


def content_komponen_jaringan():
    return dedent("""
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
    """)


def content_tcpip():
    return dedent("""
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
    """)


def content_cyber():
    return dedent("""
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
    """)


def content_teknologi_masyarakat():
    return dedent("""
    ### 🌍 Peran Teknologi Digital dalam Masyarakat
    Teknologi digital telah mengubah cara manusia hidup, bekerja, berkomunikasi, dan belajar.

    > 🧩 **Analogi:** Teknologi digital itu seperti listrik — dulu orang pakai lilin, setelah listrik semuanya berubah. Sekarang teknologi digital melakukan hal yang sama.

    ### Dampak Positif
    | Bidang | Dulu | Sekarang |
    |--------|------|----------|
    | **Komunikasi** | Surat pos (1 minggu) | WhatsApp (1 detik) |
    | **Belanja** | Ke pasar, antre | Shopee/Tokped (klik, sampai rumah) |
    | **Belajar** | Buku cetak, tatap muka | YouTube, Zoom, Classroom |
    | **Hiburan** | TV (jadwal tetap) | Netflix, YouTube, TikTok |
    | **Transportasi** | Angkot, taksi manual | Gojek, Grab (tracking) |

    ### Dampak Negatif
    1. **Kecanduan** — Scroll TikTok berjam-jam
    2. **Hoaks** — Berita palsu menyebar lebih cepat
    3. **Cyberbullying** — Perundungan di dunia digital
    4. **Privasi** — Data pribadi bocor
    5. **Kesenjangan** — Yang tidak punya akses makin tertinggal

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 dampak positif teknologi digital dalam kehidupan!
    2. Sebutkan 3 dampak negatif yang perlu diwaspadai!
    3. Menurutmu, bagaimana cara mengatasi kesenjangan digital di Indonesia?

    ### 📋 Studi Kasus
    **UMKM Naik Kelas Berkat GoFood**

    Ibu Rahma punya usaha katering rumahan. Sebelumnya, ia hanya mengandalkan pelanggan dari tetangga (rata-rata 10 porsi/hari). Setelah daftar GoFood, dalam 3 bulan pelanggannya naik jadi 50 porsi/hari. Ia juga belajar dari YouTube cara foto makanan yang menarik dan mengelola keuangan digital.

    *Pertanyaan:*
    1. Dampak positif apa yang dialami Ibu Rahma dari teknologi digital?
    2. Tantangan apa yang mungkin muncul jika semua UMKM beralih ke digital?
    """)


def content_medsos():
    return dedent("""
    ### 📱 Media Sosial: Pisau Bermata Dua
    Media sosial adalah platform digital untuk berinteraksi, berbagi, dan berkomunikasi online. Contoh: Instagram, TikTok, YouTube, X (Twitter).

    > 🧩 **Analogi:** Media sosial itu seperti panggung raksasa. Semua orang bisa naik panggung, menunjukkan bakat, berbicara. Tapi di panggung yang sama, ada juga yang berteriak, melempar sampah, atau menyebar gosip. **Kamu yang memilih peranmu!**

    ### Dampak Positif
    ✅ Tempat belajar (tutorial, tips)
    ✅ Bisnis (jualan online, brand building)
    ✅ Networking (kenalan, relasi kerja)
    ✅ Kreativitas (konten kreatif)

    ### Dampak Negatif
    ❌ **FOMO** — takut ketinggalan tren
    ❌ **Cyberbullying** — body shaming, komentar jahat
    ❌ **Dopamine loop** — notifikasi bikin ketagihan
    ❌ **Echo chamber** — cuma lihat yang setuju -> makin ekstrem
    ❌ **Sleep deprivation** — begadang karena scroll

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 dampak positif dan 3 dampak negatif media sosial!
    2. Apa yang dimaksud dengan dopamine loop di media sosial?
    3. Berapa batas waktu ideal bermedia sosial per hari?

    ### 📋 Studi Kasus
    **Komentar Bodyshaming di TikTok**

    Seorang siswi SMA mengunggah video dance TikTok. Tiba-tiba ada komentar jahat tentang berat badannya. Komentar itu mendapat banyak likes dan balasan yang lebih parah. Korban jadi minder dan tidak mau sekolah. Teman-teman sekelasnya bingung harus bagaimana.

    *Pertanyaan:*
    1. Termasuk dampak negatif apa kasus di atas? (FOMO/Cyberbullying/Dopamine loop?)
    2. Apa yang sebaiknya dilakukan korban, teman-temannya, dan pihak sekolah?

    ### Tips Bijak Bermedsos
    ```
      ⏰  Batasi waktu: maks 2 jam/hari
      🔇  Matikan notifikasi tidak penting
      ✅  Follow akun yang menginspirasi
      🚫  Jangan sebarkan info yang belum pasti benar
    ```
    """)


def content_digital_pendidikan():
    return dedent("""
    ### 🎓 Teknologi Digital dalam Pendidikan
    Teknologi digital telah mengubah dunia pendidikan secara fundamental.

    ### Bentuk Digitalisasi Pendidikan
    | Teknologi | Fungsi | Contoh |
    |-----------|--------|--------|
    | **LMS** | Learning Management System | Google Classroom, Moodle |
    | **Video Conference** | Belajar jarak jauh | Zoom, Google Meet |
    | **E-book** | Buku digital | Buku Kemendikdasmen (.pdf) |
    | **AI Tutor** | Bantuan belajar pribadi | ChatGPT, Khan Academy AI |
    | **Lab Virtual** | Praktik tanpa alat fisik | Wokwi, Tinkercad, PhET |
    | **Gamifikasi** | Belajar lewat game | Quizizz, Kahoot |

    ### Keuntungan
    1. **Akses 24/7** — Belajar kapan saja, di mana saja
    2. **Personalized** — Materi bisa disesuaikan kemampuan
    3. **Kolaboratif** — Kerja proyek lintas sekolah
    4. **Multimedia** — Video, animasi lebih menarik

    ### Tantangan
    1. **Kesenjangan akses** — Tidak semua punya laptop/internet
    2. **Disrupsi fokus** — Godaan game saat belajar online
    3. **Kesiapan guru** — Tidak semua guru melek teknologi

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 bentuk digitalisasi pendidikan!
    2. Apa keuntungan LMS dibanding belajar tatap muka saja?
    3. Apa tantangan terbesar digitalisasi pendidikan di Indonesia?

    ### 📋 Studi Kasus
    **Belajar dari Rumah di Daerah 3T**

    SMP Nusantara di daerah terpencil kesulitan saat pandemi. Hanya 30% siswa punya smartphone, sinyal internet tidak stabil, dan listrik sering padam. Guru terpaksa menggunakan radio komunitas dan modul cetak untuk mengajar. Siswa yang punya HP mengirim tugas lewat WhatsApp ketika ada sinyal.

    *Pertanyaan:*
    1. Tantangan digitalisasi pendidikan apa yang tergambar dalam kasus ini?
    2. Solusi kreatif apa yang bisa diterapkan selain yang sudah dilakukan?
    """)


def content_ekonomi_digital():
    return dedent("""
    ### 💰 Ekonomi Digital: E-commerce & Fintech
    Ekonomi digital adalah kegiatan ekonomi berbasis teknologi digital. Dua pilar utamanya: **E-commerce** (jual-beli online) dan **Fintech** (teknologi finansial).

    > 🧩 **Analogi:** Ekonomi digital itu seperti pasar modern versi online. Kalau pasar tradisional: kamu datang, lihat barang, bayar cash, bawa pulang. Ekonomi digital: kamu buka hape, klik, transfer, barang diantar ke rumah.

    ### E-commerce di Indonesia
    | Platform | Jenis | Keunggulan |
    |----------|-------|-----------|
    | **Shopee** | Marketplace | Gratis ongkir, banyak voucher |
    | **Tokopedia** | Marketplace | Pembayaran via GoPay |
    | **Lazada** | Marketplace | Barang impor, flash sale |
    | **Bukalapak** | Marketplace | Fokus UMKM Indonesia |

    ### Fintech di Indonesia
    - **Pembayaran:** GoPay, OVO, DANA, ShopeePay
    - **Pinjaman:** Akulaku, Kredivo, Modalku
    - **Investasi:** Ajaib, Bibit, Stockbit
    - **Asuransi:** PasarPolis, Cermati

    ### Dampak
    ✅ **Positif:** UMKM bisa jual seluruh Indonesia, transaksi lebih cepat
    ❌ **Negatif:** Pinjaman online ilegal, konsumtif, penipuan toko palsu

    ### 🔍 Cek Pemahaman
    1. Apa perbedaan e-commerce dan fintech? Berikan contoh masing-masing!
    2. Sebutkan 3 platform fintech di Indonesia!
    3. Apa dampak negatif dari kemudahan pinjaman online?

    ### 📋 Studi Kasus
    **Pinjol Ilegal Menjerat Pelajar**

    Seorang siswa SMA tergiur iklan pinjaman online yang mudah cair. Ia pinjam Rp500.000 untuk beli sepatu. Ternyata bunganya sangat tinggi, dalam 2 minggu utangnya jadi Rp1.500.000. Debt collector meneror dia dan keluarganya. Siswa tersebut akhirnya curhat ke guru BK.

    *Pertanyaan:*
    1. Termasuk kategori fintech apa pinjaman online? (legal/ilegal?)
    2. Apa yang seharusnya dilakukan siswa sebelum meminjam online?
    """)


def content_uu_ite():
    return dedent("""
    ### ⚖️ UU ITE: Aturan Main di Dunia Digital
    UU ITE (Undang-Undang Informasi dan Transaksi Elektronik) adalah hukum yang mengatur aktivitas di dunia digital di Indonesia.

    > 🧩 **Analogi:** UU ITE itu seperti rambu-rambu lalu lintas untuk dunia digital. Sama seperti di jalan raya ada aturan, di dunia digital juga ada aturan yang harus dipatuhi.

    ### Dasar Hukum
    - **UU No. 11 Tahun 2008** tentang ITE (pertama)
    - **UU No. 19 Tahun 2016** (revisi pertama)
    - **UU No. 1 Tahun 2024** (revisi kedua — terbaru)

    ### Pasal-Pasal Penting
    | Pasal | Isi | Ancaman Hukuman |
    |-------|-----|----------------|
    | **Pasal 27 ayat 1** | Menyebarkan konten asusila | 6 tahun penjara |
    | **Pasal 27 ayat 3** | Pencemaran nama baik | 4 tahun penjara |
    | **Pasal 28 ayat 1** | Menyebarkan berita bohong | 6 tahun penjara |
    | **Pasal 28 ayat 2** | Ujaran kebencian SARA | 6 tahun penjara |
    | **Pasal 30** | Akses ilegal (hacking) | 7 tahun penjara |
    | **Pasal 45A** | Penghinaan terhadap pemerintah | 6 tahun penjara |

    ### Yang Harus Kamu Hindari
    ❌ **JANGAN:** Menghina orang di medsos, menyebar hoaks, membagikan foto orang tanpa izin

    ### 🔍 Cek Pemahaman
    1. Apa yang diatur dalam Pasal 27 ayat 3 UU ITE?
    2. Berapa ancaman hukuman untuk penyebaran berita bohong?
    3. Sebutkan 3 hal yang harus dihindari di media sosial menurut UU ITE!

    ### 📋 Studi Kasus
    **Status WA Berujung Laporan Polisi**

    Seorang siswa SMA membuat status WhatsApp yang berisi hinaan terhadap guru. Status itu di-screenshot dan disebar ke grup kelas. Guru yang bersangkutan melaporkan ke polisi dengan pasal pencemaran nama baik (UU ITE Pasal 27 ayat 3). Siswa tersebut terancam hukuman 4 tahun penjara.

    *Pertanyaan:*
    1. Apakah tindakan siswa tersebut melanggar UU ITE? Pasal berapa?
    2. Apa yang sebaiknya dilakukan jika tidak setuju dengan guru?
    """)


def content_apa_proyek():
    return dedent("""
    ### 🔧 Apa Itu Proyek Lintas Bidang?
    Proyek Lintas Bidang adalah **proyek yang mengintegrasikan berbagai disiplin ilmu** untuk menyelesaikan **masalah nyata** di lingkungan sekitar.

    > 🧩 **Analogi:** Proyek lintas bidang itu seperti membangun rumah. Tidak cukup cuma satu keahlian. Arsitek, tukang, teknisi listrik — semua harus bekerja sama. Begitu juga proyek ini — kamu akan menggunakan semua ilmu yang sudah dipelajari!

    ### Ilmu yang Diintegrasikan
    | Bab | Ilmu | Peran dalam Proyek |
    |-----|------|-------------------|
    | 1 | Literasi Digital, IoT, AI | Memilih teknologi yang tepat |
    | 2 | Sistem Komputer, Arduino | Hardware prototipe |
    | 3 | Pemrograman C | Coding prototipe |
    | 4 | Jaringan Komputer | Koneksi dan komunikasi data |
    | 5 | Dampak Sosial | Analisis dampak solusi |

    ### Contoh Topik Proyek
    1. 🌡️ Sistem Monitoring Suhu untuk greenhouse sekolah
    2. 🚪 Smart Door Lock dengan RFID untuk lab komputer
    3. 🗑️ Smart Trash Can yang otomatis terbuka
    4. 💧 Automatic Plant Watering untuk taman sekolah
    5. 🚦 Smart Parking untuk area parkir sekolah

    ### 🔍 Cek Pemahaman
    1. Apa yang dimaksud dengan proyek lintas bidang?
    2. Sebutkan ilmu dari bab apa saja yang diintegrasikan!
    3. Berikan 2 contoh topik proyek lintas bidang selain yang disebutkan!

    ### 📋 Studi Kasus
    **Proyek Tong Sampah Pintar**

    SMA Bumi Hijau memiliki masalah: tong sampah sering penuh dan bau karena tidak diangkut tepat waktu. Tim proyek lintas bidang kelas XII membuat solusi: Smart Trash Can yang otomatis memberi notifikasi ke petugas kebersihan saat tong sudah 80% penuh. Mereka menggunakan Arduino (Bab 2&3), sensor ultrasonik (Bab 2), dan modul WiFi (Bab 4) untuk mengirim data.

    *Pertanyaan:*
    1. Ilmu dari bab apa saja yang digunakan dalam proyek ini?
    2. Apa dampak sosial (Bab 5) dari proyek ini?
    """)


def content_identifikasi():
    return dedent("""
    ### 🔍 Tahap 1: Identifikasi Masalah
    Semua proyek besar dimulai dari satu hal: **MASALAH**. Tanpa masalah, proyek tidak punya tujuan.

    > 🧩 **Analogi:** Identifikasi masalah itu seperti periksa ke dokter. Dokter tidak akan langsung kasih obat tanpa tahu penyakitnya. Pertama tanya: "Sakit apa?" — itu identifikasi masalah.

    ### Langkah-Langkah
    1. **Amati lingkungan sekitarmu** — Apa yang tidak efisien? Apa yang masih manual?
    2. **Tanyakan 5W+1H** — What, Why, Who, Where, When, How
    3. **Prioritaskan** — Mana yang paling mendesak? Bisa diselesaikan dengan teknologi?

    ### Lembar Kerja
    | Pertanyaan | Jawaban Tim |
    |------------|-------------|
    | Masalah apa yang ingin diselesaikan? | |
    | Mengapa ini penting? | |
    | Siapa yang merasakan dampaknya? | |
    | Di mana masalah ini terjadi? | |
    | Solusi apa yang sudah ada? | |
    | Bagaimana teknologi bisa membantu? | |

    ### 🔍 Cek Pemahaman
    1. Mengapa identifikasi masalah adalah tahap pertama yang penting?
    2. Apa itu 5W+1H dan bagaimana penerapannya dalam identifikasi masalah?
    3. Bagaimana cara memprioritaskan masalah yang akan diselesaikan?

    ### 📋 Studi Kasus
    **Antrean Panjang di Kantin Sekolah**

    Setiap jam istirahat, kantin SMA Nusantara selalu penuh sesak. Siswa harus antre 15-20 menit hanya untuk membeli makanan. Akibatnya, banyak siswa tidak kebagian waktu untuk makan. Tim proyek mencoba menerapkan 5W+1H: What (antrean panjang), Why (sistem pembayaran manual), Who (siswa dan penjual), Where (kantin), When (jam istirahat), How (teknologi bisa membantu).

    *Pertanyaan:*
    1. Identifikasi masalah utama dan usulkan solusi teknologi yang tepat!
    2. Terapkan 5W+1H untuk masalah lain di lingkungan sekolahmu!
    """)


def content_perencanaan():
    return dedent("""
    ### 📋 Tahap 2: Perencanaan Proyek
    Setelah masalah teridentifikasi, saatnya membuat rencana. Proyek yang baik adalah proyek yang direncanakan dengan matang.

    > 🧩 **Analogi:** Perencanaan proyek itu seperti menulis skenario film. Sebelum syuting, sutradara sudah tahu: siapa pemainnya, di mana lokasinya, berapa biayanya, kapan selesainya.

    ### Tujuan SMART
    | Kriteria | Contoh |
    |----------|--------|
    | **S**pecific | Membuat alat penyiram tanaman otomatis |
    | **M**easurable | Tanaman tersiram setiap 6 jam |
    | **A**chievable | Dengan Arduino + sensor kelembaban |
    | **R**elevant | Menghemat air di taman sekolah |
    | **T**ime-bound | Selesai dalam 4 minggu |

    ### Timeline Proyek
    | Minggu | Kegiatan | Output |
    |--------|----------|--------|
    | 1 | Identifikasi & Perencanaan | Laporan masalah |
    | 2 | Desain solusi | Diagram & flowchart |
    | 3-4 | Implementasi prototipe | Prototipe berfungsi |
    | 5 | Pengujian & perbaikan | Hasil uji coba |
    | 6 | Dokumentasi & presentasi | Laporan & slide |

    ### Pembagian Tugas Tim
    | Peran | Tanggung Jawab |
    |-------|----------------|
    | Ketua Tim | Koordinasi, presentasi |
    | Teknisi Hardware | Merangkai komponen |
    | Programmer | Menulis kode Arduino |
    | Dokumentasi | Laporan & video |

    ### 🔍 Cek Pemahaman
    1. Apa kepanjangan dari SMART dan jelaskan masing-masing!
    2. Mengapa timeline proyek penting?
    3. Sebutkan minimal 3 peran dalam tim proyek!

    ### 📋 Studi Kasus
    **Proyek Smart Parking: 3 Minggu atau Gagal**

    Tim proyek "Smart Parking" memiliki waktu 3 minggu untuk menyelesaikan prototipe. Mereka membuat timeline: Minggu 1 (identifikasi + desain), Minggu 2 (implementasi), Minggu 3 (pengujian + dokumentasi). Ketua tim membagi tugas: Andi (programmer), Budi (teknisi), Cici (dokumentasi). Tujuan SMART mereka: "Membuat prototipe sistem parkir otomatis menggunakan sensor ultrasonik dan Arduino yang bisa mendeteksi ketersediaan slot parkir dalam waktu 3 minggu."

    *Pertanyaan:*
    1. Apakah tujuan proyek sudah memenuhi kriteria SMART? Jelaskan!
    2. Buat timeline alternatif jika waktu yang tersedia hanya 2 minggu!
    """)


def content_desain():
    return dedent("""
    ### ✏️ Tahap 3: Desain Solusi
    Desain solusi adalah penerjemahan rencana menjadi gambar teknis. Di sinilah kamu membuat blueprint prototipe.

    > 🧩 **Analogi:** Desain solusi itu seperti arsitek membuat denah rumah. Sebelum tukang mulai membangun, arsitek sudah punya gambar. Kalau tidak ada denah, rumah bisa roboh!

    ### 1. Diagram Blok Sistem
    ```
                      ┌──────────────────┐
      ┌────────┐       │   ARDUINO UNO    │      ┌──────────┐
      │ SENSOR │──────►│                  │──────►│  AKTUATOR │
      │ Suhu   │       │  ┌────────────┐  │      │  (LED/    │
      │ DHT11  │       │  │ Program C │  │      │   Buzzer) │
      └────────┘       │  └────────────┘  │      └──────────┘
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │  Serial Monitor   │
                        └──────────────────┘
    ```

    ### 2. Flowchart Program
    ```
            ┌───────────────┐
            │     START     │
            └───────┬───────┘
                    ▼
            ┌───────────────┐
            │ Baca sensor   │
            └───────┬───────┘
                    ▼
            ┌───────────────┐
            │  Suhu > 30°C? │────Ya──→ LED Merah ON
            └───────┬───────┘
                    │ Tidak
                    ▼
            ┌───────────────┐
            │  Suhu 25-30°C?│────Ya──→ LED Kuning ON
            └───────┬───────┘
                    │ Tidak
                    ▼
            ┌───────────────┐
            │  Suhu < 25°C? │────Ya──→ LED Hijau ON
            └───────┬───────┘
                    │ Tidak
                    ▼
            ┌───────────────┐
            │ Tunggu 2 detik│
            └───────┬───────┘
                    ▼
            ┌───────────────┐
            │ Ulangi (loop) │
            └───────────────┘
    ```

    ### 3. Skema Rangkaian
    Gambarkan pin-by-pin koneksi komponen ke Arduino.

    ### 🔍 Cek Pemahaman
    1. Apa tujuan dari diagram blok sistem?
    2. Apa perbedaan diagram blok dan flowchart?
    3. Mengapa perlu membuat desain sebelum implementasi?

    ### 📋 Studi Kasus
    **Merancang Sistem Penyiraman Tanaman**

    Kelompok proyek ingin membuat penyiram tanaman otomatis. Mereka membuat diagram blok: Sensor Kelembaban → Arduino → Relay → Pompa Air. Flowchart-nya: Baca sensor → Jika kering → Pompa ON 5 detik → Jika basah → Pompa OFF → Ulangi. Skema rangkaian menunjukkan pin sensor ke A0, relay ke pin 7, dan power eksternal untuk pompa.

    *Pertanyaan:*
    1. Gambarkan diagram blok sistem penyiraman otomatis berdasarkan deskripsi di atas!
    2. Identifikasi input, proses, dan output dari sistem ini!
    """)


def content_implementasi():
    return dedent("""
    ### 🔨 Tahap 4: Implementasi Prototipe
    Ini tahap paling seru — kamu mulai **membangun** prototipe! Dari gambar di kertas menjadi benda nyata.

    > 🧩 **Analogi:** Ini seperti memasak setelah punya resep. Kamu sudah punya daftar belanja (alat & bahan), instruksi (flowchart), sekarang saatnya eksekusi! Mungkin ada yang gosong, mungkin ada yang kurang asin — itu normal. Yang penting terus dicoba sampai berhasil!

    ### Langkah Implementasi
    ```
      ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
      │  Rangkai │   │  Tulis   │   │  Upload  │   │   Uji    │
      │ Hardware │──►│  Program │──►│  ke Board│──►│  Coba    │
      └──────────┘   └──────────┘   └──────────┘   └────┬─────┘
                                                         │
                                  ┌──────────┐          │
                                  │  Debug & │◄─────────┘
                                  │ Perbaiki │
                                  └──────────┘
    ```

    ### Tips Implementasi
    1. **Rangkai bertahap** — Mulai dari 1 sensor dulu
    2. **Cek rangkaian** — Pastikan tidak ada kabel terbalik
    3. **Tulis program bertahap** — Mulai dari digitalWrite sederhana
    4. **Gunakan Serial.print** — Untuk debugging
    5. **Dokumentasi setiap langkah** — Foto/video tiap tahap

    ### Checklist
    | No | Item | Status |
    |----|------|--------|
    | 1 | Semua komponen tersedia | ☐ |
    | 2 | Rangkaian di breadboard | ☐ |
    | 3 | Program berhasil di-compile | ☐ |
    | 4 | Sensor membaca dengan benar | ☐ |
    | 5 | Aktuator merespons sesuai logika | ☐ |
    | 6 | Rangkaian stabil > 10 menit | ☐ |

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 langkah implementasi prototipe secara berurutan!
    2. Mengapa sebaiknya merangkai komponen secara bertahap?
    3. Apa fungsi `Serial.print()` dalam proses implementasi?

    ### 📋 Studi Kasus
    **LED Tidak Menyala!**

    Raka merangkai LED ke Arduino sesuai diagram. Setelah upload program, LED tidak menyala. Ia panik, tapi kemudian menerapkan debugging bertahap:
    1. Cek kabel: ternyata kabel jumper longgar di GND
    2. Cek polaritas LED: kaki panjang (+) ke pin 13, pendek ke GND
    3. Cek resistor: harusnya 220 Ohm, ternyata 10k Ohm (terlalu besar)
    Setelah memperbaiki ketiganya, LED menyala dengan indah!

    *Pertanyaan:*
    1. Mengapa resistor 10k Ohm menyebabkan LED tidak menyala?
    2. Langkah debugging apa yang pertama kali harus dilakukan jika rangkaian tidak bekerja?
    """)


def content_pengujian():
    return dedent("""
    ### 🧪 Tahap 5: Pengujian & Perbaikan
    Pengujian adalah memastikan prototipe bekerja sesuai yang diharapkan. Dan akan selalu ada yang perlu diperbaiki — itu normal!

    > 🧩 **Analogi:** Pengujian itu seperti quality control di pabrik. Sebelum smartphone dijual, ia diuji ratusan kali. Prototipemu juga begitu!

    ### Jenis Pengujian
    | Jenis | Apa yang Diuji | Cara Uji |
    |-------|---------------|----------|
    | **Unit Test** | Setiap komponen (sensor, LED) | Uji satu per satu |
    | **Integration Test** | Semua komponen bekerja bersama | Jalankan program lengkap |
    | **Stress Test** | Stabil dalam waktu lama? | Biarkan jalan 1 jam |
    | **User Test** | Mudah digunakan? | Minta teman coba |

    ### Dokumentasi Pengujian
    | Skenario | Input | Output Diharapkan | Output Aktual | Status |
    |----------|-------|-------------------|---------------|--------|
    | Suhu 25°C | 25°C | LED hijau nyala | LED hijau nyala | ✅ |
    | Suhu 32°C | 32°C | LED kuning nyala | LED kuning nyala | ✅ |
    | Suhu 36°C | 36°C | LED merah nyala | Tidak nyala | ❌ |

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 jenis pengujian dan jelaskan masing-masing!
    2. Apa yang harus dilakukan jika hasil pengujian tidak sesuai harapan?
    3. Mengapa stress test penting untuk prototipe?

    ### 📋 Studi Kasus
    **Kipas Mati Setelah 1 Jam**

    Tim Smart Fan sudah berhasil membuat prototipe kipas otomatis. Saat diuji, kipas menyala sempurna saat suhu > 30°C. Tapi setelah 45 menit berjalan terus, kipas mati sendiri. Setelah diperiksa, ternyata relay overheat karena spesifikasinya hanya untuk 5V, tapi kipas menarik arus lebih besar.

    *Pertanyaan:*
    1. Jenis pengujian apa yang mengungkap masalah ini?
    2. Solusi apa yang tepat untuk masalah relay overheat?
    """)


def content_dokumentasi():
    return dedent("""
    ### 📝 Tahap 6: Dokumentasi & Laporan
    Dokumentasi adalah catatan lengkap tentang proyek yang kamu buat. Agar orang lain bisa memahami, mengapresiasi, dan mereproduksi karyamu.

    > 🧩 **Analogi:** Dokumentasi itu seperti buku resep. Kalau kamu berhasil membuat kue yang enak, tanpa resep, orang lain tidak tahu cara membuatnya. Dengan resep (dokumentasi), siapa pun bisa membuat kue yang sama!

    ### Format Laporan
    1. **Halaman Judul** — Nama proyek, logo sekolah, anggota tim
    2. **Bab 1: Pendahuluan** — Latar belakang, rumusan masalah, tujuan
    3. **Bab 2: Kajian Teori** — Teori pendukung, referensi
    4. **Bab 3: Metode Perancangan** — Diagram blok, flowchart, skema
    5. **Bab 4: Implementasi & Pengujian** — Foto, hasil uji, kendala
    6. **Bab 5: Penutup** — Kesimpulan, saran, refleksi
    7. **Lampiran** — Kode program, foto alat, slide

    ### 🔍 Cek Pemahaman
    1. Sebutkan struktur laporan proyek yang lengkap!
    2. Mengapa dokumentasi penting dalam sebuah proyek?
    3. Apa saja yang harus difoto/direkam selama proses proyek?

    ### 📋 Studi Kasus
    **Laporan yang Membantu Adik Kelas**

    Tim proyek "Smart Trash Can" membuat dokumentasi sangat lengkap: foto rangkaian, video demo, flowchart, kode program dengan komentar, dan catatan kendala. Setahun kemudian, adik kelas menggunakan dokumentasi mereka untuk mengembangkan proyek serupa. Tanpa dokumentasi, mereka harus memulai dari nol.

    *Pertanyaan:*
    1. Bagian laporan apa yang paling membantu adik kelas?
    2. Apa yang terjadi jika tim tidak membuat dokumentasi?

    ### Tips Dokumentasi
    ✅ **Foto setiap tahap** — identifikasi, rangkaian, coding, pengujian
    ✅ **Rekam video demo** — tunjukkan prototipe bekerja
    ✅ **Catat kendala** — apa yang sulit dan bagaimana mengatasinya
    ✅ **Tulis dengan bahasa sendiri** — jangan copas dari internet
    """)


def content_presentasi():
    return dedent("""
    ### 🎤 Tahap 7: Presentasi & Refleksi
    Tahap terakhir adalah berbagi hasil dengan orang lain dan merenungkan apa yang sudah dipelajari.

    > 🧩 **Analogi:** Presentasi itu seperti pameran karya seni. Kamu bukan cuma memajang lukisan, tapi juga menceritakan: ide di baliknya, proses membuatnya, tantangannya, dan apa yang kamu pelajari.

    ### Struktur Presentasi (10 menit)
    | Slide | Konten | Durasi |
    |-------|--------|--------|
    | 1 | Judul & anggota tim | 1 menit |
    | 2-3 | Masalah & desain solusi | 3 menit |
    | 4-5 | Implementasi & demo | 5 menit |
    | 6 | Refleksi & penutup | 1 menit |

    ### Rubrik Penilaian
    | Aspek | Skor 4 | Skor 3 | Skor 2 | Skor 1 |
    |-------|--------|--------|--------|--------|
    | **Konten** | Lengkap, akurat | Lengkap | Kurang lengkap | Tidak terstruktur |
    | **Demo** | Bekerja sempurna | Dengan bantuan | Sebagian | Tidak bekerja |
    | **Komunikasi** | Jelas, percaya diri | Jelas | Kurang jelas | Tidak siap |
    | **Visual** | Menarik, informatif | Cukup menarik | Kurang menarik | Tidak ada |

    ### 🔍 Cek Pemahaman
    1. Berapa durasi ideal presentasi proyek?
    2. Sebutkan 4 aspek yang dinilai dalam rubrik penilaian!
    3. Mengapa refleksi penting setelah proyek selesai?

    ### 📋 Studi Kasus
    **Presentasi Gagal karena Demo Error**

    Tim proyek "Smart Parking" melakukan demo saat presentasi. Namun sensor ultrasonik tiba-tiba tidak mendeteksi dengan benar karena kabel longgar. Alih-alih panik, ketua tim menjelaskan dengan tenang: "Ini adalah contoh nyata pentingnya pengujian — kami menemukan bahwa kabel sensor perlu diperkuat. Dalam versi berikutnya, kami akan menggunakan konektor yang lebih kokoh."

    *Pertanyaan:*
    1. Apa yang baik dari cara tim menangani kegagalan demo?
    2. Persiapan apa yang bisa dilakukan untuk mengantisipasi error saat presentasi?

    ### Pertanyaan Refleksi
    1. Apa yang paling berhasil dari proyek ini?
    2. Apa yang paling sulit dan bagaimana kalian mengatasinya?
    3. Apa yang akan kalian lakukan berbeda jika bisa mengulang?
    4. Ilmu baru apa yang kalian dapatkan di luar materi kelas?

    ---
    > 🎉 **Selamat!** Kalian telah menyelesaikan perjalanan belajar Informatika kelas XII. Bukan cuma tentang coding dan Arduino, tapi tentang berpikir kritis, bekerja sama, dan menciptakan solusi untuk masalah nyata. **Teruslah berkarya!** 🚀
    """)


# ─── CONTENT MAP ──────────────────────────────────────────────

CONTENT_MAP = {
    "literasi_digital": content_literasi_digital,
    "revolusi_industri": content_revolusi_industri,
    "iot": content_iot,
    "big_data": content_big_data,
    "ai": content_ai,
    "cloud": content_cloud,
    "sbc": content_sbc,
    "arduino": content_arduino,
    "ide": content_ide,
    "komponen": content_komponen,
    "simulator": content_simulator,
    "praktik_dasar": content_praktik_dasar,
    "proyek_mini": content_proyek_mini,
    "mengapa_bk": content_mengapa_bk,
    "dasar_c": content_dasar_c,
    "struktur_c": content_struktur_c,
    "kontrol": content_kontrol,
    "array": content_array,
    "fungsi_library": content_fungsi_library,
    "proyek_akhir": content_proyek_akhir,
    "apa_jaringan": content_apa_jaringan,
    "topologi": content_topologi,
    "komponen_jaringan": content_komponen_jaringan,
    "tcpip": content_tcpip,
    "cyber": content_cyber,
    "teknologi_masyarakat": content_teknologi_masyarakat,
    "medsos": content_medsos,
    "digital_pendidikan": content_digital_pendidikan,
    "ekonomi_digital": content_ekonomi_digital,
    "uu_ite": content_uu_ite,
    "apa_proyek": content_apa_proyek,
    "identifikasi": content_identifikasi,
    "perencanaan": content_perencanaan,
    "desain": content_desain,
    "implementasi": content_implementasi,
    "pengujian": content_pengujian,
    "dokumentasi": content_dokumentasi,
    "presentasi": content_presentasi,
}

# ─── SUB CHAPTER KEYWORDS ─────────────────────────────────────

SUB_KEYS = {
    "1_A": "literasi_digital","1_B": "revolusi_industri","1_C": "iot","1_D": "big_data","1_E": "ai","1_F": "cloud",
    "2_A": "sbc","2_B": "arduino","2_C": "ide","2_D": "komponen","2_E": "simulator","2_F": "praktik_dasar","2_G": "proyek_mini",
    "3_A": "mengapa_bk","3_B": "dasar_c","3_C": "struktur_c","3_D": "kontrol","3_E": "array","3_F": "fungsi_library","3_G": "proyek_akhir",
    "4_A": "apa_jaringan","4_B": "topologi","4_C": "komponen_jaringan","4_D": "tcpip","4_E": "cyber",
    "5_A": "teknologi_masyarakat","5_B": "medsos","5_C": "digital_pendidikan","5_D": "ekonomi_digital","5_E": "uu_ite",
    "6_A": "apa_proyek","6_B": "identifikasi","6_C": "perencanaan","6_D": "desain","6_E": "implementasi","6_F": "pengujian","6_G": "dokumentasi","6_H": "presentasi",
}


# ─── GENERATE ──────────────────────────────────────────────────

def generate_all():
    print("=" * 60)
    print("GENERATOR MATERI AJAR KELAS XII")
    print("6 Bab — format menarik, analogi, diagram, contoh nyata")
    print("=" * 60)

    total_lines = 0

    for bab in BAB:
        k = bab["id"]
        judul = bab["judul"]
        emoji = bab["emoji"]
        smt = bab["smt"]
        sub = bab["sub"]
        idx = int(k) - 1  # 0-indexed

        lines = []
        lines.append(f"# {emoji} Bab {k}: {judul}")
        lines.append("")
        lines.append(f"> **Semester {'Ganjil' if smt == 1 else 'Genap'}** | **Fase F** | **Kelas XII** | **{len(sub)*5} JP**")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Pemetaan CP
        lines.append("---")
        lines.append("## 📊 Pemetaan Capaian Pembelajaran\n")
        lines.append("| Elemen CP | Deskripsi CP |")
        lines.append("|-----------|-------------|")
        for elemen, desc in CP_MAP.get(k, []):
            lines.append(f"| {elemen} | {desc} |")
        lines.append("")

        # Tujuan
        lines.append("## 🎯 Tujuan Pembelajaran\n")
        for h, jdl in sub:
            lines.append(f"- **{h}.** {jdl}")
        lines.append("")

        # Peta Konsep
        lines.append("## 🗺️ Peta Konsep\n")
        lines.append("```")
        lines.append(f"               {emoji} {judul.upper()}")
        lines.append(f"                     |")
        for i, (h, jdl) in enumerate(sub):
            prefix = "                     ├──" if i < len(sub)-1 else "                     └──"
            lines.append(f"{prefix} {h}. {jdl}")
        lines.append("```\n")

        # Content for each sub
        for h, jdl in sub:
            key = SUB_KEYS.get(f"{k}_{h}", "")
            content_fn = CONTENT_MAP.get(key, None)
            lines.append(f"## {h}. {jdl}\n")
            if content_fn:
                lines.append(content_fn())
            else:
                lines.append(f"*[Materi {jdl} sedang dikembangkan]*\n")
            lines.append("")
            lines.append("> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?\n")
            lines.append("---\n")

        # Proyek Mini
        proyek = PROYEK.get(k)
        if proyek:
            lines.append("---")
            lines.append(f"## 🏗️ Proyek Mini: {proyek['judul']}\n")
            lines.append(f"{proyek['deskripsi']}\n")
            lines.append("**Alat dan Bahan:**")
            for alat in proyek['alat']:
                lines.append(f"- {alat}")
            lines.append("")
            lines.append("**Langkah-langkah:**")
            for i, langkah in enumerate(proyek['langkah'], 1):
                lines.append(f"{i}. {langkah}")
            lines.append("")
            lines.append(f"> **Output:** {proyek['output']}")
            lines.append("")

        # Rangkuman
        lines.append("## 📝 Rangkuman\n")
        for i, poin in enumerate(RANGKUMAN.get(k, []), 1):
            lines.append(f"{i}. {poin}")
        lines.append("")

        # Latihan
        lines.append("---\n")
        lines.append("## ✍️ Latihan Soal\n")
        lines.append("### A. Pilihan Ganda\n")
        pg_soal = SOAL_PG.get(k, [])
        for i, s in enumerate(pg_soal, 1):
            lines.append(f"{i}. {s['q']}")
            for huruf, opsi in zip(['a','b','c','d','e'], s['o']):
                lines.append(f"   {huruf}. {opsi}")
            lines.append(f"   **Jawaban: {s['a']}**\n")
        lines.append("### B. Uraian\n")
        for i, soal in enumerate(SOAL_URAIAN.get(k, []), 1):
            lines.append(f"{i}. {soal}\n")

        # Rubrik
        rubrik = RUBRIK.get(k)
        if rubrik:
            lines.append("---")
            lines.append("## 📋 Rubrik Penilaian Proyek\n")
            lines.append("| Aspek | Kurang | Cukup | Baik |")
            lines.append("|-------|--------|-------|------|")
            for i in range(len(rubrik['aspek'])):
                lines.append(f"| {rubrik['aspek'][i]} | {rubrik['level1'][i]} | {rubrik['level2'][i]} | {rubrik['level3'][i]} |")
            lines.append("")

        # Pengayaan
        lines.append("---")
        lines.append("## 🚀 Tugas Pengayaan\n")
        for t_judul, t_desc in PENGAYAAN.get(k, []):
            lines.append(f"### {t_judul}")
            lines.append(f"{t_desc}\n")

        # Glosarium
        lines.append("---")
        lines.append("## 📖 Glosarium\n")
        for term, defn in GLOSARIUM.get(k, []):
            lines.append(f"- **{term}**: {defn}")
        lines.append("")

        # Media Pembelajaran
        lines.append("---")
        lines.append("## 📺 Sumber & Media Pembelajaran\n")
        lines.append("| Platform | Sumber | Tautan | Keterangan |")
        lines.append("|----------|--------|--------|------------|")
        for platform, nama, link, ket in MEDIA.get(k, []):
            lines.append(f"| {platform} | {nama} | `{link}` | {ket} |")
        lines.append("")

        out = "\n".join(lines)

        fname = f"Bab_{k}_{judul.replace(' ','_')}.md"
        fp = os.path.join(BASE, fname)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(out)

        n_lines = out.count("\n") + 1
        total_lines += n_lines
        print(f"  ✓ Bab {k}: {emoji} {judul} ({n_lines} baris)")

    print(f"\n  → {len(BAB)} file Materi Ajar dibuat.")
    print(f"  → Total: ~{total_lines} baris")
    print("=" * 60)


if __name__ == "__main__":
    generate_all()
