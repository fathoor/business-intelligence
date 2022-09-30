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
