num = input("введіть число: ")
num1 = num[::-1]
if num1 == num:
    print(num1)
else:
    print("це не паліндром")