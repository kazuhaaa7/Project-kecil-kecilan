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


# ================================================ REGIS AS OPERATOR ======================================================
def regisOperator():
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
        print('║' + "REGISTER AKUN OPERATOR".center(48)+ '║')
        print('╚' + '═'*48 + '╝') 

        df = pd.read_csv(FILE_OPERATOR)
        # kondisi 1
        # while True:
        username = input("Masukkan Username: ").strip().lower()
        if not username:
            print("\nUsername tidak boleh kosong")
            continue
        if len(username) < 3:
            print('\nUsername harus berisi minimal 3 karakter!')
            continue
        if (df['username'] == username).any():
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
        return 

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
                print("\nUsername tidak boleh kosong")
                continue
            if len(username) < 3:
                print('\nUsername harus berisi minimal 3 karakter!')
                continue

            # kondisi 2
            password = input("Masukkan Password: ").strip().lower()
            if not password:
                print("Password tidak boleh kosong")
                continue


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
                print("\nUsername tidak boleh kosong")
                continue
            if len(username) < 3:
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

    df = pd.read_csv(FILE_PELANGGAN, dtype={'noTelp': 'str'})
    # writer.writerow(["ID", "Nama_Petani", "No_Telp", "Alamat"])  # <-- header kolom


    nama = input("Nama Petani: ").strip().upper()
    if not nama:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    

    notelp = input("Masukkan No. Telepon (awali dengan 62): ")
    if not notelp.isdigit():
        print("Masukkan nomor telp dnegan angka ya :<")
        print("Porgram akan kembali ke menu dalam 3 detik dari sekarang")
        return
    alamat = input("Masukkan Alamat Lengkap : ").strip()
    
# cari id cus
    # if os.path.exists(data_customer):
    customer_id = 1
    try:
        with open(FILE_PELANGGAN, mode="r", encoding="utf-8") as file:
            read = list(csv.reader(file))
        if len(read) >= 1:
            idTerakhir = int(read[-1][0]) #pahami syntax
            customer_id = idTerakhir + 1
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
        df = pd.read_csv(FILE_PELANGGAN, dtype={'noTelp': 'str'})

        if df.empty:
            print(" Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        # ubah type data
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        input("\nTekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {e}")
        input("\nTekan Enter untuk melanjutkan...")
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
        df = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
   
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
        return


    # cek apakah ID ada
    if idPelanggan not in df['id'].values:
        print("Pelanggan dengan ID tersebut tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return 
    

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
        return
    
    alamatBaru = input(f"Alamat baru (Enter untuk tidak mengubah): ").strip().lower()

    if namaBaru:
        df.loc[df['id'] == idPelanggan, 'namaPetani'] = namaBaru
    if notelpBaru :
        # notelpBaru = f"62{notelpBaru}"
        df.loc[df['id'] == idPelanggan, 'noTelp'] = str(notelpBaru)
    if alamatBaru :
        df.loc[df['id'] == idPelanggan, 'alamat'] = alamatBaru

# sv perubahan di csv
    df.to_csv(FILE_PELANGGAN, index=False, encoding='utf-8')


    print(f"\n✓ Data pelanggan berhasil diupdate!")
    print(f"\nData pelanggan ID {idPelanggan} berhasil diperbarui!")



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

    df = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})

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

        # df['id'] = range(1, len(df) + 1)
        df.to_csv(FILE_PELANGGAN, index=False)  
        print("Pelanggan berhasil dihapus!")
    elif confirm == 'n':
        print("Penghapusan data dibatalkan. \nprogram akan berjalan 2 detik dari sekarang")
        return hapusDataPelanggan()
    else:
        print("Masukkan huruf yang sesuai dengan pilihan. \nprogram akan berjalan 2 detik dari sekarang")
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
        print(f"\nHarga saat ini: Rp {float(hargaTerakhir):,}/kg (ditetapkan pada {last_date}") # format replace: ("yg akan diganti", "pengganti")
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
        hargaBaru = f"Rp {hargaBaru}"
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
        "harga/kg":  hargaBaru,
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
            inpTgl = datetime.now().strftime("%d-%m-%Y")

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

            filter = df[df['tanggal'] == inpTgl]
            print(tabulate(filter, headers='keys', tablefmt='fancy_grid', showindex=False))

            jumlahTf= len(filter['idPel'])
            jumlahBobot= filter['berat'].sum()

            print(f"\n Tanggal {inpTgl}")
            print(f" Jumlah Transaksi: {jumlahTf}")
            print(f" Total Berat: {jumlahBobot} Kg")
            print(f" Total Pendapatan: Rp {filter['total'].sum():,.0f}")
            input("\n Enter untuk kembali...")
            return
        except ValueError:
            print("Ada yang salah dari program")

# ============================= FITUR ADMIN 3 | LAPORAN PERIODE ===================
def laporanPerdiode():
    os.system('cls')
    while True:
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
        print('║' + "Laporan Periode Penggilingan".center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        if not os.path.exists(FILE_PELANGGAN):
            print(" Belum ada data pelanggan.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        

        if not os.path.exists(FILE_TRANSAKSI):
            print(" Belum ada data pelanggan.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        df1 = pd.read_csv(FILE_PELANGGAN, dtype={'noTelp' : 'str'})    
        df2 = pd.read_csv(FILE_TRANSAKSI)    

        if df1.empty or df2.empty:
            print(" Data pelanggan masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        dfc = pd.merge(df1, df2, left_on='id', right_on='idPel', how='inner')
        dfc.drop(columns=['idPel'], inplace=True)
        print(tabulate(dfc, headers='keys', tablefmt="fancy_grid", showindex=False))

        dfc['tanggal'] = pd.to_datetime(dfc['tanggal'], format='%d-%m-%Y')
        while True:
            try:
                print("\nMasukkan tanggal dalam format DD-MM-YYY") 
                start = input("Tanggal Awal: ")
                end = input("Tanggal Akhir: ")

                start_date = pd.to_datetime(start, format='%d-%m-%Y')
                end_date = pd.to_datetime(end, format='%d-%m-%Y')

                if start_date > end_date:
                    print("Tanggal awal tidak boleh lebih besar dari tanggal akhir")
                    return
                namaPeriode = f"Periode {start} s/d {end}"
                break

            except:
                print("Format tangall salah, Gunakan format DD-MM-YYYY")
        
        # memfilter tanggal yg diminta yg ada di var dfc
        filtered = dfc[
            (dfc['tanggal']>= start_date) &
            (dfc['tanggal'] <= end_date)
        ] 
        
        #mengelompokkan data tanggal yg ada di var filtered dan (agg = > agregat) mencari totalnya 
        laporanPerdiode = filtered.groupby(filtered['tanggal']).agg({
            'total' : 'sum'
        }).reset_index()
        laporanPerdiode.index += 1

        print(f"Laporan Periode {namaPeriode}:")
        if len(laporanPerdiode) > 0:
            print(tabulate(laporanPerdiode, headers='keys', tablefmt="fancy_grid", showindex=False))
            print(f"Total keuntungan: Rp {laporanPerdiode['total'].sum():,.0f}")
            input("Tekan Enter untuk kembali...")
            return
#             : = Menandakan awal dari format specifier
#             , = Pemisah ribuan(menambahkan koma sebagai pemisah ribuan, jutaan, dst.)
#             .0 = tidak menampilkan desimal
#             f = Tipe format: fixed-point number (angka desimal, tapi di sini dibulatkan karena.0 
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
        print("2. Laporan Periode")
        print("3. Laporan Semua Transaksi")
        print("4. Statistik Keseluruhan")
        print("0. Kembali")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            laporanHarian()
        elif choice == "2":
            laporanPerdiode()
        elif choice == "3":
            riwayatKeseluruhan()
        elif choice == "4":
            statistik()
        elif choice == "0":
            return
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
        df['password'] = df['password'].astype(str)
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
        input("\nTekan Enter untuk melanjutkan...")
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
    username = input("Masukkan username sebelumnya untuk konfirmasi: ").strip().lower()
    user = df[df['username'] == username] 
    if user.empty:
        print("Username tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Verifikasi password
    if username != user.iloc[0]['username']:
        print("username salah!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Input username baru
    usernameBaru = input(f"Masukkan username baru (saat ini: {username}): ").strip().lower()
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

    df = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
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


        df_pelanggan = pd.read_csv(FILE_PELANGGAN, dtype={'noTelp': 'str'})
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
            print(f'\nharga jasa penggilingan saat ini {p:,.0f} Kg')
        
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
            df1 = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
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


        object = input("Cari berdasarkan id: ")
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
            # hasil = dfc[dfc['id'].str.contains(object)] #case=False membuat pencarian tidak sensitif huruf besar/kecil
            hasil = dfc[dfc['id'].astype(str) == object] # aku ubah biar jadi str, klo int ga kedeteksi
            print(tabulate(hasil, headers='keys', tablefmt="fancy_grid", showindex=False))


        except ValueError:
            print("ERROR bagian pencrian data")
            return
        # .str.contains() adalah fungsi pencarian teks (substring match) pada kolom bertipe string.
        # if not dfc['namaPetani'].str.contains(object, case=False).any():
        if hasil.empty:
            print("id yang kamu cari mungkin belum didaftarkan")
            print("\nSilahkan daftar terlebih dahulu")

        input("\nEnter untuk kembali...")
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
        inpTanggal = input("\nMasukkan tanggal (DD-MM-YYY) atau Enter untuk hari ini: ").strip()
        if not inpTanggal:
            inpTanggal = datetime.now().strftime("%d-%m-%Y")

    # cek keberadaan file
        if not os.path.exists(FILE_TRANSAKSI) or not  os.path.exists(FILE_PELANGGAN) :
            print(" Belum ada data tranksaski.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
# baca file
        df1 = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
        df2 = pd.read_csv(FILE_TRANSAKSI)

# memeriksa file
        if df1.empty or df2.empty:
                print(" Data pelanggan atau data transaksi masih kosong.")
                input("\nTekan Enter untuk melanjutkan...")
                return
        
        # gabungkan data
        dfc = pd.merge(df1, df2, left_on = 'id', right_on='idPel' ,how='inner')
        dfc.drop(columns=['idPel'], inplace=True)

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
        print(tabulate(filter,headers='keys', tablefmt='fancy_grid', showindex=False))

        # tampilkan ringkasan
        print(f"\nTanggal {inpTanggal}")
        print(f"Jumlah Transaksi: {len(filter)}")
        print(f"Total Berat: {totalBerat} Kg")
        print(f"Total Pendapatan: Rp {filter['total'].sum():,.0f}\n")



        input("\nKlik Enter untuk kemabli...")
        return riwayatTransaksi()
        
# ==================================MENU FITUR OPERATOR - Tansaksi | based petani ====================================
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
    print('║' + "RIWAYAT BERDASARKAN ID PETANI".center(48) + '║')
    print('╚' + '═'*48 + '╝') 
    while True:
# tampilkan data pelanggan
        df1 = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
        print("Daftar Petani:".center(50))
        print(tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False))



# input tanggal yg ingin ditentukkan
        inpPetani = input("Masukkan id Petani: ")
        if not inpPetani:
            print("id petani tidak boleh kosong")
            input("Enter untuk kembali...")
            return

    # cek keberadaan file
        if not os.path.exists(FILE_TRANSAKSI) or not  os.path.exists(FILE_PELANGGAN) :
            print(" Belum ada data tranksaski.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
# baca file
        df1 = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
        df2 = pd.read_csv(FILE_TRANSAKSI)

# memeriksa file
        if df1.empty or df2.empty:
                print(" Data pelanggan atau data transaksi masih kosong.")
                input("\nTekan Enter untuk melanjutkan...")
                return
        
        # gabungkan data

        dfc = pd.merge(df1, df2, left_on = 'id', right_on='idPel' ,how='inner')
        dfc['id'] = dfc['id'].astype(str) 
        dfc = dfc.drop(columns=['idPel'])
# apabila dfc ada value yg kosong
        if dfc.empty:
            print(" Data pelanggan atau data transaksi masih kosong.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        

# Pastikan kolom tanggal dalam format datetime
        # dfc['tanggal'] = pd.to_datetime(dfc['namaPetani'], ) 
        # mengubah value 'tanggal' menjaddi object pd datetime| dayfrist= dimulai dari hari

# filter transaksi based tanggal yg iidinput
        filter = dfc[dfc['id'] == inpPetani]
        if filter.empty:
            print("\nPetani yang kamu cari belum melakukan transaksi")
            print("Silahkan isi dengan id yang sudah melakukan transaksi")
            time.sleep(1.4)
            return riwayatBasedPetani()
        # if not filter.empty:
        #     namaPetani = filter['namaPetani'].iloc[0]
        # filter = dfc[dfc['id'].str.contains(inpPetani)]

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
        print(tabulate(filter,headers='keys', tablefmt='fancy_grid', showindex=False))

        print("Petani ditemukan".center(50))
        print(f"\nNama petani: {namaPetani}")
        print(f"Jumlah Transaksi: {len(filter)}")
        print(f"Total Berat: {totalBerat} Kg")
        print(f"Total Pendapatan: Rp {totalBiaya:,.0f}\n")

        input("\nKlik Enter untuk kembali...")
        return riwayatTransaksi()


# ==================================MENU FITUR OPERATOR - Tansaksi ====================================
def riwayatKeseluruhan():
    os.system('cls')
    while True:
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
        

        if not os.path.exists(FILE_TRANSAKSI):
            print(" Belum ada data pelanggan.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        
        try:
            df1 = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
            df2 = pd.read_csv(FILE_TRANSAKSI)

            if df1.empty or df2.empty:
                print(" Data pelanggan masih kosong.")
                input("\nTekan Enter untuk melanjutkan...")
                return
            # ubah type data
            dfc = pd.merge(df1, df2, left_on='id', right_on='idPel', how='inner')
            dfc.drop(columns=['idPel'], inplace=True)
            print(tabulate(dfc, headers='keys', tablefmt="fancy_grid", showindex=False))

        except Exception as e:
            print(f"Terjadi kesalahan saat membaca data: {e}")
            time.sleep(2)
            return
        id = len(dfc['id'])
        sumbobot = dfc['berat'].sum()

        print(f"\nJumlah Transkasi: {id}  ")
        print(f"Jumlah berat: {sumbobot} Kg")
        print(f"Jumlah Pendapatn: Rp {dfc['total'].sum():,.0f}")
        input("\nTekan Enter untuk melanjutkan...")
        os.system('cls')
        return

# ==================================MENU FITUR OPERATOR - Tansaksi statistik ====================================
def statistik():
    os.system('cls')
    while True:
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
        

        if not os.path.exists(FILE_TRANSAKSI):
            print(" Belum ada data pelanggan.")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        try:
            df1 = pd.read_csv(FILE_PELANGGAN,dtype={'noTelp': 'str'})
            df2 = pd.read_csv(FILE_TRANSAKSI)

            if df1.empty or df2.empty:
                print(" Data pelanggan masih kosong.")
                input("\nTekan Enter untuk melanjutkan...")
                return
            # ubah type data
            dfc = pd.merge(df1, df2, left_on='id', right_on='idPel', how='inner')
            dfc.drop(columns=['idPel'], inplace=True)
            # print(tabulate(dfc, headers='keys', tablefmt="fancy_grid", showindex=False))

        except Exception as e:
            print(f"Terjadi kesalahan saat membaca data: {e}")
            return
        id = len(dfc['id'])
        sumbobot = dfc['berat'].sum()
        sumpendapatan = dfc['total'].sum()
        sumpelanggan = len(df1)
        sumtransaski = len(df2)
        hargaNow = df2['harPerKg'].iloc[-1]
        sigmaBobot = sumbobot // id
        sigmaPendapatan = sumpendapatan // id 


        print(f"\nTotal Pelanggan: {sumpelanggan} ")
        print(f"Total Transaksi: {sumtransaski}")
        print(f"Total Berat Diling: {sumbobot} Kg")
        print(f"Total Pendapatan: Rp {dfc['total'].sum():,.0f}")
        print(f"Harga Saat Ini: Rp {hargaNow}")
        print(f"Rata-rata Berat per Transaksi: {sigmaBobot} Kg")
        print(f"Rata-rata Pendapatan per Transaksi: Rp {sigmaPendapatan:,.0f}")
        input("\nTekan Enter untuk melanjutkan...")
        return

# ==================================MENU FITUR OPERATOR - Tansaksi ====================================
def riwayatTransaksi():
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
        print("[2]. Riwayat transaksi berdasarkan nama petani")
        print("[3]. Riwayat Keseleruhan")
        print("[0]. Kembali")
        
        choice = input("\nPilih menu: ")

        
        if choice == "1":
            riwayatHarian()
        elif choice == "2":
            riwayatBasedPetani()
        elif choice == "3":
            riwayatKeseluruhan()
        elif choice == "0":
            return 
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
        
        print(df['password'].dtype)
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        
        # ubah jadi str
        df['password'] = df['password'].astype(str)
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
        passwordBaru = input(f"Masukkan password baru : ").strip().lower()
        if not passwordBaru:
            print("Password baru tidak boleh kosong!")
            input("\nTekan Enter untuk melanjutkan...")
            return 
            

        # Update password
        df.loc[df['password'] == password, 'password'] = passwordBaru
        df.to_csv(FILE_OPERATOR, index=False)

        print(f"\npassword berhasil diubah menjadi '{passwordBaru}'!")
        os.system('cls')
        return

## ==============================l====MENU FITUR OPERATOR - ubah user operator ====================================
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

        # ubah jadi str
        df = df[df['username'] == username].astype(str)


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
        
        # apabila len user < 3
        if len(usernameBaru) <3 :
            print("\nUsername minimmal 3 character")
            input("Enter untuk kembali ke menu")
            return

        # Update username
        df.loc[df['username'] == username, 'username'] = usernameBaru
        df.to_csv( FILE_OPERATOR, index=False)

        print(f"\nUsername berhasil diubah menjadi '{usernameBaru}'!")
        input("Tekan Enter untuk kembali...")
        return

# ================================== KELOLA AKUN OPERATOR ===========================================
def kelolaOperator(username):
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

        print("[1]. Registrasi Akun Operator")
        print("[2]. Ubah Password Operator")
        print("[3]. Ubah Ussername Operator")
        print("[0]. Kembali")
        
        choice = input("\nPilih menu: ")
        if choice == '1':
            regisOperator()
        elif choice == '2':
            ubahPWOperator()
        elif choice == '3':
            ubahUSEROperator(username)
        elif choice == '0':
            return
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

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
        print("[6]. Kelola Akun Operator ")
        print("[0]. Kembali ")
        
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
        elif choice == "6":
            kelolaOperator(username)
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
        print("[0]. Kembali")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            tambahDataPelanggan()
        elif choice == "2":
            transaksi()
        elif choice == "3":
            cariPetani()
        elif choice == "4":
            riwayatTransaksi()
        # elif choice == "5":
        #     new_password = ubahPWOperator()
        #     if new_password:
        #         # Logout after username change
        #         print("\nAnda akan logout untuk login ulang.\nSilahkan Login ulang")
        #         input("Tekan Enter untuk melanjutkan...")
        #         return loginOperator()
        # elif choice == "6":
        #     new_username = ubahUSEROperator(username)
        #     if new_username:
        #         # Logout after username change
        #         print("\nAnda akan logout untuk login ulang.\nSilahkan Login ulang")
        #         input("Tekan Enter untuk melanjutkan...")
        #         return loginOperator()
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
        print('║' + 'Penggilingan Padi Terpercaya di Indonesia'.center(50) + '║')
        print('╚' + '═'*48 + '╝') 
        print('\n [1]. Masuk\n [0]. Keluar\n ')  
    
        piliihan = input("\nMenu yang dipilih: (1/2/0) ")
        while True:
# ==============================================REGISTRASI======================================================
            # if piliihan == '1':
            #     regisOperator()
                        
# ==============================================LOGIN======================================================
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
                print('║' + "LOGIN AKUN".center(48) + '║')
                print('╚' + '═'*48 + '╝') 
                print('\n[1]. Sebagai Admin \n[2]. Sebagai Operator \n[0]. Kembali\n')

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
                print('\nTerima kasih telah menggunakan aplikasi kami :)')
                time.sleep(3)
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

            print('\nTerima kasih telah menggunakan aplikasi kami :)')
            time.sleep(3)
    
main()