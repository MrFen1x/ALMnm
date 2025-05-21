import re

mili = ""


class ExpressionEvaluator:
    def is_valid(self, expr: str) -> bool:
        expr = expr.replace(" ", "")
        global mili
        mili = mili + "s1->"
        mili = mili + "s2->"
        # Проверка допустимых символов
        if not re.fullmatch(r"[0-9\.\+\-\*/\(\)]+", expr):
            return False

        # Проверка скобок
        stack = []
        mili = mili + "s3->"
        for char in expr:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        mili = mili + "s4->"
        if stack:
            return False

        # Проверка всех чисел в выражении — только > 0 и ≤ 65535
        numbers = [float(n) for n in re.findall(r'(?<!\w)-?\d+\.?\d*', expr)]
        mili = mili + "s5->"
        if not all(n >= -32768 and n <= 32767 for n in numbers):
            return False
        return True

    def evaluate(self, expr: str) -> float:
        global mili
        if re.search(r'/\s*0+(\.0*)?(?!\d)', expr):
            print("Деление на ноль невозможно")
            mili = mili + "s0"
            print(mili)
            exit(0)
        result = eval(expr, {"__builtins__": None}, {})
        mili = mili + "s6->"
        if not (result > -32768 and result <= 32767):
            print("Результат вне допустимого диапазона (-32768 и ≤ 32767).")
            mili = mili + "s0"
            print(mili)
            exit(0)
        return result


if __name__ == "__main__":
    mili = mili + "s0->"
    with open("alm3_input.txt", 'r', encoding='utf-8') as file:
        expression = file.read().strip()
    evaluator = ExpressionEvaluator()

    if evaluator.is_valid(expression):
        result = evaluator.evaluate(expression)
        print(result)
        mili = mili + "s7->s0"
    else:
        print("Не корректное выражение")
        mili = mili + "s0"
print(mili)
