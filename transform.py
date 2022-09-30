#!/usr/bin/python

from extract import *

print("# Transform\n")
print("Sedang melakukan transformasi data...\n")

# Transform data
print("Menghilangkan beberapa kolom yang tidak diperlukan...\n")
data = etl.cut(data, 'CustomerId','FirstName', 'LastName', 'Address', 'City', 'Country')
print(data)

print("Mengubah nama kolom...\n")
data = etl.rename(data, {'CustomerId': 'ID Pelanggan', 'FirstName': 'Nama Depan', 'LastName': 'Nama Belakang', 'Address': 'Alamat', 'City': 'Kota', 'Country': 'Negara'})
print(data)

print("Menggabungkan kolom Nama Depan dan Nama Belakang menjadi Nama Lengkap...\n")
data = etl.addfield(data, 'Nama Lengkap', lambda rec: rec['Nama Depan'] + ' ' + rec['Nama Belakang'])
data = etl.cut(data, 'ID Pelanggan', 'Nama Lengkap', 'Alamat', 'Kota', 'Negara')
print(data)

print("Mengambil data yang berasal dari negara United Kingdom saja...\n")
data = etl.select(data, lambda rec: rec['Negara'] == 'United Kingdom')
print(data)

print("Data berhasil di-transform\n\n")
