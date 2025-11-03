print("Basic Calculator")
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
print("\n1. Addition \n2.Subtraction \n3. Multiplication \n4. Division \n")
choice=int(input("Enter your choice: "))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    ans=num1/num2 if num2!=0 else float("inf")
    print(ans)
else:
    print("Wrong choice. Choose again!")
