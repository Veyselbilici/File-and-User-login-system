
def yeni_kullanici():
    # Yeni kullanıcı bilgileri kullanıcıdan al
    # Alınan veriler uygun şekilde dosyaya yaz

    with open("kullanicilar.txt", "a") as dosya:
        kullanici_adi = input("Kullanıcı adı: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        dogum_tarihi = input("Doğum tarihi (GG/AA/YYYY): ")
        dogum_yeri =  input("Dogum yeri : ")
        dosya.write(f"{kullanici_adi},{ad},{soyad},{dogum_tarihi},{dogum_yeri}\n")
        print("Kullanıcı eklendi.")

def kullanici_getir():
    # Kullanıcının bilgileri ID ile sorgulanır
    # Girilen ID geçersizse, kullanıcı tekrar ID girmesi için istenir
    while True:
        girilen_id = input("Lütfen kullanıcı ID girin: ")
        with open("kullanicilar.txt", "r") as dosya:
            next(dosya)
            for satir in dosya:
                satir = satir.strip().lower().split(",")
                if satir[0] == girilen_id.lower():
                    print(f"Kullanıcı Adı: {satir[1]}\nAdı: {satir[2]}\nSoyadı: {satir[3]}\nDoğum Tarihi: {satir[4]}\nDogum yeri:{satir[5]}")
                    return
            print("Girdiğiniz ID geçersiz. Tekrar deneyin.")


def kullaniciAdi_sifre_uret(kullanicilar):
    kullanici_adi_listesi= []
    sifre_listesi = []
    karakterler = ['*', '/', '!', '_', '(', ')', '&', '%', '+', '-', '.', ',', '<', '>']
    try:             # try/except kullanılarak okuma hatası durumunu denetler
        with open(kullanicilar.txt, 'r') as dosya:
            dosya.readline()  # İlk satır okunmuyor
            for satir in dosya:
                satir = satir.lower().strip()
                if satir:
                    # Kullanıcı adı oluşturma
                    ad, soyad, dogumTarihi, dogumYeri = satir.split()
                    adim1 = ad[1] + ad[3]
                    adim2 = soyad[-3:].replace(soyad[-2], random.choice(karakterler))
                    adim3 = str(int(dogumTarihi[-4:-2]) + int(dogumTarihi[-2:]) + 25) + dogumTarihi[-2:]
                    kullaniciAdi = adim2 + adim1 + adim3
                    kullanici_adi_listesi.append(kullaniciAdi)

                    # Şifre oluşturma kısmı
                    adim1 = ad[0].upper() + ad[-1]
                    adim2 = soyad[-2:].replace(soyad[-2], random.choice(karakterler))
                    adim3 = str(int(dogumTarihi[-2:]) + int(dogumTarihi[-4:-2]) ** 2)
                    adim4 = dogumYeri[1:-1].title()
                    adim5 = str(random.randint(10, 99))
                    sifre = adim4 + adim5 + adim1 + adim3 + adim2
                    sifre_listesi.append(sifre)
                    print("Kullanıcı adları:")
                    print(kullanici_adi_listesi)
                    print("Şifreler:")
                    print(sifre_listesi)
         with open("kullaniciAdi_sifre.txt", "w") as f:
       # dosyadan alınan kullanıcı verileri ile oluşturdugumuz kullanıcı adı ve şifreler dosyaya yazılıyor
             for id, kullanici_adi_listesi, sifre_listesi in zip(range(1, len(kullanici_adi_listesi) + 1), kullanici_adi_listesi, sifre_listesi):
                 f.write(f"{id},{kullanici_adi_listesi},{sifre_listesi}\n")


def anlik_uret():
    # Kullanıcıdan tüm kullanıcı bilgilerini tek bir girdi olarak al
    bilgiler = input("Lütfen kullanıcı bilgilerini (id, Ad, Soyad, Doğum Tarihi, Doğum Yeri) virgülle ayırarak girin: ")

    # Girdiyi küçük harflere dönüştür
    bilgiler = bilgiler.lower()

    # Bilgileri virgülden ayır
    bilgiler = bilgiler.split(",")

    # Kullanıcı adı ve şifre oluşturmak için kullanılacak değerleri belirle
    ad = bilgiler[1]
    soyad = bilgiler[2]
    dogum_tarihi = bilgiler[3]
    dogum_yeri = bilgiler[4]

    # Kullanıcı adını oluştur
    kullanici_adi = ad[1] + ad[3] + soyad[-3:] + dogum_tarihi[-2:]

    # Şifreyi oluştur
    sifre = ad[0] + ad[-1] + soyad[-2:] + dogum_tarihi[-2:] + str(int(bilgiler[3].split("-")[1]) ** 2) + dogum_yeri[1:-1]+str(random.randint(10,99))

    # Kullanıcı adı ve şifreyi ekrana yazdır
    print("Kullanıcı Adı:", kullanici_adi)
    print("Şifre:", sifre)



