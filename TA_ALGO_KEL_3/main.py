import csv
import pandas as pd
import time
import tabulate
import os
from fitur.fituradmin import view_reports, atur_harga_jasa, crud_customers
from fitur.admin.change import ubah_password, change_username, ubahPw, ubahUser
from fitur.operator.crudop import add_customer, search_farmers, input_transaction
# from fitur.operator.reportop import laporan_hari_ini,laporan_transaksi, riwayat_laporan, laporan_transaksi_customer 


# registrasi dulu
def registrasi_admin():
    os.system('cls')
    print("=" * 50)
    print("REGISTER AKUN".center(50))
    print("=" * 50 + "\n")


    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password (min 8 karakter): ").strip()

    # Validasi password
    if len(password) < 8:
        print("Password minimal 8 karakter!")
        return
        

    # Jika file belum ada, buat file baru
    if not os.path.exists('data_admin.csv'):
        df = pd.DataFrame(columns=['Username', 'Password'])
        df.to_csv('data_admin.csv', index=False)

    # Cek apakah username sudah ada
    df = pd.read_csv('data_admin.csv')
    if username in df['Username'].values:
        print("Username sudah terpakai! Gunakan yang lain.")
        return

    # Simpan data baru
    new_data = pd.DataFrame([[username, password]], columns=['Username', 'Password'])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv('data_admin.csv', index=False)

    print("Registrasi berhasil! Silakan login...")


def registrasi_operator():
    os.system('cls')
    print("=" * 50)
    print("REGISTER AKUN".center(50))
    print("=" * 50 + "\n")


    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password (min 8 karakter): ").strip()

    # Validasi password
    if len(password) < 8:
        print("Password minimal 8 karakter!")
        return
        

    # Jika file belum ada, buat file baru
    if not os.path.exists('dt_operator.csv'):
        df = pd.DataFrame(columns=['Username', 'Password'])
        df.to_csv('operator.csv', index=False)

    # Cek apakah username sudah ada
    df = pd.read_csv('dt_operator.csv')
    if username in df['Username'].values:
        print("Username sudah terpakai! Gunakan yang lain.")
        return

    # Simpan data baru
    new_data = pd.DataFrame([[username, password]], columns=['Username', 'Password'])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv('dt_operator.csv', index=False)

    print("Registrasi berhasil! Silakan login...")

# fungsi login
def login(role):
    os.system('cls')
    print("=" * 50)
    print("SISTEM PENGGGILINGAN PADI".center(50))
    print("=" * 50 + "\n")

    
    # Cek apakah file admin ada
    if not os.path.exists('data_admin.csv'):
        print("File data_admin.csv tidak ditemukan!")
        df = pd.DataFrame(columns=['Username', 'Password'])
        df.to_csv('data_admin.csv', index=False)
        print("Silakan buat akun admin terlebih dahulu.")
        input("Tekan Enter...")
        return
    
    if not os.path.exists('dt_operator.csv'):
        print("File data_operator.csv tidak ditemukan!")
        df = pd.DataFrame(columns=['Username', 'Password'])
        df.to_csv('dt_operator.csv', index=False)
        print("Silakan buat akun admin terlebih dahulu.")
        input("Tekan Enter...")
        return
    # baca file
    df_admin = pd.read_csv('data_admin.csv')
    df_operator = pd.read_csv('dt_operator.csv')

    username = input("Username: ")
    password = input("Password: ")
    if len(password) < 8 :
        print("Password harus minimal 8 karakter!")
        input()
        return  
    
# Cek username & password di CSV
# Dalam pandas, kamu tidak bisa memakai and, or, atau not langsung.
# Kamu harus pakai &, |, dan ~, serta setiap kondisi harus dalam tanda kurung ( ).
    user_exists_admin = df_admin[(df_admin['Username'] == username) & (df_admin['Password'] == password)].astype(str)
    user_exists_operator = df_operator[(df_operator['Username'] == username) & (df_operator['Password'] == password)].astype(str)

    if not user_exists_admin.empty :##
        time.sleep(1)
        admin_menu(username)
    elif not user_exists_operator.empty:
        time.sleep(1)
        operator_menu(username)
    else:
        print("\nUssername atau password salah!")
        return
    # df= pd.DataFrame({'Ussername' : [ussername], 'Password' : [password]})
    # df = pd.concat([df, pd.DataFrame([{'Ussername' : ussername, 'Password': password}])], ignore_index=True)
    # df = df.to_csv('data_admin.csv', index=False)
    # print("DATA ADMIN SUDAH DITAMBAHKAN")


def admin_menu(username):
    while True:
        os.system('cls')
        print("=" * 50)
        print("MENU ADMIN".center(50))
        print("=" * 50 + "\n")

        # print(f"Selamat datang, {username}!\n")
        print(f"\nLogin berhasil sebagai ADMIN! Selamat datang, {username}")
        print("[1]. Manajemen Data Pelanggan (Petani)")
        print("[2]. Atur Harga Jasa per kg")
        print("[3]. Lihat Laporan Penggilingan ")
        print("[4]. Ubah Password")
        print("[5]. Ubah Username")
        print("[0]. Logout")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            crud_customers()
        elif choice == "2":
            atur_harga_jasa()
        elif choice == "3":
            view_reports()
        elif choice == "4":
            new_password =  ubah_password(username)
            if new_password:
                # Logout after username change
                print("\nAnda akan logout untuk login ulang dengan username baru.")
                input("Tekan Enter untuk melanjutkan...")
                return 
        elif choice == "5":
            new_username = change_username(username)
            if new_username:
                # Logout after username change
                print("\nAnda akan logout untuk login ulang dengan username baru.")
                input("Tekan Enter untuk melanjutkan...")
                return
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

def operator_menu(username):
    """Operator menu"""
    os.system('cls')
    while True:
        print(f"\nLogin berhasil sebagai OPERATOR! Selamat datang, {username}")
        print("[1]. Tambah Pelanggan (Petani)")
        print("[2]. Transaksi")
        print("[3]. Cari Petani")
        print("[4]. Lihat Riwayat Transaksi")
        print("[5]. Ubah Password")
        print("[6]. Ubah Username")
        print("[0]. Logout")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            add_customer()
        elif choice == "2":
            input_transaction(username)
        elif choice == "3":
            search_farmers()
        # elif choice == "4":
        #     laporan_transaksi()
        elif choice == "5":
            new_password = ubahPw(username)
            if new_password:
                # Logout after username change
                print("\nAnda akan logout untuk login ulang dengan username baru.")
                input("Tekan Enter untuk melanjutkan...")
                break
        elif choice == "6":
            new_username = ubahUser(username)
            if new_username:
                # Logout after username change
                print("\nAnda akan logout untuk login ulang dengan username baru.")
                input("Tekan Enter untuk melanjutkan...")
                break
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

# ========================Home Page
while True:
    os.system('cls')
    print("=" * 50)
    print("PILIHAN MENU".center(50))
    print("=" * 50 + "\n")

    print("[1]. REGISTRASI AKUN")
    print("[2]. LOGIN AKUN")
    print("[0]. KELUAR")

    piliihan = input("\nMenu yang dipilih: (pilih angka) ")
    os.system('cls')
    if piliihan == '1':
        os.system('cls')
        while True:
            print("=" * 50)
            print("PILIHAN MENU | REGISTRASI ".center(50))
            print("=" * 50 + "\n")
            
            print("[1]. SEBAGAI ADMIN")
            print("[2]. SEBAGAI OPERATOR")
            print("[0]. Kembali")
            subchoice = input("\n REGISTRASI SEBAGAI (pilih angka): ")
            if subchoice == '1':
                registrasi_admin()
            elif subchoice == '2':
                registrasi_operator()
            elif subchoice == '0':
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
    elif piliihan == '2':
        os.system('cls')
        while True:
            print("=" * 50)
            print("PILIHAN MENU | LOGIN".center(50))
            print("=" * 50 + "\n")
            
            print("1. SEBAGAI ADMIN")
            print("2. SEBAGAI OPERATOR")
            print("0. Kembali")
            subchoice = input("\n LOGIN SEBAGAI (pilih angka): ")
            if subchoice == '1':
                login("admin") #role
            elif subchoice == '2':
                login("operator") #role
            elif subchoice == '0':
                os.system('cls')
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk melanjutkan...")

    elif piliihan == "0" :
        os.system('cls')
        break
    else: 
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk melanjutkan...")






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

