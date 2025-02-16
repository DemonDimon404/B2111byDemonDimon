result = []

def divider(a, b):
    if a < b:
        raise ValueError(f"{a} має бути більше або дорівнювати {b}")
    if b > 100:
        raise IndexError(f"{b} не може бути бiльшим за 100")
    return a / b

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
    for key in data:
        try:
            res = divider(key, data[key])
            result.append(res)
        except (ValueError, IndexError) as e:
            print(f"Помилка при дiлленi {key} на {data[key]}: {e}")

except Exception as e:
    print(f"помилка: {e}")

print(result)