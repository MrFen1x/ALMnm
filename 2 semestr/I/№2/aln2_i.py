err = ""
kod = 00
op1 = 00000000
op2 = 00000000
result = 00000000
with open("alm2_cod.txt", "r", encoding="utf-8") as file:
    cod = file.read().strip()


def ex(): print(err);exit();


if len(cod) == 18:
    kod = cod[:2]
    op1 = cod[2:10]
    op2 = cod[10:18]
    if kod == "10" or kod == "01":
        if set(cod) <= {"0", "1"}:
            if kod == "01":
                result = bin(int(op1, 2) * int(op2, 2))[2:]
                if len(result) <= 8:
                    print(result)
                    exit()
                else:
                    err = "Слишком большой ответ"
                    ex()

            elif kod == "10":
                if int(op2,2) != 0:
                    result = bin(int(int(op1, 2) / int(op2, 2)))[2:]
                    if len(result) <= 8:
                        print(result)
                        exit()
                    else:
                        err = "Слишком большой ответ"
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
