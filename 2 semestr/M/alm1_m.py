import re
str="s0->"
with open("alm1_input.cpp", "r", encoding="utf-8") as file:
    source_code = file.read()
pattern = r"(int\s+x\s*=\s*0\s*;)\s*do\s*\{((?:[^}{]+|\{(?:[^}{]+|\{[^}{]*\})*\})*)(x\+\+\s*;)\s*\}\s*while\s*\((x\s*<\s*10)\)\s*;"
match = re.search(pattern, source_code, re.DOTALL)
str=str+"s1->"
if match:
    init_x = match.group(1)  # int x = 0;
    body_full = match.group(2).strip()  # Полное тело цикла
    x_increment = match.group(3)  # x++;
    condition = match.group(4)  # x < 10
    body_without_x_increment = re.sub(r"x\+\+\s*;", "", body_full).strip()
    for_loop = f"for ({init_x} {condition}; {x_increment}) {{\n    {body_without_x_increment}\n}}"
    new_code = re.sub(pattern, for_loop, source_code, count=1, flags=re.DOTALL)
    with open("alm1_output.cpp", "w", encoding="utf-8") as file:
        file.write(new_code)
    str=str+"s2->s0"
else:
    with open("alm1_output.cpp", "w", encoding="utf-8") as file:
        file.write(source_code)
    str = str + "s3->s0"
print(str)
