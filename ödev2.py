import random
parola_listesi = []  #parola seçenekleri tutuluyor.
sonuc_parola = []   #ekrana yazdırılacak parola burda oluşuyor.

print("RANDOM PAROLA OLUŞTURMA UYGULAMASINA HOŞGELDİNİZ...")
print("****************************************************")
print("Karşınıza gelecek sorulara E\H cevaplarını veriniz!")
print("****************************************************\n")

sayi = input("Parolanız sayıları içersin mi: ")
harf = input("Parolanız harfleri içersin mi: ")
ozel_karakter = input("Parolanız özel karakterleri içersin mi: ")

if sayi == "E":
    for i in range(10):
        parola_listesi.append(i)

if harf == "E":
    alfabe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
              "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in alfabe:
        parola_listesi.append(i)

if ozel_karakter == "E":
    ozel_karakterler = ['"', '!', '.', ',', '@', '#']
    for i in ozel_karakterler:
        parola_listesi.append(i)

max_parola = int(input("Parolanız max kaç karakter olsun: "))
min_parola = int(input("Parolanız min kaç karakter olsun: "))
print()

parola_uzunlugu = random.randint(min_parola, max_parola)

for i in range(parola_uzunlugu):
    sonuc_parola.append(random.choice(parola_listesi))

print("PAROLANIZ...")
for k in range(len(sonuc_parola)):
    print(sonuc_parola[k], end="")
