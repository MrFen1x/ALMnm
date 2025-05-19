import re


class ExpressionEvaluator:
    def is_valid(self, expr: str) -> bool:
        expr = expr.replace(" ", "")

        # Проверка допустимых символов
        if not re.fullmatch(r"[0-9\.\+\-\*/\(\)]+", expr):
            return False

        # Проверка скобок
        stack = []
        for char in expr:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False

        # Проверка всех чисел в выражении — только > 0 и ≤ 65535
        numbers = [int(n) for n in re.findall(r'(?<!\w)-?\d+\.?\d*', expr)]
        if not all(n >= 0 and n <= 255 for n in numbers):
            return False
        return True

    def evaluate(self, expr: str) -> float:
        if re.search(r'/\s*0+(\.0*)?(?!\d)', expr):
            print("Деление на ноль невозможно")
            exit(0)
        result = eval(expr, {"__builtins__": None}, {})
        if not (result > 0 and result <= 255):
            print("Результат вне допустимого диапазона (0 и ≤ 255).")
            exit(0)
        return result


if __name__ == "__main__":
    with open("alm3_input.txt", 'r', encoding='utf-8') as file:
        expression = file.read().strip()
    evaluator = ExpressionEvaluator()

    if evaluator.is_valid(expression):

        result = evaluator.evaluate(expression)
        print(result)
    else:
        print("Не корректное выражение")
