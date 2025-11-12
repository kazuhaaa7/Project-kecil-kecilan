from datetime import datetime
import os
import pandas as pd
from .admin.crud import  view_all_customers, search_customer, edit_customer, delete_customer
from .admin.report import view_daily_report,view_all_transactions,view_monthly_report,view_statistics
from .admin.change import ubah_password


# from .crud.atur_harga import add_customer

# semua fitur admin jadi 1 di sini, tp klo eksekusi bedakan
# ============================= FITUR ADMIN 1 ===================
def crud_customers():
    os.system('cls')
    while True:
        print("MANAJEMEN DATA PELANGGAN (PETANI)")
        print("[1]. Lihat Semua Pelanggan")
        print("[2]. Cari Pelanggan")
        print("[3]. Edit Pelanggan")
        print("[4]. Hapus Pelanggan")
        print("[0]. Kembali")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            view_all_customers()
        elif choice == "2":
            search_customer()
        elif choice == "3":
            edit_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")

# ============================= FITUR ADMIN 2 ===================
# ga kepake
# def set_price(): # pahami lagi dri penjelasan syntax syntax 
#     """Set service price per kg"""
#     print("ATUR HARGA JASA PER KG")

#     # ===== FUNGSI DALAM (helper) =====
#     def format_rupiah(amount):
#         return f"Rp{amount:,.0f}".replace(",", ".")

#     def input_float(prompt):
#         while True:
#             try:
#                 return float(input(prompt))
#             except ValueError:
#                 print("Masukkan angka yang valid!")

#     def print_header(title):
#         os.system('cls')
#         print("=" * 40)
#         print(title.center(40))
#         print("=" * 40 + "\n")
#     # ================================

#     # Cetak header
#     print_header("ATUR HARGA JASA PER KG")

#     data_harga = "data_harga.csv"

#     # Cek apakah file sudah ada
#     if os.path.exists(data_harga):
#         df = pd.read_csv(data_harga)
#     else:
#         df = pd.DataFrame(columns=["price_per_kg", "effective_date", "created_at"])

#     # Tampilkan harga terakhir
#     if not df.empty:
#         latest = df.iloc[-1]
#         print(f"Harga saat ini : {format_rupiah(latest['price_per_kg'])}/kg")
#         print(f"Efektif sejak  : {latest['effective_date']}\n")
#     else:
#         print("Belum ada harga yang ditetapkan.\n")

#     # Input harga baru
#     new_price = float(input("Masukkan harga baru per kg: "))

#     if new_price <= 0:
#         print("Harga harus lebih dari 0!")
#         input("\nTekan Enter untuk melanjutkan...")
#         return

#     # Tambahkan harga baru ke DataFrame
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     new_row = {
#         "price_per_kg": new_price,
#         "effective_date": now,
#         "created_at": now
#     }
#     df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

#     # Simpan ke CSV
#     df.to_csv(data_harga, index=False)

#     print(f"\nHarga baru {format_rupiah(new_price)}/kg berhasil ditetapkan!")
#     input("\nTekan Enter untuk melanjutkan...")
#     # Get current price

def atur_harga_jasa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("ATUR HARGA JASA PER KG".center(50))
    print("=" * 50)

    file_path = "data_harga.csv"

    # Pastikan file CSV ada
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["price_per_kg", "effective_date"])
        df.to_csv(file_path, index=False)

    # Baca data CSV
    df = pd.read_csv(file_path)

    # Tampilkan harga terakhir jika ada
    if not df.empty:
        last_price = df.iloc[-1]["price_per_kg"]
        last_date = df.iloc[-1]["effective_date"]
        print(f"\nHarga saat ini: Rp{int(last_price):,}/kg (ditetapkan pada {last_date})".replace(",", "."))
    else:
        print("\n Belum ada harga jasa yang ditetapkan.")

    # Tanyakan apakah ingin update harga
    print()
    pilihan = input("Apakah Anda ingin mengubah harga jasa? (y/n): ").strip().lower()

    if pilihan != "y":
        print("\nTidak ada perubahan harga. Kembali ke menu...")
        input("Tekan Enter untuk keluar...")
        return  # langsung keluar dari fungsi

    # Input harga baru jika user memilih "y"
    try:
        new_price = float(input("\nMasukkan harga baru per kg: "))
        if new_price <= 0:
            print("Harga harus lebih dari 0!")
            input("Tekan Enter untuk kembali...")
            return
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        input("Tekan Enter untuk kembali...")
        return

    # Simpan ke CSV
    new_data = {
        "price_per_kg": new_price,
        "effective_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(file_path, index=False)

    print(f"\nHarga baru Rp{int(new_price):,}/kg berhasil disimpan!".replace(",", "."))
    input("\nTekan Enter untuk melanjutkan...")




# ============================= FITUR ADMIN 3 ===================
def view_reports():
    """View milling reports"""
    while True:
        print("LAPORAN PENGGILINGAN")
        print("1. Laporan Harian")
        print("2. Laporan Bulanan")
        print("3. Laporan Semua Transaksi")
        print("4. Statistik Keseluruhan")
        print("0. Kembali")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            view_daily_report()
        elif choice == "2":
            view_monthly_report()
        elif choice == "3":
            view_all_transactions()
        elif choice == "4":
            view_statistics()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
