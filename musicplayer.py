import os,shutil
import winsound
import fnmatch
#winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
def kullaniciolustur():
    print("Şimdi size özel klasör yapacağız bunu için kullanıcı adı ve şifre girmeniz gerekiyor!!!")
    while True:
     kullaniciisim=str(input("lütfen kullanıcı adınızı giriniz :"))
     if not kullaniciisim:
        print("kullanıcı adı boş geçilemez!!!")
     else:
        if len(kullaniciisim)<20:
            os.mkdir(f"{kullaniciisim}")
            os.listdir
            dosya= open(f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{kullaniciisim}\\{kullaniciisim}.txt","w")
            dosya.write(f"{kullaniciisim}\n")
            break
        else:
            print("kullanıcı adınız çok uzun ")
    while True:
                sifre=str(input("lütfen bir şifre girin :"))
                if len(sifre)>=8:
                    print("şifreniz uygundur.")
                    dosya.write(f"{sifre}")
                    break
                else:
                    print("şifreniz en az 8 haneli olmalıdır")
   # with open(dosya1,"r",encoding="utf-8") as d:
       # icerik=d.readlines()
   # with open(dosya1,"w",encoding="utf-8") as d:
    #    for index, line in enumerate(icerik):
     #    if index==silineceksatir:
      #      d.write("\n")
       # else:
         #   d.write(line) bu işlemler ilk satırı siliyor
def kayıtsil(kayıtismi):
    os.remove(f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{kayıtismi}\\{kayıtismi}.txt")
    os.rmdir(f"{kayıtismi}")
def şarkıekle(sarkıismi,klasorad):
    print()
    kaynak1 = f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\sarkılar\\{sarkıismi}.wav"
    hedef2 = "C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\sarkıyedegi"
    if not os.path.exists(hedef2):
        os.makedirs(hedef2)
    shutil.copy(kaynak1,hedef2)    
    kaynak=f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\sarkıyedegi\\{sarkıismi}.wav"
    hedef=f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{klasorad}"
    if not os.path.exists(hedef):
     	os.makedirs(hedef)
    shutil.move(kaynak, hedef)
def şarkıçal(çalmakad,şarkıçalmak):
   print("şu anda ÇALIYOR")
   while True: 
     winsound.PlaySound(f'C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{çalmakad}\\{şarkıçalmak}.wav', winsound.SND_FILENAME)
     çalsınmı=str(input("şarkı tekrardan çalsınmı :"))
     if çalsınmı=="evet":
        print()
     else:   
        print("şarkı bitti")
        kullanicigiris()
def randomçal(adal):
  # file_count = sum(len(files) for _, _, files in os.walk(f'C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{adal}'))
  # print(file_count) bu komutlar klasör içinde kaç adet dosya olduğunu gösterir
  print()
def şarkısil(sarkısil,kullanicadisarkısil,sarkıresmisilme):
    os.remove(f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{kullanicadisarkısil}\\{sarkısil}.wav")
    os.remove(f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{kullanicadisarkısil}\\{sarkıresmisilme}.png")
def kullanicigiris():
    #  print ( os.path.abspath(f"{kullaniciadi}.txt")) bulunan dosyanın sana yolunu gösterir
    #os.remove("/tmp/<file_name>.txt") kayıt silde kullancağız
    kontrol=[]
    kontrolsifre=[]
    while True:
      kullaniciadi=str(input("lütfen kullanıcı adınızı giriniz :"))
      insankontrol=open(f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{kullaniciadi}\\{kullaniciadi}.txt","r")
      aduzunluk=len(kullaniciadi)
      kullanicisifre=str(input("lütfen şifrenizi giriniz :"))
      kontrol.append(insankontrol.read(aduzunluk))
      kontrolsifre.append(insankontrol.readline())
      kontrolsifre.append(insankontrol.readline())
      if kontrol[0]==kullaniciadi:
        print("kullanıcı adı doğru")
        adet=kontrolsifre.count(kullanicisifre)
        print(adet)
        if adet==1:
            print(f"giriş başarılı hoş geldin {kullaniciadi}")
            sorgu=str(input(f"Merhaba {kullaniciadi} müzik çalarında ne yapmak istersin : "))
            if sorgu=="şarkı ekle":
                şarkıeklesorgu=str(input("hangi şarkıyı klasöre eklemek istersiniz :) :"))
                şarkıekle(şarkıeklesorgu,kullaniciadi)
            elif sorgu == "şifre güncelle":
                mevcutşifre=str(input("mevcut şifrenizi girermisiniz :"))
                mevcut=kontrolsifre.count(mevcutşifre)
                if mevcut==1:
                    print("şifre doğru")
                    yenişifre=str(input("yeni şifreyi giriniz :"))
                    if mevcutşifre!=yenişifre:
                        print("şifreniz değiştirilmiştir :))")
                        dosya2=open(f"C:\\Users\\utkan\\OneDrive\\Masaüstü\\müzik çalar\\{kullaniciadi}\\{kullaniciadi}.txt","w")
                        dosya2.write(f"{kullaniciadi}\n")
                        dosya2.write(f"{yenişifre}")
                        dosya2.close()
                        print("şifreniz değiştirilmiştir :))")
                    else:
                        print("mevcut şifre ile yeni şifre aynı olamaz")    
                else:
                    print("mevcut şifreniz yanlış programdan çıkıyorsunuz!!!")    
            elif sorgu == "şarkı çal":
                sorgular=str(input("randommu yoksa istek mi :"))
                if sorgular=="istek":
                 çalsorgu=str(input("çalmak istediğiniz şarkıyı yazınız :"))
                 şarkıçal(kullaniciadi,çalsorgu)
                elif sorgular=="random":
                    randomçal(kullaniciadi) 
            elif sorgu == "şarkı sil":
                şarkısilsorgu=str(input("hangi şarkıyı silmek istersiniz :"))
                silresimsorgu=str(input("resim adını giriniz :"))
                şarkısil(şarkısilsorgu,kullaniciadi,silresimsorgu)
            elif seçim=="kayıt sil":
                silinecekisim=str(input("klasör ismini yazınız :"))
                kayıtsil(silinecekisim)
                print("kayıt başarılı bir şekilde silindi!!!")
            elif seçim=="çıkış":
                break                       
        else :
            print("şifre yanlış giriş başarısız")
            kontrolsifre.clear()  
      else:
        print("giriş başarısız kullanıcı adı yanlış")        
print("Merhaba uygulamaya HOŞ GELDİNİZ lütfen aşağıda hangi seçeceğe gitmek istediğnizi seçin :) ")
seçim=str(input("lütfen seçimininizi giriniz :"))
if seçim=="kayıt":
    kullaniciolustur()
elif seçim=="giriş":
    kullanicigiris()                                              