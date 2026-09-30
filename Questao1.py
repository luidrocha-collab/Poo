def altera_no_local(obj):
    antes = id(obj)

    try:
        if isinstance(obj, list):
            obj.append(10)
        elif isinstance(obj, dict):
            obj["novo"] = 10
        elif isinstance(obj, set):
            obj.add(10)
        elif isinstance(obj, bytearray):
            obj.append(10)
        else:
            return False

        return id(obj) == antes

    except:
        return False


lista = [1, 2]
dicionario = {"a": 1}
conjunto = {1, 2}
bytes_array = bytearray(b"abc")

print("list:", altera_no_local(lista))
print("dict:", altera_no_local(dicionario))
print("set:", altera_no_local(conjunto))
print("bytearray:", altera_no_local(bytes_array))
