from tabulate import tabulate
import pandas as pd
import os


# fitur tambah data

def tambah_member():
    nama = input("Masukkan Nama: ").upper()
    try:
        nim = int(input("Masukkan nim:  "))

    except ValueError:
        print("Masukkan NIM dnegan angka ya :<")
        return
    prodi = input("Masukkan Program Studi: ").upper()

    
    df = pd.read_csv('mhs.csv') # klo udah dibaca harus disimpan ke csv lagi | otomatis buat file csv baru apabila tdk ada file csv
    df = pd.concat([df, pd.DataFrame([{'Nama' : nama, 'NIM': nim, 'Prodi': prodi}])], ignore_index=True)

    df.to_csv('mhs.csv', index=False)
    print("Data berhasil ditambahkan")
# =========================================================================================================
    # fitur ubah data
def ubah_member():# masih eror, ini ga spesfik karna pebubahan datanya masih rancu
    df = pd.read_csv('mhs.csv')

    # Hapus kolom unnamed jika ada
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
# df.columns	Ambil semua nama kolom
# .str.contains("^Unnamed")	Cek kolom mana yang namanya diawali "Unnamed"
# ~	Negasi (kebalikan) → pilih kolom yang bukan Unnamed
# df.loc[:, ...]	Pilih semua baris (:) dan hanya kolom yang cocok dengan filter
# Jadi hasilnya hanya kolom valid, tanpa kolom “Unnamed…”.


# .loc untuk	Nama kolom/baris	df.loc[:, ['Nama','NIM']]
# .iloc  untuk	Index angka	df.iloc[:, [0,1]]

    # Reset index biar rapi lagi
    df = df.reset_index(drop=True )
        
    # Buang kolom NO lama kalau ada
    if 'No' in df.columns:
        df = df.drop(columns=['No'])


    #  Buat nomor urut dari index
    # format .insert by pandas: DataFrame.insert(loc, column, value, allow_duplicates=False)
    df.insert(0, 'No', range(1, len(df)+1)) # untuk rangenya disarankan begitu untuk case tabel

    # tampilkan data dulu
    print("="* 6, "WELLOME DI PROGRAM UBAH DATA", "=" * 6)

    print("=" * 6 , "DATA MAHASISWA", "=" * 6)
    namakolom = ['No','Nama', 'NIM', 'Prodi']
    print(tabulate(df, headers=namakolom, tablefmt="fancy_grid", showindex=False)) 

# error handling
    try:
        idx = int(input("Masukkan value indeks kek berapa yang akan diubah: ")) -1
        if idx < 0  or idx >= len(df):
            print('index tidak valid')
            return
        
    except:
        print("input harus angka")
        return


    nama_baru = input('Masukkan nama yang baru: ').upper()
    try:
        nim_baru = int(input("Masukkan NIM yang baru: "))
    except ValueError:
        print("Masukkan NIM dnegan angka ya :<")
        return
    prodi_baru = input('Masukkan Prodi yang baru: ').upper()


    # eksekusi, harus satu satu ya. ga bisa bebarengan
    df.loc[idx,'Nama'] = nama_baru
    df.loc[idx,'NIM'] = nim_baru
    df.loc[idx,'Prodi'] = prodi_baru


    # add to csv|  # harus save ya stelah mmebaca csv
    df.to_csv('mhs.csv', index=False)# apabila index=true, maka ada kolom tambahan no index yg sebenernya tdk terlalu dibutuhkan
    print("Data berhasil Diubah")

    # fitur hapus data
def del_member():# error, masih blm spesfik
    df = pd.read_csv('mhs.csv')

# ================================KASUS APABILA ADA KESALAHAN nan dan Unnamed
# Hapus kolom unnamed jika ada
    # df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    
    # menghapus value yg bernilai nan. mengahapus 1 kolom apabila axis= menghapus 1, 1 baris apabila axis=0
    df = df.dropna(axis=1)
    
# ============================================================================
# Reset index dan bangun NO dari awal
    df = df.reset_index(drop=True)


# Buang kolom NO lama (kalau ada)
    if 'No' in df.columns:
        df = df.drop(columns=['No'])


#  Buat nomor urut dari index
    df.insert(0, 'No', range(1, len(df)+1)) # untuk rangenya disarankan begitu untuk case tabel
    
    # tampilkan tabel
    print("="* 6, "WELLOME DI PROGRAM HAPUS DATA", "=" * 6)
    print("=" * 6 , "DATA MAHASISWA", "=" * 6)
    headers = ['No','Nama', 'NIM', 'Prodi']
    print(tabulate(df, headers=headers, tablefmt="fancy_grid", showindex=False))


    try:
        idx = int(input("Masukkan index ke berapa yang ingin dihapus: ")) -1 # untuk menyesuaikan dgn index
    # antisipasi jikalau:
        if idx < 0  or idx >= len(df):
            print('index tdk valid')
            return
        df = df.drop(idx)

    except:
        print("Masukkan angka ya...")
        print("Tidak berhasil menghapus data")
        return
    
        
# save action ke csv
    df.to_csv('mhs.csv', index=False)
    print("Data berhasil dihapus")



# membuat csv langsung di sini      
file_name = 'mhs.csv'

# cek, apakah file csv sudah ada #1 - use if-else
if not os.path.exists(file_name):

    # buat file csv kosong dgn header
    df = pd.DataFrame(columns=['Nama','NIM', 'Prodi'])
    df.to_csv('mhs.csv', index=False)
    print('flle csv sudah dibuat')
else:
    print('file sudah ada')


def show_data():
    df = pd.read_csv('mhs.csv')

# Hapus kolom unnamed jika ada
# df = df.loc[:, ~df.columns.str.contains("^Unnamed")] #cari aa maksudnya
# untuk menghapus value nan
    df = df.dropna(axis=1)
    
    # Reset index dan bangun NO dari awal
    df = df.reset_index(drop=True)
 
# =================================================================== tabel
    # data show only
    df_display = df.copy()
        # Buang kolom NO lama kalau ada
    if 'No' in df.columns:
        df = df.drop(columns=['No'])

    #  Buat nomor urut dari index
    df.insert(0, 'No', range(1, len(df_display)+1)) # untuk rangenya disarankan begitu untuk case tabel
    # arti dri kode di atas(df.insert): (mau di taro dii indx kolom brp, <nama kolom>, <akan muncul brp banyak>)

    print("=" * 6 , "DATA MAHASISWA", "=" * 6)
    headers = ['No','Nama', 'NIM', 'Prodi']
    print(tabulate(df, headers=headers, tablefmt="fancy_grid", showindex=False))
# ===================================================================

while True:
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    if pilihan == '1':
        show_data()
    elif pilihan == '2':
        tambah_member()
    elif pilihan == '3':
        ubah_member()
    elif pilihan == '4':
        del_member()
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak valid.")
        exit()
