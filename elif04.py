masofa=int(input("masofa:"))

if masofa >0:
    if 0 <= masofa <1:
        print("piyoda yuring")
    elif 1 <= masofa < 5:
        print("velosipedda yurish")
    elif 5<= masofa < 50:
        print("avtobus yoki mashinada")
    elif masofa>= 50:
        print("poezd yoki samolyot") 
else:
    print("masofa manfiy bo'la olmaydi")                   
