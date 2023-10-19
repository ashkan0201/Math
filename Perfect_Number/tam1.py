number = 1
list_of_numbers = []
finaly_list = []
while True:
    for num1 in range(1,500):
        for num2 in range(1,500):
            if num1 * num2 == number:
                list_of_numbers.append(num1)
    list_of_numbers.pop()
    try:
        if sum(list_of_numbers) == number:
            finaly_list.append(number)
    except:
        pass
    list_of_numbers.clear()
    number += 1
    if number == 500:
        break
for everything in finaly_list:
    print(everything)
