# Kullanıcının adını ve yaşını alın
name = input("Lütfen Adınızı Girin: ")
age = int(input("Lütfen Yaşınızı Girin: "))

# Kullanıcının ehliyet alıp alamayacağını kontrol edin
if age < 16:
    print(f"Üzgünüz, {name}, eğer 16 yaşın altındaysanız ehliyet alamazsınız.")
else:
    # Kullanıcının eğitim durumunu alın
    education = input('Lütfen Eğitim Durumunuzu Girin: "İlkokul", "Ortaokul", "Lise", "Üniversite", "Yüksek Lisans", "Doktora", "Önlisans": ')

    # Eğitime göre ehliyet uygunluğunu belirleyin
    if education == "İlkokul" or education == "Ortaokul":
        print(f"Üzgünüz, {name}, eğitim seviyeniz ({education}) ehliyet almak için yeterli değil.")
    else:
        print(f"Tebrikler, {name}! Yaşınız ve eğitim seviyeniz ({education}) itibariyle ehliyet almak için uygunsunuz.")
    
    # Kullanıcının soruları varsa sormasını sağlayın
    soru_sormak = input("Ehliyet almakla ilgili herhangi bir sorunuz var mı? (evet/hayır): ").strip().lower()
    if soru_sormak == "evet":
        print("Sorularınızı sormaktan çekinmeyin. Yardımcı olmak için buradayız!")
    else:
        print("Gelecekte sorularınız olursa sormaktan çekinmeyin. İyi günler dileriz!")


input("break")
    
# Bu satır gereksizdir ve kaldırılabilir.
# input("break")
