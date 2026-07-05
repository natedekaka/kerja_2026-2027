#!/usr/bin/env python3
import os
import re
import glob

KAIH_MAP_X = {
    "BK": "Gemar Belajar, Bermasyarakat",
    "TIK": "Makan Sehat, Bangun Pagi",
    "SK": "Beribadah, Berolahraga",
    "JKI": "Bermasyarakat, Gemar Belajar",
    "AD": "Makan Sehat, Tidur Cepat",
    "AP": "Gemar Belajar, Bangun Pagi",
    "DSI": "Beribadah, Bermasyarakat",
    "PLB": "Semua 7 KAIH",
}

KAIH_MAP_XI = {
    "1": "Gemar Belajar, Bermasyarakat",
    "2": "Gemar Belajar, Bangun Pagi",
    "3": "Beribadah, Bermasyarakat",
    "4": "Bermasyarakat, Tidur Cepat",
    "5": "Gemar Belajar, Makan Sehat",
    "6": "Makan Sehat, Olahraga",
}

MEANING_X = {
    "BK": "Dekomposisi, pengenalan pola, abstraksi, dan algoritma adalah fondasi berpikir komputasional yang digunakan sehari-hari — dari merencanakan liburan hingga memecahkan masalah kompleks di dunia kerja.",
    "TIK": "Kemampuan mengolah kata, angka, dan presentasi secara terintegrasi adalah skill esensial di dunia perkantoran dan akademik modern.",
    "SK": "Memahami bagaimana komputer bekerja dari dalam membantu kita merawat perangkat, memilih spesifikasi yang tepat, dan memecahkan masalah teknis sehari-hari.",
    "JKI": "Internet dan jaringan adalah infrastruktur modern — memahami cara kerjanya membuat kita lebih bijak dan aman dalam menggunakan teknologi.",
    "AD": "Data adalah 'minyak baru' di era digital. Kemampuan menganalisis data membuka peluang karir dan membantu pengambilan keputusan yang lebih baik.",
    "AP": "Pemrograman adalah cara kita 'berbicara' dengan komputer dan menciptakan solusi digital untuk masalah nyata.",
    "DSI": "Teknologi membawa dampak luas ke masyarakat — memahaminya membantu kita menjadi pengguna teknologi yang bertanggung jawab.",
    "PLB": "Proyek lintas bidang melatih kita menerapkan semua elemen informatika untuk menyelesaikan masalah nyata di sekitar kita.",
}

MEANING_XI = {
    "1": "Informatika bukan sekadar coding — 8 elemennya saling terkait dan membentuk fondasi karir di era digital.",
    "2": "Strategi algoritmik membantu kita memilih solusi terbaik, bukan sekadar solusi yang bekerja — efisiensi itu penting!",
    "3": "Berpikir kritis di era digital adalah senjata melawan hoaks dan misinformasi yang menyebar setiap hari.",
    "4": "Jaringan komputer adalah tulang punggung internet — memahaminya membantu kita bekerja lebih aman dan efisien.",
    "5": "Aplikasi mobile dengan AI bukan lagi fiksi — kalian bisa membuatnya sekarang dengan tools yang tersedia.",
    "6": "Data lingkungan bisa menyelamatkan bumi — analisis data membantu kita memahami dan mengambil tindakan nyata.",
}

REFLECTION_ADD = """
---

### G. REFLEKSI PEMBELAJARAN (DEEP LEARNING + 7 KAIH)

#### Refleksi Guru:
| Aspek | Catatan |
|-------|---------|
| Apakah pendekatan Mindful \\u2192 Mining \\u2192 Joyful berjalan efektif? | |
| Apakah siswa aktif berpartisipasi? | |
| Apakah integrasi 7 KAIH terlaksana? | |
| Apa yang perlu diperbaiki? | |
| Tindak lanjut: remedial/pengayaan? | |

#### Refleksi Siswa:
| Pertanyaan | Jawaban |
|------------|---------|
| **Mindful:** Apa yang aku pelajari hari ini? | |
| **Meaningful:** Bagaimana ini berguna untuk kehidupanku? | |
| **Joyful:** Hal paling menyenangkan dari pembelajaran hari ini? | |
| **7 KAIH:** Kebiasaan baik apa yang aku praktikkan hari ini? | |
| **Dimensi:** Dimensi Profil Lulusan mana yang terasah? | |
"""

def get_kaih_for_file(filename, kelas):
    if kelas == "X":
        for elem, kaih in KAIH_MAP_X.items():
            if elem in filename:
                return kaih
        return "Gemar Belajar, Bermasyarakat"
    else:
        for bab, kaih in KAIH_MAP_XI.items():
            if f"Bab{bab}" in filename or f"Bab_{bab}" in filename:
                return kaih
        return "Gemar Belajar, Kemandirian"

def get_meaning_for_file(filename, kelas):
    if kelas == "X":
        for elem, meaning in MEANING_X.items():
            if elem in filename:
                return meaning
        return "Materi ini terhubung langsung dengan kehidupan sehari-hari dan keterampilan abad 21."
    else:
        for bab, meaning in MEANING_XI.items():
            if f"Bab{bab}" in filename or f"Bab_{bab}" in filename:
                return meaning
        return "Materi ini relevan dengan perkembangan teknologi dan kebutuhan dunia kerja."

def update_x_modul_ajar(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    filename = os.path.basename(filepath)
    kaih = get_kaih_for_file(filename, "X")
    meaning = get_meaning_for_file(filename, "X")

    if "Integrasi 7 KAIH" not in content:
        pattern = r"(\| \*{0,2}Integrasi 8 Dimensi\*{0,2} .*? \|)"
        repl = r"\1\n| **Integrasi 7 KAIH** | " + kaih + r" |\n| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |"
        content = re.sub(pattern, repl, content, count=1)

    if "PEMAHAMAN BERMAKNA" not in content:
        p_meaning = f"""### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
{meaning}

"""
        content = re.sub(
            r"(### B\. TUJUAN PEMBELAJARAN\n)",
            r"\1" + p_meaning,
            content, count=1
        )

    # 3. Add Pertanyaan Pemantik
    if "PERTANYAAN PEMANTIK" not in content:
        p_pemantik = """### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

"""
        content = re.sub(
            r"(#### B\.1 Tujuan)",
            p_pemantik + r"\1",
            content, count=1
        )
        content = re.sub(
            r"(### B\.1 Tujuan)",
            p_pemantik + r"\1",
            content, count=1
        )

    header_pattern = r"\| \*{0,2}Tahap\*{0,2} \| \*{0,2}Waktu\*{0,2} \| \*{0,2}Aktivitas Guru\*{0,2} \| \*{0,2}Aktivitas Siswa\*{0,2} \| \*{0,2}Media/Sumber\*{0,2} \|"
    if re.search(header_pattern, content) and "**Fase DL**" not in content:
        content = re.sub(header_pattern, "| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |", content)
        content = re.sub(r"\|-{3,}\|-{3,}\|-{3,}\|-{3,}\|-{3,}\|", "|---|---|---|---|---|---|", content)
        content = re.sub(r"\| \*{0,2}Pendahuluan\*{0,2} \| (\d+)", r"| **MINDFULL** | **Pemanasan** | \1", content)
        content = re.sub(r"\| \*{0,2}Inti\b", r"| **MINING FULL** | **Eksplorasi**", content)
        content = re.sub(r"\| \*{0,2}Penutup\*{0,2} \| (\d+)", r"| **JOYFULL** | **Penutup Kreatif** | \1", content)

    # 5. Add 7 KAIH reflection to existing refleksi or add new section
    if "### F. REFLEKSI GURU" in content:
        content = content.replace(
            "### F. REFLEKSI GURU (Diisi setelah pembelajaran)",
            "### F. REFLEKSI PEMBELAJARAN (Deep Learning + 7 KAIH)\n\n#### Refleksi Guru (Diisi setelah pembelajaran)"
        )
        # Add student reflection before bahan bacaan
        if "### G. BAHAN BACAAN UNTUK GURU" in content:
            content = content.replace(
                "### G. BAHAN BACAAN UNTUK GURU",
                "#### Refleksi Siswa:\n| Pertanyaan | Jawaban |\n|---|---|\n| **Mindful:** Apa yang aku pelajari hari ini? | |\n| **Meaningful:** Bagaimana ini berguna untuk hidupku? | |\n| **Joyful:** Hal paling menyenangkan hari ini? | |\n| **7 KAIH:** Kebiasaan baik apa yang aku praktikkan? | |\n| **Dimensi:** Dimensi Profil Lulusan mana yang terasah? | |\n\n---\n\n### G. BAHAN BACAAN UNTUK GURU"
            )
    else:
        # Add reflection before the closing
        if "Mengetahui," in content:
            content = content.replace(
                "Mengetahui,  \nKepala Sekolah",
                REFLECTION_ADD + "\nMengetahui,  \nKepala Sekolah"
            )

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def update_xi_modul_ajar(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    filename = os.path.basename(filepath)
    kaih = get_kaih_for_file(filename, "XI")
    meaning = get_meaning_for_file(filename, "XI")

    # 1. Add Integrasi 7 KAIH and Deep Learning after Integrasi 8 Dimensi
    pattern = r"(\| \*\*Integrasi 8 Dimensi\*\* .*? \|)"
    repl = r"\1\n| **Integrasi 7 KAIH** | " + kaih + r" |\n| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |"
    content = re.sub(pattern, repl, content, count=1)

    # 2. Add Pemahaman Bermakna
    p_meaning = f"""### B. PEMAHAMAN BERMAKNA (MEANINGFUL)
{meaning}

### C. PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika konsep ini tidak ada?
2. Bagaimana ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk masa depanmu?

"""
    # XI format: has A. TUJUAN PEMBELAJARAN, then B. PEMAHAMAN BERMAKNA, then C. PERTANYAAN PEMANTIK
    # If B and C already exist in some form, skip
    if "PEMAHAMAN BERMAKNA" not in content:
        content = re.sub(
            r"(### A\. TUJUAN PEMBELAJARAN\n)",
            r"\1" + p_meaning,
            content, count=1
        )

    # 3. Update kegiatan table: change Pendahuluan/Inti/Penutup to Mindful/Mining/Joyful
    if "| **Tahap** | **Aktivitas** | **Waktu** |" in content:
        content = content.replace(
            "| **Tahap** | **Aktivitas** | **Waktu** |",
            "| **Fase DL** | **Tahap** | **Aktivitas** | **Waktu** |"
        )
        content = re.sub(
            r"\| \*\*Pendahuluan\*\* \|",
            r"| **MINDFULL** | **Pemanasan** |",
            content
        )
        content = re.sub(
            r"\| \*\*Inti\*\* \|",
            r"| **MINING FULL** | **Eksplorasi** |",
            content
        )
        content = re.sub(
            r"\| \*\*Penutup\*\* \|",
            r"| **JOYFULL** | **Penutup Kreatif** |",
            content
        )
        # Fix table separator
        content = re.sub(
            r"\|----------\|-----------\|-------\|",
            r"|----------|-----------|-----------|-------|",
            content
        )
        content = re.sub(
            r"\|-----------\|----------\|-------\|",
            r"|-----------|-----------|----------|-------|",
            content
        )

    # 4. Add or update reflection
    if "Refleksi" in content or "refleksi" in content:
        pass  # Already has reflection, may need enhancement
    else:
        # Add before closing
        repl_reflection = """### REFLEKSI PEMBELAJARAN (DEEP LEARNING + 7 KAIH)

| Pertanyaan | Jawaban |
|---|---|
| **Mindful:** Apa yang aku pelajari hari ini? | |
| **Meaningful:** Bagaimana ini berguna untuk hidupku? | |
| **Joyful:** Hal paling menyenangkan hari ini? | |
| **7 KAIH:** Kebiasaan baik apa yang aku praktikkan? | |
| **Dimensi:** Dimensi Profil Lulusan mana yang terasah? | |

"""
        if "Mengetahui,  \nKepala Sekolah" in content:
            content = content.replace(
                "Mengetahui,  \nKepala Sekolah",
                repl_reflection + "Mengetahui,  \nKepala Sekolah"
            )

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    base = os.path.expanduser("~/Documents/kerja_2026-2027")
    updated = 0
    skipped = 0

    # Kelas X - static modul ajar
    x_dir = os.path.join(base, "administrasi_guru_kelas_X", "modul_ajar")
    if os.path.exists(x_dir):
        print(f"\\n=== Memproses Kelas X ({x_dir}) ===")
        for f in sorted(glob.glob(os.path.join(x_dir, "*.md"))):
            fname = os.path.basename(f)
            if fname.startswith("PTS") or fname.startswith("PAT") or fname.startswith("Review"):
                # Skip PTS, PAT, Review files
                continue
            if update_x_modul_ajar(f):
                print(f"  \\u2713 {fname}")
                updated += 1
            else:
                skipped += 1

    # Kelas XI - static modul ajar
    xi_dir = os.path.join(base, "administrasi_guru_kelas_XI", "modul_ajar")
    if os.path.exists(xi_dir):
        print(f"\\n=== Memproses Kelas XI ({xi_dir}) ===")
        for f in sorted(glob.glob(os.path.join(xi_dir, "*.md"))):
            fname = os.path.basename(f)
            if fname.startswith("PTS") or fname.startswith("PAT") or fname.startswith("Review"):
                continue
            if update_xi_modul_ajar(f):
                print(f"  \\u2713 {fname}")
                updated += 1
            else:
                skipped += 1

    print(f"\\n=== Selesai! ===")
    print(f"  Diperbarui: {updated}")
    print(f"  Dilewati:   {skipped}")

if __name__ == "__main__":
    main()
