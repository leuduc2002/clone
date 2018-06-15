# for i in range(5):
#     for j in range(5):
n=20

for i in range(n):
    # print one line
    for j in range(n):
      if j >= n - i:
        print("* ", end="")
      else:
          print("  ", end="")

    print()








