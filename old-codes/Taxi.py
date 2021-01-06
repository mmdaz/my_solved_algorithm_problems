n = int (input())
numberString = input()
numbers = [int(num) for num in numberString.split(" ")]
taxiNumbers = 0
numbers.sort()
#print(numbers)
counter = 0
num1 = 0
num2 = 0
num3 = 0
for i in numbers:
    if i==4:
        counter+=1
    if i==3:
        num3+=1
    if i==2:
        num2+=1
    if i==1:
        num1+=1

counter+= int(num2/2)
num2 = int(num2%2)
#print(num2)
if (num3<=num1):
    counter+=num3
    num1 -= num3
    num3=0
else:
    num3 -= num1
    counter += num1
    num1 = 0
# if num2!=0:
#     if num1>1:
#         counter+=1
#         num1 -= 2
counter+= num3
counter += int((num1 + num2*2)/4)
if ((num1 + num2*2)%4) > 0 :
    counter += 1
print(counter)


