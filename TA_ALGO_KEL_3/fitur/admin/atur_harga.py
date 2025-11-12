import os
import pandas as pd
from datetime import datetime

def atur_harga_jasa():
    """Atur atau perbarui harga jasa per kg dan simpan ke CSV"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("ATUR HARGA JASA PER KG".center(50))
    print("=" * 50)

    file_path = "harga_jasa.csv"

    # Pastikan file CSV ada
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Harga_per_Kg", "Tanggal_Ditetapkan"])
        df.to_csv(file_path, index=False)

    # Baca data CSV
    df = pd.read_csv(file_path)

    # Tampilkan harga terakhir jika ada
    if not df.empty:
        last_price = df.iloc[-1]["Harga_per_Kg"]
        last_date = df.iloc[-1]["Tanggal_Ditetapkan"]
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
        "Harga_per_Kg": new_price,
        "Tanggal_Ditetapkan": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(file_path, index=False)

    print(f"\nHarga baru Rp{int(new_price):,}/kg berhasil disimpan!".replace(",", "."))
    input("\nTekan Enter untuk melanjutkan...")

