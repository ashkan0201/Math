from getpass import getpass

while True:
    input_user = int(input("A number between (0,209): "))
    if input_user <= 209:
        list1 = []
        index1 = 0
        for everything1 in range(1,21):
            index1 += 1
            for everything2 in range(1,21):
                list1.append(f"{index1}/{everything2}")
        index2 = 0
        index3 = 20
        list2 = []
        for everything in range(20):
            list2.append(list1[index2:index3])
            index2 += 20
            index3 += 20
        list3=[]
        def Odd1(*args):
            for everything in args:
                index4 = everything
                index5 = 0
                for nothing in range(100):
                    if index4 >= 0:
                        list3.append([index4 , index5])
                        index4 -= 1
                        index5 += 1
        Odd1(1,3,5,7,9,11,13,15,17,19,21)
        list4 = []
        def Even1(*args):
            for everything in args:
                idnex6 = 0
                idnex7 = everything
                for nothing in range(100):
                    if idnex7 >= 0:
                        list4.append([idnex6 , idnex7])
                        idnex6 += 1
                        idnex7 -= 1
        Even1(2,4,6,8,10,12,14,16,18,20,22)
        Odd2 = [everything for everything in range(3,24) if everything %2 == 1]
        Odd2 = iter(Odd2)
        index8 = 0
        list5 = []
        for nothing in range(10):
            result1 = index8 + next(Odd2)
            list5.append(list4[index8:result1])
            index8 = result1
        Even2 = [everything for everything in range(2,23) if everything %2 == 0]
        Even2 = iter(Even2)
        index9 = 0
        list6 = []
        for nothing in range(10):
            result2 = index9 + next(Even2)
            list6.append(list3[index9:result2])
            index9 = result2
        list7 = []
        for index in range(10):
            list7.append(list6[index])
            list7.append(list5[index])
        Finaly1 = []
        Finaly1.append([0,0])
        for index10 in range(19):
            for index11 in list7[index10]:
                Finaly1.append(index11)
        Finaly2 = Finaly1[input_user]
        print(f"The corresponding number {input_user} in the table is equivalent to: {list2[Finaly2[0]][Finaly2[1]]}")
        break
    else:
        pass


getpass("<<< Enter to finish >>>")