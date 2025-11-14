from datetime import datetime
import os, sys
import pandas as pd
import time
from tabulate import tabulate


def ubah_password(password): #pahami dan ubah syntax sepaham kmu
    """Ubah username di file CSV"""
    os.system('cls')
    print("=" * 50)
    print("UBAH PASSWORD".center(50))
    print("=" * 50 + "\n")

    file_path = r"C:\Users\ADVAN\OneDrive\Desktop\Projek Akhir - Semester 1\TA_ALGO_KEL_3\data_admin.csv"  # nama file CSV

    # Pastikan file ada
    if not os.path.exists('data_admin.csv'):
        print("File data_admin.csv belum ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Baca file CSV
    df = pd.read_csv('data_admin.csv')

    # Cek apakah kolom yang dibutuhkan ada
    if not {'Username', 'Password'}.issubset(df.columns):
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
    new_password = input(f"Masukkan password baru (saat ini: {password}): ").strip()
    if not new_password:
        print("Password baru tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return 
    
    if len(new_password) < 8:
        print("masukkan Minimal 8 karakter") 
        input("aa")
        return 

    if new_password == password:
        print("Username baru sama dengan yang lama.")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Cek apakah username baru sudah dipakai
    if new_password in df['Password'].values:
        print("Username sudah digunakan oleh user lain!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Update password
    df.loc[df['Username'] == username, 'Password'] = new_password
    df.to_csv('data_admin.csv', index=False)

    print(f"\nUsername berhasil diubah menjadi '{new_password}'!")
    time.sleep(1.5)
    os.system('cls')
    return new_password



def change_username(username: str): #pahami dan ubah syntax sepaham kmu
    """Ubah username di file CSV"""
    os.system('cls')
    print("=" * 50)
    print("UBAH USERNAME".center(50))
    print("=" * 50 + "\n")

    file_path = "data_admin.csv"  # nama file CSV

    # Pastikan file ada
    if not os.path.exists( file_path):
        print("File data_admin.csv belum ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Baca file CSV
    df = pd.read_csv(file_path)

    # Cek apakah kolom yang dibutuhkan ada
    if not {'Username', 'Password'}.issubset(df.columns):
        print("File CSV tidak memiliki kolom 'username' atau 'password'.")
        input("\nTekan Enter untuk melanjutkan...")
        return username
    print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))

    # Cari user
    user_row = df[df['Username'] == username]

    if user_row.empty:
        print("Username tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Verifikasi password
    password = input("Masukkan password untuk konfirmasi: ").strip()
    if password != user_row.iloc[0]['Password']:
        print("Password salah!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Input username baru
    new_username = input(f"Masukkan username baru (saat ini: {username}): ").strip()
    if not new_username:
        print("Username baru tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    if new_username == username:
        print("Username baru sama dengan yang lama.")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Cek apakah username baru sudah dipakai
    if new_username in df['Username'].values:
        print("Username sudah digunakan oleh user lain!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Update username
    df.loc[df['Username'] == username, 'Username'] = new_username
    df.to_csv( file_path, index=False)

    print(f"\nUsername berhasil diubah menjadi '{new_username}'!")
    time.sleep(1.5)
    os.system('cls')
    return new_username
# =======================================================================================================================
def ubahPw(password): #pahami dan ubah syntax sepaham kmu
    """Ubah username di file CSV"""
    os.system('cls')
    print("=" * 50)
    print("UBAH PASSWORD".center(50))
    print("=" * 50 + "\n")


    # Pastikan file ada
    if not os.path.exists('dt_operator.csv'):
        print("File dt_operator.csv belum ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return password

    # Baca file CSV
    df = pd.read_csv('dt_operator.csv')

    # Cek apakah kolom yang dibutuhkan ada
    if not {'Username', 'Password'}.issubset(df.columns):
        print("File CSV tidak memiliki kolom 'username' atau 'password'.")
        input("\nTekan Enter untuk melanjutkan...")
        return password
    
    print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
    
    # Cari user

    username = input("Masukkan username untuk konfirmasi: ").strip()
    user_row = df[df['Username'] == username]

    if user_row.empty:
        print("Username tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Verifikasi password
    if username != user_row.iloc[0]['Username']:
        print("Username salah!")
        input("\nTekan Enter untuk melanjutkan...")
        return password

    # Input pw baru
    new_password = input(f"Masukkan password baru (saat ini: {password}): ").strip()
    if not new_password:
        print("Password baru tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    if len(new_password) < 8:
        print("masukkan Minimal 8 karakter") 
        return

    if new_password == password:
        print("Username baru sama dengan yang lama.")
        input("\nTekan Enter untuk melanjutkan...")
        return 

    # Cek apakah username baru sudah dipakai
    if new_password in df['Password'].values:
        print("Username sudah digunakan oleh user lain!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Update password
    df.loc[df['Username'] == username, 'Password'] = new_password
    df.to_csv('data_admin.csv', index=False)

    print(f"\nUsername berhasil diubah menjadi '{new_password}'!")
    time.sleep(1.5)
    os.system('cls')
    return new_password



def ubahUser(username): #pahami dan ubah syntax sepaham kmu
    """Ubah username di file CSV"""
    os.system('cls')
    print("=" * 50)
    print("UBAH USERNAME".center(50))
    print("=" * 50 + "\n")

    file_path = "dt_operator.csv"  # nama file CSV

    # Pastikan file ada
    if not os.path.exists( file_path):
        print("File data_admin.csv belum ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Baca file CSV
    df = pd.read_csv(file_path)

    # Cek apakah kolom yang dibutuhkan ada
    if not {'Username', 'Password'}.issubset(df.columns):
        print("File CSV tidak memiliki kolom 'username' atau 'password'.")
        input("\nTekan Enter untuk melanjutkan...")
        return username
    print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))

    # Cari user
    user_row = df[df['Username'] == username]

    if user_row.empty:
        print("Username tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Verifikasi password
    password = input("Masukkan password untuk konfirmasi: ").strip()
    if password != user_row.iloc[0]['Password']:
        print("Password salah!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Input username baru
    new_username = input(f"Masukkan username baru (saat ini: {username}): ").strip()
    if not new_username:
        print("Username baru tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    if new_username == username:
        print("Username baru sama dengan yang lama.")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Cek apakah username baru sudah dipakai
    if new_username in df['Username'].values:
        print("Username sudah digunakan oleh user lain!")
        input("\nTekan Enter untuk melanjutkan...")
        return username

    # Update username
    df.loc[df['Username'] == username, 'Username'] = new_username
    df.to_csv( file_path, index=False)

    print(f"\nUsername berhasil diubah menjadi '{new_username}'!")
    time.sleep(1.5)
    os.system('cls')
    return new_username
