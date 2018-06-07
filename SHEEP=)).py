flock = [5, 7, 300, 90, 24, 50, 75]
month = 0
sum = 0
end = 1
print("Hello my name is Duc and these are my sheep size:")
print(flock)

while True:
    maximum = max(flock)
    while True:
        action = input("Next action: Shear / Pass / Sell: ")
        action_low = action.lower()
        if action_low == "shear":
            print("Now my biggest sheep has size", maximum, ". Let's shear it.")
            for i in range(7):
                if int(flock[i]) == maximum:
                    flock[i] = 8
            print("After shearing, here is my flock:")
            print(flock)
            for i in range(7):
                flock[i] = flock[i] + 50
            break
        elif action_low == "pass":
            for i in range(7):
                flock[i] = flock[i] + 50
            break
        elif action_low == "sell":
            for i in range(7):
                sum = sum + flock[i]
            print("My flock has size in total", sum)
            print("I would get ", sum, " * 2$ = ", sum * 2, "$", sep="")
            end = 0
            break
        else:
            print("syntax error")
    if end == 0:
        break
    month = month + 1
    print("MONTH", month, ":\nOne month passes, now here is my flock")
    print(flock)


