# final-project-super-cashier
Final Project Python Class at Pacmann

## Latar Belakang
Seorang pemilik supermarket membutuhkan sistem kasir self-service yang memungkinkan pembeli untuk memasukkan nama item, jumlah item, dan harga item yang ingin dibeli secara mandiri sehingga pembeli dapat membeli item dari mana saja tanpa harus datang ke supermarket.

## Requirements & Objectives
1. Setiap pembeli dapat membuat ID transaksi
2. Setiap pembeli dapat memasukkan nama item, jumlah item, dan harga satuan item
3. Setiap pembeli dapat memperbaiki daftar pembelian apabila terdapat kesalahan input:
   - Memperbaiki nama item
   - Memperbaiki jumlah item
   - Memperbaiki harga satuan item
4. Setiap pembeli dapat menghapus item dari daftar pembelian
5. Setiap pembeli dapat mengosongkan atau mereset daftar pembelian
6. Setiap pembeli dapat mengecek daftar pembelian dan kebenaran datanya
7. Setiap pembeli dapat menghitung total harga pembelian dengan discount tertentu sesuai total harga pembeliannya

## Alur Program
1. Pembeli mendefinisikan ID transaksi
2. Pembeli memasukkan nama item, jumlah item, dan harga satuan item. Proses ini akan dilakukan berkali-kali sampai semua item yang ingin dibeli sudah dimasukkan
3. Pembeli memperbaiki nama item, jumlah item, atau harga satuan item apabila terdapat kesalahan input data
4. Pembeli menghapus item dari daftar pembelian atau mereset daftar pembelian apabila terdapat item yang tidak jadi dibeli
5. Pembeli mengecek kembali kebenaran daftar pembelian
6. Pembeli menghitung total harga pembelian

## Penjelasan Kode
1. class Transaction
   - Merupakan _class_ yang menyimpan seluruh _attribute_ dan _function_ terkait proses transaksi
   - Secara default, _instance_ _attribute_ pada _class_ ini akan berupa _empty_ _dictionary_
2. function add_item()
   - Definisi: Fungsi untuk menambah item yang dibeli
   - Parameters:
     - item_name (str): nama item yang ditambahkan
     - item_quantity (int): jumlah item yang ditambahkan
     - item_price (int): harga satuan item yang ditambahkan
   - Returns:
     - item (dict): dictionary yang menyimpan seluruh item
3. function update_item_name()
   - Definisi: Fungsi untuk mengganti nama item yang dibeli
   - Parameters:
     - item_name (str): nama item yang ingin diupdate namanya
     - item_name_new (str): nama item terupdate
   - Returns:
     - item (dict): dictionary yang menyimpan seluruh item
4. function update_item_quantity()
   - Definisi: Fungsi untuk mengganti jumlah item yang dibeli
   - Parameters:
     - item_name (str): nama item yang ingin diupdate jumlahnya
     - item_quantity_new (int): jumlah item terupdate
   - Returns:
     - item (dict): dictionary yang menyimpan seluruh item
5. function update_item_price()
   - Definisi: Fungsi untuk mengganti harga item yang dibeli
   - Parameters:
     - item_name (str): nama item yang ingin diupdate harganya
     - item_price_new (int): harga satuan item terupdate
   - Returns:
     - item (dict): dictionary yang menyimpan seluruh item
6. function delete_item()
   - Definisi: Fungsi untuk menghapus item yang dibeli
   - Parameters:
     - item_name (str): nama item yang ingin didelete
   - Returns:
     - item (dict): dictionary yang menyimpan seluruh item yang tersisa
7. function reset_transaction()
   - Definisi: Fungsi untuk menghapus seluruh item yang dibeli
   - Parameters:
     - None
   - Returns:
     - None
8. function check_order()
   - Definisi: Fungsi untuk mengecek daftar item yang dibeli
   - Parameters:
     - None
   - Returns:
     - item (dict): dictionary yang menyimpan seluruh item yang tersisa
9. function total_price()
   - Definisi: Fungsi untuk menjumlahkan total harga seluruh item yang dibeli
   - Parameters:
     - None
   - Returns:
     - grand_total (int): total harga setelah diskon
    
## Hasil Test Case
### Case 1: Menambahkan Dua Item Baru
Code:
```
trnsct_123.add_item(item_name='Ayam Goreng', item_quantity=2, item_price=20000)
trnsct_123.add_item(item_name='Pasta Gigi', item_quantity=3, item_price=15000)
trnsct_123.check_order()
```

Output:
```
Item yang dibeli adalah {'Ayam Goreng': [2, 20000], 'Pasta Gigi': [3, 15000]}
Pemesanan sudah benar
```

### Case 2: Menghapus Salah Satu Item
Code:
```
trnsct_123.delete_item(item_name='Pasta Gigi')
trnsct_123.check_order()
```

Output:
```
Item yang dibeli adalah {'Ayam Goreng': [2, 20000]}
Pemesanan sudah benar
```

### Case 3: Menghapus Seluruh Item
Code:
```
trnsct_123.reset_transaction()
```

Output:
```
Semua item berhasil di delete!
```

### Case 4: Memasukkan Item dan Menghitung Total Belanja
Code:
```
trnsct_123.add_item(item_name='Ayam Goreng', item_quantity=2, item_price=20000)
trnsct_123.add_item(item_name='Pasta Gigi', item_quantity=3, item_price=15000)
trnsct_123.add_item(item_name='Mainan Mobil', item_quantity=1, item_price=200000)
trnsct_123.add_item(item_name='Mi Instan', item_quantity=5, item_price=3000)
trnsct_123.check_order()
trnsct_123.total_price()
```

```
Item yang dibeli adalah {'Ayam Goreng': [2, 20000], 'Pasta Gigi': [3, 15000], 'Mainan Mobil': [1, 200000], 'Mi Instan': [5, 3000]}
Pemesanan sudah benar
Total belanja yang harus dibayarkan adalah 285000.0
```

## Conclusion
Pada final project ini telah dibuat program sederhana yang memungkinkan pembeli untuk melakukan transaksi secara self-service dari mana saja tanpa harus ke supermarket.

## Future Work
Untuk kedepannya scope program pada final project ini dapat lebih ditingkatkan lagi, seperti:
1. Pencatatan data membership setiap customer
2. Pemberian promo khusus untuk setiap metode pembayaran
3. Perhitungan pajak
