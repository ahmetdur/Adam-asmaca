# Import gerekirse 
import random
print("Başlıyor...")

# modul1.txt dosyasından tüm kelimeleri okuyun.
import csv
with open(r'D:\modul1.txt' , 'r') as f:
    kelimeler = f.read().splitlines()

# Dosyadan okuduğunuz kelimelerden birini RASTGELE seçiniz.
gizli_kelime = random.choice(kelimeler)
#print(gizli_kelime)
bos = ' ' #çizgi koyulursa karakter kadar çizgi koyulur
kelime_cizgisi = list(bos*len(gizli_kelime))
# Tüm tahminleri tutan değişken
tahminler = []


# Oyuncunun kaç hakkı olduğunu tutan bir değişken
hak = 10

# While Döngüsü kullanıcının hakkı olduğu sürece çalışacak.

dongu=1
while (dongu):
    print(' '.join(kelime_cizgisi))
    karakter = input ('Tahmininizi Büyük Harf ile Giriniz: ')
    try:
        int(karakter)
        print('Sayı giremezsin.\n')
        
    except:
        if len(karakter) > 1:
            print('Tek harf giriniz!\n')

        else:
            if karakter in tahminler:
                print ('Bu harfi zaten girdiniz.\n')
        
        
   
            else:
    # Kullanıcının kaç hata yaptığını tutun. Başlangış kaç olabilir. :)
                hata = None
    

    # Gizli kelime içindeki her karakter için   
                for i in range(len(gizli_kelime)):
                    if karakter == gizli_kelime[i]:
                        hata = True
                        kelime_cizgisi[i] = karakter
                        # Tahmini tahminlere ekleyin.
                        tahminler.append(karakter)
                        # Karakteri yazdır
                        #print('Tebrikler {} kelime içinde var :)'.format(karakter))
                
                        
                        
                # Oyuncu başarılı olur. Oyun biter. Oyuncuya kazandığını bildir.
                        if bos not in kelime_cizgisi:
                            print('\n{}'.format(gizli_kelime))
                            print('\nTebrikler kelimeyi buldunuz!')
                            dongu = 0
                       
    # Eğer tahmin gizli kelimemizde yoksa hakkını azalt ve kullanıcıya yalnış de ve kaç hakkı kaldığını söyle.

                else:
                    if hata != True:
                        # Bulunamazsa _ yazılacak
                        print ('_')
                        hak -= 1
                        print('Yanlış harf. Kalan hakkınız: {}\n'.format(hak))
    # Eğer hak 0'a eşitse oyun bitti demek lazım.. :(
                    if hak ==0:
                        print ('Kaybettiniz')
                        print ('Doğru kelime {} idi.'.format (gizli_kelime))
        # ve çıkış yapıyoruz.
                        break              



                    





 
        
        

