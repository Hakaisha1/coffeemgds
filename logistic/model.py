from django.db import models

class Barang(models.Model):
    # Nama barang, harus unik agar tidak ada duplikasi
    nama = models.CharField(max_length=100, unique=True)
    
    # Jumlah stok saat ini, harus angka bulat
    stok = models.IntegerField(default=0)
    
    # Harga barang (menggunakan DecimalField untuk akurasi mata uang)
    harga = models.DecimalField(max_digits=10, decimal_places=2) 
    
    # Tanggal kadaluarsa, bisa kosong (null=True, blank=True)
    kadaluarsa = models.DateField(null=True, blank=True) 

    def __str__(self):
        # Representasi string objek, bagus untuk panel Admin Django
        return self.nama
    
# logistik/models.py (Lanjutan)

class Supplier(models.Model):
    # Nama pemasok
    nama = models.CharField(max_length=100)
    
    # Informasi kontak (email/telepon)
    kontak = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
    
# logistik/models.py (Lanjutan)

class TransaksiPembelian(models.Model):
    # Relasi: Pembelian ini terkait dengan SATU Supplier.
    # models.PROTECT mencegah penghapusan Supplier jika masih ada transaksi terkait.
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT) 
    
    # Relasi: Pembelian ini terkait dengan SATU Barang.
    barang = models.ForeignKey(Barang, on_delete=models.PROTECT) 
    
    # Jumlah barang yang dibeli dalam transaksi ini
    jumlah = models.IntegerField()
    
    # Tanggal transaksi, otomatis diisi saat objek pertama dibuat
    tanggal = models.DateField(auto_now_add=True) 

    def proses_transaksi(self):
        """Metode untuk menambahkan jumlah pembelian ke stok barang terkait."""
        # Akses objek Barang yang terkait
        self.barang.stok += self.jumlah
        # Simpan perubahan stok ke database
        self.barang.save()
        
    def __str__(self):
        return f"Pembelian {self.jumlah} {self.barang.nama} dari {self.supplier.nama} pada {self.tanggal}"