def flatten_nested_dict(key, x):
    result = {}
    if isinstance(x, dict) and len(x) > 0:
        for k, value in x.items():
            temp = flatten_nested_dict(str(key) + f".{k}", value)
            result.update(temp)
    elif isinstance(x, list) and len(x) > 0:
        for i in range(0, len(x)):
            temp = flatten_nested_dict(str(key)+ f"[{i}]", x[i])
            result.update(temp)

    else:
        result[key] = x
    return result


def flatten(x):
    result = {}
    for key, value in x.items():
        temp = flatten_nested_dict(key, value)
        result.update(temp)
    return result


print(flatten({
    "a": {
        "b": {"c": 1, "d": 2},
        "e": 3
    },
    4: 4,
    "g": [
        {"h": 5},
        {
            "i": 6,
            "j": [
                {"k": 7},
                {"l": 8}
            ],
        }
    ]
}))
