# Jelajah Tuban

Website pariwisata Kabupaten Tuban menggunakan Flask, HTML, CSS, dan Jinja2.

## Fitur
- 4 route statis: Beranda, Tentang, Destinasi, Kontak.
- Dynamic route `/cek/<username>` dengan tiga kondisi validasi.
- Dynamic route `/user/<username>`.
- Route converter integer `/produk/<int:id>`.
- `abort(404)` dan custom error page 404.
- Penggunaan `url_for()` dan `redirect()`.
- Template induk `base.html` dan `{% extends %}`.
- Jinja2 `{% if %}`, `{% for %}`, serta filter kustom `rupiah`.

## Cara menjalankan (Windows PowerShell)

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Buka alamat `http://127.0.0.1:5000`.

## Rute untuk pengujian
- `/` - Beranda
- `/tentang` - Tentang
- `/destinasi` - Daftar destinasi
- `/kontak` - Kontak
- `/cek` - Form pengecekan username
- `/cek/aksa` - Username sudah dipakai
- `/cek/admin` - Username sudah dipakai
- `/cek/penjelajah` - Username tersedia
- `/cek/a` - Username tidak valid
- `/user/aksa` - Profil contoh
- `/produk/1` - Detail Pantai Boom
- `/produk/999` - Custom 404
- `/produk/abc` - 404 karena converter `int`

## Catatan
Data username dan tiket merupakan data simulasi untuk tugas. Foto memakai URL gambar eksternal sehingga browser memerlukan koneksi internet.
