from getpass import getpass
finaly_list = []
for number in range(200):
    if number > 1:
        for zoj_yab in range(2, number):
            if number % zoj_yab == 0:
                break
        else:
            finaly_list.append(number)
for index , num in enumerate(finaly_list):
    print(f"{index+1}, {2 ** (num - 1 ) * (2 ** num - 1)}")


print(f"\n\nQty: {len(finaly_list)}")
getpass("<<< Enter to finish >>>")