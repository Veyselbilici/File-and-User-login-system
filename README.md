# File-and-User-login-system
Kullanıcı girişi yapılan bir sistem ve anlık olarak dosyaya kayıt edip ,yeni giriş yapılan kullanıcı için de şifre oluşturan login işlemleri yapan sistem
1.BAŞLA
2.Kullanıcıdan secim yapması için "menu_goruntule" fonksiyonu OLUŞTUR:
 Ekrana "Lütfen bir seçenek seçin:" yazdır.
 Ekrana "1. Yeni kullanıcı ekle" seçeneğini yazdır.
 Ekrana "2. Dosyadan Kullanıcı bilgilerini getir" seçeneğini yazdır.
 Ekrana "3.Dosyadaki bilgilerden Kullanıcı adı ve şifre üret" seçeneğini yazdır.
 Ekrana "4. Anlık girdiyle kullanıcı adı ve şifre üret" seçeneğini yazdır.
3.Yeni kullanıcı ekle için "yeni_kullanici" fonksiyonu yaz :
 a)Kullanıcıdan yeni kullanıcı bilgilerini iste (id,Ad,Soyad,Dogum-Tarihi,Dogum-Yeri).
 b)Dosyadaki mevcut kullanıcı verilerini etkilemeden veri girrişi yap.
 c)Yeni kullanıcı bilgilerini dosyaya ekle.
 Dosyayı kaydet.
4.Dosyadan kullanıcı getirmek iççin "kullanici_getir" fonksiyonu :
 a)Kullanıcıdan bir kullanıcı ID'si iste.
 b)Dosyadaki kullanıcı verilerini oku.
 c)Girilen kullanıcı ID'si ile eşleşen kullanıcı verilerini ekrana yazdır.
 d)Eğer girilen kullanıcı ID'si bulunamazsa, kullanıcıya tekrar ID girmesi istenir.
5.Dosyadaki kullanıcıdan kullanıcı adı ve şifre üretmek için "kullaniciAdi_sifre_uret" 
fonksiyonu yaz ve sözde kod şu şekilde :
a)Okunan dosyadaki tüm metin küçük harfe dönüştür.
b)Dosyadan ilk satır atlanır.
c)Boş bir kullanıcı adı ve şifre listesi oluşturulur.
d)Dosya satır satır okunur.
e)Her bir satırda kullanıcı adı ve doğum tarihi, soyadı ve doğum yeri bilgileri ayrıştırılır.
f)Kullanıcı adı oluşturmak için adın 2. ve 4. harfleri, soyadın son 3 harfi ve doğum yılının 
son iki rakamı kullanılır. Bu değerler kullanarak kullanıcı adı oluşturulur ve listeye eklenir.
g)Şifre oluşturmak için adın ilk ve son harfleri, soyadın son 2 harfi, doğum yılının son iki 
rakamı, doğum ayının karesi, doğum yerinin ilk ve son harfi hariç kalan kısmı ve rastgele 2 
basamaklı bir sayı kullanılır. Bu değerler kullanarak şifre oluşturulur ve listeye eklenir.
h)Oluşturulan kullanıcı adı ve şifre listeleri ekrana yazdırılır.
6.Anlık girdiyle kulanıcı adı ve şifre üret için ‘’anlik_uret ‘’ fonksiyonu olacaktır.
 a)Tüm kullanıcı bilgilerini virgülü olarak tek girişte kullanıcıdan alınır
 b)Girdiyi küçük harflere çevir
 c)5.adıma geri dön ve ordaki işlemleri tekrar uygula
 d)Elde edilen kullanıcı adı ve şifreyi EKRANA YAZ.                        
