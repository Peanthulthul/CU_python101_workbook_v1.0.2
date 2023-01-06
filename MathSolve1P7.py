#Math Solve
#Page 7 of CU python101_workbook_v1.0.2 
#Input: รับจำนวนเต็ม 1 จำนวนจากแป้นพิมพ์ เก็บใน X 
#Process: y = 2-x+(3/7)*x**2-(5/11)x**3+ log(x)
# Output: ค่า y ที่คำนวณได้

import math
x = float(input())
y = 2-x+(3/7)*x**2-(5/11)*x**3+math.log10(x)
print(y)