def older(persons):
    result = None
    max_age = None
    for dni, age in persons.items():
        if not max_age or age > max_age:
            result = dni
            max_age = age

    return result

print(older({"0": 15, "1": 3, "2": 58, "3": 22, "4": 58}))
