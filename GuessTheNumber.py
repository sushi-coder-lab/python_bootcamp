# import random
# computer_number = random.randint(1,5)
# for i in range(3):
#     number = int(input("guss a number : "))
#     if number == computer_number:
#         print("you win, congratulation")
#         break
#     else:
#         print("wrong guss atempt again")
#         print("you have only",3-(i+1), "times")

arr = [10,50,-5,75]
number = 0
for num in arr:
    number = number + 1

count = 0
for i in range(number):
    if arr[i]>0:
        count = count+arr[i]
        # continue
print(count,number)
