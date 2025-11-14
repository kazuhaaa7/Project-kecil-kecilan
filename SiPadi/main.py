import csv
import pandas as pd
import time
from tabulate import tabulate
import os
from datetime import datetime

FILE_ADMIN = 'data_admin.csv'
FILE_OPERATOR = 'data_operator.csv'
FILE_HARGA = 'data_harga.csv'
FILE_PELANGGAN = 'data_pelanggan.csv'
FILE_TRANSAKSI = 'data_trasaksi.csv'
# ================================================ CEK DATA ======================================================
def cekData():
    if not os.path.exists(FILE_ADMIN):  
        user = pd.DataFrame(columns=['username', 'password']) 
        user.to_csv(FILE_ADMIN, index=False) 
    if not os.path.exists(FILE_OPERATOR):  
        user = pd.DataFrame(columns=['username', 'password']) 
        user.to_csv(FILE_OPERATOR, index=False) 
    if not os.path.exists(FILE_HARGA):  
        user = pd.DataFrame(columns=['harga/kg', 'tanggal','dibuat']) 
        user.to_csv(FILE_HARGA, index=False) 
    if not os.path.exists(FILE_PELANGGAN):  
        user = pd.DataFrame(columns=['id', 'namaPetani','noTelp', 'alamat']) 
        user.to_csv(FILE_PELANGGAN, index=False) 
    if not os.path.exists(FILE_TRANSAKSI):  
        user = pd.DataFrame(columns=['no', 'berat','harga/kg', 'total', 'tanggal']) 
        user.to_csv(FILE_TRANSAKSI, index=False) 

    # if not os.path.exists(folder_admin):
    #     os.makedirs(folder_admin)
    # if not os.path.exists(folder_toko):
    #     os.makedirs(folder_toko)
    # if not os.path.exists(folder_pembeli):
    #     os.makedirs(folder_pembeli)
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
        password = input("Masukkan Password: ").strip()
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
        if len(username) <= 3:
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
# =========================FITUR 1=============================
def tambahDataPelanggan():
    """Add new customer"""
    os.system('cls')
    print("=" * 50)
    print("TAMBAH PELANGGAN BARU".center(50))
    print("=" * 50 + "\n")


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
# =======================FITUR 2===============================
def lihatData():
    os.system('cls')
    print("=" * 50)
    print("DAFTAR SEMUA PELANGGAN".center(50))
    print("=" * 50 + "\n")

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
        print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
        input("\nTekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {e}")


# =======================FITUR 3===============================
def cariPelanggan():
    """Search customer by name or phone"""
    os.system('cls')
    print("=" * 50)
    print("CARI PELANGGAN".center(50))
    print("=" * 50 + "\n")

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
            df['Nama_Petani'].str.contains(keyword, case=False)]
# tampilkan hasil pencarian
    if not hasil.empty:
        os.system('cls')
        print("\n Hasil pencarian ditemukan:\n")
        print(tabulate(hasil, headers='keys', tablefmt="fancy_grid", showindex=False))
        input("Tekan Enter untuk melanjutkan...")
        return
    
    else:
        print("\nTidak ada data yang cocok dengan keyword tersebut.")

# =======================FITUR 4===============================
def editDataPelanggan():
    """Edit customer information"""
    os.system('cls')
    print("=" * 50)
    print("EDIT PELANGGAN".center(50))
    print("=" * 50 + "\n")


        # pastikan file ada
    if not os.path.exists(FILE_PELANGGAN):
        print("Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    

    df= pd.read_csv(FILE_PELANGGAN)

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
    if idPelanggan not in df['ID'].values:
        print("Pelanggan dengan ID tersebut tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return
    

    # ambil data pelanggan yang sesuai
    dt_Customer = df[df['ID'] == idPelanggan].iloc[0]
    

    print(f"\nData saat ini:")
    print(f"Nama: {dt_Customer['Nama_Petani']}")
    print(f"Telepon: {dt_Customer['No_Telp']}")
    print(f"Alamat: {dt_Customer['Alamat'] } \n")
    

    # input data baru
    namaBaru = input(f"Nama baru (Enter untuk tidak mengubah): ").strip().upper()
    notelpBaru = int(input(f"Telepon baru (Enter untuk tidak mengubah): "))
    if notelpBaru.isdigit() :
        df.loc[df['ID'] == idPelanggan, 'No_Telp'] = notelpBaru
    else: 
        print("Masukkan nomor dengan angka!")
        return
    alamatBaru = input(f"Alamat baru (Enter untuk tidak mengubah): ").strip().lower()

    if namaBaru:
        df.loc[df['ID'] == idPelanggan, 'Nama_Petani'] = namaBaru
    if notelpBaru :
        df.loc[df['ID'] == idPelanggan, 'No_Telp'] = notelpBaru
    if alamatBaru :
        df.loc[df['ID'] == idPelanggan, 'Alamat'] = alamatBaru

# sv perubahan di csv
    df.to_csv(FILE_PELANGGAN, index=False, encoding='utf-8')


    print(f"\n✓ Data pelanggan berhasil diupdate!")
    print(f"\nData pelanggan ID {idPelanggan} berhasil diperbarui!")

input("\nTekan Enter untuk melanjutkan...")


# =======================FITUR 5==============================
def hapusDataPelanggan():
    """Delete customer"""
    os.system('cls')
    print("=" * 50)
    print("HAPUS PELANGGAN".center(50))
    print("=" * 50 + "\n")

        # Pastikan file ada
    if not os.path.exists(FILE_PELANGGAN):
        print("Belum ada data pelanggan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    df = pd.read_csv('data_customer.csv')

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

    if idPelanggan not in df['ID'].astype(str).values:
        print("Pelanggan dengan ID tersebut tidak ditemukan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

# konfirmasih penghapusan
    confirm = input("\nYakin ingin menghapus? (y/n): ").strip().lower()
    if confirm == 'y':
        # Hapus data dan reset index agar tetap rapi
        df = df[df['ID'].astype(str) != idPelanggan]  
        df.reset_index(drop=True, inplace=True)  # Optional: perbarui kolom ID agar urut kembali

        df['ID'] = range(1, len(df) + 1)
        df.to_csv(FILE_PELANGGAN, index=False)  
        print("Pelanggan berhasil dihapus!")
    elif confirm == 'n':
        print("Penghapusan dibatalkan.")
    else:
        print("Masukkan huruf yang sesuai dengan pilihan")


    input("Tekan Enter untuk melanjutkan...")

# ============================= FITUR ADMIN 1 |AKU ADMIN DAN KAU ROOTS ===================
def crud_customers():
    os.system('cls')
    while True:
        print("MANAJEMEN DATA PELANGGAN (PETANI)")
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
    print("=" * 50)
    print("ATUR HARGA JASA PER KG".center(50))
    print("=" * 50)
    
    read = pd.read_csv(FILE_HARGA)

    # Pastikan file CSV ada
    if not os.path.exists(FILE_HARGA):
        df = pd.DataFrame(columns=["price_per_kg", "effective_date"])
        df.to_csv(FILE_HARGA, index=False)

    # Baca data CSV
    df = pd.read_csv(FILE_HARGA)

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
    df.to_csv(FILE_HARGA, index=False)

    print(f"\nHarga baru Rp{int(new_price):,}/kg berhasil disimpan!".replace(",", "."))
    input("\nTekan Enter untuk melanjutkan...")




# ============================= FITUR ADMIN 3 | LAPORAN===================
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


# ============================= FITUR ADMIN 3 | UBAH PW===================
def ubahPassword(password): #pahami dan ubah syntax sepaham kmu"
    os.system('cls')
    print("=" * 50)
    print("UBAH PASSWORD".center(50))
    print("=" * 50 + "\n")

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
    print("=" * 50)
    print("UBAH USERNAME".center(50))
    print("=" * 50 + "\n")

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
            break
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
            print('jkahdjkabwka')
        # elif choice == "2":
        #     input_transaction(username)
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
            break
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
                        '''pilihan1 = input('\n(Y) untuk kembali | (enter) untuk keluar : ').lower()
                        if pilihan1 == 'y':
                            os.system('cls')
                        else:
                            kondisi = False'''
                    elif pilih == '2':
                        regisOperator()
                        '''pilihan2 = input('\n(Y) untuk kembali | (enter) untuk keluar : ').lower()
                        if pilihan2 == 'y':
                            os.system('cls')
                        else:
                            kondisi = False'''
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