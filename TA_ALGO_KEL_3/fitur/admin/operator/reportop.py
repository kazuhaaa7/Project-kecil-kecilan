def laporan_hari_ini()
def laporan_transaksi_customer()
def riwayat_laporan()
    

def lap0ran_transaksi():
    while True:
        print("RIWAYAT TRANSAKSI")
        print("1. Riwayat Transaksi Hari Ini")
        print("2. Riwayat Transaksi Petani")
        print("3. Riwayat Semua Transaksi")
        print("0. Kembali")
        
        choice = input("\nPilih menu: ")
        
        if choice == "1":
            laporan_hari_ini()
        elif choice == "2":
            laporan_transaksi_customer()
        elif choice == "3":
            laporan_tra()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")