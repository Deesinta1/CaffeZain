from django.db import models

# Create your models here.

class Kopi(models.Model):
    nama_kopi = models.CharField(max_length=255)
    harga = models.IntegerField()
    gambar_kopi = models.FileField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.nama_kopi