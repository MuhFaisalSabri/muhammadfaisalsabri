data_barang = ["Mouse","Keyboard","Monitor"]
print("===========List Barang============")
print(data_barang)
while (True):
    print("==============Menu================")
    print("a : Tambah Barang")
    print("b : Hapus Barang")
    print("c : Edit Barang")
    print("d : Cari Barang")
    

    menu = input('Pilih Menu : ')
    if menu == "a":
        x = input('Nama Barang : ')
        data_barang.append(x)
        print("===========List Barang============")
        print(data_barang)
    elif menu == "b":
        x = input('Nama Barang : ')
        data_barang.remove(x)
        print("===========List Barang============")
        print(data_barang)
    elif menu == "c":
        x = int(input('No Barang : '))
        y = input('Nama Barang : ')
        data_barang[x]=y
        print("===========List Barang============")
        print(data_barang)
    elif menu == "d":
        x = int(input('No Barang : '))
        print(data_barang[x])
        print("===========List Barang============")
        print(data_barang)
    
