import csv, os
import pandas as pd
import time
from tabulate import tabulate
from datetime import datetime 


def input_transaction(operator):
    os.system('cls')
    print("Operator", operator) # fungsi ini untuk membantu param, ketika dipanggil dan dicetak kolom "as" akan diisi dgn vallue dri operator ini
    print("\n==== INPUT TRANSAKSI PENGGILINGAN ====\n")

    # Search customer
    keyword = input("Masukkan nama petani yang sudah kamu dafatrkan sebelumnya: ").strip().upper()

    # apabila var keyword kosong 
    if not keyword:
        print("Keyword tidak boleh kosong!")
        input("Enter untuk lanjut...")
        return
    
    # apabila file path csv kosong
    if not os.path.exists("data_customer.csv"):
        print("Data pelanggan belum ada!")
        input("Enter untuk lanjut...")
        return

# buka data csv dgn mode baca, encoding UTF-8 untuk membaca karakter dengan benar (misal huruf Indonesia/Unicode)
    with open("data_customer.csv", mode="r", encoding="utf-8") as f:
        reader = list(csv.reader(f)) # membaca file yg sudah dibuka lewat "with open" lalu dijadikan sebuha list
        data = reader[1:] # heeader = mengambil value dari data f untuk dijadikan nama kolom. lalu mengambil data dri index 1 hingga terkahir untuk dijadikan sebuah list.

    # Find matching customers
    customers =  []
    for i in data:
        if keyword in i[1] or keyword in i[2]:
            customers.append(i)

    if not customers:
        print("Petani tidak ditemukan!")
        input("Enter untuk lanjut...")
        return

    # Select customer if multiple found
    if len(customers) > 1:
        print("\nDitemukan beberapa petani:")
        print(f"{'ID':<5} {'Nama':<20} {'Telepon'}")
        print("-"*35)
        for c in customers:
            print(f"{c[0]:<5} {c[1]:<20} {c[2]}")
        customer_id = input("\nMasukkan ID Petani: ").strip()# ganti degn yg identik dgn petani atau klo mau d tambahkan sendiri otomatis

        selected = [c for c in customers if c[0] == customer_id]
        if not selected:
            print("ID Petani tidak valid!")
            input("Enter untuk lanjut...")
            return
        customer = selected[0]

    else:
        customer = customers[0]
        print(f"\nPetani ditemukan: {customer[1]}")
        customer_id = customer[0]

    # Get current price
    if not os.path.exists("data_harga.csv"):
        print("Harga belum ditetapkan admin!")
        input("Enter untuk lanjut...")
        return

    with open("data_harga.csv", mode="r", encoding="utf-8") as f:
        price_data = list((csv.reader(f)))[1:]

    price_data = [[float(i[0]), [i[1]], [i[2]]] for i in price_data]

    print(f"Harga saat ini: Rp{price_data[-1][0]}/kg")

    # Input weight
    try:
        weight_kg = float(input("Masukkan berat gabah (kg): "))
    except:
        print("Berat harus berupa angka dan lebih dari 0!")
        input("Enter untuk lanjut...")
        return
    print(price_data[-1][0])
    total_cost = weight_kg * price_data[-1][0]

    print("\n===== RINCIAN TRANSAKSI =====")
    print(f"Petani     : {customer[1]}")
    print(f"Berat      : {weight_kg} kg")
    print(f"Harga/kg   : Rp{price_data[-1][0]}")
    print(f"Total Biaya: Rp{int(total_cost)}")

    confirm = input("\nSimpan transaksi? (y/n): ").strip().lower()
    if confirm != "y":
        print("Transaksi dibatalkan.")
        input("Enter untuk lanjut...")
        return

    # Save to CSV
    file_name = "data_transactions.csv"
    df = pd.read_csv(file_name)
    new_id = 1
    # Jika file belum ada, buat file baru
    if not os.path.exists(file_name):
        df = pd.DataFrame(columns=["ID","BERAT_KG","HARGA","TOTAL_HARGA","DATE"])
        df.to_csv(file_name, index=False)
    
        with open(file_name, "r", encoding="utf-8") as f:
            rows = list(csv.reader(f))
            print(rows[-1][0])
    transaksi = {
        "ID":  new_id,
        "BERAT_KG" : weight_kg,
        "HARGA" : price_data[-1][0],
        "TOTAL_HARGA" : total_cost,
        "DATE" : datetime.now()
    }
    df = pd.concat([df,pd.DataFrame([transaksi])], ignore_index=True)
    df.to_csv(file_name, index=False)


    print("\nTransaksi berhasil disimpan!")
    input("Enter untuk lanjut...")
def add_customer():
    data_customer = 'data_customer.csv'
    os.system('cls')
    print("=" * 50)
    print("TAMBAH PELANGGAN BARU".center(50))
    print("=" * 50 + "\n")


# jika file blm ada, buat file baru
    if not os.path.exists(data_customer):
        with open(data_customer, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama_Petani", "No_Telp", "Alamat"])  # <-- header kolom



    name = input("Nama Petani: ").strip().upper()
    if not name:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    try:
        phone = int(input("Masukkan No. Telepon : "))
    except ValueError:
        print("Sedang di proses ya...")
        time.sleep(3)
        print("Masukkan nomor telp dnegan angka ya :<")
        return
    address = input("Masukkan Alamat Lengkap : ").strip().lower()
    
# cari id cus
    # if os.path.exists(data_customer):
    customer_id = 1
    try:
        with open("data_customer.csv", mode="r", encoding="utf-8") as file:
            read = list(csv.reader(file))
        if len(read) >= 1:
            last_id = int(read[-1][0]) #pahami syntax
            customer_id = last_id + 1
    except:
            pass


    # sv ke csv
    with open(data_customer, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, name, phone, address])
    
    
    print(f"\nPelanggan '{name}' berhasil ditambahkan! (ID: {customer_id})")
    input("\nEnter untuk lanjut untuk kami arahkan ke transaksi ")
    time.sleep(1)

    # ====================FITUR SEARCH
def search_farmers():
    """Search farmers from CSV"""
    file_name = "data_customer.csv"
    df = pd.read_csv(file_name)
    df = df.astype(str)
    
    
    print("=" * 50)
    print("SEARCH PETANI".center(50))
    print("=" * 50)



    print("CARI PETANI")
    keyword = input("Masukkan nama : ").strip().upper()

    if not keyword:
        print("Keyword tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return

    # Cek file ada atau tidak
    if not os.path.exists(file_name):
        print("Data customer belum tersedia.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    results = []

    # Baca CSV dan cari keyword
    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (keyword in row["Nama_Petani"].upper()):
                results.append(row)

    # Tampilkan hasil.tampilin tabel data based pencarian nama 
    if not results:
        print("Petani tidak ditemukan.")
    else:
        # #kasih tabel u
        # print(f"\n{'ID':<5} {'Nama':<25} {'Telepon':<15} {'Alamat':<30}")
        # for r in results:
        #     print(f"{r['ID']:<5} {r['Nama_Petani']:<25} {r['No_Telp'] or '-':<15} {r['Alamat'] or '-':<30}")
        result = df[
            df['Nama_Petani'].str.contains(keyword, case=False)
        ]
        print(tabulate(result, headers='keys', tablefmt="fancy_grid",showindex=False))

    input("\nTekan Enter untuk melanjutkan...")