'''
+     Addition
-     Subtraction
*     Multiplication
/     Division
//    Floor Division  (10 ÷ 3 = 3.333... floor → 3) it will give 3
%     Modulus (remainder)
**    Power
'''

n=1234
print(n%10)
print(n//10)

while n>0:
    digit=n%10
    print(digit)
    n=n//10