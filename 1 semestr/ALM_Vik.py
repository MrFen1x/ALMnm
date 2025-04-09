print("Ананьев Виктор, Вариант - 17")
while True:
    x = input("Введите x1-x4: ")
    if len(x) == 4 and x.isdigit():
        x1, x2, x3, x4 = map(int, x)
    elif x.lower() == "q":
        print("Выход из программы.")
        break
    else:
        print("Неправильный ввод. Попробуйте снова.")
        continue
    outputs = {
        "S0": "y1=0\ny2=0\ny3=0\ny4=0\ny5=0\ny6=0\n",
        "S1": "y1=1\ny2=0\ny3=1\ny4=0\ny5=0\ny6=0\n",
        "S2": "y1=0\ny2=0\ny3=1\ny4=0\ny5=1\ny6=0\n",
        "S3": "y1=0\ny2=1\ny3=0\ny4=0\ny5=0\ny6=1\n",
        "S4": "y1=0\ny2=1\ny3=1\ny4=0\ny5=0\ny6=0\n",
        "S5": "y1=0\ny2=0\ny3=1\ny4=0\ny5=1\ny6=0\n"
    }
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k=0
    f1 = (x1 == 1 and x2 == 0 and x3 == 0) or (x2 == 1 and x3 == 1 and x4 == 1)
    f2 = (x1 == 1 and x2 == 1) or (x1 == 1 and x3 == 0 and x4 == 1)
    f3 = (x1 == 1 and x2 == 0 and x4 == 1) or (x1 == 1 and x2 == 1 and x3 == 1)
    print("f1=", f1)
    print("f2=", f2)
    print("f3=", f3, "\n")
    state = "S0"
    old_state = ""
    while True:
        if k1 >= 1 or k2 >= 1 or k3 >= 1 or k4 >= 1 or k5 >= 1:
            print("Цикл зациклился")
            break
        if state == "S0" and f1 == True:
            old_state = state
            state = "S1"
            k1 += 1
            k += 1
            print(k, "S0->S1")
            print(outputs[old_state])
        if state == "S0" and f1 == False:
            old_state = state
            state = "S4"
            k4 += 1
            k += 1
            print(k, "S0->S4")
            print(outputs[old_state])
        if state == "S1" and f1 == True:
            old_state = state
            state = "S1"
            k1 += 1
            k += 1
            print(k, "S1->S1")
            print(outputs[old_state])
        if state == "S1" and f1 == False and f2 == True:
            old_state = state
            state = "S2"
            k2 += 1
            k += 1
            print(k, "S1->S2")
            print(outputs[old_state])
        if state == "S1" and f1 == False and f1 == False:
            old_state = state
            state = "S4"
            k4 += 1
            k += 1
            print(k, "S1->S4")
            print(outputs[old_state])
        if state == "S1" and f1 == False and f3 == False:
            old_state = state
            state = "S5"
            k5 += 1
            k += 1
            print(k, "S1->S5")
            print(outputs[old_state])
        if state == "S5" and f2 == False and f3 == True:
            old_state = state
            state = "S2"
            k2 += 1
            k += 1
            print(k, "S5->S2")
            print(outputs[old_state])
        if state == "S4" and f1 == False and f3 == True:
            old_state = state
            state = "S2"
            k2 += 1
            k += 1
            print(k, "S4->S2")
            print(outputs[old_state])
        if state == "S2":
            old_state = state
            state = "S3"
            k3 += 1
            k += 1
            print(k, "S2->S3")
            print(outputs[old_state])
        if state == "S3" and f1 == False:
            old_state = state
            state = "S0"
            k += 1
            print(k, "S3->S0")
            print(outputs[old_state])
            print("Цикл завершен")
            break
        if state == "S3" and f1 == True:
            old_state = state
            state = "S4"
            k4 += 1
            k += 1
            print(k, "S3->S4")
            print(outputs[old_state])
        if state == "S4" and f1 == True:
            old_state = state
            state = "S1"
            k1 += 1
            k += 1
            print(k, "S4->S1")
            print(outputs[old_state])
        if state == "S4" and f1 == True and f1 == False:
            old_state = state
            state = "S4"
            k4 += 1
            k += 1
            print(k, "S4->S4")
            print(outputs[old_state])
        if state == "S4" and f1 == False and f3 == False:
            old_state = state
            state = "S5"
            k5 += 1
            k += 1
            print(k, "S4->S5")
            print(outputs[old_state])
        if state == "S5" and f2 == True:
            old_state = state
            state = "S0"
            k += 1
            print(k, "S5->S0")
            print(outputs[old_state])
            print("Цикл завершен")
            break
        if state == "S5" and f2 == False and f3 == False:
            old_state = state
            state = "S5"
            k5 += 1
            k += 1
            print(k, "S5->S5")
            print(outputs[old_state])
    user_input = input("Введите 'q' для выхода или Enter для перезапуска: ")
    if user_input.lower() == "q":
        print("Выход из программы.")
        break
