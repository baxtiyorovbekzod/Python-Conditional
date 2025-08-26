yosh=int(input("yoshizni kiriting:"))
narx=100
if 0<= yosh<=6:
    print(narx+(narx*0.5))
if 7<= yosh<= 17:
    print(narx+(narx*0.2))
if 18<= yosh<= 60:
    print(narx) 
if yosh>60:
    print(narx+(narx*0.3))       