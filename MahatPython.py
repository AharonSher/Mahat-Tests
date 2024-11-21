# Rozenman's branch.

# 1.
# def is_perfect(number):
#     sum_digits = 0
#     for char in str(number):
#         sum_digits += int(char)
#     if number % sum_digits == 0:
#         print(number)
#
#
# for num in range(1, 1001):
#     is_perfect(num)


# itamar's commit no. 2

# 2.
# import re
#
# def is_num_phon_correct():
#     counter = 0
#     while True:
#         counter += 1
#         my_phone = input("Enter a phone number: ")
#         pattern = "(^05)[0-9](-)[0-9]{7}$"
#         if re.match(pattern, my_phone) is not None:
#             print(f"Teh number phone {my_phone} is correct!")
#             print(f"several attempts: {counter}")
#             break
#         else:
#             print("Input a valid number!!!")
#
#
# is_num_phon_correct()


# 3.
# import random
#
# def is_ordered(list):
#     highest_even_index = 0
#     lowest_odd_index = 0
#     for index in range(len(list)):
#         if list[index] % 2 == 0:
#             highest_even_index = index
#
#     for i in range(len(list)):
#         if list[-(1 + i)] % 2 != 0:
#             temp_index = -(1+i)
#             lowest_odd_index = len(list) + temp_index
#
#     if highest_even_index < lowest_odd_index:
#         return True
#     return False
#
# # l = [4, 5, 8, 1, 3, 8, 3, 8, 4]
# # print(is_ordered(l))
#
# def build_ordered(x, y, size):
#     iterations_counter = 0
#     while True:
#         iterations_counter +=1
#         my_list = []
#         for i in range(size):
#             my_list.append(random.randint(x, y))
#         print(my_list)
#         print(iterations_counter)
#         if is_ordered(my_list) == True:
#             return my_list
#
# print(build_ordered(1, 20, 8))

# 4.
# class Time:
#
#     def __init__(self, hour, minutes):
#         self.hour = hour
#         self.minutes = minutes
#
#     def difference(self, other):
#         hours = 0
#         if self.hour > other.hour:
#             hours = 24 - self.hour + other.hour
#         else:
#             hours = other.hour - self.hour
#         minutes = other.minutes - self.minutes
#         sum_minutes = hours * 60 + minutes
#         return sum_minutes
#
# def check_company():
#     times_list = []
#     for i in range(4):
#         times_list.append(int(input("Enter a number:")))
#
#     t1 = Time(times_list[0], times_list[1])
#     t2 = Time(times_list[2], times_list[3])
#
#     if t1.difference(t2) <= 180:
#         print("a reliable company!")
#     else:
#         print("Exceeding time!!")
#
# for i in range(100):
#     check_company()

# 6.
# def secret(s):
#     for i in range(0, len(s), 2):
#         if s[i]>='A' and s[i]<='Z':
#             return False
#     for i in range(1, len(s), 2):
#         if s[i]<'A' or s[i]>'Z':
#             return False
#     return True
#
# s = "0A/D>>"
# print(secret(s))

# 7.
# class Coffee:
#     def __init__(self, name, kind, strength, price):
#         self.name = name
#         self.kind = kind
#         self.strength = strength
#         self.price = price
#
#     def __str__(self):
#         return f"name: {self.name}, kind: {self.kind}, strength: {self.strength}, price: {self.price}"
#
# c1 = Coffee("Nestle", "Espreso", 5, 25.5)
# c2 = Coffee("Nespreso", "Reverse coffee", 8, 30.8)
# c3 = Coffee("Nestle", "Black coffee", 12, 21.2)
# c4 = Coffee("Nestle", "Nescoffee", 2, 45.0)
#
# list = [c1, c2, c3, c4]
#
# def same_products(list):
#     first_manufacturer = list[0].name
#     for product in list:
#         if product.name != first_manufacturer:
#             return False
#     return True
#
# print(same_products(list))
#
#
# def weak_sorts(arr, num):
#     new_list = []
#     for coffee in arr:
#         if coffee.strength < num:
#             new_list.append(coffee.kind)
#     return new_list
#
# print(weak_sorts(list, 6))
#
#
# def most_expensive(arr):
#     prise = 0
#     expensive_coffee = None
#     for coffee in arr:
#         if coffee.price > prise:
#             prise = coffee.price
#             expensive_coffee = coffee
#     return expensive_coffee
#
# print(most_expensive(list))



# 8.
# def is_reversed(l1, l2):
#     new_l2 = list(reversed(l2))
#     return new_l2 == l1

# def is_reversed(l1, l2):
#     new_l2 = l2[::-1]
#     return new_l2 == l1

# def is_reversed(l1, l2):
#     if len(l1) != len(l2):
#         return False
#     for i in range(len(l1)):
#         if l1[i] != l2[-(1+i)]:
#             return False
#     return True
#
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
#
# print(is_reversed(list1, list2))

# 9.
# class Digits:
#     def __init__(self, integer):
#         self.arr_digits = [0 for _ in range(10)]
#         for digit in str(integer):
#             self.arr_digits[int(digit)] += 1

#     def equals(self, other):
#         return self.arr_digits == other.arr_digits
#
#     def compare_to(self, other):
#         if sum(self.arr_digits) > sum(other.arr_digits):
#             return 1
#         elif sum(self.arr_digits) < sum(other.arr_digits):
#             return 2
#         else:
#             return 0
#
#
#     def display(self):
#         print(self.arr_digits)
#
#
# num1 = Digits(244888)
# num2 = Digits(244888)
#
# # print(num1.equals(num2))
# print(num1.compare_to(num2))


# 10.
# class Building:
#     def __init__(self, address, apartments):
#         self.address = address
#         self.apartments = apartments
#
#     def __str__(self):
#         apps_str = ""
#         for app in self.apartments:
#             apps_str += str(app) + "\n"
#         return f"address: {self.address}, \napartments:\n {apps_str}"
#
# class App:
#     def __init__(self, app_num, owner, rooms, rate):
#         self.app_num = app_num
#         self.owner = owner
#         self.rooms = rooms
#         self.rate = rate
#
#     def month_cost(self):
#         meters_in_room_per_month = 0
#         total_meters_in_apartment = 0
#         for room in self.rooms:
#             meters_in_room_per_month = room.area * room.freq
#             total_meters_in_apartment += meters_in_room_per_month
#         return self.rate * total_meters_in_apartment
#
#
#     def __str__(self):
#         rooms_str = ""
#         for room in self.rooms:
#             rooms_str += str(room) + "\n"
#         return f"app_num: {self.app_num}, owner: {self.owner}, \nrooms:\n{rooms_str}, rate: {self.rate}"
#
# class Room:
#     def __init__(self, kind, area, freq):
#         self.kind = kind
#         self.area = area
#         self.freq = freq
#
#     def __str__(self):
#         return f"kind: {self.kind}, area: {self.area}, freq: {self.freq}"
#
#
# def month_report(builds, clients):
#     for client in clients:
#         total_cost = 0
#         for build in builds:
#             for apartment in build.apartments:
#                 if apartment.owner == client:
#                     print(apartment.owner)
#                     print(apartment)
#                     print(apartment.month_cost())
#                     total_cost += apartment.month_cost()
#         print(f"total: {total_cost}")
#
#
#
# r1 = Room("bedroom", 12, 2)
# r2 = Room("restroom", 4, 4)
# r3 = Room("kitchen", 9, 3)
#
# rooms1 = [r1, r2]
# rooms2 = [r2, r3]
#
# a1 = App(10, "Shloimi", rooms1, 10)
# a2 = App(7, "Shloimi", rooms2, 30)
# a3 = App(6, "Ronen", rooms1, 30)
#
# apps1 = [a1, a2]
# apps2 = [a2, a3]
#
#
#
# b1 = Building("Hraby milubavich 125", apps1)
# b2 = Building("Hraby milubavich 155", apps2)
# b3 = Building("Hraby milubavich 255", apps1)
#
# builds = [b1, b2]
#
# names = ["Shloimi", "Ronen"]
#
# # print(a1)
# # print(a1.month_cost())
# month_report(builds, names)


# 11.
# prices = {"apple": 10.0, "banana": 6.5, "milk": 6.90, "coca-cola": 7.5}
# shopping_list = [('apple', 3), ("milk", 2), ("coca-cola", 3)]
# sister_list = ['milky', 'shoko', 'fries', 'milk', 'chocolate', 'coca-cola']
#
#
# def total_price_shopping(prices, shopping_list):
#     price = 0
#     for product in shopping_list:
#         price += prices[product[0]] * product[1]
#     return price
#
#
# def what_is_missing(prices, sister_list):
#     product_list = prices.keys()
#     missing_products = []
#     for product in sister_list:
#         if product not in product_list:
#             missing_products.append(product)
#     return missing_products
#
# print(total_price_shopping(prices, shopping_list))
# print(what_is_missing(prices, sister_list))

# --------------------------------------------------------------------------------


# 1.
# temp_num = 0
# list_num = []
# while len(str(temp_num)) != 3:
#     temp_num = int(input("Enter a number: "))
#     list_num.append(temp_num)
# print(f"min. number: {max(list_num)}")
# print(f"max number: {min(list_num)}")
# print(list_num)


# 2.
# def is_valid(str):
#     if len(str) % 2 == 0:
#         return False
#     if str[0] == str[len(str) // 2] == str[-1]:
#         return True
#     return False
# # s = "AsdfA'yuA"
# # print(is_valid(s))
#
# valid = 0
# invalid = 0
# for i in range(5):
#     my_str = input("Enter a string: ")
#     if is_valid(my_str):
#         valid += 1
#     else:
#         invalid += 1
#
# print(f"valid: {valid}\ninvalid: {invalid}")

# 3.
# def is_valid_list(list1):
#     positive = 0
#     negative = 0
#     zero = 0
#     for num in list1:
#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += 1
#         else:
#             zero += 1
#     if zero == 0 and positive == negative:
#         print(list1)
#     else:
#         list1 = list(reversed(list1))
#         print(list1)

# my_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 0]
# is_valid_list(my_list)

# class FlowerPackage:
#     def __init__(self, type, num, time, price):
#         self.type = type
#         self.num = num
#         self.time = time
#         self.price = price
#
#     # def __init__(self, type, price):
#     #     self.type = type
#     #     self.num = 2000
#     #     self.time = 12
#     #     self.price = price
#
#     def __str__(self):
#         return f"type: {self.type}, num: {self.num}, time: {self.time}, price: {self.price}"
#
#
# # f1 = FlowerPackage("Vered", 50, 10, 5.5)
# f2 = FlowerPackage("Kalanit", 1)
# f3 = FlowerPackage("Sagol", 2)
# f4 = FlowerPackage("Katom", 3)
# f5 = FlowerPackage("Yafe", 4)
#
# my_list = [f2, f3, f4, f5]
#
# for i in my_list:
#     print(i)
#
# def compensation(arr, fly_time):
#     total_losses = 0
#     for sending in arr:
#         if sending.time < fly_time:
#             print(f"invalid sending:\n{sending}")
#             total_losses += sending.num * sending.price
#     return total_losses

# class Client:
#
#     def __init__(self, address, persons, current, prev):
#         self.address = address
#         self.persons = persons
#         self.current = current
#         self.prev = prev
#
#     def update_current(self, new_current):
#         self.prev = self.current
#         self.current = new_current
#
#     def payment(self, rate1, rate2):
#         discounted_quantity = self.persons * 7
#         expensive_quantity = self.current - self.prev - discounted_quantity
#         return (discounted_quantity * rate1) + (expensive_quantity * rate2)
#
#
#     def __str__(self):
#         return f"address: {self.address}, persons: {self.persons}, current: {self.current}, prev: {self.prev}"
#
#
# def proposal(arr, num, rate1, rate2):
#     temp_pay = 0
#     temp_amount = 0
#     for client in arr:
#         if client.persons == num:
#             temp_pay += client.payment(rate1, rate2)
#             temp_amount += 1
#     average = temp_pay / temp_amount
#     print(average)
#     for client in arr:
#         if client.persons == num and client.payment(rate1, rate2) > average:
#             print(f"address: {client.address}")
#
#
# c1 = Client("Hrabi milubavich 155", 3, 140, 100)
# c2 = Client("Hrabi milubavich 255", 2, 160, 100)
# c3 = Client("Hrabi milubavich 355", 5, 200, 100)
# c4 = Client("Hrabi milubavich 455", 3, 150, 100)
# c5 = Client("Hrabi milubavich 555", 3, 160, 100)
#
# list_of_client = [c1, c2, c3, c4, c5]
#
# proposal(list_of_client, 3, 8, 15)
#
# # print(c1)
# # c1.update_current(200)
# # print(f"update {c1}")
#
# print(c1.payment(8, 15))
# print(c4.payment(8, 15))
# print(c5.payment(8, 15))


# 9.
# def net_weight(num):
#     net_num_str = str(num)[1:-1]
#     sum = 0
#     for i in net_num_str:
#         sum += int(i)
#     return sum
#
# # print(net_weight(12349))
#
# def is_sorted_list(arr):
#     for i in range(len(arr) -1):
#         if net_weight(arr[i]) > net_weight(arr[i+1]):
#             return False
#     return True
#
# def unique_net_list(arr1, arr2):
#     net_list1 = []
#     net_list2 = []
#     for num in arr1:
#         net_list1.append(net_weight(num))
#     for num in arr2:
#         net_list2.append(net_weight(num))
#     print(arr1)
#     print(net_list1)
#     for i, num in enumerate(net_list1):
#         if num not in net_list2:
#             print(arr1[i])
#     for i, num in enumerate(net_list2):
#         if num not in net_list1:
#             print(arr2[i])
#
#
#
# l1 = [35, 923, 781, 12349,1892]
# l2 = [2, 358, 181, 5821, 1742, 36621, 27731]
#
# unique_net_list(l1, l2)


# 10.
# def is_sorted_by_remainder_of_k(arr, k):
#     for i in range(len(arr) -1):
#         print(arr[i]%k)
#         if arr[i] % k == arr[i+1] % k or arr[i] % k == arr[i+1] % k - 1:
#             continue
#         else:
#             return False
#     return True
#
# import random
# def sort_the_list(arr, k):
#     while True:
#         if is_sorted_by_remainder_of_k(arr, k):
#             return arr
#         random.shuffle(arr)
#
# def sort_the_list2(arr, k):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j] % k > arr[j+1] % k:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
#
# # my_list1 = [4, 8, 1, 13, 9, 2, 7, 15]
# # my_list2 = [15, 1, 2, 7, 13, 8, 4, 9]
# # # print(is_sorted_by_remainder_of_k(my_list1, 4))
# # print(is_sorted_by_remainder_of_k(my_list2, 5))
#
# my_list3 = [15, 2, 1, 13, 8, 7, 9, 4]
# print(sort_the_list(my_list3, 4))
# print(sort_the_list2(my_list3, 4))


# 11.
# def is_perm(num1, num2):
#     if num1 == num2:
#         return False
#     if sorted(str(num1)) == sorted(str(num2)):
#         return True
#     return False
#
#
# def is_super_perm(arr):
#     for list in arr:
#         is_perm_list = False
#         for i in list:
#             for j in list:
#                 if is_perm(i, j):
#                     is_perm_list = True
#         if not is_perm_list:
#             return False
#     return True
#
#
# # a = 1232
# # b = 3123
# # print(is_perm(a, b))
# arr = [
#     [232, 456, 232, 324],
#     [456, 654, 565, 587],
#     [989, 998, 741, 852]
# ]
# print(is_super_perm(arr))


# --------------------------------------------------


# 1.
# for i in range(100):
#     num = int(input("Enter a number: "))
#     if len(str(num)) == 3:
#         sum_digits = 0
#         for digit in str(num):
#             sum_digits += int(digit)
#         print(f"sum: {sum_digits}")


# 2.
# my_str = ""
# counter = 0
# while len(my_str) < 13:
#     my_str = input("Enter a string: ")
#     if "X" in my_str and not "Y" in my_str:
#         counter += 1
# print(counter)

# 3.
# def is_in_array(arr, index, value):
#     ind = -1
#     for i in range(len(arr)):
#         if arr[i] == value:
#             ind = i
#     if ind < 0:
#         return False
#     if ind <= index:
#         return False
#     return True
#
# # arr = [1,2,8,4,5,67, 8,67]
# # print(is_in_array(arr,3,8))
#
# def is_unique_array(arr):
#     for i in range(len(arr)):
#         num = arr[i]
#         if is_in_array(arr, i, num):
#             return False
#     return True
#
# arr = [1, 2, 3, 4, 5]
# print(is_unique_array(arr))

# 4.

# 5.
# def found_first_digit(num):
#     while num > 10:
#         num //= 10
#     return num
#
#
# def found_last_digit(num):
#     return num % 10
#
# def brothers(num1, num2):
#     if num1 > 0 and num2 > 0 and num1 % 1 == 0 and num2 % 1 == 0:
#         return found_last_digit(num1) == found_last_digit(num2) and found_first_digit(num1) == found_first_digit(num2)
#     else:
#         raise ValueError("negative number or float number!")
#
# # n1 = 12
# # n2 = 123
# # print(brothers(n1, n2))
#
# def brothers_list(arr1, arr2):
#     for i in range(len(arr1)):
#         flag = False
#         for j in range(len(arr2)):
#             if brothers(arr1[i], arr2[j]):
#                 flag = True
#         if not flag:
#             return False
#     return True
#
#
# l1 = [123, 78002, 591, 13, 7, 25]
# l2 = [752, 153, 5681, 757, 215, 183, 452]
# l3 = [123, 78002, 591, 13, 7, 25]
#
# print(brothers_list(l2, l1))

# 11.
# def is_lone(arr, row, col):
#     my_num = arr[row][col]
#     n = len(arr)
#     for current_row_index in range(n):
#         if current_row_index == row:
#             continue
#         if arr[current_row_index][col] == my_num:
#             return False
#     for index in range(len(arr[row])):
#         if index == col:
#             continue
#         if arr[row][index] == my_num:
#             return False
#     return True
#
# def max_lone(arr):
#     max_lone = -1
#     for row_index in range(len(arr)):
#         for num_index in range(len(arr[row_index])):
#             if is_lone(arr, row_index, num_index) and arr[row_index][num_index] > max_lone:
#                 max_lone = arr[row_index][num_index]
#     return max_lone
#
#
#
# arr = [
#     [12, 23, 42, 857, 32, 65],
#     [98, 65, 87, 456, 85, 47],
#     [85, 65, 96, 857, 98, 78]
# ]
#
# print(is_lone(arr, 1, 2))
# print(max_lone(arr))


# ==================   3   =====================
# 1.
# counter_even = 0
# sum_odd = 0
# for _ in range(5):
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         counter_even += 1
#     else:
#         sum_odd += num
#     if len(str(num)) == 3:
#         sum_digits = 0
#         while num > 0:
#             sum_digits += num % 10
#             num //= 10
#         print(sum_digits)
# print(counter_even)
# print(sum_odd)

# 4.
# def is_perfect(arr):
#     if len(arr) % 2 == 0:
#         return False
#     for i in range(0, len(arr) // 2):
#         if arr[i] <= 0 or arr[i] > 9:
#             return False
#     for i in range(len(arr)//2+1, len(arr)):
#         if 0 < arr[i] < 10:
#             return False
#     if arr[len(arr)//2] != 0:
#         return False
#     return True
#
# arr = [1, -2, 3, 0, 21, 45, 74]
# print(is_perfect(arr))

# 6.
# def is_valid_string(str):
#     if str[0] == "." or str[-1] == ".":
#         return False
#     for i in range(len(str)-1):
#         if str[i] == "." and str[i+1] == ".":
#             return False
#     return True


# 9
# import re
# def is_palindrom(str):
#     pattern = "[A-Z]"
#     clean_list = re.findall(pattern, str)
#     new_str = "".join(clean_list)
#     revers_list = new_str[::-1]
#     return new_str == revers_list
#
# def max_palindrom(arr):
#     len_str = 0
#     for st in arr:
#         if is_palindrom(st) and len(st) > len_str:
#             len_str = len(st)
#     return len_str
#
# s = "fA%B##rkC1^BAdd"
# print(is_palindrom(s))


# 10.
# def sum_evens(num):
#     evens = 0
#     while num > 0:
#         if num % 2 == 0:
#             evens += 1
#         num //= 10
#     return evens
#
# def max_rank(arr):
#     max = 0
#     for num in arr:
#         if sum_evens(num) > max:
#             max = sum_evens(num)
#     return max
#
# def ordered_list(arr):
#     high_rank = max_rank(arr)
#     if len(arr) != high_rank + 1:
#         return False
#     my_list = []
#     for num in arr:
#         if sum_evens(num) in my_list:
#             return False
#         my_list.append(sum_evens(num))
#     if len(my_list) != len(arr + 1):
#         return False
#     return True
#
# num = 123456
# print(sum_evens(num))
# l = [1234, 45652, 85214, 2222222, 85274144]
# print(max_rank(l))


# ===========    4   ============

# 3.
def triangula(arr):
    n = len(arr)
    if n % 3 != 0:
        return False
    for i in range(3, n, 3):
        if arr[i] != arr[i-3]:
            return False
    for i in range(4, n, 3):
        if arr[i] != arr[i-3]:
            return False
    for i in range(5, n, 3):
        if arr[i] != arr[i-3]:
            return False
    return True

l1 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
l2 = [1, 1, 1, 1, 1, 1]
l3 = [1, 2, 1, 2, 2, 2]
print(triangula(l3))




# 14.
def is_sad(arr, num):
    for row in range(len(arr)):
        if row == 0 or row == len(arr) -1:
            continue
        for i in range(len(arr[row])):
            if i == 0 or i == len(arr[row]) -1:
                continue
            if arr[row][i] == num:
                no_friends = 0
                for r in range(row-1, row+2):
                    for j in range(i-1, i+2):
                        if r == row and j == i:
                            continue
                        if arr[r][j] != num:
                            no_friends += 1
                if no_friends == 8:
                    return True
    return False

def sads(arr):
    my_set = set()
    for row in arr:
        for num in row:
            if is_sad(arr, num):
                my_set.add(num)
    if len(my_set) == 0:
        return None
    return my_set

def highest_num(arr):
    sadses = sads(arr)
    highest = -1
    for num in sadses:
        if num > 9 and num < 100 and num > highest:
            highest = num
    if highest > 0:
        return highest
    return "no found"



metrix = [
    [5, 4, 1, 0, 0, 3],
    [1, 10, 7, 1, 123, 3],
    [6, 1, 7, 0, 0, 2],
    [1, 10, 21, 5, 5, 2],
    [1, 10, 1, 10, 10, 1]
]

# print(is_sad(metrix, 215))
print(sads(metrix))
print(highest_num(metrix))
