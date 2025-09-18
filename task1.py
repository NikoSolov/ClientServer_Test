string = input()

sym_dict = {
    "{": 0,
    "(": 0,
    "[": 0,
}

for sym in string:
    match sym:
        case "{":
            sym_dict["{"] += 1
        case "}":
            sym_dict["{"] -= 1
        case "(":
            sym_dict["("] += 1
        case ")":
            sym_dict["("] -= 1
        case "[":
            sym_dict["["] += 1
        case "]":
            sym_dict["["] -= 1

print(not any(sym_dict.values()))