import json
import datetime

menu = {}
file_path = "menu.json"

try:
  with open(file_path, "r") as file:
    menu = json.load(file)
except Exception as e:
  print(f"Terjadi kesalahan: {e}")

# Tampilkan menu makanan dan minuman
print()
print("|=======================================|")
print("| DAFTAR MENU |")
print("|=======================================|")
print(f"| Kode | Menu | Harga |")
print("|=======================================|")
for item, info in menu.items():
  print(f"| {info['kode']:4} | {item:14} | Rp{info['harga']:8} |")
print("|=======================================|")

# Fungsi mengambil pesanan dari pelanggan
def take_order(menu):
  name = input("Masukkan Nama Anda: ")
  orders = []
  total_harga = 0
  print("Masukkan nomor menu dan porsi (Contoh: 4, 2)")
  print("(Pilih nomor 0 untuk selesai)")
  while True:
    try:
      order = input("Pesanan: ")
      if order.lower() == "0":
        break
      kode_pesanan, porsi = order.split(", ")
      if kode_pesanan in [info["kode"] for info in menu.values()]:
        item_terpilih = next(item for item, info in menu.items() if info["kode"] == kode_pesanan)
        harga_terpilih = menu[item_terpilih]["harga"]
        print(f"Anda memesan {item_terpilih} dengan harga Rp{harga_terpilih}.")
        harga = harga_terpilih * int(porsi)
        total_harga += harga
        orders.append({"item": item_terpilih, "porsi": int(porsi), "harga": harga})
      else:
        print("Kode menu tidak valid.")
    except:
      print("Format input salah")
  return name, orders, total_harga

# Menyimpan pesanan ke dalam file
def save_orders(nama_pelanggan, orders, total_harga):
  order_details = {
    "Nama Pelanggan": nama_pelanggan,
    "orders": orders,
    "total_harga": total_harga,
  }
  with open("catatan.txt", "a") as file:
    file.write(json.dumps(order_details) + "\n")

def transaksi(total_harga):
    while True:
        print(f'Total Harga: Rp{total_harga:.2f}')
        try:
            nominal = int(input("Masukkan nominal yang akan dibayar: "))
            if nominal >= total_harga:
                kembalian = nominal - total_harga
                print(f"Kembalian: Rp{kembalian:.2f}")
                return kembalian,nominal
            else:
                print("Nominal yang anda masukkan kurang.")
        except ValueError:
            print("Input harus berupa angka.")
    

# Membaca dan menampilkan pesanan dari file
def read_orders(kembalian,nominal):
    with open("catatan.txt", "r") as file:
      lines = file.readlines()
      baris_terakhir = lines[-1]
      order_details = json.loads(baris_terakhir)
      date = datetime.datetime.now()
      id = f"{date.year}{date.month}{date.day}{date.time().hour}{date.time().minute}{date.time().second}"
      format_date = f"{date.year}-{date.month}-{date.day} {date.time().hour}:{date.time().minute}:{date.time().second}"
    print()
    print("|=======================================|")
    print("|Kode Transaksi :        ",id,                "|")
    print(f"|Nama Pelanggan: {order_details['Nama Pelanggan']:15}        |")
    print("|=======================================|")
    print("|Tanggal Pemesanan : ",format_date,"|")
    print("|=======================================|")
    print("|            DETAIL PESANAN             |")
    print("|=======================================|")
    print(f"|      Menu    |   Porsi |     Harga    |")
    print("|========================================|")
    for order in order_details["orders"]:
      print(f"| {order['item']:17} | {order['porsi']:5} | Rp{order['harga']:8} |")
    print("|=======================================|")
    print(f"   Total Harga: Rp{order_details['total_harga']:8}")
    print(f"Nominal :  {nominal}")
    print(f"Kembalian :  {kembalian}")
    print("|=======================================|")
    print("|              TERIMA KASIH             |")
    print("|=======================================|")

# Menjalankan program
nama_pelanggan, orders, total_harga = take_order(menu)
save_orders(nama_pelanggan, orders, total_harga)
kembalian,nominal = transaksi(total_harga)
read_orders(kembalian,nominal)