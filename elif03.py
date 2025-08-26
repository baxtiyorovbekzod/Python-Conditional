soat=int(input("soat kiring:"))
if 0<= soat <=23:
 if 5<= soat <= 11:
    print("ertalab")
 elif 12<= soat <= 17:
    print("kunduzi")
 elif 18<= soat<= 21:
    print("kechqurun")
 elif 22<= soat <= 23 or 0 <= soat<= 4:
    print("tun")
else:
    print("soat 0-23 oralig'ida bo'lishi kerak")