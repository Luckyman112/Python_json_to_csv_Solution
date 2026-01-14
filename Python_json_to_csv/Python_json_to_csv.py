from json import load
from csv import DictWriter

def all_keys_equal(dict_list):
    if not dict_list:
        return True
    if not all(isinstance(d, dict) for d in dict_list):
        return False
    first_keys = set(dict_list[0].keys())
    return all(set(d.keys()) == first_keys for d in dict_list[1:])

with open("aaa.json", "r", encoding="utf-8") as f:
    try:
        data = load(f)
    except Exception:
        print("Ошибка")
    else:
        if not isinstance(data, list) or not data or not all(isinstance(d, dict) for d in data):
            print("Ошибка")
        else:
            first_keys = set(data[0].keys())
            if not all(set(d.keys()) == first_keys for d in data[1:]):
                print("Ошибка")
            else:
                fieldnames = list(data[0].keys())
                with open("aaa.csv", "w", newline='', encoding="utf-8") as out:
                    dw = DictWriter(out, fieldnames=fieldnames)
                    dw.writeheader()
                    dw.writerows(data)
                print("Успех")