# Challenge 1
minutes = int(input("Input minutes:")) * 60
hours = int(input("Input hours:")) * 3600
days = int(input("Input days:")) * 24 * 60 * 60

time1 = minutes
time2 = hours
time3 = days

print()
print(time1, "&", time2, "&", time3, "seconds!")
print()


# Challenge 2
# Write a function that converts seconds into hours.
def convert_seconds(s):
    s = s % (24 * 3600)
    hour = s // 3600
    print(hour, "hour/s")
    print()


s = 3600
convert_seconds(s)

# Challenge 3
list_of_numbers = [2, 9, 3, 11, 87, 22, 1, 11, 0]


# Write a function that returns the largest number in the list above.
# Coach Mike's Extra Credit
def largest_number(list_of_numbers):
    return list_of_numbers


list_of_numbers = [2, 9, 3, 11, 87, 22, 1, 11, 0]
original_list = list_of_numbers

print('Before the Sort')
print(list_of_numbers)
print()
len_of_list = len(list_of_numbers)

print('# of Numbers')
print(len_of_list)
print()
list_of_numbers.sort(key=largest_number)

print('After the Sort')
print(list_of_numbers)
print()

print('The smallest number from the ascending & original list is:')
print(list_of_numbers[(len_of_list - 9)])
print()

print('The LARGEST number from the ascending & original list is:')
print(list_of_numbers[(len_of_list - 1)])

# Challenge 4
product_1 = {
    "cost_price": 10.00,
    "sell_price": 45.00,
    "inventory": 400
}
product_2 = {
    "cost_price": 25.50,
    "sell_price": 300.00,
    "inventory": 200
}
product_3 = {
    "cost_price": 2.10,
    "sell_price": 12.00,
    "inventory": 1000
}


def caculate_profit(product):
    cost = product.get("cost_price")
    cost_as_float = float(cost)

    sell = product.get("sell_price")
    sell_as_float = float(sell)

    product_profit = sell_as_float - cost_as_float
    total_product_profit = product_profit * product.get("inventory")
    return total_product_profit


profit_for_product_1 = caculate_profit(product_1)
print("$", profit_for_product_1, "Product 1 Total profit")
print()

profit_for_product_2 = caculate_profit(product_2)
print("$", profit_for_product_2, "Product 2 total profit")
print()

profit_for_product_3 = caculate_profit(product_3)
print("$", profit_for_product_3, "Product 3 total profit")
print()

total_profit = profit_for_product_1 + profit_for_product_2 + profit_for_product_3
print("$", total_profit, "is the total profit from all inventory")
print()


# Challenge 5
def reverse_string():
    original_string = "Ebonee Gilford"
    print(original_string)
    reversed_string = ' '.join(original_string.split()[::-1])
    return reversed_string


print(reverse_string())
print()


# Challenge 6
def reverse_date():
    original_format = "05/07/1982"
    print(original_format)
    reverse_date = original_format[6:] + original_format[3:5] + original_format[:2]
    return reverse_date


print(reverse_date())
print()
