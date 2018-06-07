#In 20 so bat dau tu 0
print(*range(20))
#In n so bat dau tu 0
so_nhap = None
while so_nhap is None:
    try:
        so_nhap = int(input("Enter a positive integer: "))
        if so_nhap < 1:
            print("not a positive integer")
            so_nhap = None
    except ValueError:
        print("syntax error")
print(*range(so_nhap))