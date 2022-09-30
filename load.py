#!/usr/bin/python

from transform import *

print("# Load\n")
print("Sedang melakukan load data...\n")

# Load data ke dalam file CSV
print("Menyimpan data ke dalam file pelanggan_transform.csv...\n")
etl.tocsv(data, 'pelanggan_transform.csv')

print("Data berhasil di-load\n\n")
