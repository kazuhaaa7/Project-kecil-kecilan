# import os
# import pandas as pd
# from datetime import datetime

# # def laporan_harian() :
#     os.system('cls')  # Bersihkan layar terminal
#     print("=" * 50)
#     print("LAPORAN HARIAN".center(50))
#     print("=" * 50 + "\n")

#     # Input tanggal
#     date_str = input("Masukkan tanggal (DD-MM-YYY) atau Enter untuk hari ini: ").strip()
#     if not date_str:
#         date_str = datetime.now().strftime("%Y-%m-%d")

#     transaksi_file = "data_transaksi.csv" # di isi dgn aksi operator
#     customer_file = "data_customer.csv"

#         # Pastikan file ada
#     if not os.path.exists(transaksi_file) or not os.path.exists(customer_file):
#         print("File data transaksi atau pelanggan belum tersedia.")
#         input("\nTekan Enter untuk melanjutkan...")
#         return
    
#     # Baca data dari CSV
#     df_transaksi = pd.read_csv(transaksi_file)
#     df_customer = pd.read_csv(customer_file)

#     # Gabungkan transaksi dengan nama pelanggan (seperti SQL JOIN)
#     df = pd.merge(df_transaksi, df_customer, left_on="customer_id", right_on="id", how="left")

#     # Pastikan kolom tanggal dalam format yang benar
#     df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime("%Y-%m-%d")

#     # Filter transaksi berdasarkan tanggal yang dimasukkan
#     df_filtered = df[df['date'] == date_str]

#     # Jika tidak ada data pada tanggal itu
#     if df_filtered.empty:
#         print(f"Tidak ada transaksi pada tanggal {date_str}.")
#         input("\nTekan Enter untuk melanjutkan...")
#         return

#     # Hitung total
#     total_weight = df_filtered['weight_kg'].sum()
#     total_cost = df_filtered['total_cost'].sum()

    



# def laporan_transaksi_customer()
    
# # def riwayat_laporan()
    

# def laporan_transaksi():
#     while True:
#         print("RIWAYAT TRANSAKSI")
#         print("1. Riwayat Transaksi Hari Ini")
#         print("2. Riwayat Transaksi Petani")
#         print("3. Riwayat Semua Transaksi")
#         print("0. Kembali")
        
#         choice = input("\nPilih menu: ")
        
#         # if choice == "1":
#             # laporan_harian()
#         # elif choice == "2":
#             # laporan_transaksi_customer()
#         # elif choice == "3":
#             # riwayat_laporan()
#         # # elif choice == "0":
#         #     break
#         # else:
#         #     print("Pilihan tidak valid!")