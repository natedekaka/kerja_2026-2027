#!/usr/bin/env python3
"""Convert all .md administration files to a static HTML website."""

import os
import re
import markdown
import shutil
from pathlib import Path

BASE_DIR = Path(os.path.expanduser("~/Documents/kerja_2026-2027"))
OUT_DIR = BASE_DIR / "docs"
GRADE_DIRS = [
    ("Kelas X (Fase E)", BASE_DIR / "administrasi_guru_kelas_X"),
    ("Kelas XI (Fase F)", BASE_DIR / "administrasi_guru_kelas_XI"),
    ("Kelas XII (Fase F)", BASE_DIR / "administrasi_guru_kelas_XII"),
]

MD = markdown.Markdown(extensions=["extra", "toc", "nl2br", "sane_lists", "smarty"])

CSS = """/* ============================================
   ADMINISTRASI GURU INFORMATIKA
   Theme: Portal Pemerintah (Rumah Pendidikan)
   SMA Negeri 6 Cimahi — 2026/2027
   ============================================ */

:root {
  --primary: #003D7A;
  --primary-dark: #002B56;
  --primary-light: #1A56DB;
  --accent: #F59E0B;
  --accent-light: #FEF3C7;
  --bg: #FFFFFF;
  --bg-section: #F0F4F8;
  --card: #FFFFFF;
  --border: #E2E8F0;
  --text: #1E293B;
  --text-muted: #64748B;
  --text-light: #94A3B8;
  --sidebar-bg: #002B56;
  --sidebar-hover: rgba(255,255,255,0.06);
  --radius: 12px;
  --shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-lg: 0 10px 25px rgba(0,0,0,0.08);
  --header-height: 56px;
  --transition: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.dark-mode {
  --primary: #60A5FA;
  --primary-dark: #1E3A5F;
  --primary-light: #93C5FD;
  --accent: #FBBF24;
  --accent-light: #78350F;
  --bg: #0F172A;
  --bg-section: #1E293B;
  --card: #1E293B;
  --border: #334155;
  --text: #F1F5F9;
  --text-muted: #94A3B8;
  --text-light: #64748B;
  --shadow: 0 1px 3px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.2);
  --shadow-lg: 0 10px 25px rgba(0,0,0,0.4);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  display: flex;
  min-height: 100vh;
}

/* ═══ SIDEBAR ═══ */
.sidebar {
  width: 260px;
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
  padding: 1.5rem 1.25rem;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.sidebar-header .logo-icon {
  width: 42px; height: 42px;
  background: rgba(255,255,255,0.1);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.3rem;
  margin-bottom: 0.6rem;
}
.sidebar-header h1 {
  font-size: 0.95rem;
  font-weight: 700;
  color: #fff;
  line-height: 1.3;
}
.sidebar-header p {
  font-size: 0.68rem;
  color: rgba(255,255,255,0.45);
  margin-top: 0.2rem;
  line-height: 1.4;
}
.sidebar-nav { padding: 0.5rem 0; }
.sidebar-nav a {
  display: flex; align-items: center; gap: 0.5rem;
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
  font-size: 0.62rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: rgba(255,255,255,0.3);
  padding: 1rem 1.25rem 0.25rem;
  font-weight: 600;
}
.sidebar-nav .nav-sub a { padding-left: 2.75rem; font-size: 0.78rem; }

/* ═══ CONTENT ═══ */
.content { margin-left: 260px; flex: 1; padding: 0; max-width: 100%; }

.content-inner {
  max-width: 960px;
  margin: 0 auto;
  padding: 2rem 2.5rem 3rem;
}

/* ═══ BREADCRUMB ═══ */
.breadcrumb-wrap {
  background: var(--bg-section);
  border-bottom: 1px solid var(--border);
  padding: 0.6rem 2.5rem;
}
.breadcrumb {
  max-width: 960px;
  margin: 0 auto;
  font-size: 0.78rem;
  color: var(--text-muted);
}
.breadcrumb a { color: var(--primary-light); text-decoration: none; }
.breadcrumb a:hover { text-decoration: underline; }

/* ═══ TYPOGRAPHY ═══ */
.content h1 {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--primary);
  margin: 1.5rem 0 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 3px solid var(--accent);
}
.content h2 { font-size: 1.25rem; font-weight: 700; color: var(--primary); margin: 1.75rem 0 0.75rem; }
.content h3 { font-size: 1.1rem; font-weight: 600; color: var(--text); margin: 1.25rem 0 0.5rem; }
.content h4 { font-size: 1rem; font-weight: 600; margin: 1rem 0 0.5rem; }
.content p { margin-bottom: 1rem; color: var(--text); }
.content a { color: var(--primary); }
.content ul, .content ol { margin: 0.5rem 0 1rem 1.5rem; }
.content li { margin-bottom: 0.3rem; }
.content hr { border: none; border-top: 2px solid var(--border); margin: 2rem 0; }
.content strong { color: var(--text); }

/* ═══ TABLES ═══ */
.content table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0 1.5rem;
  font-size: 0.86rem;
}
.content th, .content td {
  border: 1px solid var(--border);
  padding: 0.55rem 0.7rem;
  text-align: left;
  vertical-align: top;
}
.content th {
  background: var(--bg-section);
  font-weight: 700;
  font-size: 0.8rem;
  color: var(--primary);
}
.content tr:nth-child(even) { background: #FAFBFC; }
.content tr:hover { background: #EEF2FF; }

/* ═══ CODE ═══ */
.content code {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.85em;
  background: #F1F5F9;
  padding: 0.15em 0.4em;
  border-radius: 4px;
}
.content pre {
  background: #1E293B;
  color: #E2E8F0;
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
  background: #F0F4FF;
  padding: 0.75rem 1.25rem;
  margin: 1rem 0;
  border-radius: 0 var(--radius) var(--radius) 0;
}

/* ═══ HERO (Frontpage) ═══ */
.hero {
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
  color: #fff;
  padding: 3rem 2.5rem;
  margin-bottom: 2.5rem;
  border-radius: var(--radius);
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute; top: -60%; right: -15%;
  width: 500px; height: 500px;
  background: rgba(255,255,255,0.03);
  border-radius: 50%;
}
.hero::after {
  content: ''; position: absolute; bottom: -30%; left: -10%;
  width: 300px; height: 300px;
  background: rgba(255,255,255,0.02);
  border-radius: 50%;
}
.hero .hero-icon {
  width: 56px; height: 56px;
  background: rgba(255,255,255,0.12);
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.6rem;
  margin-bottom: 1rem;
  position: relative; z-index: 1;
}
.hero h1 {
  font-size: 1.8rem;
  font-weight: 800;
  color: #fff;
  border: none;
  padding: 0;
  margin: 0 0 0.35rem;
  position: relative; z-index: 1;
}
.hero p {
  font-size: 1rem;
  color: rgba(255,255,255,0.85);
  margin: 0;
  position: relative; z-index: 1;
}
.hero .sub {
  font-size: 0.82rem;
  color: rgba(255,255,255,0.55);
  margin-top: 0.5rem;
  position: relative; z-index: 1;
}

/* ═══ CATEGORY CARDS (Root · Modul Ajar · Materi) ═══ */
.category-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
  max-width: 900px;
  margin: -1.25rem auto 2.5rem;
}
.cat-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.75rem 1.5rem;
  text-align: center;
  box-shadow: var(--shadow);
  transition: transform var(--transition), box-shadow var(--transition);
  position: relative;
  overflow: hidden;
}
.cat-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  border-radius: var(--radius) var(--radius) 0 0;
}
.cat-card-root {
  background: linear-gradient(180deg, #F0F7FF 0%, var(--card) 40%);
}
.cat-card-modul {
  background: linear-gradient(180deg, #ECFDF5 0%, var(--card) 40%);
}
.cat-card-materi {
  background: linear-gradient(180deg, #F5F3FF 0%, var(--card) 40%);
}
.cat-card-root::before { background: var(--primary); }
.cat-card-modul::before { background: #059669; }
.cat-card-materi::before { background: #7C3AED; }
.cat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}
.cat-card .cat-icon {
  width: 52px; height: 52px;
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 0.75rem;
  font-size: 1.4rem;
}
.cat-card-root .cat-icon { background: #EFF6FF; }
.cat-card-modul .cat-icon { background: #ECFDF5; }
.cat-card-materi .cat-icon { background: #F5F3FF; }
.cat-card h3 {
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
  border: none;
  padding: 0;
}
.cat-card-root h3 { color: var(--primary); }
.cat-card-modul h3 { color: #059669; }
.cat-card-materi h3 { color: #7C3AED; }
.cat-card .cat-desc {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-bottom: 0.75rem;
}
.cat-card .cat-stats {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 1.25rem;
}
.cat-card .cat-stat {
  font-size: 0.7rem;
  color: var(--text-muted);
  background: var(--bg-section);
  padding: 0.2rem 0.5rem;
  border-radius: 6px;
}
.cat-card .cat-stat strong {
  color: var(--text);
  font-weight: 600;
}
.cat-card .cat-grade-links {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.cat-card .cat-grade-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.2rem;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  text-decoration: none;
  letter-spacing: 0.02em;
  transition: all var(--transition);
  border: 1.5px solid;
  min-width: 52px;
}
.cat-card .cat-grade-btn-x {
  background: #DBEAFE;
  color: #1D4ED8;
  border-color: #BFDBFE;
}
.cat-card .cat-grade-btn-xi {
  background: #D1FAE5;
  color: #047857;
  border-color: #A7F3D0;
}
.cat-card .cat-grade-btn-xii {
  background: #FEF3C7;
  color: #B45309;
  border-color: #FDE68A;
}
.cat-card .cat-grade-btn:hover {
  filter: brightness(1.08);
  transform: scale(1.05);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.dark-mode .cat-card .cat-grade-btn-x {
  background: rgba(59,130,246,0.15);
  color: #93C5FD;
  border-color: rgba(59,130,246,0.3);
}
.dark-mode .cat-card .cat-grade-btn-xi {
  background: rgba(16,185,129,0.15);
  color: #6EE7B7;
  border-color: rgba(16,185,129,0.3);
}
.dark-mode .cat-card .cat-grade-btn-xii {
  background: rgba(245,158,11,0.15);
  color: #FCD34D;
  border-color: rgba(245,158,11,0.3);
}

/* dark mode overrides */
.dark-mode .cat-card-root .cat-icon { background: rgba(96,165,250,0.15); }
.dark-mode .cat-card-modul .cat-icon { background: rgba(52,211,153,0.15); }
.dark-mode .cat-card-materi .cat-icon { background: rgba(167,139,250,0.15); }
.dark-mode .cat-card-root { background: linear-gradient(180deg, rgba(96,165,250,0.07) 0%, var(--card) 40%); }
.dark-mode .cat-card-modul { background: linear-gradient(180deg, rgba(52,211,153,0.07) 0%, var(--card) 40%); }
.dark-mode .cat-card-materi { background: linear-gradient(180deg, rgba(167,139,250,0.07) 0%, var(--card) 40%); }
.dark-mode .cat-stat { background: rgba(255,255,255,0.05); }

/* responsive */
@media (max-width: 768px) {
  .category-cards { grid-template-columns: 1fr; gap: 1rem; margin: -0.5rem auto 2rem; }
  .cat-card { padding: 1.25rem 1rem; }
  .cat-card .cat-icon { width: 44px; height: 44px; font-size: 1.2rem; }
  .cat-card h3 { font-size: 0.95rem; }
}
@media (max-width: 480px) {
  .category-cards { gap: 0.75rem; }
  .cat-card { padding: 1rem 0.75rem; }
  .cat-card .cat-stats { gap: 0.4rem; }
  .cat-card .cat-stat { font-size: 0.65rem; }
}

/* ═══ STATS ROW ═══ */
.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 2.5rem;
}
.stat-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem 1rem;
  text-align: center;
  box-shadow: var(--shadow);
}
.stat-card .num {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--primary);
  line-height: 1.2;
}
.stat-card .num.accent { color: var(--accent); }
.stat-card .label {
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-top: 0.15rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* ═══ SECTION TITLE ═══ */
.section-title {
  display: flex; align-items: center; gap: 0.5rem;
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--primary);
  margin: 2rem 0 1.25rem;
}
.section-title .icon {
  width: 36px; height: 36px;
  background: #EEF2FF;
  border-radius: 10px;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 1rem;
}

/* ═══ GRADE CARDS (like Ruang cards) ═══ */
.grade-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
  margin: 1.5rem 0;
}
.grade-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  transition: all 0.2s;
  cursor: default;
  position: relative;
}
.grade-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-light);
}
.grade-card .card-icon {
  width: 48px; height: 48px;
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.4rem;
  margin-bottom: 1rem;
}
.grade-card .card-icon.x { background: #DBEAFE; }
.grade-card .card-icon.xi { background: #DCFCE7; }
.grade-card .card-icon.xii { background: #FEF3C7; }
.grade-card h3 {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 0.15rem;
}
.grade-card .badge {
  display: inline-block;
  background: #EEF2FF;
  color: var(--primary);
  font-size: 0.68rem;
  padding: 0.15rem 0.55rem;
  border-radius: 999px;
  font-weight: 600;
  margin-bottom: 0.7rem;
}
.grade-card .detail {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 0.9rem;
  line-height: 1.5;
}
.grade-card .links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}
.grade-card .links a {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.3rem 0.65rem;
  background: var(--bg-section);
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 0.75rem;
  color: var(--text);
  text-decoration: none;
  transition: all 0.12s;
  font-weight: 500;
}
.grade-card .links a:hover {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}

/* ═══ IDENTITY CARD ═══ */
.identity-section {
  background: var(--bg-section);
  border-radius: var(--radius);
  padding: 1.5rem 2rem;
  margin: 2rem 0;
  border: 1px solid var(--border);
}
.identity-section h2 {
  margin: 0 0 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border);
}
.identity-grid {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.3rem 1.5rem;
  font-size: 0.88rem;
}
.identity-grid .label {
  color: var(--text-muted);
  font-weight: 600;
}
.identity-grid .value { color: var(--text); font-weight: 500; }

/* ═══ FOOTER ═══ */
.site-footer {
  background: var(--primary-dark);
  color: rgba(255,255,255,0.7);
  padding: 2rem 2.5rem 1.5rem;
  margin-top: 3rem;
}
.site-footer .footer-inner {
  max-width: 960px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}
.site-footer .footer-brand h3 {
  color: #fff;
  font-size: 0.95rem;
  margin: 0 0 0.2rem;
}
.site-footer .footer-brand p {
  font-size: 0.75rem;
  color: rgba(255,255,255,0.5);
  margin: 0;
}
.site-footer .footer-links {
  display: flex; gap: 1.5rem; flex-wrap: wrap;
}
.site-footer .footer-links a {
  color: rgba(255,255,255,0.6);
  text-decoration: none;
  font-size: 0.78rem;
  transition: color 0.15s;
  display: inline-flex; align-items: center; gap: 0.3rem;
}
.site-footer .footer-links a:hover { color: var(--accent); }
.site-footer .footer-links .brand {
  font-weight: 700;
  letter-spacing: 0.02em;
  color: rgba(255,255,255,0.85);
}
.site-footer .footer-links .brand:hover { color: var(--accent); }
.site-footer .footer-bottom {
  max-width: 960px;
  margin: 1.25rem auto 0;
  padding-top: 1rem;
  border-top: 1px solid rgba(255,255,255,0.08);
  text-align: center;
  font-size: 0.72rem;
  color: rgba(255,255,255,0.4);
}

/* ═══ RESPONSIVE ═══ */

/* Tablet landscape */
@media (max-width: 1024px) {
  .content-inner { max-width: 100%; padding: 1.5rem 2rem; }
  .grade-grid { grid-template-columns: repeat(2, 1fr); }
  .stats-row { grid-template-columns: repeat(2, 1fr); }
  .content h1 { font-size: 1.4rem; }
  .hero h1 { font-size: 1.5rem; }
  .hero::before, .hero::after { display: none; }
}

/* Tablet portrait / small laptop */
@media (max-width: 768px) {
  .sidebar-header { padding: 1rem 1.25rem; }
  .sidebar-nav a { padding: 0.4rem 1.25rem; font-size: 0.78rem; }
  .content { margin-left: 0; }
  .content-inner { padding: 1.25rem 1.5rem; max-width: 100%; }
  .breadcrumb-wrap { padding: 0.5rem 1.5rem; }
  .breadcrumb { font-size: 0.72rem; }

  .hero { padding: 1.75rem 1.5rem; margin-bottom: 1.5rem; }
  .hero h1 { font-size: 1.3rem; }
  .hero p { font-size: 0.9rem; }
  .hero::before, .hero::after { display: none; }

  .grade-grid { grid-template-columns: 1fr; gap: 1rem; }
  .stats-row { grid-template-columns: repeat(2, 1fr); gap: 0.6rem; }
  .stat-card { padding: 0.9rem 0.75rem; }
  .stat-card .num { font-size: 1.3rem; }

  .grade-card { padding: 1.25rem; }
  .grade-card .links a { font-size: 0.72rem; padding: 0.25rem 0.55rem; }

  .content h1 { font-size: 1.2rem; }
  .content h2 { font-size: 1.1rem; }

  .site-footer { padding: 1.5rem 1.5rem 1rem; }
  .site-footer .footer-inner { flex-direction: column; text-align: center; gap: 1rem; }

  .identity-section { padding: 1.25rem 1.25rem; }
  .identity-grid { font-size: 0.82rem; gap: 0.25rem 1rem; }
  .identity-grid .label { width: 100px; }

  /* Tables scroll horizontally on mobile */
  .content table { font-size: 0.78rem; display: block; overflow-x: auto; white-space: nowrap; }
  .content th, .content td { padding: 0.4rem 0.5rem; }
  .content pre { font-size: 0.75rem; padding: 1rem; }
}

/* Phone */
@media (max-width: 480px) {
  .sidebar-header { padding: 0.75rem 1rem; }
  .sidebar-header h1 { font-size: 0.85rem; }
  .sidebar-nav a { padding: 0.35rem 1rem; font-size: 0.72rem; }
  .sidebar-nav .nav-section { font-size: 0.55rem; }
  .sidebar-nav .nav-sub a { padding-left: 2rem; }

  .content-inner { padding: 1rem 1rem; }
  .breadcrumb-wrap { padding: 0.4rem 1rem; }
  .breadcrumb { font-size: 0.65rem; }

  .hero { padding: 1.25rem 1rem; border-radius: 8px; }
  .hero h1 { font-size: 1.1rem; }
  .hero p { font-size: 0.8rem; }
  .hero .sub { font-size: 0.7rem; }
  .hero .hero-icon { width: 40px; height: 40px; font-size: 1.2rem; margin-bottom: 0.6rem; }
  .hero::before, .hero::after { display: none; }

  .stats-row { grid-template-columns: repeat(2, 1fr); gap: 0.5rem; }
  .stat-card { padding: 0.7rem 0.5rem; }
  .stat-card .num { font-size: 1.1rem; }
  .stat-card .label { font-size: 0.62rem; }

  .grade-card { padding: 1rem; }
  .grade-card .card-icon { width: 38px; height: 38px; font-size: 1.1rem; margin-bottom: 0.6rem; }
  .grade-card h3 { font-size: 0.9rem; }
  .grade-card .detail { font-size: 0.72rem; }
  .grade-card .links a { font-size: 0.65rem; padding: 0.2rem 0.45rem; }

  .content h1 { font-size: 1.1rem; }
  .content h2 { font-size: 1rem; }
  .content h3 { font-size: 0.9rem; }

  .section-title { font-size: 1rem; }
  .section-title .icon { width: 28px; height: 28px; font-size: 0.8rem; }

  .identity-section { padding: 1rem; }
  .identity-grid { font-size: 0.75rem; }
  .identity-grid .label { width: 80px; }

  .site-footer { padding: 1.25rem 1rem 0.75rem; }
  .site-footer .footer-brand h3 { font-size: 0.82rem; }
  .site-footer .footer-brand p { font-size: 0.65rem; }
  .site-footer .footer-links a { font-size: 0.7rem; }
  .site-footer .footer-bottom { font-size: 0.62rem; }

  .content table { font-size: 0.72rem; }
  .content th, .content td { padding: 0.3rem 0.4rem; }
  .content pre { font-size: 0.68rem; padding: 0.75rem; }
  .content ul, .content ol { margin-left: 1rem; }
  .content blockquote { padding: 0.5rem 0.75rem; }
  .search-wrap { margin: 0 auto 1rem; }
  .search-wrap input { padding: 0.6rem 0.8rem 0.6rem 2.2rem; font-size: 0.8rem; }
}

@media print {
  .sidebar { display: none; }
  .content { margin-left: 0; }
  .site-footer { display: none; }
  .breadcrumb-wrap { display: none; }
  .hero { background: none !important; color: #000 !important; border: 1px solid #ccc; }
  .hero h1 { color: #000 !important; }
  .hero p { color: #333 !important; }
  .hero .sub { color: #666 !important; }
  .grade-card { break-inside: avoid; }
  .content-inner { max-width: 100%; }
}

/* ═══ ANIMATIONS ═══ */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 0 0 rgba(245,158,11,0.3); }
  50%      { box-shadow: 0 0 0 8px rgba(245,158,11,0); }
}
.anim-fade-in  { animation: fadeIn 0.5s ease both; }
.anim-fade-up  { animation: fadeInUp 0.5s ease both; }
.anim-delay-1  { animation-delay: 0.1s; }
.anim-delay-2  { animation-delay: 0.2s; }
.anim-delay-3  { animation-delay: 0.3s; }
.anim-delay-4  { animation-delay: 0.4s; }
.anim-delay-5  { animation-delay: 0.5s; }

/* ═══ DARK MODE TOGGLE ═══ */
.theme-toggle {
  position: fixed;
  bottom: 24px; right: 24px;
  z-index: 999;
  width: 44px; height: 44px;
  border-radius: 50%;
  border: none;
  background: var(--primary);
  color: #fff;
  font-size: 1.2rem;
  cursor: pointer;
  box-shadow: var(--shadow-lg);
  transition: transform var(--transition), background var(--transition);
  display: flex; align-items: center; justify-content: center;
}
.theme-toggle:hover {
  transform: scale(1.1);
  background: var(--accent);
  color: #000;
}

/* ═══ BACK TO TOP ═══ */
.back-to-top {
  position: fixed;
  bottom: 76px; right: 24px;
  z-index: 999;
  width: 44px; height: 44px;
  border-radius: 50%;
  border: none;
  background: var(--card);
  color: var(--primary);
  font-size: 1.1rem;
  cursor: pointer;
  box-shadow: var(--shadow-lg);
  transition: transform var(--transition), opacity var(--transition), background var(--transition);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; pointer-events: none;
}
.back-to-top.visible {
  opacity: 1; pointer-events: auto;
}
.back-to-top:hover {
  transform: scale(1.1);
  background: var(--primary);
  color: #fff;
}

/* ═══ HAMBURGER MOBILE ═══ */
.hamburger {
  display: none;
  position: fixed;
  top: 12px; left: 12px;
  z-index: 200;
  width: 40px; height: 40px;
  border-radius: 8px;
  border: none;
  background: var(--primary);
  color: #fff;
  font-size: 1.2rem;
  cursor: pointer;
  box-shadow: var(--shadow);
  transition: background var(--transition);
  align-items: center; justify-content: center;
}
.hamburger:hover { background: var(--primary-light); }
.sidebar-overlay {
  display: none;
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  z-index: 99;
}

/* ═══ SEARCH ═══ */
.search-wrap {
  width: 100%;
  max-width: 600px;
  margin: -1.5rem auto 2rem;
  position: relative;
}
.search-wrap input {
  width: 100%;
  padding: 0.85rem 1rem 0.85rem 2.8rem;
  border: 2px solid var(--border);
  border-radius: 50px;
  font-size: 0.9rem;
  background: var(--card);
  color: var(--text);
  transition: border-color var(--transition), box-shadow var(--transition);
  outline: none;
}
.search-wrap input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(0,61,122,0.12);
}
.search-wrap .search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 1rem;
  pointer-events: none;
}
.search-wrap .search-clear {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 1rem;
  display: none;
  padding: 0.25rem;
}
.search-wrap .search-clear.visible { display: block; }
.search-no-results {
  display: none;
  padding: 2rem;
  text-align: center;
  color: var(--text-muted);
}
.search-no-results.visible { display: block; }
.search-match {
  background: rgba(245,158,11,0.2);
  border-radius: 2px;
  padding: 0 0.1rem;
}

/* ═══ TEACHER SECTION ═══ */
.teacher-section {
  background: var(--bg-section);
  border-radius: var(--radius);
  padding: 2rem;
  margin: 2rem auto;
  max-width: 860px;
  text-align: center;
}
.teacher-section h2 {
  font-size: 1.2rem;
  color: var(--text);
  margin-bottom: 1.25rem;
}
.teacher-section h2 span {
  color: var(--accent);
}
.teacher-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  text-align: center;
}
.teacher-card {
  background: var(--card);
  padding: 1.25rem 0.75rem;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  transition: transform var(--transition), box-shadow var(--transition);
  border: 1px solid var(--border);
}
.teacher-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}
.teacher-card .avatar {
  width: 56px; height: 56px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-light));
  color: #fff;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 0.6rem;
  font-size: 1.3rem;
  font-weight: 700;
}
.teacher-card .name {
  font-weight: 600;
  font-size: 0.85rem;
  color: var(--text);
}
.teacher-card .role {
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-top: 0.15rem;
}
.teacher-card .nip {
  font-size: 0.65rem;
  color: var(--text-light);
  margin-top: 0.1rem;
}

/* ═══ PROGRESS BARS ═══ */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  max-width: 860px;
  margin: 2rem auto;
}
.stat-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem;
  text-align: center;
  transition: transform var(--transition), box-shadow var(--transition);
}
.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
.stat-card .stat-icon {
  font-size: 1.5rem;
  margin-bottom: 0.4rem;
}
.stat-card .stat-number {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--primary);
  line-height: 1.2;
}
.stat-card .stat-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.15rem;
}
.progress-wrap {
  margin: 2rem auto;
  max-width: 860px;
}
.progress-item {
  margin-bottom: 1rem;
}
.progress-item .progress-header {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  margin-bottom: 0.3rem;
}
.progress-item .progress-header .grade-name {
  font-weight: 600;
  color: var(--text);
}
.progress-item .progress-header .grade-pct {
  color: var(--primary);
  font-weight: 600;
}
.progress-bar-bg {
  width: 100%;
  height: 8px;
  background: var(--border);
  border-radius: 4px;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  border-radius: 4px;
  background: linear-gradient(90deg, var(--primary), var(--primary-light));
  transition: width 0.8s ease;
}

/* ═══ BADGE / TAG ═══ */
.doc-badge {
  display: inline-block;
  font-size: 0.6rem;
  font-weight: 600;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  vertical-align: middle;
  margin-left: 0.25rem;
}
.doc-badge-blue {
  background: #DBEAFE; color: #1E40AF;
}
.doc-badge-green {
  background: #D1FAE5; color: #065F46;
}
.doc-badge-purple {
  background: #EDE9FE; color: #5B21B6;
}
.dark-mode .doc-badge-blue {
  background: #1E3A5F; color: #93C5FD;
}
.dark-mode .doc-badge-green {
  background: #064E3B; color: #6EE7B7;
}
.dark-mode .doc-badge-purple {
  background: #3B0764; color: #C4B5FD;
}

/* ═══ GLOW ENHANCEMENTS ═══ */
.grade-card { transition: transform var(--transition), box-shadow var(--transition); }
.grade-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.grade-card .grade-icon { transition: transform var(--transition); }
.grade-card:hover .grade-icon { transform: scale(1.15); }

.cta-card-group a { transition: transform var(--transition), box-shadow var(--transition); }
.cta-card-group a:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }

.footer-links a { transition: opacity var(--transition); }
.footer-links a:hover { opacity: 0.8; }

.sidebar-nav a { transition: background var(--transition), border-color var(--transition), color var(--transition); }

/* ═══ MOBILE OVERRIDES ═══ */
@media (max-width: 768px) {
  .hamburger { display: flex; }
  .sidebar-overlay.active { display: block; animation: fadeIn 0.2s ease; }
  .sidebar {
    width: 280px;
    height: 100vh;
    position: fixed;
    top: 0; left: 0;
    z-index: 100;
    transform: translateX(-100%);
    transition: transform 0.3s ease;
  }
  .sidebar.open { transform: translateX(0); }
  .search-wrap { margin: 0 auto 1.5rem; }
}

@media (min-width: 769px) {
  .sidebar { transform: none !important; }
  .sidebar-overlay { display: none !important; }
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
    html.append('  <h1>\U0001f4cb Adm. Guru &middot; Modul Ajar &middot; Materi</h1>')
    html.append('  <p>MGMP Informatika<br>SMA N 6 Cimahi &middot; 2026/2027</p>')
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

    bc = ''
    if breadcrumb_items:
        bc = '<nav class="breadcrumb">'
        for label, link in breadcrumb_items:
            if link:
                bc += f'<a href="{link}">{label}</a> / '
            else:
                bc += f'<span>{label}</span>'
        bc += '</nav>'

    pfx = "../" * depth
    css_path = f"{pfx}css/style.css"

    js_path = f"{pfx}js/app.js"

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} \u2014 Adm. Guru &amp; Modul Ajar 2026/2027</title>
  <link rel="stylesheet" href="{css_path}">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>\U0001f4cb</text></svg>">
</head>
<body>
  <button class="hamburger" id="hamburgerBtn" aria-label="Toggle menu">\u2630</button>
  <div class="sidebar-overlay" id="sidebarOverlay"></div>
  <aside class="sidebar" id="sidebar">{sidebar}</aside>
  <main class="content">
    <div class="breadcrumb-wrap">{bc}</div>
    <div class="content-inner">
    {content_html}
    </div>
  </main>
  <button class="back-to-top" id="backToTop" aria-label="Back to top">\u2191</button>
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">\u263d</button>
  <script src="{js_path}"></script>
</body>
</html>"""


def generate_index():
    content = []

    # ─── scan totals ───
    total_md = 0
    total_lines = 0
    totals = {}
    grade_data_info = [
        ("Kelas X", "Fase E", "2 JP/minggu", "x", "9 Bab &middot; Informatika &amp; Keterampilan Generik",
         "administrasi_guru_kelas_X"),
        ("Kelas XI", "Fase F", "5 JP/minggu", "xi", "6 Bab &middot; Strategi Algoritmik + AI + Data",
         "administrasi_guru_kelas_XI"),
        ("Kelas XII", "Fase F", "5 JP/minggu", "xii", "6 Bab &middot; IoT + Arduino + Robotics",
         "administrasi_guru_kelas_XII"),
    ]
    grade_stats = {}
    for name, fase, jp, short, desc, slug in grade_data_info:
        root_count = len(list((BASE_DIR / slug).glob("[0-9]*.md")))
        ma_count = len(list((BASE_DIR / slug / "modul_ajar").glob("*.md"))) if (BASE_DIR / slug / "modul_ajar").exists() else 0
        mt_count = len(list((BASE_DIR / slug / "Materi").glob("*.md"))) if (BASE_DIR / slug / "Materi").exists() else 0
        subtotal = root_count + ma_count + mt_count
        sublines = sum(len(f.read_text().splitlines()) for f in (BASE_DIR / slug).rglob("*.md"))
        totals[slug] = (subtotal, sublines)
        grade_stats[short] = {"total": subtotal, "lines": sublines, "root": root_count, "ma": ma_count, "mt": mt_count}
        total_md += subtotal
        total_lines += sublines

    # ─── hero ───
    content.append('<div class="hero">')
    content.append('  <div class="hero-icon">\U0001f4da</div>')
    content.append('  <h1>Administrasi Guru, Modul Ajar &amp; Materi</h1>')
    content.append('  <p>MGMP Informatika SMA Negeri 6 Cimahi \u2014 Tahun Pelajaran 2026/2027</p>')
    content.append('  <div class="sub">Musyawarah Guru Mata Pelajaran Informatika</div>')
    content.append('</div>')

    # ─── category cards (Root · Modul Ajar · Materi) ───
    total_root = sum(grade_stats[s["short"]]["root"] for s in [{"short":"x"},{"short":"xi"},{"short":"xii"}])
    total_ma = sum(grade_stats[s["short"]]["ma"] for s in [{"short":"x"},{"short":"xi"},{"short":"xii"}])
    total_mt = sum(grade_stats[s["short"]]["mt"] for s in [{"short":"x"},{"short":"xi"},{"short":"xii"}])

    cat_items = [
        ("root", "\U0001f4c1", "Root Dokumen", "Administrasi guru: prota, prosem, ATP, jurnal, dll.", total_root,
         [("X", grade_stats["x"]["root"]), ("XI", grade_stats["xi"]["root"]), ("XII", grade_stats["xii"]["root"])],
         "#"),
        ("modul", "\U0001f4d6", "Modul Ajar", "Perangkat ajar lengkap setiap pertemuan.", total_ma,
         [("X", grade_stats["x"]["ma"]), ("XI", grade_stats["xi"]["ma"]), ("XII", grade_stats["xii"]["ma"])],
         "#"),
        ("materi", "\U0001f4da", "Materi", "Bahan ajar per bab untuk setiap kelas.", total_mt,
         [("X", grade_stats["x"]["mt"]), ("XI", grade_stats["xi"]["mt"]), ("XII", grade_stats["xii"]["mt"])],
         "#"),
    ]

    content.append('<div class="category-cards">')
    for key, icon, title, desc, total, per_grade, link in cat_items:
        content.append(f'  <div class="cat-card cat-card-{key} anim-fade-up">')
        content.append(f'    <div class="cat-icon">{icon}</div>')
        content.append(f'    <h3>{title}</h3>')
        content.append(f'    <div class="cat-desc">{desc}</div>')
        content.append('    <div class="cat-stats">')
        for grade_lbl, count in per_grade:
            if count > 0:
                content.append(f'      <span class="cat-stat">Kelas {grade_lbl}: <strong>{count}</strong></span>')
        content.append(f'      <span class="cat-stat">Total: <strong>{total}</strong></span>')
        content.append('    </div>')
        # Tombol per kelas
        grade_slugs = [
            ("X", "administrasi_guru_kelas_X", "x"),
            ("XI", "administrasi_guru_kelas_XI", "xi"),
            ("XII", "administrasi_guru_kelas_XII", "xii"),
        ]
        content.append('    <div class="cat-grade-links">')
        for grade_lbl, slug, gs in grade_slugs:
            if key == "root":
                href = f"{slug}/index.html"
            elif key == "modul":
                href = f"{slug}/modul_ajar/index.html"
            else:
                href = f"{slug}/Materi/index.html"
            content.append(f'      <a href="{href}" class="cat-grade-btn cat-grade-btn-{gs}">{grade_lbl} \u2192</a>')
        content.append('    </div>')
        content.append('  </div>')
    content.append('</div>')

    # ─── search bar ───
    content.append('<div class="search-wrap anim-fade-up anim-delay-1">')
    content.append('  <span class="search-icon">\U0001f50d</span>')
    content.append('  <input type="text" id="docSearch" placeholder="Cari dokumen, kelas, atau topik..." autocomplete="off">')
    content.append('  <button class="search-clear" id="searchClear">&times;</button>')
    content.append('</div>')

    # ─── stats grid ───
    content.append('<div class="stats-grid">')
    content.append(f'  <div class="stat-card anim-fade-up anim-delay-1"><div class="stat-icon">\U0001f4c4</div><div class="stat-number">{total_md}</div><div class="stat-label">Total Dokumen</div></div>')
    content.append(f'  <div class="stat-card anim-fade-up anim-delay-2"><div class="stat-icon">\U0001f4dd</div><div class="stat-number">{total_lines:,}</div><div class="stat-label">Baris Konten</div></div>')
    content.append(f'  <div class="stat-card anim-fade-up anim-delay-3"><div class="stat-icon">\U0001f3eb</div><div class="stat-number">3</div><div class="stat-label">Jenjang Kelas</div></div>')
    content.append(f'  <div class="stat-card anim-fade-up anim-delay-4"><div class="stat-icon">\U0001f4e6</div><div class="stat-number">197</div><div class="stat-label">File .md</div></div>')
    content.append('</div>')

    # ─── progress bars ───
    content.append('<div class="progress-wrap">')
    max_files = max(s["total"] for s in grade_stats.values())
    for grade_lbl, short, slug in [("Kelas X — Fase E", "x", "administrasi_guru_kelas_X"),
                                    ("Kelas XI — Fase F", "xi", "administrasi_guru_kelas_XI"),
                                    ("Kelas XII — Fase F", "xii", "administrasi_guru_kelas_XII")]:
        st = grade_stats[short]
        pct = (st["total"] / max_files * 100) if max_files else 0
        content.append('  <div class="progress-item anim-fade-up">')
        content.append(f'    <div class="progress-header"><span class="grade-name">{grade_lbl}</span><span class="grade-pct">{st["total"]} dokumen &middot; {st["lines"]:,} baris</span></div>')
        content.append(f'    <div class="progress-bar-bg"><div class="progress-bar-fill" style="width:0" data-pct="{pct:.0f}"></div></div>')
        content.append('  </div>')
    content.append('</div>')

    # ─── grade grid ───
    content.append('<div class="section-title anim-fade-up"><span class="icon">\U0001f4da</span> Jelajahi Kelas</div>')
    content.append('<div class="grade-grid">')

    icons = {"x": "\U0001F4CB", "xi": "\U0001F4BB", "xii": "\U0001F916"}
    names_map = {"x": "X", "xi": "XI", "xii": "XII"}

    for name, fase, jp, short, desc, slug in grade_data_info:
        st = grade_stats[short]
        content.append('  <div class="grade-card">')
        content.append(f'    <div class="card-icon {short}">{icons[short]}</div>')
        content.append(f'    <h3>Kelas {names_map[short]}</h3>')
        content.append(f'    <span class="badge">{fase} &middot; {jp}</span>')
        content.append(f'    <div class="detail">{desc}<br><strong>{st["total"]} file</strong> &middot; {st["lines"]:,} baris</div>')
        content.append('    <div class="links">')
        content.append(f'      <a href="{slug}/index.html">\U0001f4c1 Root Dokumen</a>')
        content.append(f'      <a href="{slug}/modul_ajar/index.html">\U0001f4d6 Modul Ajar ({st["ma"]})</a>')
        mt_path = BASE_DIR / slug / "Materi"
        if mt_path.exists():
            mt_count = len(list(mt_path.glob("*.md")))
            content.append(f'      <a href="{slug}/Materi/index.html">\U0001f4da Materi ({mt_count})</a>')
        content.append('    </div>')
        content.append('  </div>')

    content.append('</div>')

    # ─── teacher section ───
    content.append('<div class="teacher-section anim-fade-up">')
    content.append('  <h2>Tim <span>MGMP Informatika</span> SMA Negeri 6 Cimahi</h2>')
    content.append('  <div class="teacher-grid">')
    
    teachers = [
        ("RH", "Raden Hana Amalia, ST.", "Ketua MGMP", "\u2014"),
        ("DS", "Daniarsyah, S.Kom.", "Sekretaris", "198004052022211004"),
        ("LO", "Lingga Oktaviani, S.Kom.", "Anggota", "\u2014"),
        ("RZ", "Razzib Zabbal Noor, S.Kom.", "Anggota", "\u2014"),
        ("EK", "Edi Kusnadi, M.Pd.", "Anggota", "\u2014"),
        ("MR", "Muharima Rasyid Noor, S.St.", "Anggota", "\u2014"),
    ]
    for init, nama, role, nip in teachers:
        content.append('    <div class="teacher-card">')
        content.append(f'      <div class="avatar">{init}</div>')
        content.append(f'      <div class="name">{nama}</div>')
        content.append(f'      <div class="role">{role}</div>')
        content.append(f'      <div class="nip">{"" if nip == "\u2014" else "NIP. "}{nip}</div>')
        content.append('    </div>')
    content.append('  </div>')
    content.append('</div>')

    # ─── identity ───
    content.append('<div class="identity-section anim-fade-up">')
    content.append('  <h2>\U0001f3eb MGMP Informatika SMA Negeri 6 Cimahi</h2>')
    content.append('  <div class="identity-grid">')
    content.append('    <span class="label">Ketua MGMP</span><span class="value"><strong>Raden Hana Amalia, ST.</strong></span>')
    content.append('    <span class="label">Sekretaris</span><span class="value">Daniarsyah, S.Kom.</span>')
    content.append('    <span class="label">Sekolah</span><span class="value">SMA Negeri 6 Cimahi</span>')
    content.append('    <span class="label">Tahun Pelajaran</span><span class="value">2026/2027</span>')
    content.append('  </div>')
    content.append('  <p style="margin-top:1rem;font-size:0.82rem;color:var(--text-muted);border-top:1px solid var(--border);padding-top:0.75rem;">')
    content.append('    Dokumen administrasi ini dikelola oleh MGMP Informatika SMA Negeri 6 Cimahi dan diperuntukkan bagi seluruh guru Informatika di lingkungan sekolah. Untuk luar sekolah juga dipersilahkan.')
    content.append('  </p>')
    content.append('</div>')

    # ─── footer ───
    content.append('<footer class="site-footer">')
    content.append('  <div class="footer-inner">')
    content.append('    <div class="footer-brand">')
    content.append('      <h3>Adm. Guru &middot; Modul Ajar &middot; Materi</h3>')
    content.append('      <p>MGMP Informatika SMA Negeri 6 Cimahi &middot; 2026/2027</p>')
    content.append('    </div>')
    content.append('  </div>')
    content.append('  <div class="footer-bottom">')
    content.append('    &copy; 2026 natedekaka &mdash; developed with \u2764\ufe0f for SMA Negeri 6 Cimahi')
    content.append('  </div>')
    content.append('</footer>')

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


JS_CODE = r'''(() => {
  'use strict';

  /* ─── Dark mode ─── */
  const toggle = document.getElementById('themeToggle');
  const html = document.documentElement;
  if (localStorage.getItem('dark') === 'true') {
    html.classList.add('dark-mode');
    toggle.textContent = '\u2600';
  }
  if (toggle) {
    toggle.addEventListener('click', () => {
      const on = html.classList.toggle('dark-mode');
      localStorage.setItem('dark', on);
      toggle.textContent = on ? '\u2600' : '\u263d';
    });
  }

  /* ─── Back to top ─── */
  const btt = document.getElementById('backToTop');
  if (btt) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          btt.classList.toggle('visible', window.scrollY > 300);
          ticking = false;
        });
        ticking = true;
      }
    });
    btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ─── Mobile hamburger ─── */
  const hamburger = document.getElementById('hamburgerBtn');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  if (hamburger && sidebar && overlay) {
    function closeSidebar() {
      sidebar.classList.remove('open');
      overlay.classList.remove('active');
      hamburger.style.display = '';
    }
    hamburger.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('active');
      hamburger.style.display = 'none';
    });
    overlay.addEventListener('click', closeSidebar);
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSidebar(); });
  }

  /* ─── Animate progress bars on scroll ─── */
  const fillBars = () => {
    document.querySelectorAll('.progress-bar-fill[style*="width: 0"]').forEach(bar => {
      const rect = bar.closest('.progress-item').getBoundingClientRect();
      if (rect.top < window.innerHeight - 40) {
        const pct = bar.getAttribute('data-pct') || '100';
        bar.style.width = pct + '%';
      }
    });
  };
  window.addEventListener('scroll', () => { requestAnimationFrame(fillBars); });
  window.addEventListener('load', () => { setTimeout(fillBars, 200); });

  /* ─── Search filter ─── */
  const searchInput = document.getElementById('docSearch');
  const clearBtn = document.getElementById('searchClear');
  if (searchInput) {
    /* collect all searchable items */
    const items = [];
    document.querySelectorAll('.grade-card, .teacher-card, .identity-section, .stat-card').forEach(el => {
      items.push({ el, text: el.textContent.toLowerCase() });
    });
    /* also collect all links from grade cards */
    const gradeLinks = [];
    document.querySelectorAll('.grade-card .links a').forEach(a => {
      gradeLinks.push({ el: a, href: a.getAttribute('href'), text: a.textContent.toLowerCase() });
    });

    searchInput.addEventListener('input', () => {
      const q = searchInput.value.trim().toLowerCase();
      if (q) {
        clearBtn.classList.add('visible');
      } else {
        clearBtn.classList.remove('visible');
      }

      /* filter items */
      let anyMatch = false;
      items.forEach(item => {
        const match = !q || item.text.includes(q);
        item.el.style.display = match ? '' : 'none';
        if (match && q) anyMatch = true;
      });

      /* highlight matching links */
      gradeLinks.forEach(gl => {
        const match = !q || gl.text.includes(q);
        gl.el.style.opacity = match ? '1' : '0.25';
        if (!q) gl.el.style.opacity = '1';
      });
    });
  }
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      if (searchInput) {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
        searchInput.focus();
      }
    });
  }
})();
'''

def convert_all():
    shutil.rmtree(OUT_DIR, ignore_errors=True)
    css_dir = OUT_DIR / "css"
    css_dir.mkdir(parents=True)
    (css_dir / "style.css").write_text(CSS)

    js_dir = OUT_DIR / "js"
    js_dir.mkdir(parents=True)
    (js_dir / "app.js").write_text(JS_CODE)

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
