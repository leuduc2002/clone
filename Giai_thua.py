so_nhap = None
while so_nhap is None:
    try:
        so_nhap = int(input("Enter a positive integer: "))
        if so_nhap < 1:
            print("Not a positive integer")
            so_nhap = None
    except ValueError:
        print("syntax error")
fac = 1
for i in range(so_nhap):
    fac = fac * (i + 1)
print("Giai thua la:", fac)
