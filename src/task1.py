def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargsAcceptFun(name="Alice", age=25, city="New York")
