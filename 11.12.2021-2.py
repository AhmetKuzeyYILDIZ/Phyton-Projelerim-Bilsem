
sayı=[]
for i in range(10):
    sayılar=input("Bir sayı giriniz: ")
    sayı.append(sayılar)
sıralama=input("A-Z,Z-A?")
if sıralama == "A-Z":
    sayı.sort()
    print(sayı)
elif sıralama=="Z-A":
    sayı.sort(reverse=True)
    print(sayı)
else:
    print("1 IQ")
