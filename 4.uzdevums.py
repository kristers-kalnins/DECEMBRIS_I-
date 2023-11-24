num=int(input("numurs: "))

if num<0:
    print("nav faktoriāla")
else:
    faktorials=1
    for sk in range(1, num + 1):
        faktorials *= sk
    print(f"Skaitļa {num} faktoriāls ir: {faktorials}")