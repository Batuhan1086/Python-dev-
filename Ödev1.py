
while True:
    print ("Programa hoş geldiniz. Lütfen yapmak istediğiniz işlemi seçiniz.")
    print ("-"*15)
    print ("Toplama işlemi için => 1\nÇıkarma işlemi için => 2\nÇarpma işlemi için => 3\nBölme işlemi için => 4")

    try:
        soru= int(input("Yapacağınız işlemin numarası: "))
        print ("Seçtiğiniz işlemin numarası: ",soru)

        if soru==1:
            sayi1 = int(input("Toplama işlemi için ilk sayıyı giriniz: "))
            print (sayi1)
            sayi2 = int(input("Toplama işlemi için ikinci sayıyı giriniz: "))
            print (sayi1,"+",sayi2,":",sayi1+sayi2)

        if soru==2:
            sayi3 = int(input("Çıkarma işlemi için ilk sayıyı giriniz: "))
            print (sayi3)
            sayi4 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
            print (sayi3,"-",sayi4,": ",sayi3-sayi4)

        if soru==3:
            sayi5 = int(input("Çarpma işlemi için ilk sayıyı giriniz: "))
            print (sayi5)
            sayi6 = int(input("Çarpma işlemi için ikinci sayıyı giriniz: "))
            print (sayi5,"*",sayi6,": ",sayi5*sayi6)

        if soru==4:
            sayi7 = int(input("Bölme işlemi için ilk sayıyı giriniz: "))
            print (sayi7)
            sayi8 = int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
            try:
                sonuc= sayi7/sayi8
                print (sayi7,"/",sayi8,": ",sonuc)
            except ZeroDivisionError:
                print ("Hiçbir sayı 0'a bölünemez. Lütfen farklı bir değer seçiniz!")
                print ("-"*15)
    except ValueError:
        print("Lütfen bir sayı giriniz! Ana menüye döndürülüyorsunuz.")
        print("-"*15)

