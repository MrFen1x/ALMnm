def monitor():
    global result, err, kod, op1, op2
    print("Result", result)
    print("Error", err)
    print("Kod", kod)
    print("Op1", op1)
    print("Op2", op2)


err = "00000000"
kod = "00"
op1 = "00000000"
op2 = "00000000"
result = "00000000"
print("s0->")
monitor()
with open("alm2_cod.txt", "r", encoding="utf-8") as file:
    print("s1->")
    monitor()
    cod = file.read().strip()


def ex():
    print("s0")
    monitor()
    exit();


print("s2->")
monitor()
if len(cod) == 18:
    kod = cod[:2]
    op1 = cod[2:10]
    op2 = cod[10:18]
    print("s3->")
    monitor()
    if kod == "10" or kod == "01":
        if set(cod) <= {"0", "1"}:
            if kod == "01":
                result = bin(int(op1, 2) * int(op2, 2))[2:]
                if len(result) <= 8:
                    print("s4->")
                    monitor()
                    print("s0")
                    monitor()
                    exit()
                else:
                    err = "Слишком большой ответ"
                    result = "00000000"
                    ex()

            elif kod == "10":
                if int(op2, 2) != 0:
                    result = bin(int(int(op1, 2) / int(op2, 2)))[2:]
                    print("s4->")
                    monitor()
                    if len(result) <= 8:
                        print("s0")
                        monitor()
                        exit()
                    else:
                        err = "Слишком большой ответ"
                        result = "00000000"
                        ex()

                else:
                    err = "Нельзя делить на ноль"
                    ex()
        else:
            err = "Не верный формат"
            ex()
    else:
        err = "Не верный код"
        ex()
else:
    err = "Слишком длинный или короткий ввод данных"
    ex()
