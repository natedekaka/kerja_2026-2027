#!/usr/bin/env python3
"""Convert all .md administration files to a static HTML website."""

import os
import re
import markdown
import shutil
from pathlib import Path

BASE_DIR = Path(os.path.expanduser("~/Documents/kerja_2026-2027"))
OUT_DIR = BASE_DIR / "Adm_versi_web"
GRADE_DIRS = [
    ("Kelas X (Fase E)", BASE_DIR / "administrasi_guru_kelas_X"),
    ("Kelas XI (Fase F)", BASE_DIR / "administrasi_guru_kelas_XI"),
    ("Kelas XII (Fase F)", BASE_DIR / "administrasi_guru_kelas_XII"),
]

MD = markdown.Markdown(extensions=["extra", "toc", "nl2br", "sane_lists", "smarty"])

CSS = """/* ============================================
   Administrasi Guru Informatika — SMA N 6 Cimahi
   ============================================ */

:root {
  --primary: #1e40af;      --primary-light: #3b82f6;
  --secondary: #0f172a;     --accent: #f59e0b;
  --bg: #f1f5f9;            --card: #ffffff;
  --border: #e2e8f0;        --text: #1e293b;
  --text-muted: #64748b;    --sidebar-bg: #0f172a;
  --radius: 12px;           --shadow: 0 1px 3px rgba(0,0,0,0.08);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 270px;
  background: var(--sidebar-bg);
  color: #fff;
  position: fixed;
  top: 0; left: 0;
  height: 100vh;
  overflow-y: auto;
  z-index: 100;
  flex-shrink: 0;
}
.sidebar-header {
  padding: 1.75rem 1.25rem 1.25rem;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.sidebar-header h1 {
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.01em;
}
.sidebar-header p {
  font-size: 0.7rem;
  color: rgba(255,255,255,0.45);
  margin-top: 0.3rem;
  line-height: 1.4;
}
.sidebar-nav { padding: 0.5rem 0; }
.sidebar-nav a {
  display: block;
  padding: 0.5rem 1.25rem;
  color: rgba(255,255,255,0.6);
  text-decoration: none;
  font-size: 0.82rem;
  border-left: 3px solid transparent;
  transition: all 0.15s;
}
.sidebar-nav a:hover, .sidebar-nav a.active {
  color: #fff;
  background: rgba(255,255,255,0.06);
  border-left-color: var(--accent);
}
.sidebar-nav .nav-section {
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: rgba(255,255,255,0.3);
  padding: 1rem 1.25rem 0.25rem;
  font-weight: 600;
}
.sidebar-nav .nav-sub a { padding-left: 2.5rem; font-size: 0.78rem; }

.content {
  margin-left: 270px;
  flex: 1;
  padding: 2.5rem 3rem;
  max-width: 1000px;
}

.breadcrumb {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
}
.breadcrumb a { color: var(--primary-light); text-decoration: none; }
.breadcrumb a:hover { text-decoration: underline; }

.content h1 {
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--secondary);
  margin: 2rem 0 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 3px solid var(--primary);
}
.content h2 { font-size: 1.3rem; font-weight: 700; color: var(--secondary); margin: 2rem 0 0.75rem; }
.content h3 { font-size: 1.1rem; font-weight: 600; margin: 1.5rem 0 0.5rem; }
.content h4 { font-size: 1rem; font-weight: 600; margin: 1rem 0 0.5rem; }
.content p { margin-bottom: 1rem; }
.content a { color: var(--primary); }
.content ul, .content ol { margin: 0.5rem 0 1rem 1.5rem; }
.content li { margin-bottom: 0.3rem; }
.content hr { border: none; border-top: 2px solid var(--border); margin: 2rem 0; }

.content table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0 1.5rem;
  font-size: 0.88rem;
}
.content th, .content td {
  border: 1px solid var(--border);
  padding: 0.6rem 0.75rem;
  text-align: left;
  vertical-align: top;
}
.content th {
  background: var(--sidebar);
  font-weight: 700;
  font-size: 0.82rem;
  color: var(--secondary);
}
.content tr:nth-child(even) { background: #fafafa; }
.content tr:hover { background: #eef2ff; }

.content code {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.85em;
  background: #f1f5f9;
  padding: 0.15em 0.4em;
  border-radius: 4px;
}
.content pre {
  background: #0f172a;
  color: #e2e8f0;
  padding: 1.25rem;
  border-radius: var(--radius);
  overflow-x: auto;
  margin: 1rem 0 1.5rem;
  font-size: 0.82rem;
  line-height: 1.5;
}
.content pre code { background: transparent; padding: 0; color: inherit; }

.content blockquote {
  border-left: 4px solid var(--primary-light);
  background: #eef2ff;
  padding: 0.75rem 1.25rem;
  margin: 1rem 0;
  border-radius: 0 var(--radius) var(--radius) 0;
}

@media print { .sidebar { display: none; } .content { margin-left: 0; padding: 1rem; } .breadcrumb { display: none; } }
@media (max-width: 768px) {
  body { flex-direction: column; }
  .sidebar { width: 100%; height: auto; position: relative; max-height: 50vh; }
  .content { margin-left: 0; padding: 1.25rem; }
}

.hero {
  background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
  color: #fff;
  border-radius: var(--radius);
  padding: 2.5rem 2.5rem;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}
.hero::after {
  content: '';
  position: absolute;
  top: -50%; right: -20%;
  width: 400px; height: 400px;
  background: rgba(255,255,255,0.04);
  border-radius: 50%;
}
.hero h1 {
  font-size: 1.8rem;
  font-weight: 800;
  color: #fff;
  border: none;
  padding: 0;
  margin: 0 0 0.35rem;
}
.hero p {
  font-size: 1rem;
  color: rgba(255,255,255,0.85);
  margin: 0;
}
.hero .sub {
  font-size: 0.82rem;
  color: rgba(255,255,255,0.6);
  margin-top: 0.5rem;
}

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}
.stat-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem;
  text-align: center;
  box-shadow: var(--shadow);
}
.stat-card .num {
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--primary);
  line-height: 1.2;
}
.stat-card .label {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.2rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.stat-card.accent .num { color: var(--accent); }

.grade-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin: 1.5rem 0;
}
.grade-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  transition: transform 0.15s, box-shadow 0.15s;
}
.grade-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.grade-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--secondary);
  margin: 0 0 0.25rem;
}
.grade-card .badge {
  display: inline-block;
  background: #dbeafe;
  color: var(--primary);
  font-size: 0.7rem;
  padding: 0.15rem 0.6rem;
  border-radius: 999px;
  font-weight: 600;
  margin-bottom: 0.75rem;
}
.grade-card .detail {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 1rem;
  line-height: 1.5;
}
.grade-card .links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.grade-card .links a {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.35rem 0.75rem;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 0.78rem;
  color: var(--text);
  text-decoration: none;
  transition: all 0.12s;
}
.grade-card .links a:hover {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}

.identity-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem 2rem;
  box-shadow: var(--shadow);
  margin: 1.5rem 0;
}
.identity-card h2 {
  font-size: 1.1rem;
  margin: 0 0 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border);
}
.identity-card table { margin: 0; }
.identity-card td { border: none; padding: 0.4rem 0.75rem 0.4rem 0; }
.identity-card td:first-child { color: var(--text-muted); font-weight: 600; width: 130px; }

.footer-note {
  text-align: center;
  font-size: 0.78rem;
  color: var(--text-muted);
  border-top: 1px solid var(--border);
  padding-top: 1.5rem;
  margin-top: 2rem;
}
"""


def strip_yaml_frontmatter(text):
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, flags=re.DOTALL)


def convert_md_to_html(md_text):
    html = MD.reset().convert(md_text)
    html = re.sub(r'<table>', '<div class="table-wrap"><table>', html)
    html = re.sub(r'</table>', '</table></div>', html)
    return html


def build_sidebar_html(depth=0):
    pfx = "../" * depth
    html = []
    html.append('<div class="sidebar-header">')
    html.append('  <h1>\U0001f4cb Administrasi Guru</h1>')
    html.append('  <p>Informatika \u2014 SMA N 6 Cimahi<br>2026/2027</p>')
    html.append('</div>')
    html.append('<nav class="sidebar-nav">')

    html.append(f'  <a href="{pfx}index.html">\U0001f3e0 Beranda</a>')

    for label, grade_path in GRADE_DIRS:
        grade_slug = grade_path.name
        html.append(f'  <div class="nav-section">{label}</div>')
        html.append(f'  <a href="{pfx}{grade_slug}/index.html">\U0001f4c1 Root Dokumen</a>')

        if (grade_path / "modul_ajar").exists():
            html.append(f'  <div class="nav-sub"><a href="{pfx}{grade_slug}/modul_ajar/index.html">\U0001f4d6 Modul Ajar</a></div>')

        if (grade_path / "Materi").exists():
            html.append(f'  <div class="nav-sub"><a href="{pfx}{grade_slug}/Materi/index.html">\U0001f4da Materi</a></div>')

    html.append('</nav>')
    return '\n'.join(html)


def render_page(content_html, title, breadcrumb_items=None, depth=0):
    sidebar = build_sidebar_html(depth=depth)

    breadcrumb_html = '<nav class="breadcrumb">'
    if breadcrumb_items:
        for label, link in breadcrumb_items:
            if link:
                breadcrumb_html += f'<a href="{link}">{label}</a> / '
            else:
                breadcrumb_html += f'<span>{label}</span>'
    breadcrumb_html += '</nav>'

    pfx = "../" * depth
    css_path = f"{pfx}css/style.css"

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} \u2014 Adm Guru Informatika 2026/2027</title>
  <link rel="stylesheet" href="{css_path}">
</head>
<body>
  <aside class="sidebar">{sidebar}</aside>
  <main class="content">
    {breadcrumb_html}
    {content_html}
  </main>
</body>
</html>"""


def generate_index():
    content = []

    content.append('<div class="hero">')
    content.append('  <h1>Administrasi Guru Informatika</h1>')
    content.append('  <p>SMA Negeri 6 Cimahi \u2014 Tahun Pelajaran 2026/2027</p>')
    content.append('  <div class="sub">Daniarsyah, S.Kom. \u00b7 NIP. 198004052022211004 \u00b7 Gol. IX</div>')
    content.append('</div>')

    total_md = 0
    total_lines = 0
    totals = {}
    for _, path in GRADE_DIRS:
        root_count = len(list(path.glob("[0-9]*.md")))
        ma_count = len(list((path / "modul_ajar").glob("*.md"))) if (path / "modul_ajar").exists() else 0
        mt_count = len(list((path / "Materi").glob("*.md"))) if (path / "Materi").exists() else 0
        subtotal = root_count + ma_count + mt_count
        sublines = sum(len(f.read_text().splitlines()) for f in path.rglob("*.md"))
        totals[path.name] = (subtotal, sublines)
        total_md += subtotal
        total_lines += sublines

    content.append('<div class="stats">')
    content.append(f'  <div class="stat-card"><div class="num">{total_md}</div><div class="label">Total Dokumen</div></div>')
    content.append(f'  <div class="stat-card accent"><div class="num">{total_lines:,}</div><div class="label">Baris Konten</div></div>')
    content.append(f'  <div class="stat-card"><div class="num">3</div><div class="label">Jenjang Kelas</div></div>')
    content.append(f'  <div class="stat-card"><div class="num">2.9 MB</div><div class="label">Ukuran Total</div></div>')
    content.append('</div>')

    content.append('<h2 style="border:none;margin-top:0;">\U0001f4da Pilih Kelas</h2>')
    content.append('<div class="grade-grid">')

    grade_data = [
        ("Kelas X", "Fase E", "2 JP/minggu", "9 Bab \u00b7 Informatika + Keterampilan Generik",
         "administrasi_guru_kelas_X"),
        ("Kelas XI", "Fase F", "5 JP/minggu", "6 Bab \u00b7 Strategi Algoritmik + AI + Data",
         "administrasi_guru_kelas_XI"),
        ("Kelas XII", "Fase F", "5 JP/minggu", "6 Bab \u00b7 IoT + Arduino + Robotics",
         "administrasi_guru_kelas_XII"),
    ]

    for name, fase, jp, desc, slug in grade_data:
        sroot, slines = totals[slug]
        ma_count = len(list((BASE_DIR / slug / "modul_ajar").glob("*.md"))) if (BASE_DIR / slug / "modul_ajar").exists() else 0
        content.append('  <div class="grade-card">')
        content.append(f'    <h3>{name}</h3>')
        content.append(f'    <span class="badge">{fase} \u00b7 {jp}</span>')
        content.append(f'    <div class="detail">{desc}<br><strong>{sroot} file</strong> \u00b7 {slines:,} baris</div>')
        content.append('    <div class="links">')
        content.append(f'      <a href="{slug}/index.html">\U0001f4c1 Root</a>')
        content.append(f'      <a href="{slug}/modul_ajar/index.html">\U0001f4d6 Modul Ajar ({ma_count})</a>')
        content.append(f'      <a href="{slug}/Materi/index.html">\U0001f4da Materi</a>')
        content.append('    </div>')
        content.append('  </div>')

    content.append('</div>')

    content.append('<div class="identity-card">')
    content.append('  <h2>\U0001f464 Identitas Guru</h2>')
    content.append('  <table>')
    content.append('    <tr><td>Nama</td><td><strong>Daniarsyah, S.Kom.</strong></td></tr>')
    content.append('    <tr><td>NIP</td><td>198004052022211004</td></tr>')
    content.append('    <tr><td>Pangkat / Gol.</td><td>IX</td></tr>')
    content.append('    <tr><td>Sekolah</td><td>SMA Negeri 6 Cimahi</td></tr>')
    content.append('    <tr><td>Mata Pelajaran</td><td>Informatika</td></tr>')
    content.append('  </table>')
    content.append('</div>')

    content.append('<div class="footer-note">')
    content.append('  Dokumen administrasi pembelajaran Informatika \u2014 siap cetak dan gunakan untuk tahun ajaran 2026/2027.')
    content.append('</div>')

    return render_page('\n'.join(content), "Beranda", [("Beranda", None)], depth=0)


def generate_grade_index(grade_label, grade_path):
    rel = grade_path.name
    content = [f'<h1>\U0001f4c1 {grade_label}</h1>']

    root_files = sorted(grade_path.glob("[0-9]*.md"))
    if root_files:
        content.append('<table><tr><th>#</th><th>File</th><th>Keterangan</th></tr>')
        desc_map = {
            "00_COVER": "Cover administrasi", "01_ANALISIS_ALOKASI_WAKTU": "Analisis alokasi waktu",
            "01b_RPE_Rincian_Pekan_Efektif": "Rincian Pekan Efektif", "02_PROTA": "Program Tahunan",
            "03_PROSEM": "Program Semester", "04_ATP": "Alur Tujuan Pembelajaran",
            "05_KKTP": "KKTP", "06_PEMETAAN_KOMPETENSI_PENILAIAN": "Pemetaan Kompetensi",
            "06b_BANK_SOAL": "Bank Soal", "06c_PROGRAM_KOKURIKULER_8_DIMENSI": "Kokurikuler 8 Dimensi",
            "07_JURNAL_MENGAJAR": "Jurnal Mengajar", "08_ANALISIS_CP_TP": "Analisis CP & TP",
            "09_DAFTAR_NILAI": "Daftar Nilai", "10_PROGRAM_REMEDIAL_PENGAYAAN": "Remedial & Pengayaan",
            "11_INVENTARIS_LAB": "Inventaris Lab", "12_JADWAL_LAB_BUKU_PRAKTIK": "Jadwal Lab & Buku Praktik",
        }
        for f in root_files:
            name = f.stem
            desc = "\u2014"
            for key, val in desc_map.items():
                if name.startswith(key[:5]) or name == key:
                    desc = val
                    break
            content.append(f'<tr><td>{f.stem[:2]}</td><td><a href="{f.stem}.html">{name}</a></td><td>{desc}</td></tr>')
        content.append('</table>')

    content.append('<div style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:2rem;">')
    ma_dir = grade_path / "modul_ajar"
    if ma_dir.exists():
        ma_count = len(list(ma_dir.glob("*.md")))
        content.append(f'<a href="modul_ajar/index.html" style="padding:0.8rem 1.25rem;background:var(--card);border:1px solid var(--border);border-radius:var(--radius);text-decoration:none;font-weight:600;">\U0001f4d6 Modul Ajar ({ma_count} file)</a>')
    mt_dir = grade_path / "Materi"
    if mt_dir.exists():
        mt_count = len(list(mt_dir.glob("*.md")))
        content.append(f'<a href="Materi/index.html" style="padding:0.8rem 1.25rem;background:var(--card);border:1px solid var(--border);border-radius:var(--radius);text-decoration:none;font-weight:600;">\U0001f4da Materi ({mt_count} file)</a>')
    content.append('</div>')

    breadcrumbs = [("Beranda", "../index.html"), (grade_label, None)]
    return render_page('\n'.join(content), grade_label, breadcrumbs, depth=1)


def generate_subsection_index(title, files, grade_label, grade_path):
    rel = grade_path.name
    content = [f'<h1>{title}</h1>']
    content.append('<table><tr><th>No</th><th>File</th></tr>')
    for i, f in enumerate(files, 1):
        fname = f.stem
        display = fname.replace("Modul_Ajar_", "").replace("_", " ")
        if len(display) > 60:
            display = display[:57] + "..."
        content.append(f'<tr><td>{i}</td><td><a href="{fname}.html">{fname}</a></td></tr>')
    content.append('</table>')

    clean_title = title.replace("<br>", " ").replace("\U0001f4d6 ", "").replace("\U0001f4da ", "")
    breadcrumbs = [
        ("Beranda", "../../index.html"),
        (grade_label, "../index.html"),
        (clean_title, None),
    ]
    return render_page('\n'.join(content), clean_title, breadcrumbs, depth=2)


def convert_all():
    shutil.rmtree(OUT_DIR, ignore_errors=True)
    css_dir = OUT_DIR / "css"
    css_dir.mkdir(parents=True)
    (css_dir / "style.css").write_text(CSS)

    (OUT_DIR / "index.html").write_text(generate_index())
    print(f"\u2713 index.html \u2014 Beranda (elegan)")

    for grade_label, grade_path in GRADE_DIRS:
        rel = grade_path.name
        grade_out = OUT_DIR / rel
        grade_out.mkdir(parents=True, exist_ok=True)
        print(f"\n\u2500\u2500 {grade_label} \u2500\u2500")

        for f in sorted(grade_path.glob("*.md")):
            try:
                text = strip_yaml_frontmatter(f.read_text(encoding="utf-8"))
                html_body = convert_md_to_html(text)
                breadcrumbs = [
                    ("Beranda", "../index.html"),
                    (grade_label, "index.html"),
                    (f.stem.replace("_", " "), None),
                ]
                page = render_page(html_body, f"{grade_label} \u2014 {f.stem}", breadcrumbs, depth=1)
                (grade_out / f"{f.stem}.html").write_text(page)
                print(f"  \u2713 {f.name}")
            except Exception as e:
                print(f"  \u2717 {f.name}: {e}")

        (grade_out / "index.html").write_text(generate_grade_index(grade_label, grade_path))
        print(f"  \u2713 index.html \u2014 {grade_label}")

        ma_dir = grade_path / "modul_ajar"
        if ma_dir.exists():
            ma_out = grade_out / "modul_ajar"
            ma_out.mkdir(parents=True, exist_ok=True)
            ma_files = sorted(ma_dir.glob("*.md"))
            for f in ma_files:
                try:
                    text = strip_yaml_frontmatter(f.read_text(encoding="utf-8"))
                    html_body = convert_md_to_html(text)
                    breadcrumbs = [
                        ("Beranda", "../../index.html"),
                        (grade_label, "../index.html"),
                        ("Modul Ajar", "index.html"),
                        (f.stem.replace("_", " "), None),
                    ]
                    page = render_page(html_body, f"{grade_label} \u2014 {f.stem}", breadcrumbs, depth=2)
                    (ma_out / f"{f.stem}.html").write_text(page)
                except Exception as e:
                    print(f"  \u2717 modul_ajar/{f.name}: {e}")

            (ma_out / "index.html").write_text(
                generate_subsection_index(f"\U0001f4d6 Modul Ajar \u2014 {grade_label}", ma_files, grade_label, grade_path))
            print(f"  \u2713 modul_ajar/index.html ({len(ma_files)} files)")

        mt_dir = grade_path / "Materi"
        if mt_dir.exists():
            mt_out = grade_out / "Materi"
            mt_out.mkdir(parents=True, exist_ok=True)
            mt_files = sorted(mt_dir.glob("*.md"))
            for f in mt_files:
                try:
                    text = strip_yaml_frontmatter(f.read_text(encoding="utf-8"))
                    html_body = convert_md_to_html(text)
                    breadcrumbs = [
                        ("Beranda", "../../index.html"),
                        (grade_label, "../index.html"),
                        ("Materi", "index.html"),
                        (f.stem.replace("_", " "), None),
                    ]
                    page = render_page(html_body, f"{grade_label} \u2014 {f.stem}", breadcrumbs, depth=2)
                    (mt_out / f"{f.stem}.html").write_text(page)
                except Exception as e:
                    print(f"  \u2717 Materi/{f.name}: {e}")

            (mt_out / "index.html").write_text(
                generate_subsection_index(f"\U0001f4da Materi \u2014 {grade_label}", mt_files, grade_label, grade_path))
            print(f"  \u2713 Materi/index.html ({len(mt_files)} files)")

    total_html = len(list(OUT_DIR.rglob("*.html")))
    print(f"\n{'='*50}")
    print(f"Selesai! {total_html} halaman HTML + 1 CSS")
    print(f"Buka: {OUT_DIR / 'index.html'}")

if __name__ == "__main__":
    convert_all()
