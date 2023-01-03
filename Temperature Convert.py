#Temperature Convert
#Page 12 of CU python101_workbook_v1.0.2 
# สูตรในการเปลี่ยนค่าจากองศาเซลเซียสไปเป็นองศาฟาเรนไฮต์และเคลวินมีดังนี้
#ให้อ่านข้อมูลอุณหภูมิ (หน่วยเป็นองศาเซลเซียส) จากนั้นคำนวณหาค่าองศาฟาเรนไฮต์และเคลวินด้วยสมการด้านบน
#เมื่อ C คือ องศาเซลเซียส F คือ องศาฟาเรนไฮต์ และ K คือ เคลวิน
#ข้อมูลนำเข้า หนึ่งบรรทัดประกอบด้วยค่าองศาเซลเซียสเป็นจำนวนจริง
#ข้อมูลส่งออก มีหนึ่งบรรทัดประกอบด้วยตัวเลขจำนวนจริงสองจำนวน ตัวแรกเป็นองศาฟาเรนไฮต์ และตัวที่สองเป็นเคลวิน
celsius = float(input("What is the celsius temperature?"))
fahrenhite = (9/5)*celsius+32
Kelvin = celsius+273.15
print("The temperature is",fahrenhite,"degree Fahrenhite and",Kelvin,"degree Kelvin and",celsius,"degree celcius")