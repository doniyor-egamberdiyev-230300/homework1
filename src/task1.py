def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargsAcceptFun(name="Doniyor", age=19, city="Samarkandk")
