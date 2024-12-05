from islemler import yeni_kullanici,kullanici_getir, kullaniciAdi_sifre_uret,anlik_uret
import islemler
def menu_goruntule():
    print("Lütfen bir seçim yapın:")
    print("1. Yeni kullanıcı ekle")
    print("2. Dosyadan Kullanıcı bilgilerini getir")
    print("3. Dosyadaki bilgilerden Kullanıcı adı ve şifre üret")
    print("4. Anlık girdiyle kullanıcı adı ve şifre üret")
    print("0.çıkış yap")

def main():
    while True:
        menu_goruntule()
        secim = input("Seçiminizi girin (1-4): ")
        if secim == "1":
            yeni_kullanici_ekle()   # kullanıcının girecegi verilere göre fonksiyon tanımladım.
        elif secim == "2":
            id = input("Kullanıcı ID'sini girin: ")
            kullanici_getir(id)         # dosyamızdaki kullanıcının ıd'sine göre kullanıcı çagırabilecegimiz bir fonksyon tanımladık
        elif secim == "3":
            kullanici_adi_sifre_uret()   # Dosyamızdakı kulanıcılardan  istenilen şekilde (verilen adımlar uygulanrak) şifre üretecegimiz fonksiyon taımladık
        elif secim == "4":
            anlik_uret()                # Kullanıcının  anlık girdisiyle şifre üreten fonsiyon tanımladık
        elif secim == "0":
            print("işlem sonlandı")
            break
        else:
            print("Geçersiz seçim ,lütfen tekrar deneyin.")
