# <p align="center">IS184516 - Kecerdasan Bisnis [C]</p>
<p align="center">Dosen Pengampu<br><i><strong>Radityo Prasetianto Wibowo, S.Kom., M.Kom.</strong></i></p>

***

## ETL Pipeline with Python using PETL
Untuk memulai, jalankan file `main.py` pada terminal:
```python
python main.py
```

Gambaran isi dari `main.py`:
```python
#!/usr/bin/python

import os
from os.path import exists

print("# Kecerdasan Bisnis [C]\n")
print("ETL dengan Python menggunakan library pETL\n")
print("Muhammad Fathurrahman - 5026201139\n\n")
print("Sedang melakukan ETL...\n")

# ETL
if exists("pelanggan_transform.csv"):
    print("Menghapus file pelanggan_transform.csv yang sudah ada...\n")
    os.remove("pelanggan_transform.csv")
    print("File pelanggan_transform.csv berhasil dihapus\n\n")
    os.system("python load.py")
else :
    os.system("python load.py")

print("ETL selesai\n\n")
```

> Output akan di-load ke dalam file `pelanggan_transform.csv`.

***

<p align="center"><i>This repository is only for educational purpose, as I will use this only to upload my assignments for this particular class.</i></p>