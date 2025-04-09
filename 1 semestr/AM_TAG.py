while True:
    x = input("Введите без пробелов Х(1-4): ")

    if len(x) != 4 or not x.isdigit():
        print("Неправильный ввод. Попробуйте снова.")
        continue
    x1 = int(x[0])
    x2 = int(x[1])
    x3 = int(x[2])
    x4 = int(x[3])

    outputs = {
        0: "y1=0\ny2=0\ny3=0\ny4=0\ny5=0\n",  # --
        1: "y1=1\ny2=0\ny3=1\ny4=0\ny5=1\n",  # y1, y3, y5
        2: "y1=0\ny2=1\ny3=0\ny4=1\ny5=0\n",  # y2, y4
        3: "y1=1\ny2=0\ny3=0\ny4=1\ny5=0\n",  # y1, y4
        4: "y1=1\ny2=0\ny3=0\ny4=0\ny5=1\n",  # y1, y5
        5: "y1=0\ny2=2\ny3=1\ny4=0\ny5=1\n"  # y2, y3, y5
    }

    k0 = 0
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k = 0

    f1 = (x1 == 0 and x2 == 0) or (x3 == 1 and x4 == 0) or (x1 == 1 and x3 == 1) or (x2 == 1 and x3 == 0)
    f2 = (x2 == 0) or (x1 == 1 and x3 == 0)
    f3 = (x1 == 0) or (x2 == 1) or (x3 == 1)

    statenow = "S0"

    with open("Result.txt", "w") as file:
        file.write("Борисов Илья\n")
        file.write("Введите без пробелов Х(1-4):" + str(x))
        file.write("\n\nf1 = " + str(f1) + "\nf2 = " + str(f2) + "\nf3 = " + str(f3) + "\n\n")

        while k0 < 1:

            if k1 > 1 or k2 > 1 or k3 > 1 or k4 > 1 or k5 > 1:
                file.write("Цикл зациклилися")
                print("Цикл зациклилися")
                break

            if statenow == "S0" and f2 == True:
                k0 += 1
                k += 1
                file.write(str(k) + ": " + "S0->S0\n" + outputs[0] + "\nЦикл завершен")
                print(str(k) + ": " + "S0->S0\n" + outputs[0])
                print("Цикл завершен")
                break

            if statenow == "S0" and f2 == False:
                statenow = "S1"
                k1 += 1
                k += 1
                file.write(str(k) + ": " + "S0->S1\n" + outputs[1] + "\n")
                print(str(k) + ": " + "S0->S1\n" + outputs[1])

            if statenow == "S1":
                statenow = "S2"
                k2 += 1
                k += 1
                file.write(str(k) + ": " + "S1->S2\n" + outputs[2] + "\n")
                print(str(k) + ": " + "S1->S2\n" + outputs[2])

            if statenow == "S2" and f2 == False:
                statenow = "S3"
                k3 += 1
                k += 1
                file.write(str(k) + ": " + "S2->S3\n" + outputs[3] + "\n")
                print(str(k) + ": " + "S2->S3\n" + outputs[3])

            if statenow == "S2" and f2 == True and f3 == True:
                statenow = "S3"
                k3 += 1
                k += 1
                file.write(str(k) + ": " + "S2->S3\n" + outputs[0] + "\n")
                print(str(k) + ": " + "S2->S3\n" + outputs[0])

            if statenow == "S2" and f1 == True and f2 == True and f3 == False:
                statenow = "S3"
                k3 += 1
                k += 1
                file.write(str(k) + ": " + "S2->S3\n" + outputs[0] + "\n")
                print(str(k) + ": " + "S2->S3\n" + outputs[0])

            if statenow == "S2" and f1 == False and f2 == True and f3 == False:
                statenow = "S4"
                k4 += 1
                file.write(str(k) + ": " + "S2->S4\n" + outputs[0] + "\n")
                print(str(k) + ": " + "S2->S4\n" + outputs[0])

            if statenow == "S3":
                statenow = "S4"
                k4 += 1
                k += 1
                file.write(str(k) + ": " + "S3->S4\n" + outputs[4] + "\n")
                print(str(k) + ": " + "S3->S4\n" + outputs[4])

            if statenow == "S4":
                statenow = "S5"
                k5 += 1
                k += 1
                file.write(str(k) + ": " + "S4->S5\n" + outputs[5] + "\n")
                print(str(k) + ": " + "S4->S5\n" + outputs[5])

            if statenow == "S5" and f1 == False:
                statenow = "S2"
                k2 += 1
                k += 1
                file.write(str(k) + ": " + "S5->S2\n" + outputs[0] + "\n")
            print(str(k) + ": " + "S5->S2\n" + outputs[0])

            if statenow == "S5" and f1 == True:
                statenow = "S0"
                k0 += 1
                k += 1
                file.write(str(k) + ": " + "S5->S0\n" + outputs[0] + "\nЦикл завершен")
                print(str(k) + ": " + "S5->S0\n" + outputs[0])
                print("Цикл завершен")
                break
    if input("Введите q для выхода или Enter для продолжения:")=="q":
        print("Выход из программы.")
        break
