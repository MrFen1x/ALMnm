import re

str="s0->"
with open("input.cpp", "r") as infile:
    code = infile.read()

pattern = re.compile(
    r"do\s*\{([^{}]*?(?:\{[^{}]*\}[^{}]*?)*)\}\s*while\s*\((.*?)\);", re.DOTALL
)
match = pattern.search(code)
if match:
    str=str+"s1->"
    body = match.group(1).strip()
    condition = match.group(2).strip()
    replacement = f"while ({condition}) {{\n    {body}\n}}"
    code = pattern.sub(replacement, code, count=1)

str=str+"s2->"
with open("output.cpp", "w") as outfile:
    outfile.write(code)
str = str + "s0"
print(str)