jumlah_item = int(input("Masukkan jumlah barang: "))

total_biaya = 0

for i in range(jumlah_item):
    biaya = float(input("Masukkan biaya barang ke-" + str(i+1) + ": "))
    total_biaya += biaya

print("Total biaya: Rp.", round(total_biaya, 2))