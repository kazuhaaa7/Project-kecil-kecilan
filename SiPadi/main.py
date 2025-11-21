import csv
import pandas as pd
import time
from tabulate import tabulate
import os
from datetime import datetime

FILE_ADMIN = 'data_admin.csv'
FILE_OPERATOR = 'data_operator.csv'
FILE_HARGA = 'dt_harga.csv' 
FILE_PELANGGAN = 'data_pelanggan.csv'
FILE_TRANSAKSI = 'data_trasaksi.csv'

# sinkronkan kata katanya ketika error dari kedua fungsi login
# ================================================ CEK DATA ======================================================
def cekData():
    if not os.path.exists(FILE_ADMIN):  
        user = pd.DataFrame(columns=['username', 'password']) 
        user.to_csv(FILE_ADMIN, index=False) 
    if not os.path.exists(FILE_OPERATOR):  
        user = pd.DataFrame(columns=['username', 'password']) 
        user.to_csv(FILE_OPERATOR, index=False) 
    if not os.path.exists(FILE_HARGA):  
        user = pd.DataFrame(columns=['harga/kg','tglDibuat']) 
        user.to_csv(FILE_HARGA, index=False) 
    if not os.path.exists(FILE_PELANGGAN):  
        user = pd.DataFrame(columns=['id', 'namaPetani','noTelp', 'alamat']) 
        user.to_csv(FILE_PELANGGAN, index=False) 
    if not os.path.exists(FILE_TRANSAKSI):  
        user = pd.DataFrame(columns=['idPel','tanggal', 'berat','harPerKg', 'total' ]) 
        user.to_csv(FILE_TRANSAKSI, index=False) 

# ================================================ REGIS AS ADMIN ======================================================
# def regisAdmin():
#     os.system('cls')
#     teks = """

#     ░██████╗██╗██████╗░░█████╗░██████╗░██╗
#     ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
#     ╚█████╗░██║██████╔╝███████║██║░░██║██║
#     ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
#     ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
#     ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
#     """
#     print(teks)
#     print('╔' + '═'*48 + '╗')
#     print('║' + "REGISTER AKUN ADMIN".center(48) + '║')
#     print('╚' + '═'*48 + '╝') 

#     df = pd.read_csv(FILE_ADMIN)
#     # kondisi 1
#     while True:
#         username = input("Masukkan Username: ").strip().lower()
#         if not username:
#             print("\nUsername tidak boleh kosong")
#         elif len(username) < 3:
#             print('\nUnsername harus berisi minimal 3 karakter!')
#         if (df['username'] == username).any():
#             print("\nUsername sudah ada. tentukan yang lain")
#             # error| fix bug

#     # kondisi 2
#     while True:
#         password = input("Masukkan Password: ").strip().lower()
#         break
#     # Jika file belum ada, buat file baru
#     if not os.path.exists(FILE_ADMIN):
#         df = pd.DataFrame(columns=['username', 'password'])
#         df.to_csv(FILE_ADMIN, index=False)

#     # Simpan data baru
#     df = pd.read_csv(FILE_ADMIN)
#     dataBaru = {'username' : username, 'password': password}
#     dataBaruDf = pd.DataFrame([dataBaru])
#     df = pd.concat([df, dataBaruDf], ignore_index=True)
#     df.to_csv(FILE_ADMIN, index=False)
#     print(f"\nRegistrasi {username} sebagai admin berhasil!")

#     i = input("\nKetik apa saja untuk kembali...")
#     return main()

# ================================================ REGIS AS OPERATOR ======================================================
def regisOperator():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
    print('╚' + '═'*48 + '╝') 

    df = pd.read_csv(FILE_OPERATOR)
    # kondisi 1
    while True:
        username = input("Masukkan Username: ").strip().lower()
        if not username:
            os.system('cls')
            teks = """

            ░██████╗██╗██████╗░░█████╗░██████╗░██╗
            ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
            ╚█████╗░██║██████╔╝███████║██║░░██║██║
            ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
            ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
            ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
            """
            print(teks)
            print('╔' + '═'*48 + '╗')
            print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
            print('╚' + '═'*48 + '╝') 
            print("\nUsername tidak boleh kosong")
            continue
        if len(username) < 3:
            os.system('cls')
            teks = """

            ░██████╗██╗██████╗░░█████╗░██████╗░██╗
            ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
            ╚█████╗░██║██████╔╝███████║██║░░██║██║
            ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
            ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
            ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
            """
            print(teks)
            print('╔' + '═'*48 + '╗')
            print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
            print('╚' + '═'*48 + '╝') 
            print('\nUsername harus berisi minimal 3 karakter!')
            continue
        if (df['username'] == username).any():
            os.system('cls')
            teks = """

            ░██████╗██╗██████╗░░█████╗░██████╗░██╗
            ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
            ╚█████╗░██║██████╔╝███████║██║░░██║██║
            ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
            ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
            ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
            """
            print(teks)
            print('╔' + '═'*48 + '╗')
            print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
            print('╚' + '═'*48 + '╝') 
            print("\nUsername sudah ada. tentukan yang lain")
            continue
        else:
            break

        # kondisi 2
    while True:
        password = input("Masukkan Password: ").strip().lower()
        if not password:
            print("Passwrd tidak boleh kosong")
            continue

        # Jika file belum ada, buat file baru
        if not os.path.exists(FILE_OPERATOR):
            df = pd.DataFrame(columns=['username', 'password'])
            df.to_csv(FILE_OPERATOR, index=False)

        # Simpan data baru
        df = pd.read_csv(FILE_OPERATOR)
        dataBaru = {'username' : username, 'password': password}
        dataBaruDf = pd.DataFrame([dataBaru])
        df = pd.concat([df, dataBaruDf], ignore_index=True)
        df.to_csv(FILE_OPERATOR, index=False)
        print(f"\nRegistrasi {username} sebagai admin berhasil!")

        i = input("\nKetik apa saja untuk kembali")
        return main()

# ================================================ LOGIN ADMIN ======================================================
# fungsi login
def loginAdmin():
    while True:

        os.system('cls')
        teks = """
        ░██████╗██╗██████╗░░█████╗░██████╗░██╗
        ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
        ╚█████╗░██║██████╔╝███████║██║░░██║██║
        ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
        ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
        ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
        """
        print(teks)
        print('╔' + '═'*48 + '╗')
        print('║' + "LOGIN AKUN".center(48) + '║')
        print('╚' + '═'*48 + '╝') 


        admin = pd.read_csv(FILE_ADMIN)

        # Cek apakah file admin ada
        if not os.path.exists(FILE_ADMIN):
            print("File data_admin.csv tidak ditemukan!")
            df = pd.DataFrame(columns=['Username', 'Password'])
            df.to_csv(FILE_ADMIN, index=False)
            print("Silakan buat akun admin terlebih dahulu.")
            input("Tekan Enter...")
            return

        admin['username'] = admin['username'].astype(str)
        admin['password'] = admin['password'].astype(str)

        while True:
            username = input("Masukkan Username: ").strip().lower()
            if not username:
                os.system('cls')
                teks = """

                ░██████╗██╗██████╗░░█████╗░██████╗░██╗
                ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
                ╚█████╗░██║██████╔╝███████║██║░░██║██║
                ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
                ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
                ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
                """
                print(teks)
                print('╔' + '═'*48 + '╗')
                print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
                print('╚' + '═'*48 + '╝') 
                print("\nUsername tidak boleh kosong")
                continue
            if len(username) < 3:
                os.system('cls')
                teks = """

                ░██████╗██╗██████╗░░█████╗░██████╗░██╗
                ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
                ╚█████╗░██║██████╔╝███████║██║░░██║██║
                ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
                ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
                ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
                """
                print(teks)
                print('╔' + '═'*48 + '╗')
                print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
                print('╚' + '═'*48 + '╝') 
                print('\nUsername harus berisi minimal 3 karakter!')
                continue
            else:
                break

        # kondisi 2
        while True:
            password = input("Masukkan Password: ").strip().lower()
            if not password:
                print("Password tidak boleh kosong")
                continue
            else:
                break


        # operator
        if not os.path.exists(FILE_ADMIN):
            print("File data_admin.csv tidak ditemukan!")
            df = pd.DataFrame(columns=['Username', 'Password'])
            df.to_csv('dt_operator.csv', index=False)
            print("Silakan buat akun admin terlebih dahulu.")
            input("Tekan Enter...")
            return
        # Cek username & password di CSV
        # Dalam pandas, kamu tidak bisa memakai and, or, atau not langsung.
        # Kamu harus pakai &, |, dan ~, serta setiap kondisi harus dalam tanda kurung ( ).
        min = admin[(admin['username'] == username) & (admin['password'] == password)].astype(str)
        if not min.empty:
            admin_menu(username)
        else: 
            print('\nLogin gagal! Username atau password salah.')
            print("\nTunggu sebentar, kmau akan diarahkan ke halaman login")

            time.sleep(2) #delay
            return

# ==================================LOGIN MENU===========================================
def loginOperator():
    while True:
        os.system('cls')
        teks = """

        ░██████╗██╗██████╗░░█████╗░██████╗░██╗
        ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
        ╚█████╗░██║██████╔╝███████║██║░░██║██║
        ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
        ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
        ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
        """
        print(teks)
        print('╔' + '═'*48 + '╗')
        print('║' + "LOGIN AKUN".center(48) + '║')
        print('╚' + '═'*48 + '╝') 

        admin = pd.read_csv(FILE_OPERATOR)

        # Cek apakah file admin ada
        if not os.path.exists(FILE_OPERATOR):
            print("File data_oeprator.csv tidak ditemukan!")
            df = pd.DataFrame(columns=['Username', 'Password'])
            df.to_csv(FILE_OPERATOR, index=False)
            print("Silakan buat akun admin terlebih dahulu.")
            input("Tekan Enter...")
            return

        admin['username'] = admin['username'].astype(str)
        admin['password'] = admin['password'].astype(str)

        while True:
            username = input("Masukkan Username: ").strip().lower()
            if not username:
                os.system('cls')
                teks = """

                ░██████╗██╗██████╗░░█████╗░██████╗░██╗
                ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
                ╚█████╗░██║██████╔╝███████║██║░░██║██║
                ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
                ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
                ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
                """
                print(teks)
                print('╔' + '═'*48 + '╗')
                print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
                print('╚' + '═'*48 + '╝') 
                print("\nUsername tidak boleh kosong")
                continue
            if len(username) < 3:
                os.system('cls')
                teks = """

                ░██████╗██╗██████╗░░█████╗░██████╗░██╗
                ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
                ╚█████╗░██║██████╔╝███████║██║░░██║██║
                ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
                ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
                ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
                """
                print(teks)
                print('╔' + '═'*48 + '╗')
                print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
                print('╚' + '═'*48 + '╝') 
                print('\nUsername harus berisi minimal 3 karakter!')
                continue
            else:
                break
        # kondisi 2
        while True:
            password = input("Masukkan Password: ").strip().lower()
            if not password:
                print("Password tidak boleh kosong")
                continue
            else:
                break

        # Cek username & password di CSV
        # Dalam pandas, kamu tidak bisa memakai and, or, atau not langsung.
        # Kamu harus pakai &, |, dan ~, serta setiap kondisi harus dalam tanda kurung ( ).
        min = admin[(admin['username'] == username) & (admin['password'] == password)].astype(str)
        if not min.empty:
            operator_menu(username)
        else: 
            print('\nLogin gagal! Username atau password salah.')
            print("\nTunggu sebentar, kmau akan diarahkan ke halaman login")
            time.sleep(2) #delay
            return

# ==================================MENU FITUR ADMIN===========================================
# ==================================MENU FITUR ADMIN - CRUD===========================================
# =========================FITUR 1 -- FITUR ADMIN=============================
def tambahDataPelanggan():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "TAMBAH PELANGGAN BARU".center(48) + '║')
    print('╚' + '═'*48 + '╝') 


# jika file blm ada, buat file baru
    if not os.path.exists(FILE_PELANGGAN):
        print(" Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")

    df = pd.read_csv(FILE_PELANGGAN)
    # writer.writerow(["ID", "Nama_Petani", "No_Telp", "Alamat"])  # <-- header kolom


    nama = input("Nama Petani: ").strip().upper()
    if not nama:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    try:
        notelp = int(input("Masukkan No. Telepon (awali dengan 62): "))
    except ValueError:
        print("Masukkan nomor telp dnegan angka ya :<")
        print("Porgram akan kembali ke menu dalam 3 detik dari sekarang")
        time.sleep(3)
        return
    alamat = input("Masukkan Alamat Lengkap : ").strip().lower()
    
# cari id cus
    # if os.path.exists(data_customer):
    customer_id = 1
    try:
        with open(FILE_PELANGGAN, mode="r", encoding="utf-8") as file:
            read = list(csv.reader(file))
        if len(read) >= 1:
            last_id = int(read[-1][0]) #pahami syntax
            customer_id = last_id + 1
    except:
            pass #placeholder — yaitu perintah kosong yang tidak melakukan apa-apa.

            # membuat file + menulis header
    # df = pd.DataFrame(columns= ['id','namaPetani','noTelp', 'alamat'] )
    # df.to_csv(FILE_PELANGGAN, index=False, encoding='utf-8')

    # sv ke csv
    with open(FILE_PELANGGAN, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, nama, notelp, alamat])
    
    
    
    print(f"\nPelanggan '{nama}' berhasil ditambahkan! (ID: {customer_id})")
    input("\nEnter untuk lanjut...")
# =======================FITUR 2 -- FITUR ADMIN===============================\
# ADA BUG YG PERLU DIFIX
def lihatData():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "DAFTAR PELANGGAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 

    if not os.path.exists(FILE_PELANGGAN):
        print(" Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    try:
        df = pd.read_csv(FILE_PELANGGAN)

        if df.empty:
            print(" Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        # ubah type data
        df['noTelp'] = df['noTelp'].astype(str)
        print(type(df['noTelp'].iloc[-1]))
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        input("\nTekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {e}")
        time.sleep(2)
        return
    
# =======================FITUR 3 -- FITUR ADMIN===============================
def cariPelanggan():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "CARI PELANGGAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 

# tampilkan tabel customer
    try:
        df = pd.read_csv(FILE_PELANGGAN)
   
        if df.empty:
            print(" Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))

    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {e}")

    keyword = input("Cari berdasarkan nama: ").strip().upper()
    if not keyword:
        print("Keyword tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    # lakukan pencarian
    df = df.astype(str)
    hasil = df[
            df['namaPetani'].str.contains(keyword, case=False)] #.str.contains = untuk memeriksa apakah ada suatu str yg mengandungg kata tertentu
# tampilkan hasil pencarian
    if not hasil.empty:
        os.system('cls')
        print("\n Hasil pencarian ditemukan:\n")
        print(tabulate(hasil, headers='keys', tablefmt="fancy_grid", showindex=False))
        input("Tekan Enter untuk melanjutkan...")
        return
    
    else:
        print("\nTidak ada data yang cocok dengan keyword tersebut.")

# =======================FITUR 4 -- FITUR ADMIN===============================
def editDataPelanggan():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "EDIT DATA PELANGGAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 

        # pastikan file ada
    if not os.path.exists(FILE_PELANGGAN):
        print("Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    

    df= pd.read_csv(FILE_PELANGGAN, dtype={'noTelp': 'string'})

    if df.empty:
        print("Data pelanggan masih kosong.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))

# input ID pelanggan yang mau diedit
    try:
        idPelanggan = int(input("Masukkan ID Pelanggan yang ingin diedit: "))
    except ValueError:
        print("ID harus berupa angka!")
        input("\nTekan Enter untuk melanjutkan...")
        return editDataPelanggan()


    # cek apakah ID ada
    if idPelanggan not in df['id'].values:
        print("Pelanggan dengan ID tersebut tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return editDataPelanggan()
    

    # ambil data pelanggan yang sesuai
    dt_Customer = df[df['id'] == idPelanggan].iloc[0]
    

    print(f"\nData saat ini:")
    print(f"Nama: {dt_Customer['namaPetani']}")
    print(f"Telepon: {dt_Customer['noTelp']}")
    print(f"Alamat: {dt_Customer['alamat'] } \n")
    

    # input data baru
    namaBaru = input(f"Nama baru (Enter untuk tidak mengubah): ").strip().upper()
    notelpBaru = input(f"Telepon baru (Enter untuk tidak mengubah) | (awali dengan 62): ")
# kelemahan: ga bisa memprediksi outputnya juka angka yg diawali bukan 62
    if notelpBaru.isdigit():
        df['noTelp'] = df['noTelp'].astype('string')
        df.loc[df['id'] == idPelanggan, 'noTelp'] = notelpBaru
        df["noTelp"] = df["noTelp"].astype("string").str.replace(".0", "", regex=False)

    elif not notelpBaru:
        df.loc[df['id'] == idPelanggan, 'noTelp'] = str(notelpBaru)# why diubah jadi str, karna kolom sblmny aaku jadikan float- kalo jadi float untuk output setelah input notelp akan jadi format ribuan dan bisa bisa angka 0 nya hilang
        pass
    else: 
        print("Masukkan nomor dengan angka!")
        time.sleep(1)
        return editDataPelanggan()
    
    alamatBaru = input(f"Alamat baru (Enter untuk tidak mengubah): ").strip().lower()

    if namaBaru:
        df.loc[df['id'] == idPelanggan, 'namaPetani'] = namaBaru
    if notelpBaru :
        df.loc[df['id'] == idPelanggan, 'noTelp'] = str(notelpBaru)
    if alamatBaru :
        df.loc[df['id'] == idPelanggan, 'alamat'] = alamatBaru

# sv perubahan di csv
    df.to_csv(FILE_PELANGGAN, index=False, encoding='utf-8')


    print(f"\n✓ Data pelanggan berhasil diupdate!")
    print(f"\nData pelanggan ID {idPelanggan} berhasil diperbarui!")

input("\nTekan Enter untuk melanjutkan...")

# =======================FITUR 5 -- FITUR ADMIN==============================
def hapusDataPelanggan():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "HAPUS DATA PELANGGAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 

        # Pastikan file ada
    if not os.path.exists(FILE_PELANGGAN):
        print("Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    df = pd.read_csv(FILE_PELANGGAN)

    if df.empty:
        print("Data pelanggan masih kosong.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
    idPelanggan = input("Masukkan ID Pelanggan yang akan dihapus: ")

    if not idPelanggan:
        print("ID tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    if idPelanggan not in df['id'].astype(str).values:
        print("Pelanggan dengan ID tersebut tidak ditemukan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

# konfirmasih penghapusan
    confirm = input("\nYakin ingin menghapus? (y/n): ").strip().lower()
    if confirm == 'y':
        # Hapus data dan reset index agar tetap rapi
        df = df[df['id'].astype(str) != idPelanggan]  
        df.reset_index(drop=True, inplace=False)  # Optional: perbarui kolom ID agar urut kembali

        df['id'] = range(1, len(df) + 1)
        df.to_csv(FILE_PELANGGAN, index=False)  
        print("Pelanggan berhasil dihapus!")
    elif confirm == 'n':
        print("Penghapusan data dibatalkan. \nprogram akan berjalan 2 detik dari sekarang")
        time.sleep(2)
        return hapusDataPelanggan()
    else:
        print("Masukkan huruf yang sesuai dengan pilihan. \nprogram akan berjalan 2 detik dari sekarang")
        time.sleep(2)
        return hapusDataPelanggan()


    input("Tekan Enter untuk melanjutkan...")

# ============================= FITUR ADMIN 1 |AKU ADMIN DAN KAU ROOTS ===================
def tambahPelanggan():

    while True:
        os.system('cls')    
        teks = """

        ░██████╗██╗██████╗░░█████╗░██████╗░██╗
        ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
        ╚█████╗░██║██████╔╝███████║██║░░██║██║
        ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
        ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
        ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
        """
        print(teks)
        print('╔' + '═'*48 + '╗')
        print('║' + "MANAJEMEN DATA PELANGGAN (PETANI)".center(48) + '║')
        print('╚' + '═'*48 + '╝') 
        print("[1]. Tambah Data Pelanggan")
        print("[2]. Lihat Semua Pelanggan")
        print("[3]. Cari Pelanggan")
        print("[4]. Edit Pelanggan")
        print("[5]. Hapus Pelanggan")
        print("[0]. Kembali")
        
        pilih = input("\nPilih menu: ")
        
        if pilih == "1":
            tambahDataPelanggan()
        elif pilih == "2":
            lihatData()
        elif pilih == "3":
            cariPelanggan()
        elif pilih == "4":
            editDataPelanggan()
        elif pilih == "5":
            hapusDataPelanggan()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")

# ============================= FITUR ADMIN 2 | set harga ===================
def setHarga():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "ATUR HARGA JASA PER KG)".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    
    read = pd.read_csv(FILE_HARGA)

    # Pastikan file CSV ada
    if not os.path.exists(FILE_HARGA):
        df = pd.DataFrame(columns=['harga/kg','tglDibuat'])
        df.to_csv(FILE_HARGA, index=False)

    # Baca data CSV
    df = pd.read_csv(FILE_HARGA)

    # Tampilkan harga terakhir jika ada
    if not df.empty:
        hargaTerakhir = df.iloc[-1]["harga/kg"] #mengambil nilai dari var df dengan atribut .iloc[] (yg bisa diakses dengan indeks atau nama kolom)  lalu -1 karna ingin mengambil nilai paling akhir yg ada di kolom p
        last_date = df.iloc[-1]["tglDibuat"]
        print(f"\nHarga saat ini: Rp{float(hargaTerakhir):,}/kg (ditetapkan pada {last_date}") # format replace: ("yg akan diganti", "pengganti")
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
        hargaBaru = float(input("\nMasukkan harga baru per kg: "))
        if hargaBaru <= 0:
            print("Harga harus lebih dari 0!")
            input("Tekan Enter untuk kembali...")
            return
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        input("Tekan Enter untuk kembali...")
        return

    # Simpan ke CSV
    dataBaru = {
        "harga/kg": hargaBaru,
        "tglDibuat": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    df = pd.concat([df, pd.DataFrame([dataBaru])], ignore_index=True)
    df.to_csv(FILE_HARGA, index=False)

    print(f"\nHarga baru Rp{int(hargaBaru):,}/kg berhasil disimpan!")
    input("\nTekan Enter untuk melanjutkan...")

# ============================= FITUR ADMIN 1 | LAPORAN===================
# laporan hari based tgl
def laporanHarian():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "RIWAYAT HARIAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    while True:
        df = pd.read_csv(FILE_TRANSAKSI) 

        # input tanggal yg ingin ditentukkan
        inpTgl = input("Masukkan tanggal (DD-MM-YYY) atau Enter untuk hari ini: ").strip()
        if not inpTgl:
            inpTgl = df['tanggal'].iloc[-1]

    # cek keberadaan file
        if not os.path.exists(FILE_TRANSAKSI) or not  os.path.exists(FILE_PELANGGAN) :
            print(" Belum ada data tranksaski.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        

        if df.empty:
            print(" Data transaksi masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        try:     
            os.system('cls')
            teks = """
            ░██████╗██╗██████╗░░█████╗░██████╗░██╗
            ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
            ╚█████╗░██║██████╔╝███████║██║░░██║██║
            ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
            ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
            ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
            """
            print(teks)
            print('╔' + '═'*48 + '╗')
            print('║' + "RIWAYAT HARIAN".center(48) + '║')
            print('╚' + '═'*48 + '╝ ') 
            print("Rincian Laporan Transaksi Hari Ini: ")
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

            jumlahTf= len(df['idPel'])
            jumlahBobot= df['berat'].sum()
            jumlahTotal = df['total'].sum()

            print(f"\n Tanggal {inpTgl}")
            print(f" Jumlah Transaksi: {jumlahTf}")
            print(f" Total Berat: {jumlahBobot}")
            print(f" Total Pendapatan: {jumlahTotal}")
            input("\n Enter untuk kembali...")
            return
        except ValueError:
            print("Ada yang salah dari program")

# ============================= FITUR ADMIN 3 | LAPORAN===================
def laporan():
    while True:
        os.system('cls')
        teks = """

        ░██████╗██╗██████╗░░█████╗░██████╗░██╗
        ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
        ╚█████╗░██║██████╔╝███████║██║░░██║██║
        ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
        ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
        ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
        """
        print(teks)
        print('╔' + '═'*48 + '╗')
        print('║' + "LAPORAN PENGGILINGAN".center(48) + '║')
        print('╚' + '═'*48 + '╝')   
        print()
        print("1. Laporan Harian")
        print("2. Laporan Bulanan")
        print("3. Laporan Semua Transaksi")
        print("4. Statistik Keseluruhan")
        print("0. Kembali")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            laporanHarian()
        # elif choice == "2":
        #     view_monthly_report()
        # elif choice == "3":
        #     view_all_transactions()
        # elif choice == "4":
        #     view_statistics()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")

# ============================= FITUR ADMIN 3 | UBAH PW===================
def ubahPasswordAdmin(): #pahami dan ubah syntax sepaham kmu"
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "UBAH PASSWORD".center(48) + '║')
    print('╚' + '═'*48 + '╝') 

    while True:
        # Pastikan file ada
        if not os.path.exists(FILE_ADMIN):
            print("File data_admin.csv belum ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            return 

        # Baca file CSV
        df = pd.read_csv(FILE_ADMIN)

        # Cek apakah kolom yang dibutuhkan ada
        if not {'username', 'password'}.issubset(df.columns):
            print("File CSV tidak memiliki kolom 'username' atau 'password'.")
            input("\nTekan Enter untuk melanjutkan...")
            return 
        
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        
        # Cari user
        password = input("Masukkan password sebelumnya untuk konfirmasi: ").strip().lower()
        passwordCheck = df[df['password'] == password]


        if passwordCheck.empty:
            print("Username tidak ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            return 

        # # Verifikasi password
        if password != passwordCheck.iloc[0]['password']:
            print("Username salah!")
            input("\nTekan Enter untuk melanjutkan...")
            return 
    
        # Input pw baru       
        passwordBaru = input("Masukkan password baru: ").strip().lower()     
        if not passwordBaru:
            print("Password baru tidak boleh kosong!")
            input("\nTekan Enter untuk melanjutkan...")
            return 
        
        # Update password
        df.loc[df['password'] == password, 'password'] = passwordBaru
        df.to_csv(FILE_ADMIN, index=False)
        print(f"\npassword berhasil diubah menjadi '{passwordBaru}'!")
        time.sleep(1.5)
        os.system('cls')
        return 

## ==============================l====MENU FITUR ADMIN - ubah admin operator ====================================
def ubahUsername(username): #pahami dan ubah syntax sepaham kmu

    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "UBAH USERNAME".center(48) + '║')
    print('╚' + '═'*48 + '╝') 


# baca file
    df = pd.read_csv(FILE_ADMIN)


    # Pastikan file ada
    if not os.path.exists( FILE_ADMIN):
        print("File data_admin.csv belum ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Baca file CSV
    df = pd.read_csv(FILE_ADMIN)

    # Cek apakah kolom yang dibutuhkan ada
    if not {'username', 'password'}.issubset(df.columns):
        print("File CSV tidak memiliki kolom 'username' atau 'password'.")
        input("\nTekan Enter untuk melanjutkan...")
        return 
    
    print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
    # Cari user
    username = input("Masukkan username sebelumnya untuk konfirmasi: ").strip()
    user = df[df['username'] == username] 
    if user.empty:
        print("Username tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Verifikasi password
    if username != user.iloc[0]['username']:
        print("username salah!")
        print(user)
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Input username baru
    usernameBaru = input(f"Masukkan username baru (saat ini: {username}): ").strip()
    if not usernameBaru :
        print("Username baru tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    if usernameBaru == username:
        print("Username baru sama dengan yang lama.")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Cek apakah username baru sudah dipakai
    if usernameBaru in df['username'].values:
        print("Username sudah digunakan oleh user lain!")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Update username
    df.loc[df['username'] == username, 'username'] = usernameBaru
    df.to_csv( FILE_ADMIN, index=False)

    print(f"\nUsername berhasil diubah menjadi '{usernameBaru}'!")
    # time.sleep(1.5)
    return


# ==================================MENU FITUR OPERATOR===========================================
# ==================================MENU FITUR OPERATOR - add cust ====================================
def tambahDataPelanggan():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "TAMBAH PELANGGAN BARU".center(48) + '║')
    print('╚' + '═'*48 + '╝') 


# jika file blm ada, buat file baru
    if not os.path.exists(FILE_PELANGGAN):
        print(" Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")

    df = pd.read_csv(FILE_PELANGGAN)
    # writer.writerow(["ID", "Nama_Petani", "No_Telp", "Alamat"])  # <-- header kolom


    nama = input("Nama Petani: ").strip().upper()
    if not nama:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    try:
        notelp = int(input("Masukkan No. Telepon (awali dengan 62): "))
    except ValueError:
        print("Masukkan nomor telp dengan angka ya :<")
        input("Tekan Enter untuk melanjutkan...")
        return
    alamat = input("Masukkan Alamat Lengkap : ").strip().lower()
    
# cari id cus
    # if os.path.exists(data_customer):
    idPelanggan = 1
    try:
        with open(FILE_PELANGGAN, mode="r") as file: #ecnode agar dijadikan bytes
            baca = list(csv.reader(file))
        if len(baca) >= 1:
            idTerakhir = int(baca[-1][0]) #pahami syntax
            idPelanggan = idTerakhir + 1
    except:
            pass #placeholder — yaitu perintah kosong yang tidak melakukan apa-apa.

            # membuat file + menulis header - ga usah karna udah bikin dan udah ada headernya juga
    # df = pd.DataFrame(columns= ['id','namaPetani','noTelp', 'alamat'] )
    # df.to_csv(FILE_PELANGGAN, index=False, encoding='utf-8')

    # sv ke csv | a for append
    with open(FILE_PELANGGAN, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([idPelanggan, nama, notelp, alamat])
    
    
    print(f"\nPelanggan '{nama}' berhasil ditambahkan! (ID: {idPelanggan})")
    input("\nEnter untuk lanjut...")

# ==================================MENU FITUR OPERATOR - transaksi ====================================
def transaksi():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "TANSAKSI PELANGGAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    while True:
# bikin alert jika tidak ada file pelanggan
        if not os.path.exists(FILE_PELANGGAN):
            print(" Belum ada data pelanggan.")
            input("\nTekan Enter untuk melanjutkan...")


        df_pelanggan = pd.read_csv(FILE_PELANGGAN, )
        print(tabulate(df_pelanggan, headers='keys', tablefmt="fancy_grid", showindex=False))

        id = input("Transaksi akan dilakukan berdasarkan id :")
        
        # alert jika var namaPncarian kosong
        if not id:
            print("Keyword tidak boleh kosong!")
            input("Enter untuk lanjut...")
            return
        
        # tujuan diencoding untuk data menjadi byts dann menghindar error ketika value dari csv mengandung karakter unik
#         with open(FILE_PELANGGAN, mode='r', encoding='utf-8') as file:
#             baca = list(csv.reader(file))
#             data = baca[1:]

# # menambah data ke list
#         pelanggan = []
#         for i in data:
#             if id in i[1]:
#                 pelanggan.append(i)
        
#         # alert jika iterasi di atas gagal
#         if not pelanggan:
#             print("Petani tidak ditemukan!")
#             input("Enter untuk lanjut...")
#             return
        
        # if len(pelanggan) > 1:
        #     print("\n ditemukan beberapa petani")
        #     print(tabulate(pelanggan, headers='keys', showindex=False))

            # mencari baris yang ID-nya sama dengan input user
        elif id in df_pelanggan['id'].astype(str).values:
            # .loc[ ..., 'namaPetani']
            # → ambil kolom namaPetani
            nama = df_pelanggan.loc[df_pelanggan['id'].astype(str) == id, 'namaPetani'].values[0] #→ ambil nilai pertama (karena hasil pencarian berupa array)
            print(f"Petani ditemukan, atas nama {nama}")

# baca data harga
        if not os.path.exists(FILE_HARGA):
            print("Harga belum ditetapkan admin!")
            input("Enter untuk lanjut...")
            return

        with open(FILE_HARGA, mode='r', encoding='utf-8') as file:
            harga = list(csv.reader(file)) [1:]
        
        if harga:
            w = harga[-1]
            p = float(w[0])
            print(f'\nharga jasa penggilingan saat ini {p}/kg')
        
        # input gabah
        try:
            gabah = float(
                input("Masukkan berat gabah yang akan digiling:  "))
                # next stepp dikali sm harga tiap kg dgn gabah
        except:
            print('Masukkan berat gabah dengan angka!')
            input('Klik Enter untuk kembali')
            return
        x = gabah * p
        print(x)
    
        tgl = datetime.now().strftime("%d-%m-%Y")
        id_last = 1
    # buat id 
        try:
            with open(FILE_TRANSAKSI, mode='a', newline='', encoding='utf-8') as afile:
                baca = list(csv.reader(afile))
        except ValueError: 
                pass
        
    # save ke csv
        with open(FILE_TRANSAKSI, mode='a', newline='', encoding='utf-8') as file:
            sv = csv.writer(file)
            sv.writerow([id, tgl ,gabah, p, x])
            input("\nTransaksi selesai, tekan Enter untuk kembali...")
            return
        # kolom id tidak + 1
        # input id bila diluar batas ga ada peringatan

# ==================================MENU FITUR OPERATOR - cari petani ====================================
def cariPetani():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "CARI PETANI".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    while True:
# bikin alert jika tidak ada file pelanggan
        if not os.path.exists(FILE_PELANGGAN):
            print(" Belum ada data pelanggan.")
            input("\nTekan Enter untuk melanjutkan...")


        # df1 = df1['id'] .astype(str)
        # df2 = df2['idPelanggan'].astype(str)
        try:
            df1 = pd.read_csv(FILE_PELANGGAN)
            df2 = pd.read_csv(FILE_TRANSAKSI)
        
            if df1.empty or df2.empty:
                print(" Data pelanggan atau Data Transaksi tidak ada file.")
                input("\nTekan Enter untuk melanjutkan...")
                return  
            dfc = pd.merge(df1, df2, left_on = 'id', right_on='idPel' ,how='inner') 
            dfc.drop(columns='idPel', inplace=True)
            print(tabulate(dfc, headers='keys', tablefmt="fancy_grid", showindex=False))
        except Exception as e:
                print(f"Terjadi kesalahan saat membaca data: {e}")


        object = input("Cari berdasarkan nama: ").upper()
        if not object:
            print("Keyword tidak boleh kosong!")
            input("Tekan Enter untuk melanjutkan...")
            return
        # elif object not in dfc['namaPetani']:
       
            

        # lakukan pencarian
        try:
            os.system('cls')
            teks = """

            ░██████╗██╗██████╗░░█████╗░██████╗░██╗
            ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
            ╚█████╗░██║██████╔╝███████║██║░░██║██║
            ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
            ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
            ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
            """
            print(teks)
            print('╔' + '═'*48 + '╗')
            print('║' + "CARI PETANI".center(48) + '║')
            print('╚' + '═'*48 + '╝') 
            hasil = dfc[dfc['namaPetani'].str.contains(object, case=False)] #case=False membuat pencarian tidak sensitif huruf besar/kecil
            print(tabulate(hasil, headers='keys', tablefmt="fancy_grid", showindex=False))


        except ValueError:
            print("ERROR bagian pencrian data")
            return
        # .str.contains() adalah fungsi pencarian teks (substring match) pada kolom bertipe string.
        if not dfc['namaPetani'].str.contains(object, case=False).any():
            print("Nama yang kamu cari mungkin belum didaftarkan")
            print("\nSilahkan daftar terlebih dahulu")

        input("\nEnter untuk kembali")
        return

# ==================================MENU FITUR OPERATOR - Transkasi | harian ====================================

def riwayatHarian():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "RIWAYAT HARIAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    while True:

# input tanggal yg ingin ditentukkan
        inpTanggal = input("Masukkan tanggal (DD-MM-YYY) atau Enter untuk hari ini: ").strip()
        if not inpTanggal:
            inpTanggal = datetime.now().strftime("%d-%m-%Y")

    # cek keberadaan file
        if not os.path.exists(FILE_TRANSAKSI) or not  os.path.exists(FILE_PELANGGAN) :
            print(" Belum ada data tranksaski.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
# baca file
        df1 = pd.read_csv(FILE_PELANGGAN)
        df2 = pd.read_csv(FILE_TRANSAKSI)

# memeriksa file
        if df1.empty or df2.empty:
                print(" Data pelanggan atau data transaksi masih kosong.")
                input("\nTekan Enter untuk melanjutkan...")
                return
        
        # gabungkan data
        dfc = pd.merge(df1, df2, left_on = 'id', right_on='idPel' ,how='inner')

# apabila dfc ada value yg kosong
        if dfc.empty:
            print(" Data pelanggan atau data transaksi masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return

# Pastikan kolom tanggal dalam format datetime
        dfc['tanggal'] = pd.to_datetime(dfc['tanggal'], dayfirst=True )
        # mengubah value 'tanggal' menjaddi object pd datetime| dayfrist= dimulai dari hari

# filter transaksi based tanggal yg gdiinout
        filter = dfc[dfc['tanggal'] == inpTanggal]

    # Urutkan berdasarkan tanggal terbaru
        dfc = dfc.sort_values(by="tanggal", ascending=False)
        # mengurutkan baris' dlm kolom based (by='tanggal)| asceding=false => mengurutkan data daru yg terbaru ke terlama, jika asceding=true => mengurutkan data terlama ke terbaru
        if dfc.empty:
            print("Belum ada transaksi atau belum ada pelanggan.")
            input("\nTekan Enter untuk melanjutkan...")


        totalBerat = filter['berat'].sum()
        totalBiaya = filter['total'].sum()

        # tampilkan ringkasan
        print(f"\nTanggal {inpTanggal}")
        print(f"Jumlah Transaksi {len(filter)}")
        print(f"Total Berat {totalBerat}")
        print(f"Total Pendapatan {totalBiaya}\n")

        print(tabulate(filter,headers='keys', tablefmt='fancy_grid', showindex=False))


        input("\nKlik Enter untuk kemabli...")
        return riwaywatTranskasi()
        
# ==================================MENU FITUR OPERATOR - Tansaksi based petani ====================================
def riwayatBasedPetani():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "RIWAYAT BERDASARKAN PETANI".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    while True:

# tampilkan data pelanggan
        df1 = pd.read_csv(FILE_PELANGGAN)
        print(tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False))



# input tanggal yg ingin ditentukkan
        inpPetani = input("Masukkan nama Petani: ").strip().upper()
        if not inpPetani:
            print("Nama petani tidak boleh kosong")
            input("Enter untuk kembali...")
            return

    # cek keberadaan file
        if not os.path.exists(FILE_TRANSAKSI) or not  os.path.exists(FILE_PELANGGAN) :
            print(" Belum ada data tranksaski.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
# baca file
        df1 = pd.read_csv(FILE_PELANGGAN)
        df2 = pd.read_csv(FILE_TRANSAKSI)

# memeriksa file
        if df1.empty or df2.empty:
                print(" Data pelanggan atau data transaksi masih kosong.")
                input("\nTekan Enter untuk melanjutkan...")
                return
        
        # gabungkan data
        dfc = pd.merge(df1, df2, left_on = 'id', right_on='idPel' ,how='inner')

# apabila dfc ada value yg kosong
        if dfc.empty:
            print(" Data pelanggan atau data transaksi masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return

# Pastikan kolom tanggal dalam format datetime
        # dfc['tanggal'] = pd.to_datetime(dfc['namaPetani'], ) 
        # mengubah value 'tanggal' menjaddi object pd datetime| dayfrist= dimulai dari hari

# filter transaksi based tanggal yg gdiinout
        filter = dfc[dfc['namaPetani'] == inpPetani]
        filter = dfc[dfc['namaPetani'].str.contains(inpPetani, case= False)]

    # Urutkan berdasarkan tanggal terbaru
        # dfc = dfc.sort_values(by="tanggal", ascending=False)
        # mengurutkan baris' dlm kolom based (by='tanggal)| asceding=false => mengurutkan data daru yg terbaru ke terlama, jika asceding=true => mengurutkan data terlama ke terbaru
        # if dfc.empty:
        #     print("Belum ada transaksi atau belum ada pelanggan.")
        #     input("\nTekan Enter untuk melanjutkan...")


        totalBerat = filter['berat'].sum()
        totalBiaya = filter['total'].sum()
        namaPetani = filter['namaPetani'].iloc[0]
        namatgl = filter['tanggal'].unique()

        # tampilkan ringkasan
        os.system('cls')

        print("Petani ditemukan")
        print(f"\nNama petani: {namaPetani}")
        print(f"Jumlah Transaksi: {len(filter)}")
        print(f"Total Berat: {totalBerat}")
        print(f"Total Pendapatan: {totalBiaya}\n")
# tabel yg divari
        print(tabulate(filter,headers='keys', tablefmt='fancy_grid', showindex=False))


        input("\nKlik Enter untuk kembali...")
        return riwaywatTranskasi()

# ==================================MENU FITUR OPERATOR - Tansaksi ====================================
def riwaywatTranskasi():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "DAFTAR PELANGGAN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    while True:
    
        print("[1]. Riwayat transaksi harian")
        print("[2]. Riwayat transaksi berdasrkan nama petani")
        print("[3]. Riwayat Keseleruhan")
        print("[0]. Logout")
        
        choice = input("\nPilih menu: ")

        
        if choice == "1":
            riwayatHarian()
        elif choice == "2":
            riwayatBasedPetani()
        # elif choice == "3":
        #     view_reports()
        elif choice == "0":
            return main()
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

## ==============================l====MENU FITUR OPERATOR - ubah pw operator ====================================
def ubahPWOperator():
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "UBAH PASSWORD".center(48) + '║')
    print('╚' + '═'*48 + '╝') 

    while True:
        # Pastikan file ada
        if not os.path.exists(FILE_OPERATOR):
            print("File data_admin.csv belum ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            return 

        # Baca file CSV
        df = pd.read_csv(FILE_OPERATOR)

        # Cek apakah kolom yang dibutuhkan ada
        if not {'username', 'password'}.issubset(df.columns):
            print("File CSV tidak memiliki kolom 'username' atau 'password'.")
            input("\nTekan Enter untuk melanjutkan...")
            return 
        
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        
        # Cari user

        password = input("Masukkan password sebelumnya untuk konfirmasi: ").strip().lower()
        pwCheck= df[df['password'] == password]

        if pwCheck.empty:
            print("Username tidak ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            return 

        # Verifikasi password
        if password != pwCheck.iloc[0]['password']:
            print("Password salah!")
            input("\nTekan Enter untuk melanjutkan...")
            return password

            # Input pw baru
        passwordBaru = input(f"Masukkan password baru (saat ini: {password}): ").strip().lower()
        if not passwordBaru:
            print("Password baru tidak boleh kosong!")
            input("\nTekan Enter untuk melanjutkan...")
            return 
            

        # Update password
        df.loc[df['password'] == password, 'password'] = passwordBaru #eror disini bang
        df.to_csv(FILE_OPERATOR, index=False)

        print(f"\npassword berhasil diubah menjadi '{passwordBaru}'!")
        # time.sleep(1.5)
        os.system('cls')
        return password

def ubahUSEROperator(username):
    
    os.system('cls')
    teks = """

    ░██████╗██╗██████╗░░█████╗░██████╗░██╗
    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
    ╚█████╗░██║██████╔╝███████║██║░░██║██║
    ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
    ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
    """
    print(teks)
    print('╔' + '═'*48 + '╗')
    print('║' + "UBAH USERNAME".center(48) + '║')
    print('╚' + '═'*48 + '╝') 

    while True:
        # Pastikan file ada
        if not os.path.exists( FILE_OPERATOR):
            print("File data_admin.csv belum ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            return 

        # Baca file CSV
        df = pd.read_csv(FILE_OPERATOR)

        # Cek apakah kolom yang dibutuhkan ada
        if not {'username', 'password'}.issubset(df.columns):
            print("File CSV tidak memiliki kolom 'username' atau 'password'.")
            input("\nTekan Enter untuk melanjutkan...")
            return 
        
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        
        # # Cari user
        # user = df[df['username'] == username]
        # if user.empty:
        #     print("Username tidak ditemukan!")
        #     input("\nTekan Enter untuk melanjutkan...")
        #     return 

        # Verifikasi password
        username = input("Masukkan username sebelumnya untuk konfirmasi: ").strip()
        userCheck = df[df['username']== username]


        if userCheck.empty:
            print("Username tidak ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            return 


                # Verifikasi password
        if username != userCheck.iloc[0]['username']:
            print("username salah!")
            input("\nTekan Enter untuk melanjutkan...")
            return

        # Input username baru
        usernameBaru = input(f"Masukkan username baru (saat ini: {username}): ").strip()
        if not usernameBaru :
            print("Username baru tidak boleh kosong!")
            input("\nTekan Enter untuk melanjutkan...")
            return

        if usernameBaru == username:
            print("\nUsername baru sama dengan yang lama.")
            input("\nTekan Enter untuk melanjutkan...")
            return 
        
        # apabila len user < 3\
        if len(usernameBaru) <3 :
            print("\nUsername minimmal 3 character")
            input("Enter untuk kembali ke menu")
            return

        # Update username
        df.loc[df['username'] == username, 'username'] = usernameBaru
        df.to_csv( FILE_OPERATOR, index=False)

        print(f"\nUsername berhasil diubah menjadi '{usernameBaru}'!")
        # time.sleep(1.5)
        os.system('cls')
        return




# ==================================MENU ADMIN===========================================
def admin_menu(username):
    print(f"\nLogin berhasil sebagai ADMIN!Selamat datang, {username}")
    while True:
        os.system('cls')
        teks = """

        ░██████╗██╗██████╗░░█████╗░██████╗░██╗
        ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
        ╚█████╗░██║██████╔╝███████║██║░░██║██║
        ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
        ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
        ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
        """
        print(teks)
        print('╔' + '═'*48 + '╗')
        print('║' + "MENU ADMIN".center(48) + '║')
        print('╚' + '═'*48 + '╝') 

        print("[1]. Manajemen Data Pelanggan (Petani)")
        print("[2]. Atur Harga Jasa per kg")
        print("[3]. Lihat Laporan Penggilingan ")
        print("[4]. Ubah Password")
        print("[5]. Ubah Username")
        print("[0]. Logout")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            tambahPelanggan()
        elif choice == "2":
            setHarga()
        elif choice == "3":
            laporan()
        elif choice == "4":
            ubahPasswordAdmin()
        elif choice == "5":
            ubahUsername(username)
            input()
        elif choice == "0":
            return main()
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

# ==================================MENU OPERATOR===========================================
def operator_menu(username):
    while True:
        os.system('cls')
        teks = """

        ░██████╗██╗██████╗░░█████╗░██████╗░██╗
        ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
        ╚█████╗░██║██████╔╝███████║██║░░██║██║
        ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
        ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
        ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
        """
        print(teks)
        print('╔' + '═'*48 + '╗')
        print('║' + "MENU OPERATOR".center(48) + '║')
        print('╚' + '═'*48 + '╝') 
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
            tambahDataPelanggan()
        elif choice == "2":
            transaksi()
        elif choice == "3":
            cariPetani()
        elif choice == "4":
            riwaywatTranskasi()
        elif choice == "5":
            new_password = ubahPW()
            if new_password:
                # Logout after username change
                print("\nAnda akan logout untuk login ulang.\nSilahkan Login ulang")
                input("Tekan Enter untuk melanjutkan...")
                return loginOperator()
        elif choice == "6":
            new_username = ubahUSER(username)
            if new_username:
                # Logout after username change
                print("\nAnda akan logout untuk login ulang dengan username baru.")
                input("Tekan Enter untuk melanjutkan...")
                break
        elif choice == "0":
            return main()
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

# ========================Home Page
def main():
    cekData()
    while True:
        os.system('cls')
        teks = """

        ░██████╗██╗██████╗░░█████╗░██████╗░██╗
        ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
        ╚█████╗░██║██████╔╝███████║██║░░██║██║
        ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
        ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
        ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
        """
        print(teks)
        print('╔' + '═'*48 + '╗')
        print('║' + 'SiPadi'.center(48) + '║')
        print('╠' + '═'*48 + '╣')
        print('║' + 'Penggilingan Padi Terpercaya di Indonesia'.center(48) + '║')
        print('╚' + '═'*48 + '╝') 
        print('\n [1]. Registrasi Sebagai Operator\n [2]. Login\n [0]. Keluar\n ')  
    
        piliihan = input("\nMenu yang dipilih: (1/2/0) ")
        while True:
# ==============================================REGISTRASI======================================================
            if piliihan == '1':
                regisOperator()
                        
# ==============================================LOGIN======================================================
            elif piliihan == '2':
                os.system('cls')
                teks = """

                ░██████╗██╗██████╗░░█████╗░██████╗░██╗
                ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║
                ╚█████╗░██║██████╔╝███████║██║░░██║██║
                ░╚═══██╗██║██╔═══╝░██╔══██║██║░░██║██║
                ██████╔╝██║██║░░░░░██║░░██║██████╔╝██║
                ╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝
                """
                print(teks)
                print('╔' + '═'*48 + '╗')
                print('║' + "LOGIN AKUN".center(48) + '║')
                print('╚' + '═'*48 + '╝') 
                print('\n[1]. SEBAGAI ADMIN \n[2]. SEBAGAI OPERATOR \n[3]. Keluar\n')

                pilih = input("\n LOGIN SEBAGAI (pilih angka): ")
                if pilih == '1':
                    loginAdmin()
                elif pilih == '2':
                    loginOperator()
                elif pilih == '0':
                    os.system('cls')
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk melanjutkan...")

            elif piliihan == "0" :
                os.system('cls')
                exit()
            else: 
                os.system('cls')
                print('╔' + '═'*48 + '╗')
                print('║' + 'Sipadi'.center(48) + '║')
                print('╠' + '═'*48 + '╣')
                print('║' + 'Pilihan Terpercaya Petani Indonesia'.center(48) + '║')
                print('╚' + '═'*48 + '╝') 
                print('\n1. Registrasi\n2. Login\n3. Keluar\n')
                print('Input anda tidak sesuai pilihan!')

            print('\nTerima kasih telah menggunakan program ini :)')
    
main()