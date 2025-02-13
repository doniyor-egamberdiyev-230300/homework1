def typeBasedTransformer(**kwargs):
    transformed = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed[key] = value ** 2
        elif isinstance(value, str):
            transformed[key] = value[::-1]
        elif isinstance(value, bool):
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed[key] = value[::-1]
        elif isinstance(value, dict) and len(set(value.values())) == len(value):
            transformed[key] = {v: k for k, v in value.items()}
        else:
            transformed[key] = value
    return transformed

print(typeBasedTransformer(a=5, b=3.5, c="Hello", d=True, e=[1, 2, 3], f={"x": 1, "y": 2}))



