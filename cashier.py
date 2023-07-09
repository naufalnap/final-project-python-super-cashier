import transaction

trnsct_123 = transaction.Transaction()


print("----------Test 1----------")
trnsct_123.add_item(item_name='Ayam Goreng', item_quantity=2, item_price=20000)
trnsct_123.add_item(item_name='Pasta Gigi', item_quantity=3, item_price=15000)
trnsct_123.check_order()

print("----------Test 2----------")
trnsct_123.delete_item(item_name='Pasta Gigi')
trnsct_123.check_order()

print("----------Test 3----------")
trnsct_123.reset_transaction()

print("----------Test 4----------")
trnsct_123.add_item(item_name='Ayam Goreng', item_quantity=2, item_price=20000)
trnsct_123.add_item(item_name='Pasta Gigi', item_quantity=3, item_price=15000)
trnsct_123.add_item(item_name='Mainan Mobil', item_quantity=1, item_price=200000)
trnsct_123.add_item(item_name='Mi Instan', item_quantity=5, item_price=3000)
trnsct_123.check_order()
trnsct_123.total_price()
