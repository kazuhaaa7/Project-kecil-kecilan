import csv
import pandas as pd
import time
import tabulate
import os
from fitur.fituradmin import crud_customers, 



# registrasi dulu
def registrasi():
    os.system('cls')
    print("=== REGISTER ADMIN ===")

    ussername = input("Buat Ussername: ").strip()
    password = input("Buat Password (min 8 karakter): ").strip()

    # Validasi password
    if len(password) < 8:
        print("⚠ Password minimal 8 karakter!")
        time.sleep(2)
        return
        

    # Jika file belum ada, buat file baru
    if not os.path.exists('data_admin.csv'):
        df = pd.DataFrame(columns=['Ussername', 'Password'])
        df.to_csv('data_admin.csv', index=False)

    # Cek apakah username sudah ada
    df = pd.read_csv('data_admin.csv')
    if ussername in df['Ussername'].values:
        print("⚠ Ussername sudah terpakai! Gunakan yang lain.")
        time.sleep(2)
        return

    # Simpan data baru
    new_data = pd.DataFrame([[ussername, password]], columns=['Ussername', 'Password'])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv('data_admin.csv', index=False)

    print("✅ Registrasi berhasil! Silakan login...")
    time.sleep(2)

# fungsi login
def login():
    os.system('cls')
    print("LOGIN SISTEM PENGGILINGAN PADI")
    
    # Cek apakah file admin ada
    if not os.path.exists('data_admin.csv'):
        print("⚠ File data_admin.csv tidak ditemukan!")
        df = pd.DataFrame(columns=['Username', 'Password'])
        df.to_csv('data_admin.csv', index=False)
        print("Silakan buat akun admin terlebih dahulu.")
        input("Tekan Enter...")
        return
    # baca file
    df = pd.read_csv('data_admin.csv')

    ussername = input("Ussername: ").strip()
    password = input("Password: ").strip()
    if len(password) < 8 :
        print("Sedang di proses ya...")
        time.sleep(1.1)
        print("⚠ Password harus minimal 8 karakter!")
        return  
    
# Cek username & password di CSV
    user_exists = df[(df['Ussername'] == ussername) & (df['Password'] == password)]

    if not user_exists.empty:
        print(f"\n✅ Login berhasil! Selamat datang, {ussername}")
        time.sleep(1.5)
        admin_menu(ussername)
    else:
        print("\n❌ Ussername atau password salah!")
        time.sleep(2)

    # df= pd.DataFrame({'Ussername' : [ussername], 'Password' : [password]})
    # df = pd.concat([df, pd.DataFrame([{'Ussername' : ussername, 'Password': password}])], ignore_index=True)
    # df = df.to_csv('data_admin.csv', index=False)
    # print("DATA ADMIN SUDAH DITAMBAHKAN")


def admin_menu(ussername):
    os.system('cls')
    while True:
        print("MENU ADMIN")
        print(f"Selamat datang, {ussername}!")
        print()
        print("1. Manajemen Data Pelanggan (Petani)")
        print("2. Atur Harga Jasa per kg")
        print("3. Lihat Laporan Penggilingan")
        print("4. Ubah Password")
        print("5. Ubah Username")
        print("0. Logout")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            crud_customers()
        elif choice == "2":
            set_price()
        # elif choice == "3":
            # view_reports()
        # elif choice == "4":
            # change_password(username)
        # elif choice == "5":
            # new_username = change_username(username)
            # if new_username:
                # Logout after username change
                # print("\nAnda akan logout untuk login ulang dengan username baru.")
                # time.sleep(3)
                # input("Tekan Enter untuk melanjutkan...")
                # break
        elif choice == "0":
            break
        else:
            time.sleep(3)
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

            
while True:
    os.system('cls')
    print("pilih menu")
    print("1. regist akun")
    print("2. login akun")
    print("0. keluar")

    piliihan = input("\nmenu yg dipilih: ")
    if piliihan == '1':
        registrasi()
    elif piliihan == '2':
        login()

    elif piliihan == "0" :
        break
    else: 
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk melanjutkan...")




# def operator_menu(username: str):
#     """Operator menu"""
#     while True:
#         clear_screen()
#         print_header("MENU OPERATOR")
#         print(f"Selamat datang, {username}!")
#         print()
#         print("1. Input Transaksi Penggilingan")
#         print("2. Cari Petani")
#         print("3. Lihat Riwayat Transaksi")
#         print("4. Ubah Password")
#         print("5. Ubah Username")
#         print("0. Logout")
        
#         choice = input("\nPilih menu: ")
        
#         if choice == "1":
#             input_transaction(username)
#         elif choice == "2":
#             search_farmers()
#         elif choice == "3":
#             view_transaction_history()
#         elif choice == "4":
#             change_password(username)
#         elif choice == "5":
#             new_username = change_username(username)
#             if new_username:
#                 # Logout after username change
#                 print("\nAnda akan logout untuk login ulang dengan username baru.")
#                 input("Tekan Enter untuk melanjutkan...")
#                 break
#         elif choice == "0":
#             break
#         else:
#             print("Pilihan tidak valid!")
#             input("Tekan Enter untuk melanjutkan...")

# def main():
#     """Main application function"""
#     # Initialize database
#     init_database()
    
#     while True:
#         clear_screen()
#         print_header("SISTEM TRANSAKSI PENGGILINGAN PADI")
#         print("Selamat datang di Sistem Transaksi Penggilingan Padi")
#         print()
#         print("1. Login")
#         print("0. Keluar")
        
#         choice = input("\nPilih menu: ")
        
#         if choice == "1":
#             user = login()
#             if user:
#                 if user['role'] == 'admin':
#                     admin_menu(user['username'])
#                 elif user['role'] == 'operator':
#                     operator_menu(user['username'])
#         elif choice == "0":
#             print("\nTerima kasih! Sampai jumpa.")
#             break
#         else:
#             print("Pilihan tidak valid!")
#             input("Tekan Enter untuk melanjutkan...")

# if __name__ == "__main__":
#     main()

