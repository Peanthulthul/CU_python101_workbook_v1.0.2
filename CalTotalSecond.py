#Calculate total second

#Input: รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์ (บรรทัดละจำนวน) 
# เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที
#Process: คำนวณจำนวนวินาทีรวมที่คิดจาก h, m และ s
# Output: จำนวนวินาทีรวมทั้งหมดที่คำนวณได้

#Amount of second
S = int(input("What is the second?"))
M = int(input("What is the minute?"))
H = int(input("What is the Hour?"))
Total_S = H*60*60+M*60+S
print("Total second is" ,Total_S,"Second")