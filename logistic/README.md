# Sistem Manajemen Logistik Kopi - SQLite Version

## Perubahan dari JSON ke SQLite

Sistem ini telah diubah dari penyimpanan JSON menjadi SQLite untuk performa dan skalabilitas yang lebih baik.

## Persyaratan

- Python 3.7+
- SQLite3 (sudah built-in di Python)

## Instalasi

Tidak perlu install library ekstra! SQLite3 sudah termasuk dalam Python.

Cukup jalankan program:
```bash
python logistik.py
```

## Cara Menggunakan

### Menjalankan Program
```bash
python logistik.py
```

Database file `logistik_kopi.db` akan dibuat otomatis di folder yang sama saat pertama kali dijalankan.

### Menu Utama
1. **Tampilkan semua barang** - Lihat daftar barang dari database
2. **Cari barang** - Cari barang berdasarkan nama
3. **Tambah barang baru** - Tambahkan barang ke database
4. **Hapus barang** - Hapus barang dari database
5. **Keluar** - Tutup program

## Struktur Database

### Tabel: barang
```
id (INTEGER, Primary Key)
nama (TEXT, Unique)
stok (INTEGER)
harga (INTEGER)
kadaluarsa (TEXT, Nullable)
```

## Fitur

✓ Menambah barang ke database
✓ Menghapus barang dari database
✓ Mencari barang berdasarkan nama
✓ Melihat semua barang
✓ Manajemen supplier
✓ Tanggal kadaluarsa (opsional)
✓ Database tersimpan lokal dalam file `logistik_kopi.db`

## Keuntungan SQLite

- ✅ Tidak perlu server database terpisah
- ✅ Tidak perlu instalasi library ekstra
- ✅ File database tersimpan lokal (portabel)
- ✅ Setup mudah, cukup jalankan program
- ✅ Perfect untuk aplikasi kecil/medium
- ✅ Semua data real-time tersimpan di database

## Troubleshooting

### Error: "database is locked"
- Tutup program lain yang mengakses database
- Hapus file `logistik_kopi.db` dan jalankan ulang jika diperlukan

### Error: "table barang already exists"
- Normal! Tabel sudah dibuat, lanjutkan penggunaan

### File `logistik_kopi.db` tidak muncul
- Jalankan program dan pilih menu untuk trigger pembuatan tabel
- File akan muncul di folder yang sama dengan `logistik.py`

## Struktur File

```
logistic/
├── logistik.py              # File utama
├── logistik_kopi.db        # Database (otomatis dibuat)
├── README.md               # Dokumentasi ini
```

## Catatan

- Data disimpan otomatis di SQLite saat operasi CRUD
- Tidak perlu lagi memanggil `simpan_json()` atau `muat_json()`
- Semua data real-time tersimpan di database lokal
- Database file bisa di-backup dengan copy file `logistik_kopi.db`

