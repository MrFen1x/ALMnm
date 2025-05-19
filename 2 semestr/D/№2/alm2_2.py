def initializ():
    print("s1->")
    err = "0000"
    cod = "0000000000"
    kod = "00"
    op1 = "0000"
    op2 = "0000"
    result = "0000"
    monitor(result, err, kod, op1, op2, cod)
    return result, err, kod, op1, op2, cod


def end(result, err, kod, op1, op2, cod):
    print("s0")
    monitor(result, err, kod, op1, op2, cod)
    exit()


def input_cod(result, err, kod, op1, op2, cod):
    print("s2->")
    with open("alm2_cod.txt", "r", encoding="utf-8") as file:
        cod = file.read().strip()
    monitor(result, err, kod, op1, op2, cod)
    return cod


def monitor(result, err, kod, op1, op2, cod):
    print("err", err)
    print("cod", cod)
    print("kod", kod)
    print("op1", op1)
    print("op2", op2)
    print("result", result)


def razdel_cod(result, err, kod, op1, op2, cod):
    print("s3->")
    kod = cod[:2]
    op1 = cod[2:10]
    op2 = cod[10:18]
    monitor(result, err, kod, op1, op2, cod)
    return kod, op1, op2


def umn(result, err, kod, op1, op2, cod):
    print("s4->")
    result = bin(int(op1, 2) * int(op2, 2))[2:]
    result = "0" * (8 - len(result)) + result
    monitor(result, err, kod, op1, op2, cod)
    return result


def delenie(result, err, kod, op1, op2, cod):
    print("s10->")
    result = bin(int(int(op1, 2) / int(op2, 2)))[2:]
    result = "0" * (8 - len(result)) + result
    monitor(result, err, kod, op1, op2, cod)
    return result


def output(result, err, kod, op1, op2, cod):
    print("s5->")
    monitor(result, err, kod, op1, op2, cod)
    end(result, err, kod, op1, op2, cod)


def s6(result, err, kod, op1, op2, cod):
    print("s6")
    err = "Слишком длинный ввод данных"
    monitor(result, err, kod, op1, op2, cod)
    end(result, err, kod, op1, op2, cod)


def s7(result, err, kod, op1, op2, cod):
    print("s7->")
    err = "Не верный код"
    monitor(result, err, kod, op1, op2, cod)
    end(result, err, kod, op1, op2, cod)


def s8(result, err, kod, op1, op2, cod):
    print("s8->")
    err = "Не верный формат"
    monitor(result, err, kod, op1, op2, cod)
    end(result, err, kod, op1, op2, cod)


def s9(result, err, kod, op1, op2, cod):
    print("s9->")
    err = "Слишком большой ответ"
    monitor(result, err, kod, op1, op2, cod)
    end(result, err, kod, op1, op2, cod)


def s11(result, err, kod, op1, op2, cod):
    print("s11->")
    err = "Нельзя делить на ноль"
    monitor(result, err, kod, op1, op2, cod)
    end(result, err, kod, op1, op2, cod)


def s12(result, err, kod, op1, op2, cod):
    print("s12->")
    err = "Слишком большой ответ"
    monitor(result, err, kod, op1, op2, cod)
    end(result, err, kod, op1, op2, cod)


def main():
    print("s0->")
    err = "0000"
    cod = "0000000000"
    kod = "00"
    op1 = "0000"
    op2 = "0000"
    result = "0000"
    monitor(result, err, kod, op1, op2, cod)
    result, err, kod, op1, op2, cod = initializ()
    cod = input_cod(result, err, kod, op1, op2, cod)
    if len(cod) <= 18:
        kod, op1, op2 = razdel_cod(result, err, kod, op1, op2, cod)
        if kod == "00" or kod == "11":
            if set(cod) <= {"0", "1"}:
                if kod == "11":
                    result = umn(result, err, kod, op1, op2, cod)
                    if len(result) <= 8:

                        output(result, err, kod, op1, op2, cod)
                    else:
                        s9(result, err, kod, op1, op2, cod)
                else:
                    if int(op2, 2) != 0:
                        result = delenie(result, err, kod, op1, op2, cod)
                        if len(result) <= 8:
                            output(result, err, kod, op1, op2, cod)
                        else:
                            s12(result, err, kod, op1, op2, cod)
                    else:
                        s11(result, err, kod, op1, op2, cod)
            else:
                s8(result, err, kod, op1, op2, cod)

        else:
            s7(result, err, kod, op1, op2, cod)
    else:
        s6(result, err, kod, op1, op2, cod)


if __name__ == "__main__":
    main()
