#Triangle area
#Page 9 of CU python101_workbook_v1.0.2 
#This code calculates the area of a triangle given the lengths of its sides and the angle between them. 
# Specifically, it calculates the area using the formula:
# area = 1/2 * a * b * sin(c)
# Where a and b are the lengths of the sides of the triangle, and c is the angle between those sides. 
#The code first prompts the user to enter the values for a, b, and c as floats, and then it 
# calculates the area of the triangle and prints it out.
# จงเขียนโปรแกรมคำนวณพื้นที่สามเหลี่ยมที่ทราบความยาวด้านสองด้าน (a กับ b) และมุมระหว่างด้านสองด้านนั้น (C) จากสูตร area =(1/2)*absinC
#ข้อมูลนำเข้า 
# บรรทัดแรกคือความยาวด้าน a (หน่วยเป็นเซนติเมตร)
# บรรทัดที่สองคือความยาวด้าน b (หน่วยเป็นเซนติเมตร)
# บรรทัดที่สามคือมุมระหว่างด้านทั้งสอง C (หน่วยเป็นองศา)
#ข้อมูลส่งออก พื้นที่ของสามเหลี่ยมที่รับเป็นข้อมูลนำเข้า (หน่วยเป็นตารางเซนติเมตร)

import math
a = float(input("the lengths cm of the sides of A the triangle = "))
b = float(input("the lengths cm of the sides of B the triangle = "))
c = float(input("the degree angle between A sides and B Sides = "))
area = 1/2*a*b*math.sin(math.radians(c))
print("the area of this triangle", area,"cm2")