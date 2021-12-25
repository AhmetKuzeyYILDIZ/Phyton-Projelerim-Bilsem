şifre="31"
kullanıcıadı="eben"
while True:
    girilenkullanıcıadı=input("AQ")
    girilenşifre=input("AQ")
    if girilenkullanıcıadı != kullanıcıadı:
        print("Doğru gir yoksa döverim")
    if girilenşifre != şifre:
         print("Doğru gir yoksa döverim")
    if girilenkullanıcıadı == kullanıcıadı and girilenşifre == şifre:
        print("Selam")
        break
