#BÖLÜM 1:VERİ TİPLERİ
# 1.isim,yaş boy
name=input("İsminizi Giriniz:")
age=input("Yaşınızı Giriniz:")
tall=float(input("Boyunuzu Giriniz:"))
print("Kullanıcının ismi:"+name)
print("Kullanıcının yaşı:"+age)
print("Kullanıcının boyu:"+str(tall))

# 2.öğrenci notları
mathematics=int(input("Matematik Notunuz:"))
pyhsics=int(input("Fizik Notunuz:"))
chemistry=int(input("Kimya Notunuz:"))
GPA=float((mathematics+pyhsics+chemistry)/3)
print("Not ortalamanız:"+str(GPA))

# 3.str değişken tanımla 
text="Pyhton öğreniyorum"
print("ilk indexi:"+text[0])
print("son indexi:"+text[len(text)-1])
print("uzunluğu:"+str(len(text)))
print("ters çevrilmiş hali:"+text[::-1])

#BÖLÜM 2:OPERATÖRLER
# 4.top,çıkar,çarp,böl,mod
number_first=float(input("Birinci Sayıyı Giriniz:"))
number_second=float(input("İkinci Sayıyı Giriniz:"))
print("toplam:"+str(number_first+number_second))
print("fark:"+str(number_first-number_second))
print("çarpım:"+str(number_first*number_second))
print("bölüm:"+str(number_first/number_second))
print("mod:"+str(number_first%number_second))

# 5.geçti,kaldı
score=float(input("Notunuzu Giriniz:"))
if score>=50:
    print("geçti")
else :
    print("kaldı")
    
# 6.ehliyet
user_age=int(input("Yaşınız:"))
if user_age > 18:
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")

# 7.indirimli fiyat
product_price=float(input("Ürün fiyatı giriniz:"))
discount_price=product_price - (0.20*product_price)
print("İndirimli fiyat:",discount_price)

# 8.true false
fruits=["Elma","Armut","Portakal"]
print("Portakal" in fruits)
print("Elma" in fruits or "Kavun" in fruits)
print("Portakal" in fruits and "Karpuz" in fruits)

#BÖLÜM:3 MİNİ PROJE
# 9.alışveris sepeti
apple=10
banana=15
strawberry=20
apple_kg=float(input("kaç kg elma alacaksınız:"))
banana_kg=float(input("kaç kg muz alacaksınız:"))
strawberry_kg=float(input("kaç kg çilek alacaksınız:"))
price=((apple*apple_kg)+(banana*banana_kg)+(strawberry*strawberry_kg))
def price_discount(x):
    return (price - (x*0.10))
if price>200:
    print("fiyat:",price_discount(price))
else:
    print("fiyat:",price)

# 10.reşitlik
birth_year=int(input("Doğum yılınızı giriniz:"))
current_age=2025-birth_year
if current_age<=12:
    print("Çocuksunuz")
elif current_age>=13 and current_age<=17:
    print("Ergensiniz")
else:
    print("Yetişkinsiniz")
# diğer yol
birth_year = int(input("Doğum yılınızı giriniz: "))
current_age = 2025 - birth_year

print((current_age <= 12) * "Çocuksunuz" +
      (13 <= current_age <= 17) * "Ergensiniz" +
      (current_age >= 18) * "Yetişkinsiniz")














  
    

