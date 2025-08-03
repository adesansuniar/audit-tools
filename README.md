# 🧪 Audit Tools – Blog Adesansuniar

![Audit Status](https://github.com/adesansuniar/audit-tools/actions/workflows/auto-audit-html.yml/badge.svg)

Alat bantu otomatis untuk memeriksa status halaman HTML pada blog [`blog-adesansuniar`](https://adesansuniar.github.io/blog-adesansuniar/) dan menyimpan hasil audit dalam format Markdown.

---

## 🎯 Tujuan Audit

Repositori ini dibuat untuk:

- ✅ Memvalidasi **status URL GitHub Pages**: online, 404, atau error
- 🔍 Mengecek keberadaan file HTML lokal (`_includes`, `_layouts`)
- 📄 Menyimpan **log audit harian** otomatis ke `audit-rekap.md`
- 🔁 Menjalankan proses audit terjadwal lewat GitHub Actions

---

## ⚙️ Alur Otomatisasi

Setiap hari, workflow `auto-audit-html.yml` akan:

1. Menjalankan `audit-html.py`
2. Mengecek `daftar-public.txt` untuk status URL
3. Mengecek `daftar-internal.txt` untuk keberadaan file internal
4. Menghasilkan log audit di `audit-rekap.md` (Markdown)
5. Memperbarui badge status di halaman ini

---

## 📦 Struktur Direktori

```text
├── daftar-public.txt           # Daftar URL GitHub Pages untuk diuji
├── daftar-internal.txt         # Daftar file lokal HTML (_includes, _layouts)
├── audit-html.py               # Script audit utama
├── audit-rekap.md              # Log hasil audit harian dalam format Markdown
└── .github/
    └── workflows/
        └── auto-audit-html.yml   # Workflow otomatis GitHub Actions
