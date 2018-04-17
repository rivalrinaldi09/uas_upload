


import getpass

def login():
    print("============================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian")
    print("\t2. nilai mahasiswa")
    print("\t3. kalkulator")

    pilih = input("\n\tsilakan pilih : ")
    if pilih == "1":
        from perhitungan.nilai_mahasiswa import tt
    elif pilih == "2":
        from perhitungan.pembayaran_mahasiswa import pembayaran
    elif pilih == "3":
        from perhitungan.kalkulator import menu
    else:
        exit
    tanya()

def tanya():
    tanya = input("nKembali ke menu (y/t)? ")
    if tanya == "y":
        login()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...........!!!!")

username = input("\nUsername : ")
password = getpass.getpass()
print("===============================================")

if username == "rival09" and password == "rival999":
    login()
    
else:
    print ("maaf password atau username mu salah.....!!!")
    
