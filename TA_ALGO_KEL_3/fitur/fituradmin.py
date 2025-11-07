from datetime import datetime
import os, sys
from datetime import datetime
from .crud.crud import add_customer, view_all_customers, search_customer, edit_customer, delete_customer
# from .crud.atur_harga import add_customer

# semua fitur admin jadi 1 di sini, tp klo eksekusi bedakan
# ============================= FITUR ADMIN 1 ===================
def crud_customers():
    """CRUD operations for customers"""
    os.system('cls')
    while True:
        print("MANAJEMEN DATA PELANGGAN (PETANI)")
        print("1. Tambah Pelanggan")
        print("2. Lihat Semua Pelanggan")
        print("3. Cari Pelanggan")
        print("4. Edit Pelanggan")
        print("5. Hapus Pelanggan")
        print("0. Kembali")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            add_customer()
        elif choice == "2":
            view_all_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            edit_customer()
        elif choice == "5":
            delete_customer()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")

# ============================= FITUR ADMIN 2 ===================
def set_price():
    """Set service price per kg"""
    print("ATUR HARGA JASA PER KG")
    
    # Get current price
    

# ============================= FITUR ADMIN 3 ===================