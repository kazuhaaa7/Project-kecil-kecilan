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
        user = pd.DataFrame(columns=['no', 'berat','harga/kg', 'total', 'tanggal']) 
        user.to_csv(FILE_TRANSAKSI, index=False) 

# ================================================ REGIS AS ADMIN ======================================================
def regisAdmin():
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
    print('║' + "REGISTER AKUN ADMIN".center(48) + '║')
    print('╚' + '═'*48 + '╝') 


    # kondisi 1
    while True:
        username = input("Masukkan Username: ").strip()
        if len(username) <= 3:
            print('Username harus berisi minimal 3 karakter!')
        else:
            break

    # kondisi 2
    while True:
        password = input("Masukkan Password: "). strip()
        break
    # Jika file belum ada, buat file baru
    if not os.path.exists(FILE_ADMIN):
        df = pd.DataFrame(columns=['username', 'password'])
        df.to_csv(FILE_ADMIN, index=False)

    # Simpan data baru
    df = pd.read_csv(FILE_ADMIN)
    dataBaru = {'username' : username, 'password': password}
    dataBaruDf = pd.DataFrame([dataBaru])
    df = pd.concat([df, dataBaruDf], ignore_index=True)
    df.to_csv(FILE_ADMIN, index=False)
    print(f"\nRegistrasi {username} sebagai admin berhasil!")

    i = input("\nKetik apa saja untuk kembali")

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

    # kondisi 1
    while True:
        username = input("Masukkan Username: ").strip()
        if len(username) < 2:
            print('Username harus berisi minimal 3 karakter!')
        else:
            break

    # kondisi 2
    while True:
        password = input("Masukkan Password: ").strip()
        break
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
            username = input("Masukkan Username: ").strip()
            if len(username) <= 3:
                print('Username harus berisi minimal 3 karakter!')
            else:
                break

        # kondisi 2
        while True:
            password = input("Masukkan Password: ").strip()
            break


        # operator
        if not os.path.exists('dt_operator.csv'):
            print("File data_operator.csv tidak ditemukan!")
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
            username = input("Masukkan Username: ").strip()
            if len(username) <= 3:
                print('Username harus berisi minimal 3 karakter!')
            else:
                break

        # kondisi 2
        while True:
            password = input("Masukkan Password: ").strip()
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


    name = input("Nama Petani: ").strip().upper()
    if not name:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    try:
        phone = int(input("Masukkan No. Telepon (awali dengan 62): "))
    except ValueError:
        print("Masukkan nomor telp dnegan angka ya :<")
        print("Porgram akan kembali ke menu dalam 3 detik dari sekarang")
        time.sleep(3)
        return
    address = input("Masukkan Alamat Lengkap : ").strip().lower()
    
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
        writer.writerow([customer_id, name, phone, address])
    
    
    
    print(f"\nPelanggan '{name}' berhasil ditambahkan! (ID: {customer_id})")
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
            df['namaPetani'].str.contains(keyword, case=False)]
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
def crud_customers():

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
        print(f"\nHarga saat ini: Rp{int(hargaTerakhir):,}/kg (ditetapkan pada {last_date}") # format replace: ("yg akan diganti", "pengganti")
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


# ============================= FITUR ADMIN 3 | LAPORAN===================
def view_reports():
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


# ============================= FITUR ADMIN 3 | UBAH PW===================
def ubahPassword(password): #pahami dan ubah syntax sepaham kmu"
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

    username = input("Masukkan username untuk konfirmasi: ").strip()
    user_row = df[df['Username'] == username]

    if user_row.empty:
        print("Username tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Verifikasi password
    if username != user_row.iloc[0]['Username']:
        print("Username salah!")
        input("\nTekan Enter untuk melanjutkan...")
        return password

    # Input pw baru
    passwordBaru = input(f"Masukkan password baru (saat ini: {password}): ").strip()
    if not passwordBaru:
        print("Password baru tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return 
    

    # Update password
    df.loc[df['password'] == password, 'password'] = passwordBaru
    df.to_csv(FILE_ADMIN, index=False)

    print(f"\npassword berhasil diubah menjadi '{passwordBaru}'!")
    # time.sleep(1.5)
    os.system('cls')
    return 

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
    
    # print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
    # Cari user
    user = df[df['username'] == username]
    if user.empty:
        print("Username tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Verifikasi password
    username = input("Masukkan username sebelumnya untuk konfirmasi: ").strip()
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
    os.system('cls')
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


        df = pd.read_csv(FILE_PELANGGAN, )
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))

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
        elif id in df['id'].astype(str).values:
            # .loc[ ..., 'namaPetani']
# → ambil kolom namaPetani
            nama = df.loc[df['id'].astype(str) == id, 'namaPetani'].values[0] #→ ambil nilai pertama (karena hasil pencarian berupa array)
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
            print(f'harga jasa penggilingan saat ini {p}/kg')
        
        # input gabah
        gabah = float(
            input("Masukkan berat gabah yang akan digiling:  "))
            # next stepp dikali sm harga tiap kg dgn gabah











































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
            crud_customers()
        elif choice == "2":
            setHarga()
        elif choice == "3":
            view_reports()
        elif choice == "4":
            ubahPassword(password)
        elif choice == "5":
            ubahUsername(username)


        elif choice == "0":
            return main()
        # else:
        #     print("Pilihan tidak valid!")
        #     input("Tekan Enter untuk melanjutkan...")

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
        print('║' + "MENU ADMIN".center(48) + '║')
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
        # elif choice == "3":
        #     search_farmers()
        # # elif choice == "4":
        # #     laporan_transaksi()
        # elif choice == "5":
        #     # new_password = ubahPw(username)
        #     if new_password:
        #         # Logout after username change
        #         print("\nAnda akan logout untuk login ulang dengan username baru.")
        #         input("Tekan Enter untuk melanjutkan...")
        #         break
        # elif choice == "6":
        #     # new_username = ubahUser(username)
        #     if new_username:
        #         # Logout after username change
        #         print("\nAnda akan logout untuk login ulang dengan username baru.")
        #         input("Tekan Enter untuk melanjutkan...")
        #         break
        elif choice == "0":
            return main()
        # else:
        #     print("Pilihan tidak valid!")
        #     input("Tekan Enter untuk melanjutkan...")

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
        print('\n [1]. Registrasi\n [2]. Login\n [0]. Keluar\n ')  
    
        piliihan = input("\nMenu yang dipilih: (1/2/0) ")
        while True:
# ==============================================REGISTRASI======================================================
            if piliihan == '1':

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
                    print('║' + 'PILIHAN MENU | REGISTRASI '.center(48) + '║')
                    print('╚' + '═'*48 + '╝')  
                    print("[1]. SEBAGAI ADMIN")
                    print("[2]. SEBAGAI OPERATOR")
                    print("[0]. Kembali")
                    pilih = input("\n REGISTRASI SEBAGAI (pilih angka): ")
                    if pilih == '1':
                        regisAdmin()
                        os.system('cls')
                    elif pilih == '2':
                        regisOperator()
                    elif pilih == '0':
                        os.system('cls')
                        break
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