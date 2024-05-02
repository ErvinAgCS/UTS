def hitung_nilai_aset(harga_beli, masa_manfaat, nilai_sisa, tahun):
    susut_tahunan = (harga_beli - nilai_sisa) / masa_manfaat
    susut_total = susut_tahunan * tahun
    nilai_aset = harga_beli - susut_total
    return nilai_aset

harga_beli = 39000000
masa_manfaat = 7
nilai_sisa = 4000000
tahun = 3

nilai_aset = hitung_nilai_aset(harga_beli, masa_manfaat, nilai_sisa, tahun)
print("Nilai aset setelah", tahun, "tahun adalah:", nilai_aset)