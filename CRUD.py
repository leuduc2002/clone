intro_1 = "Our item: "
intro_2 = "Our items: "
item = ["T-Shirt", "Sweater"]
while True:
    action = input("Wecome to our shop. What do you want: (C, R, U, D) or Stop ? ")
    action_low = action.lower()
    intro = intro_2
    posi = None
    if action_low == "c":
        new_item = input("Enter new item: ")
        item.append(new_item)
        if len(item) != 1:
            intro = intro_2
        print(intro, end="")
        print(*item, sep=", ")
    elif action_low == "r":
        print(intro, end="")
        print(*item, sep=", ")
    elif action_low == "u":
        while posi is None:
            try:
                posi = int(input("Update position: "))
            except ValueError:
                print("syntax error")
                posi = None
        if posi > len(item) or posi < 1:
            print("not exist")
        else:
            new_item = input("Enter new item: ")
            item[posi - 1] = new_item
            print(intro, end="")
            print(*item, sep=", ")
    elif action_low == "d":
        while posi is None:
            try:
                posi = int(input("Delete position: "))
            except ValueError:
                print("syntax error")
                posi = None
        if posi > len(item) or posi < 1:
            print("not exist")
        else:
            item.pop(posi - 1)
            if len(item) == 1:
                intro = intro_1
            print(intro, end="")
            print(*item, sep=", ")
    elif action_low == "stop":
        print("stop")
        khoi_dong = input("Enter Start to begin, End to over: ")
        if khoi_dong.lower() == "start":
            pass
        elif khoi_dong.lower() == "end":
            break
        else:
            print("syntax error")
    else:
        print("syntax error")
print("end")