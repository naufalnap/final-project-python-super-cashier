class Transaction:
  def __init__(self):
    self.item = dict()

  def add_item(self, item_name, item_quantity, item_price):
    """Menambah item yang dibeli
    
    Parameters:
      item_name (str): nama item yang ditambahkan
      item_quantity (int): jumlah item yang ditambahkan
      item_price (int): harga satuan item yang ditambahkan

    Returns:
      item (dict): dictionary yang menyimpan seluruh item
    """
    if item_name in self.item.keys():
        raise Exception("Item tersebut sudah tersedia. Silahkan tambah item lain")
        
    self.item[item_name] = [item_quantity, item_price]

    return self.item

  def update_item_name(self, item_name, item_name_new):
    """Mengganti nama item yang dibeli
    
    Parameters:
      item_name (str): nama item yang ingin diupdate namanya
      item_name_new (str): nama item terupdate
    
    Returns:
      item (dict): dictionary yang menyimpan seluruh item
    """
    if item_name_new in self.item.keys():
        raise Exception("Nama item tersebut sudah tersedia. Silahkan gunakan nama item lain")

    try:
      self.item[item_name_new] = self.item.pop(item_name)
    except KeyError:
      print("Masukkan nama item dengan benar")

    return self.item

  def update_item_quantity(self, item_name, item_quantity_new):
    """Mengganti jumlah item yang dibeli
    
    Parameters:
      item_name (str): nama item yang ingin diupdate jumlahnya
      item_quantity_new (int): jumlah item terupdate

    Returns:
      item (dict): dictionary yang menyimpan seluruh item
    """
    try:
      self.item[item_name][0] = item_quantity_new
    except KeyError:
      print("Masukkan nama item yang benar")

    return self.item

  def update_item_price(self, item_name, item_price_new):
    """Mengganti harga item yang dibeli
    
    Parameters:
      item_name (str): nama item yang ingin diupdate harganya
      item_price_new (int): harga satuan item terupdate

    Returns:
      item (dict): dictionary yang menyimpan seluruh item
    """
    try:
      self.item[item_name][1] = item_price_new
    except KeyError:
      print("Masukkan nama item yang benar")
  
    return self.item

  def delete_item(self, item_name):
    """Menghapus item yang dibeli
    
    Parameters:
      item_name (str): nama item yang ingin didelete

    Returns:
      item (dict): dictionary yang menyimpan seluruh item yang tersisa
    """
    try:
      self.item.pop(item_name)
    except KeyError:
      print("Masukkan nama item dengan benar")

    return self.item # nama item harus tersedia

  def reset_transaction(self):
    """Menghapus seluruh item yang dibeli
    
    Parameters:
      None

    Returns:
      None
    """
    self.item.clear()
    print("Semua item berhasil di delete!")

  def check_order(self):
    """Mengecek daftar item yang dibeli

    Parameters:
      None
    
    Returns:
      item (dict): dictionary yang menyimpan seluruh item
    """
    try:
        print(f"Item yang dibeli adalah {self.item}")
    except:
        print("Terdapat kesalahan input data")
    else:
        print("Pemesanan sudah benar")
    return self.item # buat format yang bagus

  def total_price(self):
    """Menjumlahkan total harga seluruh item yang dibeli

    Parameters:
      None

    Returns:
      grand_total (int): total harga setelah diskon
    """
    price_list = [qty * price for qty, price in self.item.values()]
    price_total = sum(price_list)

    multiplier = 1
    if price_total > 500_000:
      multiplier = 1 - 0.1
    elif price_total > 300_000:
      multiplier = 1 - 0.08
    elif price_total > 200_000:
      multiplier = 1 - 0.05
    
    grand_total = price_total * multiplier  # price total after discount
    print(f"Total belanja yang harus dibayarkan adalah {grand_total}")

    return grand_total
    