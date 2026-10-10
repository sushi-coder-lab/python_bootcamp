# num = int(input("enter a number : "))
# for i in range(num):
#     row = ""
#     for j in range(num-i):
#         row = row + "*"
#     print(row)

# =========== befor -ve number print every numbers ======
# arr = []
# n = int(input("enter a length of array : "))
# for i in range(n):
#     number = int(input(f"enter a elemnt for {i} : "))
#     arr.append(number)
# for i in range(n):
#     if arr[i]<0:
#         print("here is a first -ve number")
#         break
#     else:
#         print(arr[i])


#== 1 to 30 wich number is divisible 3or4 with both skip it ==
# num = int(input("enter a range : "))
# for i in range(1, num+1):
#     if i%3==0 and i%4==0:
#         continue
#     else:
        # print(i)

# books = input("are you reading standard book Y/N : ")
# membership = input("you have membership Y/N : ")
# day = int(input("late day : "))

# def lateFee(books,membership,day):
#     if books == "y" or books == "yes":
#         if day <= 5:
#             amount = 5*5
#         else:
#             amount = 5*5 + ((day-5)*10)
#     else:
#         if day <= 5:
#             amount = 5*5
#         else:
#             amount = 5*5 + ((day-5)*20)
    
#     if membership == "y" or membership == "yes":
#         total = amount - (amount*0.20)
#     else:
#         total = amount
#     return total
# print(lateFee(books,membership,day))
