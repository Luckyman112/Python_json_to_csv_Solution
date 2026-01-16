import json

def read_json(path: str) -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
def all_keys_equal(data: list[dict[str, str]]) -> bool:
    if not data:
        return False
    keys = set(data[0].keys())
    for item in data[1:]:
        if set(item.keys()) != keys:
            return False
    return True

def write_csv(path: str, data: list[dict[str, str]]) -> None:
    headers = list(data[0].keys())
    with open(path, "w", encoding="utf-8") as f:
        f.write(",".join(headers) + "\n")
        for row in data:
            line = ",".join(row[key] for key in headers)
            f.write(line + "\n")

def main() -> None:
    try:
        data = read_json("aaa.json")
    except Exception:
        print("Ошибка")
        return
    if not isinstance(data, list):
        print("Ошибка")
        return
    if not data or not all(isinstance(item, dict) for item in data):
        print("ошибка")
        return
    if not all_keys_equal(data):
        print("Ошибка")
        return
    write_csv("aaa.csv", data)
    print("Успех")

if __name__ == "__main__":
    main()
