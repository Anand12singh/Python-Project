print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print('so What you Want?'+'+,-,/,%,*')
num3 =input()
# test comment

if num3=='*' :
    num4=num1*num2
    print(num4)
elif num3 == '+':
    plus=num2+num1
    print(plus)
elif num3 == '/':
    Dev=num2/num1
    print(Dev)
elif num3 == '-':
    Dev=num2-num1
    print(Dev)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")
while True:
    print('press 1 for continue press 2 for stop')
    x=int(input('enter no'))
    if x==2:
          break

              
    
