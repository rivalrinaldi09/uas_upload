def pembayaran():
    print("\n=================================================")
    nama = input("\n\tmasukan nama = ")
    nim = input("\tmasukan nim = ")
    print("\n\t---pilihan pembayaran---")
    print("\t1. pembayaran spp")
    print("\t2. pembayaran uts")
    print("\t3. pembayaran uas")
    print("\t4. pembayaran spp & uts")
    print("\t5. pembayaran spp & uas")
    pilih = input ("\n\tsilakan pilih : ")
    if pilih == "1":
        spp()
    elif pilih == "2" :
        uts()
    elif pilih == "3" :
        uas()
    elif pilih == "4" :
        spp_uts()
    elif pilih == "5" :
        spp_uas()
    else:
        exit
        tanya()
        
def tanya():
    tanya = input("\n\tKembali ke menu pembayaran (y/t)? ")
    if tanya == "y":
        pembayaran()
        
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input....................!!!")
        
def spp():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 500000*bulan
    print("==========================================================")
    print("\ttotal bayar spp Rp.500000 *" ,bulan," = Rp. ",total)
    tanya()
    
def uas():
    matkul = int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul)
    total = 500000 * matkul
    print("=========================================================")
    print("\ttotal yang harus dibayar Rp. 50000 *" ,matkul," = Rp. ", total)
    tanya()
    
def uts():
    matkul_uts =int(input("\n\tjumlah mata kuliah = "))
    matkul_uts =float(matkul_uts)
    total = 50000 * matkul_uts
    print("========================================================")
    print("\ttotal yang harus dibayar Rp. 50000 * ",matkul_uts," = Rp.",total)
    tanya()
    
def spp_uas():
    bulan =int(input("\n\tjumlah bulan yang di  bayar = "))
    matkul =int(input("\tjumlah mata kuliah = "))
    matkul =float(matkul)
    bulan = float(bulan)
    total_spp = 500000 * bulan
    byr_uas = 50000 * matkul
    total = total_spp + byr_uas + 5000
    print("\n\ttotal bayar spp Rp.500000 * ",bulan," = Rp.",total_spp)
    print("\ttotal bayar uas Rp.250000 * ",matkul," = Rp.",byr_uas)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("=============================================================")
    print("\ttotal yang harus di bayar" ,total)
    tanya()
    
def spp_uts():
    bulan =int(input("\n\tjumlah bulan yang di  bayar = "))
    matkul =int(input("\tjumlah mata kuliah = "))
    bulan = float(bulan)
    matkul =float(matkul)
    total_spp = 500000 * bulan
    byr_uts = 50000*matkul
    total = total_spp + byr_uts + 5000
    print("\n\ttotal bayar spp Rp.500000 * ",bulan," = Rp.",total_spp)
    print("\ttotal bayar uts Rp.50000 * ",matkul," = Rp.",byr_uts)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("=============================================================")
    print("\ttotal yang harus di bayar" ,total)
    tanya()

pembayaran()
