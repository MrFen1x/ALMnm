import re
mura=""

class ExpressionEvaluator:
    def is_valid(self, expr: str) -> bool:
        expr = expr.replace(" ", "")
        global mura
        mura = mura + "s2->"
        # Проверка допустимых символов
        if not re.fullmatch(r"[0-9\.\+\-\*/\(\)]+", expr):
            return False

        # Проверка скобок
        stack = []
        mura = mura + "s3->"
        for char in expr:
            if char == '(':
                stack.append(char)
                mura = mura + "s4->"
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
                mura = mura + "s5->"
        if stack:
            return False

        # Проверка всех чисел в выражении — только > 0 и ≤ 65535
        numbers = [int(n) for n in re.findall(r'(?<!\w)-?\d+\.?\d*', expr)]
        mura = mura + "s6->"
        if not all(n >= 0 and n <= 255 for n in numbers):
            return False
        return True

    def evaluate(self, expr: str) -> float:
        global mura
        if re.search(r'/\s*0+(\.0*)?(?!\d)', expr):
            mura = mura + "s7->s0"
            print("Деление на ноль невозможно")
            print(mura)
            exit(0)
        result = eval(expr, {"__builtins__": None}, {})
        mura = mura + "s8->"
        if not (result > 0 and result <= 255):
            mura = mura + "s11->s0"
            print("Результат вне допустимого диапазона (0 и ≤ 255).")
            print(mura)
            exit(0)
        mura = mura + "s9->"
        return result


if __name__ == "__main__":

    mura="s0->"
    with open("alm3_input.txt", 'r', encoding='utf-8') as file:
        expression = file.read().strip()
    evaluator = ExpressionEvaluator()
    mura = mura + "s1->"

    if evaluator.is_valid(expression):

        result = evaluator.evaluate(expression)
        mura = mura + "s10->"
        print(int(result))
        mura = mura + "s0"
        print(mura)
    else:
        mura = mura + "s0"
        print("Не корректное выражение")
        print(mura)
