nama = "ERVIN"  

for i in range(len(nama)):
    for j in range(i + 1):
        if j == i:
            print(nama[j], end="")
        else:
            print(nama[j], end=" ")
    for k in range(len(nama) - i - 1):
        print("*", end=" ")
    print()