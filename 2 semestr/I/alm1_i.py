import re

with open("alm1_input.p", "r", encoding="utf-8") as file:
    code = file.read()
pattern = re.compile(r'for\s+(\w+)\s*:=\s*(\d+)\s+(to|downto)\s+(\d+)\s+do\s+begin', re.IGNORECASE)
match = pattern.search(code)
if match:
    start_index = match.start()
    end_index = match.end()
    begin_count = 1
    i = end_index
    while i < len(code):
        if code[i:i + 5].lower() == 'begin':
            begin_count += 1
            i += 5
        elif code[i:i + 3].lower() == 'end':
            begin_count -= 1
            i += 3
            if begin_count == 0:
                if code[i] == ';':
                    i += 1
                break
        else:
            i += 1

    for_block = code[start_index:i]
    before = code[:start_index]
    after = code[i:]
    match = re.search(r'for\s+(\w+)\s*:=\s*(\d+)\s+(to|downto)\s+(\d+)\s+do\s+begin\s+(.*)\s+end;', for_block,
                      re.IGNORECASE | re.DOTALL)
    var, start, direction, end_val, body = match.groups()
    body_lines = body.strip()

    if direction.lower() == 'to':
        converted = (
            f"{var} := {start};\n"
            "repeat\n"
            f"  {body_lines}\n"
            f"  {var} := {var} + 1;\n"
            f"until {var} > {end_val};"
        )
    else:  # downto
        converted = (
            f"{var} := {start};\n"
            "repeat\n"
            f"  {body_lines}\n"
            f"  {var} := {var} - 1;\n"
            f"until {var} < {end_val};"
        )

    with open("alm1_output.p", "w", encoding="utf-8") as file:
        file.write(before + converted + after)
else:
    with open("alm1_output.p", "w", encoding="utf-8") as file:
        file.write(code)
