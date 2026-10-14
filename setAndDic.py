# roll_no = {123,345,567}
# #isme jab hum duplicate hota hai to usko print nhi karta hai koi error nhi deta but dublicate ko peint nhi karta hai 
# print(roll_no)

# cites = ["mumbai","dantewada","geedam","dantewada"]

# uniq_cites = set(cites)

# print(uniq_cites)

# #check if an item exists in a set

# does_it_exist = "mumbai" in uniq_cites # true/flase
# print(does_it_exist)

# #add remove with set

# uniq_cites.add("dnt")
# print(uniq_cites)

# uniq_cites.discard("dnt")
# print(uniq_cites)

# # set of 4 students 
# #check whether some student exists in that set, print the result
# #if they done exist, add them print the result

# student = ["ram","ravi","ramesh","sushil"]
# uniq = set(student)
# does_student = "ramaa" in uniq
# if does_student:
#     print(uniq)
# else:
#    uniq.add("ramaa")
#    print(uniq)

#/// compairing two set

# set1 = {"vivek","dilip","gungun"}
# set2 = {"vivek","divya","sanjay"}

# print("in both",set1 & set2)
# print("in either",set1 | set2)
# print("only set1", set1 - set2) # item in set1 only


# =================== dictinary === (key-uniq, value be duplicat) ==========>
# dis = {key1:value, }

# student = {"name":"sushil", "age":5, "rollnumber":12345} #create
# print(student)

# #opration (crud) -> supported(crud opration)

# student['location'] = "dnt" # add location
# print(student)

# student['location'] = "hyderabad" #update location
# print(student)

# check_location = "hyderabad" in student # checking key
# print(check_location)

# check_location = "hyderabad" in student.values() # checking value / student.get(("name"))---print name
# print(check_location)
'''
1. Create a dictionary of 4 items (rice 10, Soap 20) key - name of the item, value- count, print
2. Reduce the count of th items by 2, print
3. Check if a key exists, if it exists then increment the value by 1
3.1 else, create a new key with value = 10

'''

# shop = {"rice":10,
#         "potato":22,
#         "blue-rice":30,
#         "red-rice":33
#         }
# print(shop)

# shop["rice"]-=2
# print("reduced",shop)

# if "black-rice" in shop:
#     shop["black-rice"]+=1
# else:
#     shop["black-rice"] = 10

# print(shop)

'''
Manage store order and inventory

1) You have a Prices dictionary with 5 items and their prices
2) You have an out_of_stock set with 2 item of thems (from the Prices dictionary)
3) You have an order list, that has list of orders (list of items)
4) Loop through the order list
4.1) For rach order, if it is out of stock, print unavalable
4.2) else, keep a running total ( get the price from the Prices dictionary) 
5) Print the final order value 
'''

prices = {
    "apple": 20,
    "banana": 10,
    "milk": 50,
    "bread": 30,
    "eggs": 60
}

out_of_stock = {"milk", "eggs"}

orders = ["apple", "milk", "bread", "banana"]

total = 0

for item in orders:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total += prices[item]

print("Final order value:", total)
