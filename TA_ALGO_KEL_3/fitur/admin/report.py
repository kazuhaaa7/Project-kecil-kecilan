from datetime import datetime
import os, sys
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "data_admin.csv")

# INI BERKAITAN DGN TRANSAKSI YG DIMASUKKAN OLEH SI OPERATOR

#  Laporan harian
def view_daily_report():
    """Menampilkan laporan transaksi harian (berdasarkan CSV)"""
    os.system('cls')  # Bersihkan layar terminal
    print("=" * 50)
    print("LAPORAN HARIAN".center(50))
    print("=" * 50 + "\n")

    def format_rupiah(amount):
        """Mengubah angka menjadi format mata uang Rupiah"""
        # f"Rp{amount:,.0f}" → mengubah angka ke format ribuan (contoh: 15000 → Rp15,000).
        # .replace(",", ".") → ubah koma jadi titik (Indonesia style) → Rp15.000.
        return f"Rp{amount:,.0f}".replace(",", ".")

    # Input tanggal
    date_str = input("Masukkan tanggal (DD-MM-YYY) atau Enter untuk hari ini: ").strip()
    if not date_str:
        date_str = datetime.now().strftime("%d-%m-%Y")

    transaksi_file = "data_transaksi.csv" # di isi dgn aksi operator
    customer_file = "data_customer.csv"

    # Pastikan file ada
    if not os.path.exists(transaksi_file) or not os.path.exists(customer_file):
        print("File data transaksi atau pelanggan belum tersedia.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Baca data dari CSV
    df_transaksi = pd.read_csv(transaksi_file)
    df_customer = pd.read_csv(customer_file)

    # Gabungkan transaksi dengan nama pelanggan (seperti SQL JOIN)
    df = pd.merge(df_transaksi, df_customer, left_on="customer_id", right_on="id", how="left")

    # Pastikan kolom tanggal dalam format yang benar
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime("%Y-%m-%d")

    # Filter transaksi berdasarkan tanggal yang dimasukkan
    df_filtered = df[df['date'] == date_str]

    # Jika tidak ada data pada tanggal itu
    if df_filtered.empty:
        print(f"Tidak ada transaksi pada tanggal {date_str}.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Hitung total
    total_weight = df_filtered['weight_kg'].sum()
    total_cost = df_filtered['total_cost'].sum()

    # Tampilkan ringkasan
    print(f"\nTanggal: {date_str}")
    print(f"Jumlah Transaksi: {len(df_filtered)}")
    print(f"Total Berat: {total_weight:.2f} kg")
    print(f"Total Pendapatan: {format_rupiah(total_cost)}")
    print()

    # Tampilkan tabel transaksi
    print(f"{'ID':<5} {'Pelanggan':<25} {'Berat (kg)':<12} {'Harga/kg':<12} {'Total':<15}")
    print()

    # Loop untuk menampilkan tiap transaksi
    for _, row in df_filtered.iterrows():
        print(f"{row['id_x']:<5} {row['name']:<25} {row['weight_kg']:<12.2f} "
        f"{format_rupiah(row['price_per_kg']):<12} {format_rupiah(row['total_cost']):<15}")

    input("\nTekan Enter untuk melanjutkan...")

# laporan Bulanan
def view_monthly_report():
    """Menampilkan laporan transaksi bulanan dari file CSV"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print("LAPORAN BULANAN".center(70))
    print("=" * 70)
    
    def format_rupiah(amount):
        """Format angka menjadi rupiah"""
        return f"Rp{amount:,.0f}".replace(",", ".")


    # Input bulan
    month_str = input("Masukkan bulan (MM-YYYY) atau Enter untuk bulan ini: ").strip()
    if not month_str:
        month_str = datetime.now().strftime("%m-%Y")

    # Pastikan file ada
    if not os.path.exists("data/transactions.csv") or not os.path.exists("data/customers.csv"):
        print("File data transaksi atau pelanggan tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Baca data
    df_trans = pd.read_csv("data/transactions.csv")
    df_cust = pd.read_csv("data/customers.csv")

    # Gabungkan transaksi dengan nama pelanggan
    df = df_trans.merge(df_cust, left_on="customer_id", right_on="id", suffixes=("_t", "_c"))

    # Filter berdasarkan bulan
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df[df["date"].dt.strftime("%Y-%m") == month_str]

    if df.empty:
        print(f"\nTidak ada transaksi untuk bulan {month_str}.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Hitung total
    total_weight = df["weight_kg"].sum()
    total_cost = df["total_cost"].sum()

    # Tampilkan hasil
    print(f"\nBulan: {month_str}")
    print(f"Jumlah Transaksi: {len(df)}")
    print(f"Total Berat: {total_weight:.2f} kg")
    print(f"Total Pendapatan: {format_rupiah(total_cost)}\n")

    print(f"{'ID':<5} {'Tanggal':<12} {'Pelanggan':<25} {'Berat (kg)':<12} {'Total':<15}")

    for _, t in df.iterrows():
        tanggal = t["date"].strftime("%Y-%m-%d")
        print(f"{t['id_t']:<5} {tanggal:<12} {t['name']:<25} {t['weight_kg']:<12.2f} {format_rupiah(t['total_cost']):<15}")

    input("\nTekan Enter untuk melanjutkan...")


# ===========================SEMWA LAPORAN 

def view_all_transactions():
    """Menampilkan semua transaksi dari file CSV"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 80)
    print("LAPORAN KESELURUHAN".center(80))
    print("=" * 80)
    def format_rupiah(amount):
        """Format angka menjadi rupiah"""
        return f"Rp{amount:,.0f}".replace(",", ".")

    # Pastikan file ada
    if not os.path.exists("data/transactions.csv") or not os.path.exists("data/customers.csv"):
        print("File data transaksi atau pelanggan tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Baca data
    df_trans = pd.read_csv("data/transactions.csv")
    df_cust = pd.read_csv("data/customers.csv")

    # Gabungkan transaksi dan pelanggan
    df = df_trans.merge(df_cust, left_on="customer_id", right_on="id", suffixes=("_t", "_c"))

    # Pastikan kolom tanggal dalam format datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Urutkan berdasarkan tanggal terbaru
    df = df.sort_values(by="date", ascending=False).head(100)

    if df.empty:
        print("Belum ada transaksi.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Tampilkan data
    print(f"{'ID':<5} {'Tanggal':<12} {'Pelanggan':<25} {'Berat (kg)':<12} {'Harga/kg':<12} {'Total':<15}")

    for _, t in df.iterrows():
        tanggal = t["date"].strftime("%d-%m-%Y") if pd.notnull(t["date"]) else "-"
        print(f"{t['id_t']:<5} {tanggal:<12} {t['name']:<25} {t['weight_kg']:<12.2f} {format_rupiah(t['price_per_kg']):<12} {format_rupiah(t['total_cost']):<15}")

    input("\nTekan Enter untuk melanjutkan...")


# ===================================LAPORAN STATISTIK
def view_statistics():
    """Menampilkan statistik keseluruhan dari data CSV"""

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print("LAPORAN STATISTIK".center(70))
    print("=" * 70)
    
    def format_rupiah(amount):
        """Format angka menjadi rupiah"""
        return f"Rp{amount:,.0f}".replace(",", ".")


    # Pastikan file yang dibutuhkan tersedia
    if not os.path.exists("data/transactions.csv") or not os.path.exists("data/customers.csv"):
        print("File data transaksi atau pelanggan tidak ditemukan!")
        input("\nTekan Enter untuk melanjutkan...")
        return

    # Baca file CSV
    df_trans = pd.read_csv("data/transactions.csv")
    df_cust = pd.read_csv("data/customers.csv")

    # Cek file harga (opsional)
    price_file = "data/prices.csv"
    if os.path.exists(price_file):
        df_price = pd.read_csv(price_file)
        # Urutkan berdasarkan tanggal efektif terbaru
        df_price["effective_date"] = pd.to_datetime(df_price["effective_date"], errors="coerce")
        df_price = df_price.sort_values(by="effective_date", ascending=False)
        current_price = df_price.iloc[0]["price_per_kg"] if not df_price.empty else 0
    else:
        current_price = 0

    # Hitung statistik dasar
    total_customers = len(df_cust)
    total_transactions = len(df_trans)
    total_weight = df_trans["weight_kg"].sum() if "weight_kg" in df_trans.columns else 0
    total_revenue = df_trans["total_cost"].sum() if "total_cost" in df_trans.columns else 0

    # Tampilkan hasil
    print(f"Total Pelanggan: {total_customers}")
    print(f"Total Transaksi: {total_transactions}")
    print(f"Total Berat Digiling: {total_weight:.2f} kg")
    print(f"Total Pendapatan: {format_rupiah(total_revenue)}")
    print(f"Harga Saat Ini: {format_rupiah(current_price)}/kg")

    if total_transactions > 0:
        avg_weight = total_weight / total_transactions
        avg_cost = total_revenue / total_transactions
        print(f"Rata-rata Berat per Transaksi: {avg_weight:.2f} kg")
        print(f"Rata-rata Pendapatan per Transaksi: {format_rupiah(avg_cost)}")

    input("\nTekan Enter untuk melanjutkan...")
