# import csv, os

# def set_price():
#     """Set service price per kg"""
#     print("ATUR HARGA JASA PER KG")
    
#     # # Get current price
#     # cursor.execute('SELECT * FROM prices ORDER BY effective_date DESC LIMIT 1')
#     # current_price = cursor.fetchone()
    
#     if current_price:
#         print(f"Harga saat ini: {format_rupiah(current_price['price_per_kg'])}/kg")
#         print(f"Efektif sejak: {current_price['effective_date']}")
#     else:
#         print("Belum ada harga yang ditetapkan.")
    
#     print()
#     new_price = input_float("Masukkan harga baru per kg: ")
    
#     if new_price <= 0:
#         print("Harga harus lebih dari 0!")
#         conn.close()
#         input("Tekan Enter untuk melanjutkan...")
#         return
    
#     cursor.execute('''
#         INSERT INTO prices (price_per_kg, effective_date, created_at)
#         VALUES (?, ?, ?)
#     ''', (new_price, datetime.now().isoformat(), datetime.now().isoformat()))
#     conn.commit()
#     conn.close()
    
#     print(f"\n✓ Harga baru {format_rupiah(new_price)}/kg berhasil ditetapkan!")
#     input("Tekan Enter untuk melanjutkan...")
