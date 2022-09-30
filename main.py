#!/usr/bin/python

import os
from os.path import exists
from load import *

print("# Kecerdasan Bisnis [C]\n")
print("ETL dengan Python menggunakan library pETL\n")
print("Muhammad Fathurrahman - 5026201139\n")
print("Sedang melakukan ETL process...\n")

# ETL
if exists("pelanggan_transform.csv"):
    print("Menghapus file pelanggan_transform.csv yang sudah ada...\n\n")
    os.remove("pelanggan_transform.csv")
    os.system("python load.py")
else :
    os.system("python load.py")

print("ETL process selesai\n\n")
