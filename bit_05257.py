stop = "f"
while stop != "v":
    N = int(input().strip())
    if (N > 1000):
        print("ERRO")
        stop ="v"
        break

    S1 = str(input().strip())
    S2 = str(input().strip())

    expression= str(input().strip())

    #tratamento de erros
    if len(S1) != N or len(S2) != N:
        print("ERRO")
        stop ="v"
        break

    erro = "f"
    for i in range(N):
        if S1[i] != "1" and S1[i] != "0":
            erro = "v"
        elif S2[i] != "1" and S2[i] != "0":
            erro = "v"
    if erro == "v":
        print("ERRO")
        stop ="v"
        break

    final = ["0" for i in range(N)]
    #comparacoes
    if expression == "S1 AND S2"  or expression == "S2 AND S1":
        for i in range (N):
            if S1[i] == "1" and S2[i] == "1":
                final[i] = "1"
            else:
                final[i] = "0"

    if expression == "S1 OR S2" or expression == "S2 OR S1":
        for i in range(N):
            if S1[i] == "0" and S2[i] == "0":
                final[i] = "0"
            else:
                final[i] = "1"

    if expression == "S1 XOR S2" or expression == "S2 XOR S1":
        for i in range(N):
            if S1[i] == S2[i]:
                final[i] = "0"
            else:
                final[i] = "1"

    if expression == "S1 NAND S2" or expression == "S2 NAND S1":
        for i in range (N):
            if S1[i] == "1" and S2[i] == "1":
                final[i] = "0"
            else:
                final[i] = "1"

    if expression == "S1 NOR S2" or expression == "S2 NOR S1":
        for i in range (N):
            if S1[i] == "0" and S2[i] == "0":
                final[i] = "1"
            else:
                final[i] = "0"

    if expression == "S1 MOR S2":
        for i in range(N):
            if S1[i] == "1" and S2[i] == "0":
                final[i] = "0"
            else:
                final[i] = "1"

    if expression == "S2 MOR S1":
        for i in range(N):
            if S2[i] == "1" and S1[i] == "0":
                final[i] = "0"
            else:
                final[i] = "1"




    for i in range(N):
        print(final[i], end="")

