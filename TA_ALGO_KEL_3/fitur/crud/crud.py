import csv, os
import pandas as pd
import time
from tabulate import tabulate

data_customer = 'data_customer.csv'

# =========================FITUR 1=============================
def add_customer():
    """Add new customer"""
    os.system('cls')
    print("TAMBAH PELANGGAN BARU")

# jika file blm ada, buat file baru
    if not os.path.exists(data_customer):
        with open(data_customer, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama_Petani", "No_Telp", "Alamat"])  # <-- header kolom



    name = input("Nama Petani: ").strip()
    if not name:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    try:
        phone = int(input("No. Telepon (opsional): "))
    except ValueError:
        print("Sedang di proses ya...")
        time.sleep(3)
        print("Masukkan nomor telp dnegan angka ya :<")
        return
    address = input("Alamat (opsional): ").strip()
    
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
    
    
    print(f"\n✅ Pelanggan '{name}' berhasil ditambahkan! (ID: {customer_id})")
    input("\nEnter untuk lanjut...")

# =======================FITUR 2===============================
def view_all_customers():
    os.system('cls')
    print("DAFTAR SEMUA PELANGGAN")
    if not os.path.exists(data_customer):
        print(" Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    try:
        df = pd.read_csv('data_customer.csv')

        if df.empty:
            print(" Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        headers = ['ID','Nama_Petani','No_Telp','Alamat']
        print(tabulate(df, headers=headers, tablefmt="fancy_grid", showindex=False))
        input("\nTekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {e}")


# =======================FITUR 3===============================
def search_customer():
    """Search customer by name or phone"""
    os.system('cls')
    print("CARI PELANGGAN")

    

# tampilkan tabel customer
    try:
        df = pd.read_csv('data_customer.csv')

        if df.empty:
            print(" Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        headers = ['ID','Nama_Petani','No_Telp','Alamat']
        print(tabulate(df, headers=headers, tablefmt="fancy_grid", showindex=False))

    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {e}")


    keyword = input("Masukkan nama atau nomor telepon: ").strip()
    
    if not keyword:
        print("Keyword tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    # lakukan pencarian
    # konversi semua kolom ke string agar mudah dicocokkan
    df = df.astype(str)
    hasil = df[
            df['ID'].str.contains(keyword, case=False) |
            df['Nama_Petani'].str.contains(keyword, case=False) |
            df['No_Telp'].str.contains(keyword, case=False)]
    
# tampilkan hasil pencarian
    if not hasil.empty:
        os.system('cls')
        print("\n✅ Hasil pencarian ditemukan:\n")
        headers = ['ID','Nama_Petani','No_Telp','Alamat']
        print(tabulate(hasil, headers=headers, tablefmt="fancy_grid", showindex=False))
        input("Tekan Enter untuk melanjutkan...")
        return
    
    else:
        print("\n❌ Tidak ada data yang cocok dengan keyword tersebut.")

# =======================FITUR 4===============================
def edit_customer():
    """Edit customer information"""
    os.system('cls')
    print("EDIT PELANGGAN")

        # pastikan file ada
    if not os.path.exists(data_customer):
        print("❌ Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    try:
        df= pd.read_csv(data_customer)

        if df.empty:
            print("❌ Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        headers = ['ID','Nama_Petani','No_Telp','Alamat']
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
    
# input ID pelanggan yang mau diedit
        try:
            customer_id = int(input("Masukkan ID Pelanggan yang ingin diedit: "))
        except ValueError:
            print("⚠️ ID harus berupa angka!")
            input("\nTekan Enter untuk melanjutkan...")
            return


        # cek apakah ID ada
        if customer_id not in df['ID'].values:
            print("❌ Pelanggan dengan ID tersebut tidak ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            return
        

        # ambil data pelanggan yang sesuai
        dt_Customer = df[df['ID'] == customer_id].iloc[0]
        
    
        print(f"\nData saat ini:")
        print(f"Nama: {dt_Customer['Nama_Petani']}")
        print(f"Telepon: {dt_Customer['No_Telp']}")
        print(f"Alamat: {dt_Customer['Alamat'] } \n")
    

    # input data baru
        name = input(f"Nama baru (Enter untuk tidak mengubah): ").strip()
        try:
            phone = int(input(f"Telepon baru (Enter untuk tidak mengubah): ")).strip()
        except:
            print("Masukkan nomor telp dengan angka!!")
            time.sleep(1.5)
            return
        address = input(f"Alamat baru (Enter untuk tidak mengubah): ").strip()
    
        if name:
            df.loc[df['ID'] == customer_id, 'Nama_Petani'] = name
        if phone :
            df.loc[df['ID'] == customer_id, 'No_Telp'] = phone
        if address :
            df.loc[df['ID'] == customer_id, 'Alamat'] = address
    
    # sv perubahan di csv
        df.to_csv(data_customer, index=False, encoding='utf-8')


        print(f"\n✓ Data pelanggan berhasil diupdate!")
        print(f"\n✅ Data pelanggan ID {customer_id} berhasil diperbarui!")
    
    except:
        print("Terjadi kesalahan: ")

    input("\nTekan Enter untuk melanjutkan...")


# =======================FITUR 5==============================
def delete_customer():
    """Delete customer"""
    os.system('cls')
    print("HAPUS PELANGGAN")
    data_customer = 'data_customer.csv'

    if not os.path.exists(data_customer):
        print(" Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    

        # Pastikan file ada
    if not os.path.exists(data_customer):
        print("❌ Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    try:
        df = pd.read_csv('data_customer.csv')
  
        if df.empty:
            print("❌ Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        customer_id = input("Masukkan ID Pelanggan yang akan dihapus: ")
    
        if not customer_id:
            print("❌ ID tidak boleh kosong!")
            input("\nTekan Enter untuk melanjutkan...")
            return
    
        if customer_id not in df['ID'].astype(str).values:
            print("❌ Pelanggan dengan ID tersebut tidak ditemukan.")
            input("\nTekan Enter untuk melanjutkan...")
            return
    
    # konfirmasih penghapusan
        confirm = input("\nYakin ingin menghapus? (y/n): ").strip().lower()
        if confirm == 'y':
            # Hapus data dan reset index agar tetap rapi
            df = df[df['ID'].astype(str) != customer_id]  
            df.reset_index(drop=True, inplace=True)
            # Optional: perbarui kolom ID agar urut kembali
            df['ID'] = range(1, len(df) + 1)
            df.to_csv(data_customer, index=False)  
            print("✓ Pelanggan berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")

    except Exception as e:
        print(f"⚠️ Terjadi kesalahan: {e}")

    input("Tekan Enter untuk melanjutkan...")