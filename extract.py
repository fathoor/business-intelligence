#!/usr/bin/python

import petl as etl

print("# Extract\n")
print("Sedang meng-ekstrak data...\n")

# Extract data dari file CSV
data = etl.fromcsv('pelanggan.csv')

print("Data berhasil di-ekstrak\n\n")
