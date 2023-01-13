#Math Solve :  Circle overlap detection? 
#Page 26 of CU python101_labbook_v1.0.1 
#Input : รับข้อมูลของวงกลม 2 วง บรรทัดละหนึ่งวง ประกอบด้วยจำนวนจริง 3 จำนวนคั่นด้วยช่องว่าง แทน พิกัด x กับ y ของจุดศูนย์กลาง และรัศมีของวงกลม  
#Process :ตรวจว่าวงกลมสองวงที่รับมาทับกันหรือแตะกันหรือไม่
#Output: : แสดงคำว่า touch เมื่อขอบของทั้งสองวงแตะกันพอดี แสดงคำว่า overlap เมื่อสองวงทับกัน ถ้าไม่แตะหรือทับ ให้แสดงคำว่า free

import math

def circle_overlap(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if distance < r1 + r2:
        return "Overlap"
    elif distance == r1 + r2:
        return "Touching"
    else:
        return "Not Overlapping"

x1, y1, r1 = map(int, input("Enter x1, y1, and r1: ").split())# split() function on the string returned by the input() function to separate the values
x2, y2, r2 = map(int, input("Enter x2, y2, and r2: ").split())# a map() function to convert each of the values to integers.
#This way the input function returns a string of values separated by spaces, then the string is split by spaces, 
# and map function converts each of the string values to integers before passing them as arguments to the function.
print(circle_overlap(x1, y1, r1, x2, y2, r2)) 