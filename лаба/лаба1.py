import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = sum(entry["score"] * entry["weight"] for entry in data)
    rounded_result = round(total_sum, 3)
    return rounded_result


print(task())
