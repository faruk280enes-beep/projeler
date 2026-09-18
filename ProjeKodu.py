# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 12:55:48 2025

@author: enes faruk
"""

disadonukluk=0
sorumluluk=0
uyumluluk=0
aciklik=0
duygusallik=0

print("1-) Yeni bir sosyal ortama girdiğiniz zaman yaptığınız ilk şey nedir?")
print("a) ortamı gözlemleyip uygun köşe bulmak")
print("b) birkaç kişiye kendini tanıtmak")
print("c) sohbete dahil olabileceğim bir grup aramak")
print("d) ortamın merkezine gidip aktif bir iletişim kurmak")

while True:
 cvp=input("bir şık seçiniz: ")
 if cvp=="a":
    disadonukluk=disadonukluk+1
    break
 elif cvp=="b":
    disadonukluk=disadonukluk+2
    break
 elif cvp=="c":
    disadonukluk=disadonukluk+3
    break
 elif cvp=="d":
    disadonukluk=disadonukluk+4
    break
 else:
    print("geçersiz cevap girdiniz tekrar deneyiniz")
    
print("\n2-) Zor bir karar vermeniz gerektiğinde nasıl hareket edersiniz?")
print("a) Tüm seçenekleri ayrıntılı analiz ederim")
print("b) İçgüdülerime göre hızlı bir seçim yaparım")
print("c) Yakın çevremden görüş alırım")
print("d) Deneyip görme yaklaşımıyla ilerlerim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        sorumluluk = sorumluluk + 4
        break
    elif cvp == "b":
        sorumluluk = sorumluluk + 2
        break
    elif cvp == "c":
        sorumluluk = sorumluluk + 3
        break
    elif cvp == "d":
        sorumluluk = sorumluluk + 1
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")    
        
print("\n3-) Bir proje ekibinde rolünüz çoğunlukla ne olur?")
print("a) Planlayan ve düzenleyen kişi")
print("b) Motivasyonu artıran ve iletişimi kuran kişi")
print("c) Sorunlara yaratıcı çözümler bulan kişi")
print("d) Hızla uygulamaya geçen kişi")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        sorumluluk = sorumluluk + 4
        break
    elif cvp == "b":
        sorumluluk = sorumluluk + 2
        break
    elif cvp == "c":
        sorumluluk = sorumluluk + 3
        break
    elif cvp == "d":
        sorumluluk = sorumluluk + 1
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n4-) Stresli bir durumla karşılaştığınızda ilk tepkiniz nedir?")
print("a) Geri çekilip düşünmek")
print("b) Hemen çözüm aramak")
print("c) Bir arkadaşla konuşarak rahatlamak")
print("d) Durumu mizaha vurmak")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        duygusallik = duygusallik + 3
        break
    elif cvp == "b":
        duygusallik = duygusallik + 1
        break
    elif cvp == "c":
        duygusallık = duygusallik + 4
        break
    elif cvp == "d":
        duygusallik = duygusallik + 2
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n5-) Bir arkadaşınız sizden yardım istediğinde hangi yaklaşımı sergilersiniz?")
print("a) Önce detayları sorup yapabileceğimi analiz ederim")
print("b) Hızlıca çözüme yönelik öneri sunarım")
print("c) Önce onu dinler, duygusal destek veririm")
print("d) Beraber hareket etmeyi teklif ederim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        uyumluluk = uyumluluk + 2
        break
    elif cvp == "b":
        uyumluluk = uyumluluk + 1
        break
    elif cvp == "c":
        uyumluluk = uyumluluk + 4
        break
    elif cvp == "d":
        uyumluluk = uyumluluk + 3
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n6-) Bir şeyi öğrenirken hangi yöntemi tercih edersiniz?")
print("a) Sistematik plan ve notlarla çalışmak")
print("b) Video/demolar izleyerek kavramak")
print("c) Tartışarak, başkalarıyla konuşarak öğrenmek")
print("d) Yaparak, deneyerek öğrenmek")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        aciklik = aciklik + 1
        break
    elif cvp == "b":
        aciklik = aciklik + 3
        break
    elif cvp == "c":
        aciklik = aciklik + 2
        break
    elif cvp == "d":
        aciklik = aciklik + 4
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")        
        
print("\n7-) Sabah işe/okula başladığınızda çalışma tarzınız nasıldır?")
print("a) Önce yapılacakları planlarım")
print("b) Önce hızlı yapılabilecek işleri bitiririm")
print("c) Önce ekip/arkadaş ortamını kontrol ederim")
print("d) Direkt en zor işe girerim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        sorumluluk = sorumluluk + 4
        break
    elif cvp == "b":
        sorumluluk = sorumluluk + 3
        break
    elif cvp == "c":
        sorumluluk = sorumluluk + 2
        break
    elif cvp == "d":
        sorumluluk = sorumluluk + 1
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")        

print("\n8-) Bir tartışma ortamında nasıl davranırsınız?")
print("a) Mantık yürütür, kanıtlarla konuşurum")
print("b) Açık sözlü ve doğrudan konuşurum")
print("c) Uzlaşı sağlamaya çalışırım")
print("d) Yaratıcı örnekler ve benzetmeler kullanırım")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        disadonukluk = disadonukluk + 1
        break
    elif cvp == "b":
        disadonukluk = disadonukluk + 4
        break
    elif cvp == "c":
        disadonukluk = disadonukluk + 3
        break
    elif cvp == "d":
        disadonukluk = disadonukluk + 2
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")   
        
print("\n9-) Yeni bir şey denemek konusunda kendinizi nasıl tanımlarsınız?")
print("a) Temkinli, önce araştırırım")
print("b) Çoğu zaman hemen denerim")
print("c) Başkaları da katılıyorsa daha hevesli olurum")
print("d) Rutini sevmem; yenilik ararım")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        aciklik = aciklik + 1
        break
    elif cvp == "b":
        aciklik = aciklik + 3
        break
    elif cvp == "c":
        aciklik = aciklik + 2
        break
    elif cvp == "d":
        aciklik = aciklik + 4
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n10-) Bir hata yaptığınızda ne yaparsınız?")
print("a) Nedenini analiz ederim")
print("b) Hemen çözüm geliştirmeye çalışırım")
print("c) Fikir almak için birine danışırım")
print("d) Durumu abartmadan geçiştirip devam ederim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        duygusallik = duygusallik + 3
        break
    elif cvp == "b":
        duygusallik = duygusallik + 1
        break
    elif cvp == "c":
        duygusallik = duygusallik + 4
        break
    elif cvp == "d":
        duygusallik = duygusallik + 2
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n11-) Beklenmedik bir plan değişikliği olduğunda nasıl hareket edersiniz?")
print("a) Yeni planı düzenler, kontrol ederim")
print("b) Hızlıca uyum sağlarım")
print("c) Çevremle konuşup durumu netleştiririm")
print("d) Değişikliği avantaj haline getirmeye çalışırım")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        disadonukluk = disadonukluk + 1
        break
    elif cvp == "b":
        disadonukluk = disadonukluk + 3
        break
    elif cvp == "c":
        disadonukluk = disadonukluk + 2
        break
    elif cvp == "d":
        disadonukluk = disadonukluk + 4
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n12-) Zaman yönetiminde tarzınız nedir?")
print("a) Dakik ve planlıyımdır")
print("b) İşe göre esneyebilirim")
print("c) Yoğunlukla son dakikada motive olurum")
print("d) Aynı anda birden çok işle ilgilenirim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        sorumluluk = sorumluluk + 4
        break
    elif cvp == "b":
        sorumluluk = sorumluluk + 3
        break
    elif cvp == "c":
        sorumluluk = sorumluluk + 1
        break
    elif cvp == "d":
        sorumluluk = sorumluluk + 2
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n13-) Bir problemi çözmek için yaklaşımınız nedir?")
print("a) Adım adım metodik ilerlerim")
print("b) Pratik ve hızlı çözüm ararım")
print("c) Birlikte düşünmeyi tercih ederim")
print("d) Farklı, alışılmışın dışında yollar denerim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        aciklik = aciklik + 1
        break
    elif cvp == "b":
        aciklik = aciklik + 2
        break
    elif cvp == "c":
        aciklik = aciklik + 3
        break
    elif cvp == "d":
        aciklik = aciklik + 4
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n14-) Sosyal ilişkilerde kendinizi nasıl tanımlarsınız?")
print("a) Samimi ama mesafeli")
print("b) Açık, konuşkan")
print("c) Destekleyici ve uyumlu")
print("d) Eğlenceli ve enerjik")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        disadonukluk = disadonukluk + 1
        break
    elif cvp == "b":
        disadonukluk = disadonukluk + 4
        break
    elif cvp == "c":
        disadonukluk = disadonukluk + 3
        break
    elif cvp == "d":
        disadonukluk = disadonukluk + 2
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n15-) Bir ekipte çatışma çıktığında ne yaparsınız?")
print("a) Tarafsız kalıp çözüm analiz ederim")
print("b) Sorunu açıkça dile getiririm")
print("c) Taraflar arasında köprü kurarım")
print("d) Ortamı yumuşatacak yaklaşımı seçerim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        uyumluluk = uyumluluk + 2
        break
    elif cvp == "b":
        uyumluluk = uyumluluk + 1
        break
    elif cvp == "c":
        uyumluluk = uyumluluk + 4
        break
    elif cvp == "d":
        uyumluluk = uyumluluk + 3
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n16-) Uzun vadeli hedef belirleme tarzınız nedir?")
print("a) Ayrıntılı plan yaparım")
print("b) Genel bir yön belirlerim")
print("c) Hedefi çevreme danışarak şekillendiririm")
print("d) Deneyimledikçe hedefi güncellerim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        sorumluluk = sorumluluk + 4
        break
    elif cvp == "b":
        sorumluluk = sorumluluk + 2
        break
    elif cvp == "c":
        sorumluluk = sorumluluk + 3
        break
    elif cvp == "d":
        sorumluluk = sorumluluk + 1
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n17-) Günlük yaşamda ani sorunlar çıktığında tepkileriniz?")
print("a) Organize şekilde çözüm oluştururum")
print("b) Hızlıca aksiyon alırım")
print("c) Yakın çevremle durumu paylaşırım")
print("d) Esnek bir çözüm üretip ilerlerim")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        duygusallik = duygusallik + 3
        break
    elif cvp == "b":
        duygusallik = duygusallik + 1
        break
    elif cvp == "c":
        duygusallik = duygusallik + 4
        break
    elif cvp == "d":
        duygusallik = duygusallik + 2
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n18-) Başkaları sizi nasıl tarif eder?")
print("a) Düzenli ve güvenilir")
print("b) Enerjik ve girişken")
print("c) Sakin ve uyumlu")
print("d) Yaratıcı ve özgün")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        uyumluluk = uyumluluk + 2
        break
    elif cvp == "b":
        uyumluluk = uyumluluk + 1
        break
    elif cvp == "c":
        uyumluluk = uyumluluk + 4
        break
    elif cvp == "d":
        uyumluluk = uyumluluk + 3
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n19-) Boş zamanlarınızı nasıl değerlendirmeyi tercih edersiniz?")
print("a) Sessiz, planlı aktiviteler (okuma, araştırma vb.)")
print("b) Sosyal, hareketli aktiviteler")
print("c) Arkadaşlarla vakit geçirmek")
print("d) Yeni hobiler deneyerek")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        aciklik = aciklik + 1
        break
    elif cvp == "b":
        aciklik = aciklik + 2
        break
    elif cvp == "c":
        aciklik = aciklik + 3
        break
    elif cvp == "d":
        aciklik = aciklik + 4
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")

print("\n20-) Bir iş üzerinde çalışırken önceliğiniz nedir?")
print("a) Doğruluk ve sistematiklik")
print("b) Hız ve sonuç odaklılık")
print("c) Ekiple uyum")
print("d) Yaratıcılık ve özgürlük")

while True:
    cvp = input("bir şık seçiniz: ")

    if cvp == "a":
        sorumluluk = sorumluluk + 4
        break
    elif cvp == "b":
        sorumluluk = sorumluluk + 2
        break
    elif cvp == "c":
        sorumluluk = sorumluluk + 3
        break
    elif cvp == "d":
        sorumluluk = sorumluluk + 1
        break
    else:
        print("geçersiz cevap girdiniz tekrar deneyiniz")




if aciklik <= 7:
    print("\n Openness – Düşük Açıklık (4–7):")
    print("- Geleneksel, güvenli ve tanıdık seçenekleri tercih edersiniz.")
    print("- Rutinler sizi rahatlatır; ani değişikliklerden hoşlanmayabilirsiniz.")
    print("- Öğrenirken yapı, netlik ve adım adım ilerleme önceliğinizdir.")
elif aciklik <= 12:
    print("\n Openness – Orta Açıklık (8–12):")
    print("- Yeniliklere açıksınız ancak tamamen kontrolsüz deneyimleri tercih etmeyebilirsiniz.")
    print("- Hem geleneksel hem yaratıcı yaklaşımları dengeli kullanırsınız.")
    print("- Yeni fikirleri değerlendirirken temkinli ilerlersiniz.")
else:
    print("\n Openness – Yüksek Açıklık (13–16):")
    print("- Meraklı, yaratıcı ve keşfetmeye heveslisiniz.")
    print("- Farklı düşünme biçimlerini ve özgün çözümleri tercih edersiniz.")
    print("- Sanatsal, kavramsal ya da yenilikçi alanlara doğal yatkınlık gösterirsiniz.")


if sorumluluk <= 11:
    print("\n Conscientiousness – Düşük Planlılık (6–11):")
    print("- Esnek ve spontane bir çalışma tarzını benimsersiniz.")
    print("- Ayrıntılar yerine büyük resmi görmeyi tercih edersiniz.")
    print("- Zaman zaman erteleme eğilimi olabilir.")
elif sorumluluk <= 18:
    print("\n Conscientiousness – Orta Planlılık (12–18):")
    print("- Hem planlı hem de durumlara uyum sağlayabilen dengeli bir yaklaşımınız var.")
    print("- Gerektiğinde detaylara inebilir, gerektiğinde hızlı aksiyon alabilirsiniz.")
    print("- Bu grup genelde iş ortamında uyumlu ve güvenilir bulunur.")
else:
    print("\n Conscientiousness – Yüksek Planlılık (19–24):")
    print("- Düzenli, sistematik ve sorumluluk sahibi bir kişilik profiliniz var.")
    print("- Planlar, listeler ve süreç yönetimi sizin için doğal araçlardır.")
    print("- Hedef odaklı çalışır ve işlerin tamamlanmasına yüksek önem verirsiniz.")

if disadonukluk <= 7:
    print("\n Extraversion – Düşük Dışadönüklük (4–7):")
    print("- Enerjinizi yalnız kalarak tazelersiniz.")
    print("- Sosyal ortamları sevseniz bile kontrollü ve seçici yaklaşabilirsiniz.")
    print("- Derin sohbetler, yüzeysel kalabalıklardan daha anlamlı gelir.")
elif disadonukluk <= 12:
    print("\n Extraversion – Orta Dışadönüklük (8–12):")
    print("- Sosyal etkileşimlerden keyif alırsınız ancak aşırı yoğunluk yorabilir.")
    print("- Hem bireysel çalışma hem grup çalışması size uygundur.")
    print("- Denge profilidir; çoğu sosyal ortamda rahat edersiniz.")
else:
    print("\n Extraversion – Yüksek Dışadönüklük (13–16):")
    print("- Enerjik, girişken ve sosyal ortamlarda rahat davranan bir yapınız var.")
    print("- Yeni insanlarla tanışmak, grup içinde aktif olmak sizin için kolaydır.")
    print("- Liderlik, iletişim ve etkileşim gerektiren işlerde başarılı olabilirsiniz.")

if uyumluluk <= 5:
    print("\n Agreeableness – Düşük Uyumluluk (3–5):")
    print("- Daha bağımsız, doğrudan ve gerektiğinde eleştirel bir tavır sergilersiniz.")
    print("- Çatışmalardan kaçmazsınız; dürüstlüğü önceliklendirirsiniz.")
    print("- Liderlik ve karar alma gerektiren pozisyonlara uygundur.")
elif uyumluluk <= 9:
    print("\n Agreeableness – Orta Uyumluluk (6–9):")
    print("- Hem işbirlikçi hem de gerektiğinde kendi fikrini savunan dengeli bir yapınız vardır.")
    print("- İnsan ilişkilerini önemser ancak gereksiz fedakarlık yapmazsınız.")
    print("- Ekip çalışmalarında uyumu kolaylaştıran bir role girebilirsiniz.")
else:
    print("\n Agreeableness – Yüksek Uyumluluk (10–12):")
    print("- Empatik, destekleyici ve işbirliğine değer veren bir kişilik profiliniz var.")
    print("- İnsanları anlamaya yatkın, sabırlı ve yapıcı bir iletişim tarzınız vardır.")
    print("- Sosyal meslekler, rehberlik veya ekip uyumu gerektiren rollere uygunsunuz.")

if duygusallik <= 5:
    print("\n Neuroticism - Düşük Duygusal Dengesizlik (3–5):")
    print("- Duygusal olarak dengeli, stres altında sakin kalabilen bir yapınız var.")
    print("- Zorluklar karşısında kontrollü davranır, duygularınızı kolay yönetirsiniz.")
    print("- Sizi kolay kolay panik içinde görmek zordur.")
elif duygusallik <= 9:
    print("\n Neuroticism - Orta Duygusal Dengesizlik (6–9):")
    print("- Zaman zaman kaygı veya duygusal dalgalanmalar yaşarsınız ancak yönetebilirsiniz.")
    print("- Çevre koşullarına göre stres seviyeniz değişiklik gösterebilir.")
    print("- Bu grup toplum ortalamasıdır.")
else:
    print("\n Neuroticism - Yüksek Duygusal Dengesizlik (10–12):")
    print("- Stres, belirsizlik ve yoğun baskı sizi daha fazla etkileyebilir.")
    print("- Duygusal dalgalanmalar, kaygı ve zihinsel yorgunluğa yatkınlık olabilir.")
    print("- Duygusal farkındalık, mindfulness ve yapılandırılmış rutinler fayda sağlar.")


        
        

        
    
    
    
    
    
    
    
    

