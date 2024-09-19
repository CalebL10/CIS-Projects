def input_pos_float(prompt):
    number = None
    while True:
        s = input(prompt)
        number = float(s)
        if number > 0:
            break
        print("Number mut be a float > 0")
    return number