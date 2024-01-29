import json

meju = {}
file_path = 'menu.json'

try : 
        with open(file_path,'r') as file:
            #todo : Parse JSON ke DICTIONARY
            menu = json.load(file) 
except Exception as e: 
        print(f"Terjadi kesalahan : {e}")   

            #todo: Tampilkan menu makanan dan minuman
print()
print('|=======================================|')  
print('|         DAFTAR MENU          |')  
print('|=======================================|')  
print(f"|{' Kode ' :7} | {' Menu ':15} | {' Harga ': 8}|") 
print('|=======================================|')
for item,info in menu.items():
    print(f"|  {info['kode']:4} | { item:14} |  Rp{info['harga']:8 |}")
print('|=======================================|')

#todo: Fungsi mengambil pesanan dari pelanggan 
def take_order(menu):
    name = input("Masukkan Nama Anda : ")
    orders = []
    total_harga = 0
    print("Masukkan nomor menu dan porsi (Contoh : 4, 2)")
    print('(Pilih nomor 0 untuk selesai)')
    while True: 
        try: 
            order = input("Pesanan : ")
            if order.lower() == '0':
                break
            kode_pesanan, porsi = order.split(", ")
            if kode_pesanan in [info['kode'] for info in menu.values()]:
                item_terpilih = next(item for item, info in menu.items() if info['kode'] == kode_pesanan)
                harga_terpilih = menu[item_terpilih]['harga']
                print(f"Anda memesan {item_terpilih} dengan harga Rp{harga_terpilih}.")
                if item in menu:
                    harga = harga_terpilih * int(porsi)
                    total_harga += harga
                    orders.append({'item' : item_terpilih, 'porsi' : int(porsi), 'harga': harga})
                else:
                    print(f"Item {item} tidak tersedia di menu.")
            else:
                print("Kode menu tidak valid.")
        except:
            print("Format input salah")    
    return name,orders,total_harga            









#todo: Menyimpan pesanan ke dalam file 
def save_orders(nama_pelanggan, orders, total_harga):
    order_details = {
        'Nama Pelanggan' : nama_pelanggan,
        'orders' : orders,
        'total_harga': total_harga,
    }
    with open('catatan.txt','a') as file:
        file.write(json.dumps(order_details) + "\n")
#todo: Membaca dan menampilkan pesanan dari file 
def read_orders():
    with open('catatan.txt',"r") as file:
        lines = file.readlines()
        baris_terakhir = lines[-1]
        order_details = json.loads(baris_terakhir)
        print()
        print('|=======================================|')
        print(f"| Nama Pelanggan: {order_details['Nama Pelanggan']:15}    |")
        print('|=======================================|')
        print('|               DETAIL PESANAN          |')
        print('|=======================================|')
        print(f"|  {'      Menu':20}|   {'Porsi' : 2}  |    {'  Harga  ':6}  |")
        print('|=======================================|')
        for order in order_details['orders']:
            print(f"| {order['item']:17} | {order['porsi']:5} | Rp{order['harga']:8} |")
        print('|=======================================|')
        print(f"|Total Harga {'':15} Rp{order_details['total_harga']:8} |")
        print('|---------------------------------------|')
        print('|=======================================|')
        print('|               TERIMA KASIH            |')
        print('|=======================================|')

        nama_pelanggan,orders,total_harga = take_order(menu)
        save_order(nama_pelanggan,orders,total_harga)
        read_orders()
        print()