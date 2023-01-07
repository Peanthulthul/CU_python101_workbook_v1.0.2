#Math Solve : 01-03 Find the root of ax2+bx+c =0 
#Page 18 of CU python101_labbook_v1.0.1 
#Input: จำนวนจริง a, b และ c บรรทัดละค่า โดยสมการ ax2 + bx + c = 0 ที่ให้มานี้ จะมีรากเป็นค่าจริงสองค่าที่ต่างกันแน่นอน 
# Output: รากจริงทั้งสองค่าของสมการ ax2 + bx + c = 0 โดย
# - แสดงราก x1 แล้วตามด้วยราก x2
# - มีเลขหลังจุดทศนิยม 3 ตำแหน่ง (ใช้ฟังก์ชัน round เช่น round(2/3, 3) จะได้ 0.667 )
while True :
    import math
    a = float(input("a ="))
    b = float(input("b ="))
    c = float(input("c ="))
    if a == 0 :
        x = -c/b
        print("roots= ",round(x,3))
    else:
        d = b**2-4*a*c
        x1 = (-b-d**0.5)/(2*a) 
        x2 = (-b+d**0.5)/(2*a)
        x3 = round(x1,3)
        x4 = round(x2,3)  
    print("roots= ",x3, x4)
